#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_org(self, mock_org):
        """Test GithubOrgClient.org method."""
        mock_org.return_value = {'login': 'google'}
        client = GithubOrgClient('google')
        self.assertEqual(client.org, {'login': 'google'})

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url method."""
        mock_org.return_value = {
            'repos_url': 'https://api.github.com/orgs/test_org/repos'
        }
        client = GithubOrgClient('test_org')
        result = client._public_repos_url

        # Breaking the line to fit within 79 characters
        expected_url = 'https://api.github.com/orgs/test_org/repos'
        self.assertEqual(result, expected_url)

    @patch('client.get_json')
    @patch(
        'client.GithubOrgClient._public_repos_url',
        new_callable=PropertyMock
    )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test GithubOrgClient.public_repos method."""
        mock_public_repos_url.return_value = 'https://mocked-url.com'
        mock_get_json.return_value = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]
        client = GithubOrgClient('test_org')
        result = client.public_repos()
        self.assertEqual(result, ['repo1', 'repo2', 'repo3'])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

        # Breaking the line to fit within 79 characters
        called_url = mock_get_json.call_args[0][0]
        self.assertEqual(called_url, 'https://mocked-url.com')


if __name__ == '__main__':
    unittest.main()
