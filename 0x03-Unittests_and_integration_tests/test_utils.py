#!/usr/bin/env python3
""" Unit test for utils."""


import unittest
from parameterized import parameterized
from utils import access_nested_map
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Class that inherit from unittest.TestCase."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """ Method to test that the method returns the correct output"""
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, result):
        """ Method to test that a KeyError is raised"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, result)


class TestGetJson(unittest.TestCase):
    """ Class that inherits from unittest.TestCase."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Method to test utils.get_json returns the expected result."""
        with patch("requests.get") as request:
            request.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)
