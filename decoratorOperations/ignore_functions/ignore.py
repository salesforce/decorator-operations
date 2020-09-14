#  Copyright (c)  2020, salesforce.com, inc.
#  All rights reserved.
#  SPDX-License-Identifier: BSD-3-Clause
#  For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause


def ignore():
    """
    Decorator that will make a function call be ignored.
    """

    def decorator(function):
        def ignored(*args, **kwargs):
            """
            Empty because serves only as to ignore function call
            """
            pass

        return ignored

    return decorator
