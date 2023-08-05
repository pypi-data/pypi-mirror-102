# Copyright 2021 The NetKet Authors - All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings
from functools import partial
from typing import Any, Optional, Callable, Iterable, Union, Tuple, List

import numpy as np

import jax
from jax import numpy as jnp
from jax import tree_map
from jax.util import as_hashable_function

import flax
from flax import linen as nn
from flax import serialization

import netket
from netket import jax as nkjax
from netket import utils
from netket.hilbert import AbstractHilbert
from netket.sampler import Sampler, SamplerState, ExactSampler
from netket.stats import Stats, statistics, mean, sum_inplace
from netket.utils import flax as flax_utils, maybe_wrap_module
from netket.utils.types import DType, Array, PyTree, PRNGKeyT, Shape, NNInitFunc
from netket.optimizer import SR
from netket.operator import (
    AbstractOperator,
    define_local_cost_function,
    local_cost_function,
    local_value_cost,
    local_value_op_op_cost,
)

from .base import VariationalState, VariationalMixedState
from .mc_state import MCState

AFunType = Callable[[nn.Module, PyTree, jnp.ndarray], jnp.ndarray]
ATrainFunType = Callable[
    [nn.Module, PyTree, jnp.ndarray, Union[bool, PyTree]], jnp.ndarray
]


def apply_diagonal(bare_afun, w, x, *args, **kwargs):
    x = jnp.hstack((x, x))
    return bare_afun(w, x, *args, **kwargs)


