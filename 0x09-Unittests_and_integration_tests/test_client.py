#!/usr/bin/env python3
""" Unittest module """

from unittest import TestCase, mock
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
import client
from client import GithubOrgClient
import requests
from utils import access_nested_map, get_json, memoize


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

    def test_public_repos_url(self):
        ''' Test GithubOrgClient.public_repos_url property. '''

        with mock.patch('client.GithubOrgClient._public_repos_url',
                        new_callable=mock.PropertyMock) as m:
            m.return_value = 'test'

            goc = GithubOrgClient('buttercup')
            pru = goc._public_repos_url
            self.assertEqual(pru, 'test')

    @patch('client.get_json')
    def test_public_repos(self, get_json_mock):
        """ test that the list of repos is what you expect from the chosen
            payload. the public repos
        """
        jeff = {"name": "Jeff", "license": {"key": "a"}}
        bobb = {"name": "Bobb", "license": {"key": "b"}}
        suee = {"name": "Suee"}
        to_mock = 'client.GithubOrgClient._public_repos_url'
        get_json_mock.return_value = [jeff, bobb, suee]
        with patch(to_mock, PropertyMock(return_value="www.yes.com")) as y:
            x = GithubOrgClient("x")
            self.assertEqual(x.public_repos(), ['Jeff', 'Bobb', 'Suee'])
            self.assertEqual(x.public_repos("a"), ['Jeff'])
            self.assertEqual(x.public_repos("c"), [])
            self.assertEqual(x.public_repos(45), [])
            get_json_mock.assert_called_once_with("www.yes.com")
            y.assert_called_once_with()
