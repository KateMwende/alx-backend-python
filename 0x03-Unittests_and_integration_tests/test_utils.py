#!/usr/bin/env python3
"""
Unit test for utlis file
"""
import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Testing the nested map with unit test
    Args: import unittest
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """compare nested map with mapping"""
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         exception_message):
        """test that a KeyError is raised"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
            self.assertEqual(str(context.exception), str(exception_message))


class TestGetJson(unittest.TestCase):
    """Get ajson response from url test"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Make sure it returns a Mock object with a json method"""
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload
        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestClass:
    """Test class"""
    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        """Test if memoization works"""
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """Test memoization()"""
    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """Test memoization()"""
        mock_a_method.return_value = 42

        test_obj = TestClass()
        result_1 = test_obj.a_property
        result_2 = test_obj.a_property

        mock_a_method.assert_called_once()

        self.assertEqual(result_1, 42)
        self.assertEqual(result_2, 42)


if __name__ == '__main__':
    unittest.main()
