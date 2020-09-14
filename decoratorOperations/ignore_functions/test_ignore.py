#  Copyright (c)  2020, salesforce.com, inc.
#  All rights reserved.
#  SPDX-License-Identifier: BSD-3-Clause
#  For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

from unittest import TestCase

from decoratorOperations import ignore


class Test(TestCase):
    def setUp(self):
        self.func1 = 0
        self.func2 = 0

    @ignore()
    def ignored_function_1(self, value):
        self.func1 = value

    @ignore()
    def ignored_function_2(self, value):
        self.func2 = value

    def test_calling_function_gives_value_after_time(self):
        self.ignored_function_1(3)
        assert self.func1 == 0

    def test_different_functions_can_be_ignored(self):
        self.ignored_function_1(3)
        self.ignored_function_2(4)
        assert self.func1 == 0
        assert self.func2 == 0
