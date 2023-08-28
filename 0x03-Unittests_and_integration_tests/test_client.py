#!/usr/bin/env python3
"""
Testing Client file
"""
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock


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

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is
        the expected one based on the mocked payload.
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            payload = {"repos_url": "hey"}
            mock.return_value = payload
            test_sample = GithubOrgClient('trial')
            result = test_sample._public_repos_url
        self.assertEqual(result, payload["repos_url"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, answer):
        """unit test for GithubOrgClient.has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
