import requests
import os
from dotenv import load_dotenv

load_dotenv()
os.environ.get("GITHUB_TOKEN")
HEADERS = {"Authorization": f"token {os.environ.get('GITHUB_TOKEN')}"}

BASE_URL = "https://api.example.com/data"

def get_top_repos():
    url = "https://api.github.com/search/repositories"
    params = {"q": "stars:>10000", "sort": "stars", "order": "desc", "per_page": 10}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    return response.json()["items"]

def get_bug_issues(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    params = {"labels": "bug", "state": "open", "per_page": 1}
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    issues = response.json()
    if issues:
        return issues[0].get("title", "No title found") + "\n\n" + issues[0].get("body", "")
    return "none"

def main():
    repos = get_top_repos()
    for repo in repos:
        fullname = repo["full_name"]
        stars = repo["stargazers_count"]
        print("-------------------------------------------------")
        print(f"{fullname}, Stars: {stars}")
        print("Bug Issue:")
        owner, name = fullname.split('/')
        print(get_bug_issues(owner, name))
    print("-------------------------------------------------")

if __name__ == "__main__":
    main()