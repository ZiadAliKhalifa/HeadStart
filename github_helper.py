from github import Github
from colorama import Fore, Back, Style


class GithubHelper:
    def __init__(self, username, password):
        self.auth_user = Github(username, password)
        print("Logged in!")

    def create_new_repo(self, name):
        if self.check_if_repo_exists(name):
            print(
                Fore.RED + "Repository already exists!" + Style.RESET_ALL)
            name += "-Headstart!"
        else:
            print(Fore.GREEN + "Creating Git Repository..." + Style.RESET_ALL)

    def check_if_repo_exists(self, repoName):
        # Get all user repos
        user_repos = self.auth_user.get_user().get_repos()
        user_repo_names = [repo.name for repo in user_repos]
        # Returns true if a user already has a repository with the same name
        return repoName in user_repo_names


g = GithubHelper("ZiadAliKhalifa", "suggest91In")
g.check_if_repo_exists("Taskat")
