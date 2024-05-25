#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @patch('client.get_json')
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    def test_org(self, org_name, expected_json, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""

        # Configure mock behavior
        mock_get_json.return_value = expected_json

        # Initialize the client
        client = GithubOrgClient(org_name)

        # Call the org method
        result = client.org()

        # Assert that get_json was called once with the expected URL
        expected_url = f"https://api.github.com/orgs/{org_name}"
        mock_get_json.assert_called_once_with(expected_url)

        # Assert that the org method returns the expected JSON
        self.assertEqual(result, expected_json)


if __name__ == '__main__':
    unittest.main()
