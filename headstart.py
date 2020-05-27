import subprocess

from getpass import getpass
from os import listdir, path, mkdir, chdir
from colorama import Fore, Back, Style

print('\033[39m')
print("Welcome to " + Fore.CYAN + "HeadStart" + Style.RESET_ALL + "!")
print('\033[39m')

repository_name = input(
    Fore.YELLOW + "What will you be naming this project?: " + Style.RESET_ALL).strip()


# Validation for if there is a folder with the same name
folders_in_directory = [item for item in listdir(".") if path.isdir(item)]
if repository_name in folders_in_directory:
    print("A folder already exists in this path with the same name")
    exit()

# Folder's name was unique
mkdir(repository_name)
chdir(repository_name)

# Initialize a git repository locally
try:
    subprocess.run(["git", "init"])
except:
    print("Please make sure you have Git Installed on this machine.")

# Create a README file
open("README.md", "w+")

# Make the first commit
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "Initial Commit"])


# github_username = input(Fore.MAGENTA + "Please enter your github username: ")
# github_password = getpass("Please enter your github password: ")
# print('\033[39m')

# print(github_username, github_password)
