import subprocess

from os import listdir, path, mkdir, chdir
from colorama import Fore, Back, Style
from github_helper import GithubHelper

print('\033[39m')
print("Welcome to " + Fore.CYAN + "HeadStart" + Style.RESET_ALL + "!")
print('\033[39m')

repository_name = input(
    Fore.BLUE + "What will you be naming this project?: " + Style.RESET_ALL).strip()

# Validation for if there is a folder with the same name
folders_in_directory = [item for item in listdir(".") if path.isdir(item)]
if repository_name in folders_in_directory:
    print("A folder already exists in this path with the same name")
    exit()
else:
    # Folder's name was unique
    mkdir(repository_name)
    chdir(repository_name)


# Initialize a git repository locally
try:
    subprocess.run(["git", "init"])
except e:
    print("Please make sure you have Git Installed on this machine.")

# Create a README file
open("README.md", "w+")

# Make the first commit
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial Commit"])

# Checks if the user would like to upload to Github
will_upload_to_github = input(
    Fore.BLUE + "Do you need to put that project on GitHub? (y/n): " + Style.RESET_ALL).strip().lower()

if will_upload_to_github != "yes" and will_upload_to_github != "y":
    print("You are all good, then.")
    print("Do awesome things!")
    exit()

print("In order to proceed, you must have a GitHub token to use for this app!")
print("Follow this link on how to get one: https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token")


github_token = input(
    "Please enter your github token: ").strip()
repository_description = input(
    "Please enter a description for the repository: ").strip()
is_repo_private = input(
    "Do you want it to be public? (y/n) " + Style.RESET_ALL).lower().strip()

if is_repo_private != "yes" and is_repo_private != "y":
    is_repo_private = False
else:
    is_repo_private = True


# Instanciates  a GitHub class (github_helper.py)
github = GithubHelper(github_token)
response = github.create_new_repo(repository_name,
                                  github_token, repository_description, is_repo_private).json()
# Gets the tracking URL from the response of the API
github_clone_url = response["clone_url"]

# Tracks the Github repo and pushes code to master
subprocess.run(["git", "remote", "add", "origin", github_clone_url])
subprocess.run(["git", "push", "-u", "origin", "master"])

print("Do awesome things!")
