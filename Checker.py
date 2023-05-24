#!/usr/bin/env python3
from requests import get
from json import dumps
from re import match
from base64 import b64decode
from Check_Task import check_file

def fetch_commit(github, repo):
    '''fetch committer'''
    try:
        repo = get(
            f'https://api.github.com/repos/{github}/{repo}/commits',
            headers={
                'Accept': 'application/vnd.github+json',
            }).json()[0]
        return  {
            'id': repo['sha'],
            **repo['commit']['committer'],
            'html_url': repo['html_url'],
            'login': repo['committer']['login']
        }
    except Exception as E:
        return False


def check_readme(github, repo, directory, commit_id):
    '''fetch ReadME'''
    return get(
        f'https://api.github.com/repos/{github}/{repo}/contents/{directory}/README.md?ref={commit_id}'
    ).json().get('name')


def fetch_file(github, repo, directory, file, commit_id='main'):
    '''fetch github'''
    return get(f'https://api.github.com/repos/{github}/{repo}/contents/{directory}/{file}?ref={commit_id}').json().get('content')


def check_content(file_text, file_length, conditions):
    '''Check Content'''
    lines = file_text.split('\n')
    if len(lines) != file_length:
        return {
            'status': False,
            'msg': 'Invalid File Length.',
            'STEP': 3
        }
    if lines[0] != '#!/bin/bash':
        return {
            'status': False,
            'msg': 'Invalid Sh-bang',
            'STEP': 4
        }
    arguments = lines[1].replace(', ', ',').replace(' ,', ',').split(' ')
    for key, condition in enumerate(conditions):
        if condition[0] == 0:
            if condition[1]['condition'] != arguments[condition[1]['a']:condition[1]['b']]:
                return {
                    'status': False,
                    'msg': f'{condition[1]["condition"]} Not Found.',
                    'STEP': key + 5
                }
        elif condition[0] == 1:
            for c in condition[1]['condition']:
                if not c in arguments[condition[1]['a']:]:
                    return {
                        'status': False,
                        'msg': f'{c} Not Found.',
                        'STEP': key + 5
                    }
        elif condition[0] == 2:
            acheived = False
            for c in condition[1]:
                if len(arguments) == c:
                    acheived = True
            if not acheived:
                return {
                    'status': False,
                    'msg': 'Invalid Arguments Length.',
                    'STEP': key + 5
                }
        elif condition[0] == 3:
            acheived = False
            for c in condition[1]['condition']:
                if set(c).issubset(arguments[condition[1]['a']:]):
                    acheived = True
            if not acheived:
                return {
                    'status': False,
                    'msg': f'{condition[1]["condition"]} Not Found.',
                    'STEP': key + 5
                }
    return {
        'status': True,
        'msg': 'All Condition has been passed',
        'STEP': len(conditions) + 5
    }


def checker(github, repo, directory, file, conditions):
    '''checker'''
    commit_info = fetch_commit(github, repo)
    if not commit_info:
        return {
            'status': False,
            'msg': 'Repo Not Found.',
            'STEP': 0
        }
    commit_info['file_name'] = file
    if not check_readme(github, repo, directory, commit_info['id']):
        return {
            **commit_info,
            'status': False,
            'msg': 'README Not Found.',
            'STEP': 1
        }
    file_content = fetch_file(github, repo, directory, file, commit_info['id'])
    if file_content:
        file_content = b64decode(file_content[:-1]).decode('utf-8')
    return check_file(conditions, file_content)