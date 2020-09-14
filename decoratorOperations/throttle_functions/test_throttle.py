#  Copyright (c)  2020, salesforce.com, inc.
#  All rights reserved.
#  SPDX-License-Identifier: BSD-3-Clause
#  For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

from time import sleep
from unittest import TestCase

from decoratorOperations import throttle


class Test(TestCase):
    def setUp(self):
        self.func1 = 0
        self.func2 = 0

    def tearDown(self) -> None:
        sleep(0.3)

    @throttle(0.2)
    def throttled_function_1(self, value):
        self.func1 = value

    @throttle(0.1)
    def throttled_function_2(self, value):
        self.func2 = value

    def test_calling_function_gives_value_immediately(self):
        self.throttled_function_1(3)
        assert self.func1 == 3

    def test_calling_function_gives_only_last_value(self):
        self.throttled_function_1(3)
        self.throttled_function_1(4)
        assert self.func1 == 3

    def test_different_functions_can_be_throttled(self):
        self.throttled_function_1(3)
        self.throttled_function_2(4)
        self.throttled_function_1(4)
        self.throttled_function_2(5)
        assert self.func1 == 3
        assert self.func2 == 4
        sleep(0.3)
        self.throttled_function_1(4)
        self.throttled_function_2(5)
        assert self.func1 == 4
        assert self.func2 == 5
