#  Copyright (c)  2020, salesforce.com, inc.
#  All rights reserved.
#  SPDX-License-Identifier: BSD-3-Clause
#  For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause

from unittest import TestCase

import pytest

from decoratorOperations import filter


def filter_function(x):
    return True


class Test(TestCase):
    def setUp(self):
        self.func1 = 0
        self.func2 = 0
        self.func3 = 0

    @filter(lambda x, y: x > 2)
    def filtered_function_1(self, value, value2):
        self.func1 = value + value2

    @filter(lambda x: x < 10)
    def filtered_function_2(self, value):
        self.func2 = value

    @filter(filter_function)
    def filtered_function_3(self, value):
        self.func3 = value

    def test_filter_function(self):
        self.filtered_function_1(2, 3)
        assert self.func1 == 0

    def test_wrong_number_arguments(self):
        with pytest.raises(TypeError):
            self.filtered_function_1(2)

    def test_filter_works_with_function(self):
        self.filtered_function_3(1)
        assert self.func3 == 1

    def test_different_functions_can_be_filtered(self):
        self.filtered_function_1(1, 4)
        self.filtered_function_2(4)
        assert self.func1 == 0
        assert self.func2 == 4

        self.filtered_function_1(3, 4)
        self.filtered_function_2(11)
        assert self.func1 == 7
        assert self.func2 == 4
