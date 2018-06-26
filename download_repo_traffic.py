import sys
import time
import json
import datetime
from github import Github


traffic_endpoints = ['clones', 'views', 'popular/referrers', 'popular/paths']


def read_token():
    with open('token', 'r') as fh:
        token = fh.read().strip()
    return token


def get_traffic_data(repo, endpoint):
    headers, data = repo._requester.requestJsonAndCheck('GET',
        traffic_url + '/' + endpoint)
    return data


if __name__ == '__main__':
    # Get parameters
    if len(sys.argv) < 3:
        print('Usage: download_repo_traffic.py repo_owner repo_name')
        sys.exit(1)
    repo_owner = sys.argv[1]
    repo_name = sys.argv[2]

    # Connect to the repo using token
    token = read_token()
    g = Github(token)
    repo = g.get_repo('%s/%s' % (repo_owner, repo_name))

    # Get all the data for each traffic endpoint
    traffic_url = '/repos/%s/%s/traffic' % (repo_owner, repo_name)
    timestamp = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    for endpoint in traffic_endpoints:
        data = get_traffic_data(repo, endpoint)
        # Dump the data into JSONs
        fname = '%s_%s.json' % (timestamp, endpoint.replace('/', '_'))
        with open(fname, 'w') as fh:
            json.dump(data, fh, indent=1)
