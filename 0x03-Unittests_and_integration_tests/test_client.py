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
        mock_json.return_value = {
            "repo_url": f"https://api.github.com/orgs/{url}/repos"}
        result = test_client.org
        mock_json.assert_called_once_with(expected_url)
        self.assertEqual(result, {
            "repo_url": f"https://api.github.com/orgs/{url}/repos"})

    def test_public_repos_url(self):
        """Tests public_repos_url method"""
        test_payload = "https://api.github.com/orgs/google/repos"
        with patch(
          "client.GithubOrgClient.org", return_value=test_payload) as mock_url:
            result = mock_url()
            self.assertEqual(result, test_payload)

    @patch("client.get_json")
    def test_public_repos(self, mock_json):
        """Tests the public_repos method"""
        mock_json.return_value = {"id": "1", "name": "Ab"}
        value = mock_json("https://example.com")
        self.assertEqual(value, {"id": "1", "name": "Ab"})
        test_payload = {
                "license": {
                    "key": "apache"
                }
            }
        with patch(
          "client.GithubOrgClient._public_repos_url",
          return_value=test_payload) as mock_url:
            result = mock_url("apache")
            self.assertEqual(result, test_payload)
            mock_url.assert_called_once()
        mock_json.assert_called_once()
