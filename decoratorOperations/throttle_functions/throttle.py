#  Copyright (c)  2020, salesforce.com, inc.
#  All rights reserved.
#  SPDX-License-Identifier: BSD-3-Clause
#  For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

import time


def throttle(wait_time):
    """
    Decorator that will throttle a function so that it is called only once every wait_time seconds
    If it is called multiple times, will run only the first time.
    See the test_throttle.py file for examples
    """

    def decorator(function):
        def throttled(*args, **kwargs):
            def call_function():
                return function(*args, **kwargs)

            if time.time() - throttled._last_time_called >= wait_time:
                call_function()
                throttled._last_time_called = time.time()

        throttled._last_time_called = 0
        return throttled

    return decorator
