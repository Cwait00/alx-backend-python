#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @patch('client.get_json')
    @patch('client.GithubOrgClient.org')
    def test_public_repos(self, mock_org, mock_get_json):
        mock_get_json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]

        mock_org.return_value = MagicMock()
        mock_org.return_value.repos_url = (
            'https://api.github.com/orgs/test_org/repos'
        )

        with patch('client.GithubOrgClient._public_repos_url', new_callable=property) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'https://mocked-url.com'

            client = GithubOrgClient('test_org')
            repos = client.public_repos()

            mock_org.assert_called_once()
            mock_get_json.assert_called_once_with(
                'https://mocked-url.com'
            )  # Check get_json call

            self.assertEqual(repos, [{'name': 'repo1'}, {'name': 'repo2'}])
            self.assertEqual(
                mock_get_json.call_args[0][0], 'https://mocked-url.com'
            )
            self.assertEqual(mock_public_repos_url.call_count, 1)


if __name__ == '__main__':
    unittest.main()
