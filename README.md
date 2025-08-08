# GitHub User Activity Viewer

A simple Python script that fetches and displays recent commit messages from a GitHub user's public events using the GitHub API.

## Usage

```bash
python githubAPIactivity.py USERNAME
````
Replace USERNAME with the GitHub username you want to check.


## Requirements:
Python 3
requests library

Install dependencies with:
```bash
pip install requests
````
Only shows commit messages from PushEvent types.

Handles invalid usernames and API errors gracefully

This was an excersise from: https://roadmap.sh/projects/github-user-activity
