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

import netket as nk
import netket.nn.linear as linear

import jax.numpy as jnp
import numpy as np
import scipy.sparse

import pytest


def _setup_symm(symmetries, N):
    hi = nk.hilbert.Spin(1 / 2, N)

    g = nk.graph.Chain(N)
    if symmetries == "trans":
        # Only translations, N_symm = N_sites
        perms = g.translations()
    else:
        # All chain automorphisms, N_symm = 2 N_sites
        perms = g.automorphisms()

    return g, hi, np.asarray(perms)


@pytest.mark.parametrize("symmetries", ["trans", "autom"])
@pytest.mark.parametrize("use_bias", [True, False])
def test_DenseSymm(symmetries, use_bias):
    g, hi, perms = _setup_symm(symmetries, N=8)

    ma = nk.nn.create_DenseSymm(
        symmetries=perms,
        features=8,
        use_bias=use_bias,
        bias_init=nk.nn.initializers.uniform(),
    )
    pars = ma.init(nk.jax.PRNGKey(), hi.random_state(1))

    v = hi.random_state(3)
    vals = [ma.apply(pars, v[..., p]) for p in perms]
    for val in vals:
        assert jnp.allclose(jnp.sum(val, -1), jnp.sum(vals[0], -1))


@pytest.mark.parametrize("symmetries", ["trans", "autom"])
@pytest.mark.parametrize("features", [1, 2, 5])
def test_symmetrizer(symmetries, features):
    _, _, perms = _setup_symm(symmetries, N=8)

    n_symm, n_sites = perms.shape
    n_hidden = features * n_symm

    # symmetrization tensor entries
    def symmetrizer_ijkl(i, j, k, l):
        jsymm = np.floor_divide(j, n_symm)
        cond_k = k == np.asarray(perms)[j % n_symm, i]
        cond_l = l == jsymm
        return np.asarray(np.logical_and(cond_k, cond_l), dtype=int)

    symmetrizer = np.asarray(
        np.fromfunction(
            symmetrizer_ijkl,
            shape=(n_sites, n_hidden, n_sites, features),
            dtype=np.intp,
        ),
    ).reshape(-1, features * n_sites)
    symmetrizer = scipy.sparse.coo_matrix(symmetrizer)

    # Of the COO matrix attributes, rows is just a range [0, ..., n_rows)
    # and data is [1., ..., 1.]. Only cols is non-trivial.
    assert np.all(symmetrizer.row == np.arange(symmetrizer.shape[0]))
    assert np.all(symmetrizer.data == 1.0)
    assert np.all(symmetrizer.col == linear._symmetrizer_col(perms, features))
