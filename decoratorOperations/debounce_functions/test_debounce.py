#  Copyright (c)  2020, salesforce.com, inc.
#  All rights reserved.
#  SPDX-License-Identifier: BSD-3-Clause
#  For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

from time import sleep
from unittest import TestCase

from decoratorOperations import debounce


class Test(TestCase):
    def setUp(self):
        self.func1 = 0
        self.func2 = 0

    @debounce(0.3)
    def debounced_function_1(self, value):
        self.func1 = value

    @debounce(0.1)
    def debounced_function_2(self, value):
        self.func2 = value

    def test_calling_function_gives_value_after_time(self):
        self.debounced_function_1(3)
        assert self.func1 == 0
        sleep(0.4)
        assert self.func1 == 3

    def test_calling_function_gives_only_last_value(self):
        self.debounced_function_1(3)
        self.debounced_function_1(4)
        assert self.func1 == 0
        sleep(0.4)
        assert self.func1 == 4

    def test_different_functions_can_be_debounced(self):
        self.debounced_function_1(3)
        self.debounced_function_2(4)
        self.debounced_function_1(4)
        sleep(0.2)
        assert self.func1 == 0
        assert self.func2 == 4
        sleep(0.2)
        assert self.func1 == 4
