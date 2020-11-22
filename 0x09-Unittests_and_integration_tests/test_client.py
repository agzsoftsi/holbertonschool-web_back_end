#!/usr/bin/env python3
""" Unittest module """

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized

import client
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """ Class for testing GithubOrgClient """

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """ Test method returns correct output """
        gc = GithubOrgClient(org_name)
        gc.org()
        mock_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )
