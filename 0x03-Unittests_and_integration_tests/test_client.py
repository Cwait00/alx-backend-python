#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )
        self.assertEqual(result, expected)

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct URL."""
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': 'https://api.github.com/orgs/test_org/repos'
            }

            client = GithubOrgClient('test_org')
            result = client._public_repos_url

            self.assertEqual(
                result, 'https://api.github.com/orgs/test_org/repos'
            )

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test GithubOrgClient.public_repos method."""
        mock_get_json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]

        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = 'https://mocked-url.com'

            client = GithubOrgClient('test_org')
            repos = client.public_repos()

            mock_get_json.assert_called_once_with(
                'https://mocked-url.com'
            )

            self.assertEqual(repos, [{'name': 'repo1'}, {'name': 'repo2'}])
            self.assertEqual(
                mock_get_json.call_args[0][0], 'https://mocked-url.com'
            )
            self.assertEqual(mock_public_repos_url.call_count, 1)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test GithubOrgClient.has_license method."""
        client = GithubOrgClient('test_org')
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
