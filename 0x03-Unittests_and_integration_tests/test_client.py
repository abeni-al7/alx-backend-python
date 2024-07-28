#!/usr/bin/env python3
"""A module for testing the client module"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """A class for testing the GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, url: str, mock_json):
        """A method for testing the org method"""
        test_client = GithubOrgClient(url)
        expected_url = f"https://api.github.com/orgs/{url}"
        mock_json.return_value = {"repo_url": f"https://api.github.com/orgs/{url}/repos"}
        result = test_client.org
        mock_json.assert_called_once_with(expected_url)
        self.assertEqual(result, {"repo_url": f"https://api.github.com/orgs/{url}/repos"})
