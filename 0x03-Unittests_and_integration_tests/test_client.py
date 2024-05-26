#!/usr/bin/env python3
import unittest
from unittest.mock import patch, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up the integration test class"""
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        mock_get.side_effect = cls.side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down the integration test class"""
        cls.get_patcher.stop()

    @staticmethod
    def side_effect(url):
        """Side effect method for requests.get"""
        if url == 'https://api.github.com/orgs/test_org':
            return MagicMock(json=lambda: org_payload)
        elif url == 'https://api.github.com/orgs/test_org/repos':
            return MagicMock(json=lambda: repos_payload)
        return MagicMock(json=lambda: None)

    def test_public_repos(self):
        """Test the public_repos method"""
        client = GithubOrgClient('test_org')
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with the license argument"""
        client = GithubOrgClient('test_org')
        self.assertEqual(
            client.public_repos(license="apache-2.0"), self.apache2_repos
        )


if __name__ == '__main__':
    unittest.main()
