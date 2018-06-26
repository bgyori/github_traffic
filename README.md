Download GitHub traffic statistics for a repo
=============================================
GitHub doesn't show visitor and clone statistics for repos beyond two weeks.
The purpose of this script is to periodically download these statistics and store
them locally. Note that PyGithub currently doesn't natively support
getting traffic statistics.

Installation
============
```python
git clone https://github.com/bgyori/github_traffic.git
cd github_traffic
pip install -r requirements.txt
```

Also, you need to generate an access token on your GitHub profile:
https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/
and save it in a file called `token` in your github\_traffic folder.

Usage
=====
```python
python download_repo_traffic.py <owner_name> <repo_name>
```
which creates 4 time stamped JSON files for the following traffic
statistics: visitors, clones, referrers, paths
