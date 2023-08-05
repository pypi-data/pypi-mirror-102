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
import functools
import inspect


def deprecated(reason=None):
    r"""
    This is a decorator which can be used to mark functions as deprecated. It
    will result in a warning being emitted when the function is used.
    """

    def decorator(func):
        object_type = "class" if inspect.isclass(func) else "function"
        message = "Call to deprecated {} {!r}".format(object_type, func.__name__)
        if reason is not None:
            message += " ({})".format(reason)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(message, category=FutureWarning, stacklevel=2)
            return func(*args, **kwargs)

        return wrapper

    return decorator


def warn_deprecation(message):
    r"""
    This is a function that sends a deprecation warning to the user about a
    function that will is now deprecated and will be removed in a future
    major release.

    :param message: A mandatory message documenting the deprecation.
    """
    warnings.warn(message, category=FutureWarning, stacklevel=2)


def deprecated_new_name(message):
    def deprecated_decorator(func):
        @functools.wraps(func)
        def deprecated_func(*args, **kwargs):
            warnings.warn(
                (
                    "{} has been renamed to {}. The old name is "
                    "now deprecated and will be removed in the next minor version.\n"
                    "Please update your code."
                ).format(func.__name__, message),
                category=FutureWarning,
                stacklevel=2,
            )
            return func(*args, **kwargs)

        return deprecated_func

    return deprecated_decorator


from functools import wraps


def wraps_legacy(legacy_fun, argname, argtype):
    """
    Wraps a function with the same name as a legacy function
    taking as a first argument a legacy machine, and if so
    forwards the call to the legacy function.
    """

    def decorator(fun):
        @functools.wraps(fun)
        def maybe_legacy_fun(*args, **kwargs):
            if len(args) > 0:
                if isinstance(args[0], argtype):
                    return legacy_fun(*args, **kwargs)
            elif argname in kwargs:
                if isinstance(args[0], argtype):
                    return legacy_fun(*args, **kwargs)

            return fun(*args, **kwargs)

        return maybe_legacy_fun

    return decorator
