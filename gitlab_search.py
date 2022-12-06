#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
gitlab_search.py
simple script to search for a script in all your repos/branches on a gitlab environment
python3 gitlab_search.py -h for usage
"""

import requests
import time
import argparse

global headers, api_url, sleep_time, search_text


def prepare_vars():
    """
    Prepare all global vars
    :return:
    """
    global headers, api_url, sleep_time, search_text
    parser = argparse.ArgumentParser(description='Search a string into all your repos/branches in GitLab')
    parser.add_argument('--gitlab_api_url',
                        help='Your gitlab API url (if self hosted/entreprise)',
                        default='https://gitlab.example.com/api/v4/',
                        dest='api_url',
                        type=str)
    parser.add_argument('--request_sleep', help='Time to wait between two requests (in seconds, ex 0.1)',
                        default=0,
                        dest='sleep_time',
                        type=float)
    parser.add_argument('--gitlab_token',
                        help='Your gitlab token (api read)',
                        required=True
                        )
    parser.add_argument('--search_string',
                        help='String to search',
                        required=True)

    args = parser.parse_args()

    token = args.gitlab_token
    headers = {'PRIVATE-TOKEN': token}
    api_url = args.api_url
    sleep_time = args.sleep_time
    search_text = args.search_string


def launch_request(myurl):
    """
    Call the Gitlab API
    Makes a GET call and returns the return as dict
    :param myurl: The url of the PI to call
    :return: result dict
    """
    r = requests.get(myurl, headers=headers)
    r.raise_for_status()
    return r.json()


def get_groups():
    """
    List groups available for the token
    :return: group dict
    """
    return launch_request(api_url + 'groups')


def get_projects(mygroup):
    """
    List projects for a specific group
    :param mygroup: Group ID
    :return: projects dict
    """
    return launch_request(api_url + 'groups/' + str(mygroup) + '/projects')


def get_branches(myproject):
    """
    List branches for a project
    :param myproject: Project ID
    :return: branch dict
    """
    return launch_request(api_url + 'projects/' + str(myproject) + '/repository/branches')


def get_search(myproject, mybranch):
    """
    Search for a string into a specific branch of a project
    :param myproject: project id
    :param mybranch: branch name
    :return: search dict
    """
    return launch_request(api_url + 'projects/' + str(myproject) + '/search?scope=blobs&search=' + search_text + '&ref=' + mybranch)


if __name__ == '__main__':
    prepare_vars()
    groups = get_groups()
    for group in groups:
        projects = get_projects(group['id'])
        for project in projects:
            branches = get_branches(project['id'])
            for branch in branches:
                search_results = get_search(project['id'], branch['name'])
                for my_result in search_results:
                    print("Found in project " + project['name'] + ", branch " + branch['name'] + " in file " + my_result["basename"])
                time.sleep(sleep_time)
    print(' -- Over --')


