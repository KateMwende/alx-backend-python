#!/usr/bin/env python3
"""
Testing Client file
"""
from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """Test client with unittest"""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, Mock):
        """Test GithubOrgClient returs correct value"""
        test_sample = GithubOrgClient(input)
        test_sample.org()
        Mock.assert_called_once_with(f"https://api.github.com/orgs/{input}")


if __name__ == '__main__':
    unittest.main()
