import subprocess

from getpass import getpass
from colorama import Fore, Back, Style

print('\033[39m')
print("Welcome to " + Fore.CYAN + "HeadStart!")
print('\033[39m')

repository_name = input(
    Fore.YELLOW + "What will you be naming this project?: ")

dir_list = subprocess.run(["ls", "-l", "."], stdout=subprocess.PIPE)
print(dir_list.stdout)

# subprocess.run([f"mkdir {repository_name}"])

# github_username = input(Fore.MAGENTA + "Please enter your github username: ")
# github_password = getpass("Please enter your github password: ")
# print('\033[39m')

# print(github_username, github_password)
