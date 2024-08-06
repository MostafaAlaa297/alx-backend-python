#!/usr/bin/env python3
"""
test_client
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
import GithubOrgClient from client



class TestGithubOrgClient(unittest.TestCase):
    def test_org():
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

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(response, expected_response)
