#!/usr/bin/env python3
"""
test_client
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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
        """Test that GithubOrgClient._public_repos_url
        returns the correct repos URL."""
        expected_repos_url = "https://api.github.com/orgs/google/repos"
        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock
                ) as mock_org:
            mock_org.return_value = expected_repos_url

            client = GithubOrgClient("google")

            self.assertEqual(client._public_repos_url, expected_repos_url)

    @patch('client.get_json', autospec=True)
    def test_public_repos(self, mock_get_json):
        """
        Test that GithubOrgClient.public_repos
        returns the correct list of repositories.

        Mocks:
        - GithubOrgClient._public_repos_url to return a fake repos URL.
        - get_json to return a predefined list of repositories.

        Validates:
        - The returned list of repositories matches the mocked response.
        - _public_repos_url and get_json are called exactly once.
        """
        expected_repos = ["repo1", "repo2"]
        expected_repos_url = "https://api.github.com/orgs/google/repos"

        # Mock _public_repos_url and get_json
        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock
                ) as mock_repo_url:
            mock_repo_url.return_value = expected_repos_url
            mock_get_json.return_value = expected_repos

            client = GithubOrgClient("google")

            # Call public_repos and check result
            repos = client.public_repos()
            self.assertEqual(repos, expected_repos)

            # Assert the mocks were called correctly
            mock_repo_url.assert_called_once()
            mock_get_json.assert_called_once_with(expected_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": None}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test that GithubOrgClient.has_license
        checks if the repo has the specified license.

        Args:
            repo (dict): Repository info
            license_key (str): License key to check
            expected_result (bool): Expected return value
        """
        client = GithubOrgClient("google")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
    ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test GithubOrgClient"""
    @classmethod
    def setUpClass(cls):
        """Set up the patcher for requests.get and mock the response."""
        cls.get_patcher = patch('request.get', autospec=True)

        cls.mock_get = cls.get_patcher.start()

    def get_json_side_effect(url):
        if url == f"https://api.github.com/orgs/google":
            return cls.org_payload
        elif url = f"https://api.github.com/orgs/google/repos":
            return cls.repos_payload
        return None

    cls.mock_get.return_value.json.side_effect = get_json_side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher after all tests."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos
        method with the mocked payload."""
        client = GithumOrgClient("google")
        repos = client.public_repos(repolicense="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
