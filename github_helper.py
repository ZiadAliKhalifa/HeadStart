import requests
import config
import json

from github import Github
from colorama import Fore, Back, Style


class GithubHelper:
    def __init__(self,  token):
        try:
            # Logs in with token and sets "auth user" as the authinticated user
            self.auth_user = Github(login_or_token=token)
        except:
            print(
                Fore.RED + "You might have provided a wrong token. Please try again" + Style.RESET_ALL)

        print("Logged in!")

    # Wrapper function around the API call
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

    # Checks if the user already has a repo with the same name on Github
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

        try:
            response = requests.post(url, data=body, headers=headers)
        except:
            print(
                Fore.RED + "Encountered problems calling the GitHub API." + Style.RESET_ALL)

        return response
