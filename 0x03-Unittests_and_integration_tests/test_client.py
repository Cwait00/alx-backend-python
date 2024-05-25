#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from client import GithubOrgClient

# Mock function or object to replace org() behavior
mock_get_json = unittest.mock.Mock()


class TestGithubOrgClient(unittest.TestCase):

    @patch('client.get_json')
    def test_org(self, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        # Mock payload
        org_name = "testorg"
        expected_json = {"login": org_name}

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

    @patch('client.GithubOrgClient.org', new_callable=lambda: mock_get_json)
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url property of GithubOrgClient."""
        # Mock org payload
        org_name = "testorg"
        expected_payload = {"login": org_name}

        # Set the return value of the mock_org property to the expected payload
        mock_org.return_value = expected_payload

        # Initialize the client
        client = GithubOrgClient(org_name)

        # Access the _public_repos_url property
        public_repos_url = client._public_repos_url

        # Expected URL based on the mocked payload
        expected_url = f"https://api.github.com/orgs/{org_name}/repos"

        # Assert that the property returns the correct URL
        self.assertEqual(public_repos_url, expected_url)


if __name__ == '__main__':
    unittest.main()
