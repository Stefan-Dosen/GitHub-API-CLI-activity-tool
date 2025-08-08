import requests
import sys

if len(sys.argv) < 2:
    print("No command provided. Type 'python githubAPIactivity.py' USERNAME ")
    sys.exit()
    
username = sys.argv[1]


request = requests.get(f"https://api.github.com/users/{username}/events")

if request.status_code != 200:
    print(f"Error: {request.status_code} - {request.reason}")
    sys.exit()
    

data = request.json()
for event in data:
    repo_name = event.get("repo", {}).get("name", "")  #gets the repository name or returns an empty dict/string
    if event['type'] == 'PushEvent':
        for commit in event.get("payload", {}).get("commits", []):
            message = commit['message']
            print(f"{message} in {repo_name}")