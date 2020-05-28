import requests
import config

from github import Github
from colorama import Fore, Back, Style


class GithubHelper:
    def __init__(self,  token):
        self.auth_user = Github(login_or_token=token)
        print("Logged in!")

    def create_new_repo(self, repo_name, username):
        if self.check_if_repo_exists(repo_name) == True:
            print(
                Fore.RED + "Repository already exists!" + Style.RESET_ALL)
            repo_name += "-Headstart"
            print(
                f"Renaming repository to {repo_name}")

        print(Fore.GREEN + "Creating GitHub Repository..." + Style.RESET_ALL)

    def check_if_repo_exists(self, repoName):
        # Get all user repos
        user_repos = self.auth_user.get_user().get_repos()
        user_repo_names = [repo.name for repo in user_repos]
        # Returns true if a user already has a repository with the same name
        return repoName in user_repo_names


g = GithubHelper(
    config.GITHUB_TOKEN)
g.create_new_repo("Taskat", "ZiadAliKhalifa")
