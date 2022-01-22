"""
This script will check git updates every N time and if there is some, then it will pull it and quit
"""

import subprocess

subprocess.run("sudo /mnt/c/Projects/d_sh_handler/autorun/repo_watcher/git-repo-watcher -d /mnt/c/Projects/d_sh_handler", 
check=True, text=True, shell=True)
print(123)
# subprocess.run("dir", 
# check=True, text=True, shell=True)