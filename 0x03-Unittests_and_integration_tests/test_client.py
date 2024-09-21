#!/usr/bin/env python3
"""
test_client
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient  # Correct the import syntax

class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google", "id": 1}),
        ("abc", {"login": "abc", "id": 2}),
    ])
    @patch('client.get_json', autospec=True)  # This should be applied after parameterized
    def test_org(self, org_name, expected_response, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = expected_response

        client = GithubOrgClient(org_name)
        response = client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
