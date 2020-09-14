#  Copyright (c)  2020, salesforce.com, inc.
#  All rights reserved.
#  SPDX-License-Identifier: BSD-3-Clause
#  For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause


def filter(lambda_function):
    """
    Decorator that will filter a function given its parameters and the lambda function specified.
    See the test_filter.py file for examples
    """

    def decorator(function):
        def filterd(*args, **kwargs):
            def call_function():
                return function(*args, **kwargs)

            try:
                if lambda_function(*args[1:], **kwargs):
                    call_function()
            except TypeError as exc:
                raise TypeError(
                    "Different number of parameters between filter and method"
                ) from exc

        return filterd

    return decorator
