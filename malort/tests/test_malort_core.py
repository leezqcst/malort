# -*- coding: utf-8 -*-
"""
Malort Core Tests

Test Runner: PyTest

Notes:
* Expected values for string samples are any values that the sample
could contain, not the exact values.

"""
import os

import malort as mt
from malort.test_helpers import TestHelpers, TEST_FILES_1, TEST_FILES_2


class TestCore(TestHelpers):

    def test_files_1(self):
        mtresult = mt.analyze(TEST_FILES_1)
        expected = {
        'charfield': {'str': {'count': 4, 'max': 11, 'mean': 11.0,
                              'min': 11, 'sample': ['fixedlength']}},
        'floatfield': {'float': {'count': 4, 'max': 10.8392, 'mean': 5.243,
                                 'min': 2.345, 'max_precision': 6,
                                 'max_scale': 4, 'fixed_length': False}},
        'intfield': {'int': {'count': 4, 'max': 20, 'mean': 12.5,
                             'min': 5}},
        'varcharfield': {'str': {'count': 4, 'max': 12, 'mean': 7.5,
                                 'min': 3,
                                 'sample': ['var', 'varyin', 'varyingle',
                                            'varyinglengt']}}
        }
        self.assert_stats(mtresult.stats, expected)
        self.assertDictEqual(mtresult.get_conflicting_types(), {})

    def test_files_2(self):
        mtresult = mt.analyze(TEST_FILES_2, '|')
        expected = {
            'bar': {'bool': {'count': 1},
                    'float': {'count': 2, 'max': 4.0, 'mean': 3.0, 'min': 2.0,
                              'max_precision': 2, 'max_scale': 1,
                              'fixed_length': True},
                    'str': {'count': 1, 'max': 3, 'mean': 3.0, 'min': 3,
                            'sample': ['bar']}},
            'baz': {'int': {'count': 2, 'max': 2, 'mean': 1.5, 'min': 1},
                    'str': {'count': 2, 'max': 5, 'mean': 5.0, 'min': 5,
                            'sample': ['fixed']}},
            'foo': {'int': {'count': 2, 'max': 1000, 'mean': 505.0, 'min': 10},
                    'str': {'count': 2, 'max': 3, 'mean': 3.0, 'min': 3,
                            'sample': ['foo']}},
            'qux': {'int': {'count': 1, 'max': 10, 'mean': 10.0, 'min': 10},
                    'str': {'count': 3, 'max': 9, 'mean': 6.0, 'min': 3,
                            'sample': ['var', 'varyin', 'varyingle']}}
        }
        self.assert_stats(mtresult.stats, expected)
        self.assert_stats(mtresult.get_conflicting_types(), expected)