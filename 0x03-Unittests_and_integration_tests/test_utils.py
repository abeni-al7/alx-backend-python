#!/usr/bin/env python3
'''A module for testing the utils module'''
import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    '''A class for testing access_nested_map function'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested: Mapping,
                               sequence: Sequence, expected: Any) -> None:
        '''Tests access_nested_map'''
        self.assertEqual(access_nested_map(nested, sequence), expected)
