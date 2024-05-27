#!/usr/bin/env python3

"""
Unit tests for the client.GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """
    Test cases for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        mock_get_json.return_value = org_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, org_payload)
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )

    @patch(
        'client.GithubOrgClient.org',
        new_callable=PropertyMock
    )
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url returns the correct value.
        """
        mock_org.return_value = org_payload
        client = GithubOrgClient('google')
        self.assertEqual(client._public_repos_url, org_payload['repos_url'])

    @patch('client.get_json')
    @patch(
        'client.GithubOrgClient._public_repos_url',
        new_callable=PropertyMock
    )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test that GithubOrgClient.public_repos returns the correct value.
        """
        mock_public_repos_url.return_value = 'http://test_url.com'
        mock_get_json.return_value = repos_payload

        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(), expected_repos)
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with('http://test_url.com')

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that GithubOrgClient.has_license returns the correct value.
        """
        client = GithubOrgClient('google')
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload,
     "expected_repos": expected_repos, "apache2_repos": apache2_repos},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the class for integration tests.
        """
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        mock_get.side_effect = cls.get_mocked_get

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the class after integration tests.
        """
        cls.get_patcher.stop()

    @classmethod
    def get_mocked_get(cls, url):
        """
        Mock the requests.get function to return the correct fixture payload.
        """
        if url == "https://api.github.com/orgs/google":
            return MockResponse(cls.org_payload)
        elif url == "https://api.github.com/orgs/google/repos":
            return MockResponse(cls.repos_payload)
        return MockResponse(None)

    def test_public_repos(self):
        """
        Test that GithubOrgClient.public_repos returns the expected results.
        """
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test that GithubOrgClient.public_repos with license returns
        the expected results.
        """
        client = GithubOrgClient('google')
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


class MockResponse:
    """
    Mock response class for requests.get.
    """
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


if __name__ == '__main__':
    unittest.main()
