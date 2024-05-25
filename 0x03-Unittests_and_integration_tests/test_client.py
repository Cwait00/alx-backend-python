#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos method."""

        mock_payload = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]

        mock_get_json.return_value = mock_payload

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=property
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'https://mocked-url.com'

            client = GithubOrgClient('test_org')
            result = client.public_repos()

            self.assertEqual(result, ['repo1', 'repo2', 'repo3'])
            mock_get_json.assert_called_once()
            self.assertEqual(
                mock_get_json.call_args[0][0],
                'https://mocked-url.com'
            )


if __name__ == '__main__':
    unittest.main()