class MCMixedState(VariationalMixedState, MCState):
    """Variational State for a Mixed Variational Neural Quantum State.

    The state is sampled according to the provided sampler, and it's diagonal is sampled
    according to another sampler.
    """

    def __init__(
        self,
        sampler,
        model=None,
        *,
        sampler_diag: Sampler = None,
        n_samples_diag: int = 1000,
        n_discard_diag: Optional[int] = None,
        seed=nkjax.PRNGKey(),
        sampler_seed: Optional[int] = None,
        variables=None,
        **kwargs,
    ):
        """
        Constructs the MCMixedState.
        Arguments are the same as :class:`MCState`.

        Arguments:
            sampler: The sampler
            model: (Optional) The model. If not provided, you must provide init_fun and apply_fun.

        Keyword Arguments:
            n_samples: the total number of samples across chains and processes when sampling (default=1000).
            n_discard: number of discarded samples at the beginning of each monte-carlo chain (default=n_samples/10).
            parameters: Optional PyTree of weights from which to start.
            seed: rng seed used to generate a set of parameters (only if parameters is not passed). Defaults to a random one.
            sampler_seed: rng seed used to initialise the sampler. Defaults to a random one.
            mutable: Dict specifing mutable arguments. Use it to specify if the model has a state that can change
                during evaluation, but that should not be optimised. See also flax.linen.module.apply documentation
                (default=False)
            init_fun: Function of the signature f(model, shape, rng_key, dtype) -> Optional_state, parameters used to
                initialise the parameters. Defaults to the standard flax initialiser. Only specify if your network has
                a non-standard init method.
            apply_fun: Function of the signature f(model, variables, σ) that should evaluate the model. Defafults to
                `model.apply(variables, σ)`. specify only if your network has a non-standard apply method.
            training_kwargs: a dict containing the optionaal keyword arguments to be passed to the apply_fun during training.
                Useful for example when you have a batchnorm layer that constructs the average/mean only during training.
        """

        seed, seed_diag = jax.random.split(nkjax.PRNGKey(seed))
        if sampler_seed is None:
            sampler_seed_diag = None
        else:
            sampler_seed, sampler_seed_diag = jax.random.split(
                nkjax.PRNGKey(sampler_seed)
            )

        self._diagonal = None

        hilbert_physical = sampler.hilbert.physical

        super().__init__(
            sampler.hilbert.physical,
            sampler,
            model,
            **kwargs,
            seed=seed,
            sampler_seed=sampler_seed,
            variables=variables,
        )

        if sampler_diag is None:
            sampler_diag = sampler.replace(hilbert=hilbert_physical)

        sampler_diag = sampler_diag.replace(machine_pow=1)

        diagonal_apply_fun = nkjax.HashablePartial(apply_diagonal, self._apply_fun)

        for kw in ["n_samples", "n_discard"]:
            if kw in kwargs:
                kwargs.pop(kw)

        self._diagonal = MCState(
            sampler_diag,
            apply_fun=diagonal_apply_fun,
            n_samples=n_samples_diag,
            n_discard=n_discard_diag,
            variables=self.variables,
            seed=seed_diag,
            sampler_seed=sampler_seed_diag,
            **kwargs,
        )

        # build the

    # def init(self, *args, **kwargs):
    #    super().init(*args, **kwargs)

    @property
    def diagonal(self):
        return self._diagonal

    @property
    def sampler_diag(self) -> Sampler:
        """The Monte Carlo sampler used by this Monte Carlo variational state to
        sample the diagonal."""
        return self.diagonal.sampler

    @sampler_diag.setter
    def sampler_diag(self, sampler):
        self.diagonal.sampler = sampler

    @property
    def n_samples_diag(self) -> int:
        """The total number of samples generated at every sampling step
        when sampling the diagonal of this mixed state.
        """
        return self.diagonal.n_samples

    @n_samples_diag.setter
    def n_samples_diag(self, n_samples):
        self.diagonal.n_samples = n_samples

    @property
    def chain_length_diag(self) -> int:
        """
        Length of the markov chain used for sampling the diagonal configurations.

        If running under MPI, the total samples will be n_nodes * chain_length * n_batches.
        """
        return self.diagonal.chain_length

    @chain_length_diag.setter
    def chain_length_diag(self, length: int):

        self.diagonal.chain_length = length

    @property
    def n_discard_diag(self) -> int:
        """Number of discarded samples at the beginning of the markov chain used to
        sample the diagonal of this mixed state.
        """
        return self.diagonal.n_discard

    @n_discard_diag.setter
    def n_discard_diag(self, n_discard: Optional[int]):
        self.diagonal.n_discard = n_discard

    @MCState.parameters.setter
    def parameters(self, pars: PyTree):
        MCState.parameters.fset(self, pars)
        if self.diagonal is not None:
            self.diagonal.parameters = pars

    @MCState.model_state.setter
    def model_state(self, state: PyTree):
        MCState.model_state.fset(self, state)
        if self.diagonal is not None:
            self.diagonal.model_state = state

    def reset(self):
        super().reset()
        if self.diagonal is not None:
            self.diagonal.reset()

    def expect_operator(self, Ô: AbstractOperator) -> Stats:
        σ = self.diagonal.samples
        σ_shape = σ.shape
        σ = σ.reshape((-1, σ.shape[-1]))

        σ_np = np.asarray(σ)
        σp, mels = Ô.get_conn_padded(σ_np)

        # now we have to concatenate the two
        O_loc = local_cost_function(
            local_value_op_op_cost,
            self._apply_fun,
            self.variables,
            σp,
            mels,
            σ,
        ).reshape(σ_shape[:-1])

        # notice that loc.T is passed to statistics, since that function assumes
        # that the first index is the batch index.
        return statistics(O_loc.T)

    def expect_and_grad_operator(
        self, Ô: AbstractOperator, is_hermitian=None
    ) -> Tuple[Stats, PyTree]:
        raise NotImplementedError

    def to_matrix(self, normalize: bool = True) -> jnp.ndarray:
        return netket.nn.to_matrix(
            self.hilbert, self._apply_fun, self.variables, normalize=normalize
        )

    def __repr__(self):
        return (
            "MCMixedState("
            + "\n  hilbert = {},".format(self.hilbert)
            + "\n  sampler = {},".format(self.sampler)
            + "\n  n_samples = {},".format(self.n_samples)
            + "\n  n_discard = {},".format(self.n_discard)
            + "\n  sampler_state = {},".format(self.sampler_state)
            + "\n  sampler_diag = {},".format(self.sampler_diag)
            + "\n  n_samples_diag = {},".format(self.n_samples_diag)
            + "\n  n_discard_diag = {},".format(self.n_discard_diag)
            + "\n  sampler_state_diag = {},".format(self.diagonal.sampler_state)
            + "\n  n_parameters = {})".format(self.n_parameters)
        )

    def __str__(self):
        return (
            "MCMixedState("
            + "hilbert = {}, ".format(self.hilbert)
            + "sampler = {}, ".format(self.sampler)
            + "n_samples = {})".format(self.n_samples)
        )


# serialization


def serialize_MCMixedState(vstate):
    state_dict = {
        "variables": serialization.to_state_dict(vstate.variables),
        "sampler_state": serialization.to_state_dict(vstate.sampler_state),
        "diagonal": serialization.to_state_dict(vstate.diagonal),
        "n_samples": vstate.n_samples,
        "n_discard": vstate.n_discard,
    }
    return state_dict


def deserialize_MCMixedState(vstate, state_dict):
    import copy

    new_vstate = copy.copy(vstate)
    new_vstate.reset()

    # restore the diagonal first so we can relink the samples
    new_vstate._diagonal = serialization.from_state_dict(
        vstate._diagonal, state_dict["diagonal"]
    )

    new_vstate.variables = serialization.from_state_dict(
        vstate.variables, state_dict["variables"]
    )
    new_vstate.sampler_state = serialization.from_state_dict(
        vstate.sampler_state, state_dict["sampler_state"]
    )
    new_vstate.n_samples = state_dict["n_samples"]
    new_vstate.n_discard = state_dict["n_discard"]

    return new_vstate


serialization.register_serialization_state(
    MCMixedState,
    serialize_MCMixedState,
    deserialize_MCMixedState,
)
