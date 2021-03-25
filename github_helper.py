from typing import Type
import requests
import json

from colorama import Fore, Back, Style

from constants import GITHUB_BASE_API


class GithubHelper:

    auth_user = None
    token = None

    def __init__(self,  token):
        # Logs in with token and sets "auth user" as the authinticated user
        # self.auth_user = Github(login_or_token=token)
        response = requests.get(url=GITHUB_BASE_API + "/user", headers={
            'Authorization': 'Bearer ' + token
        })

        if response.status_code == 200:
            self.auth_user = response.json()
            self.token = token

            print("Logged in!")
        else:
            print(
                Fore.RED + "You might have provided a wrong token. Please try again" + Style.RESET_ALL)

    # Wrapper function around the API call

    def create_new_repo(self, repo_name, token, description, is_private):
        if self._check_if_repo_exists(repo_name) == True:
            print(
                Fore.RED + "Repository already exists on GitHub!" + Style.RESET_ALL)
            repo_name += "-Headstart"
            print(
                f"Renaming repository to {repo_name}")

        print(Fore.GREEN + "Creating GitHub Repository..." + Style.RESET_ALL)
        return self._create_repo_api(repo_name,
                                     description, is_private)

    # Checks if the user already has a repo with the same name on Github
    def _check_if_repo_exists(self, repoName):
        # Get all user repos
        if self.auth_user:
            response = requests.get(url=GITHUB_BASE_API + "/user/repos", headers={
                'Authorization': 'Bearer ' + self.token
            })
            user_repos = response.json()
            user_repo_names = [repo.get("name") for repo in user_repos]

            # Returns true if a user already has a repository with the same name
            return repoName in user_repo_names

    def _create_repo_api(self, repo_name, description, is_private):
        url = "https://api.github.com/user/repos"
        body = json.dumps({
            "name": repo_name,
            "description": description,
            "homepage": "https://github.com",
            "private": is_private
        })
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "text/plain"
        }

        try:
            response = requests.post(url, data=body, headers=headers)
        except Exception:
            print(
                Fore.RED + "Encountered problems calling the GitHub API." + Style.RESET_ALL)

        return response
