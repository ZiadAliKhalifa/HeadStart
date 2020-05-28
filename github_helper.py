import requests
import config
import json

from github import Github
from colorama import Fore, Back, Style


class GithubHelper:
    def __init__(self,  token):
        self.auth_user = Github(login_or_token=token)
        print("Logged in!")

    def create_new_repo(self, repo_name, token, description, is_private):
        if self._check_if_repo_exists(repo_name) == True:
            print(
                Fore.RED + "Repository already exists on GitHub!" + Style.RESET_ALL)
            repo_name += "-Headstart"
            print(
                f"Renaming repository to {repo_name}")

        print(Fore.GREEN + "Creating GitHub Repository..." + Style.RESET_ALL)
        return self._create_repo_api(repo_name, token,
                                     description, is_private)

    def _check_if_repo_exists(self, repoName):
        # Get all user repos
        user_repos = self.auth_user.get_user().get_repos()
        user_repo_names = [repo.name for repo in user_repos]
        # Returns true if a user already has a repository with the same name
        return repoName in user_repo_names

    def _create_repo_api(self, repo_name, token, description, is_private):
        url = "https://api.github.com/user/repos"
        body = json.dumps({
            "name": repo_name,
            "description": description,
            "homepage": "https://github.com",
            "private": is_private
        })
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "text/plain"
        }

        response = requests.post(url, data=body, headers=headers)
        print(response)
        return response
