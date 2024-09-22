#!/usr/bin/env python3
"""
test_client
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google", "id": 1}),
        ("abc", {"login": "abc", "id": 2}),
    ])
    @patch('client.get_json', autospec=True)
    def test_org(self, org_name, expected_response, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = expected_response

        client = GithubOrgClient(org_name)
        response = client.org

        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(response, expected_response)

    def test_public_repos_url(self):
        """Test that
        GithubOrgClient._public_repos_url returns the correct repos URL."""
        expected_repos_url = "https://api.github.com/orgs/google/repos"
        with mock.patch(
               'GithubOrgClient._public_repos_url', new_callable=PropertyMock
               ) as mock_org:
            mock_org.return_value = {"repos_url": expected_repos_url}

            client = GithubOrgClient("google")

            self.assertEqual(client._public_repos_url, expected_repos_url)

    @patch('client.get_json', autospec=True)
    def test_public_repos(self):
        """
        Test that GithubOrgClient._public_repos_url
        returns the correct list of repos.

        Mocks:
            - GithubOrgClient._public_repos_url to return a fake repos URL.
            - get_json to return a predefined list of repositories.

        validates:
            - The returned list of repositories matches the mocked response
            - _public_repos_url  and get_json are called exactly once
        """
        expected_repos = ["repo1", "repo2"]
        expected_repos_url = "https://api.github.com/orgs/google/repos"

        with mock.patch(
                'GithubOrgClient._public_repos_url', new_callable=PropertyMock
                ) as mock_repo_url:
            mock_repo_url.return_value = expected_repos_url
            mock_get_json.return_value = expected_repos

            client = GithubOrgClient("google")

            repos = client.public_repos()

            self.assertEqual(repos, expected_repos)

            mock_repo_url.assert_called_once()


            mock_get_json.assert_called_once_with(expected_repos_url)

if __name__ == '__main__':
    unittest.main()
