import re
from github import Github

def parse_repo_url(repo_url: str):
    """
    Extract owner and repository name from GitHub URL
    """
    match = re.search(r"github.com/([^/]+)/([^/]+)", repo_url)
    if not match:
        raise ValueError("Invalid GitHub repository URL")
    return match.group(1), match.group(2)

def fetch_repo_data(repo_url: str):
    """
    Fetch basic repository signals using GitHub API
    """
    g = Github()  # unauthenticated access
    owner, repo_name = parse_repo_url(repo_url)
    repo = g.get_repo(f"{owner}/{repo_name}")

    contents = repo.get_contents("")
    file_count = 0
    has_tests = False
    has_readme = False

    while contents:
        item = contents.pop(0)
        if item.type == "dir":
            if "test" in item.path.lower():
                has_tests = True
            contents.extend(repo.get_contents(item.path))
        else:
            file_count += 1
            if "readme" in item.name.lower():
                has_readme = True

    commit_count = repo.get_commits().totalCount

    return {
        "repo_name": repo_name,
        "owner": owner,
        "language": repo.language,
        "file_count": file_count,
        "has_readme": has_readme,
        "has_tests": has_tests,
        "commit_count": commit_count
    }
