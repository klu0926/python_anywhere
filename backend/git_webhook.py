from flask import request
import subprocess

def git_webhook():
    # Optional: You can check if it's from GitHub (e.g., check headers or secret)

    # Repo clone at my python anywhere 
    repo_path = '/home/klu0926/mysite/python_anywhere'

    # Pull the latest code, 
    # change directory to Repo (in python anywhere) then write code 'git pull'
    # 'git -C {repo_path} pull'
    # -C means change director before running this code
    subprocess.run(['git', '-C', repo_path, 'pull'])

    # Touch the WSGI file to restart the app (important on PythonAnywhere)
    subprocess.run(['touch', '/var/www/klu0926_pythonanywhere_com_wsgi.py'])

    return 'Code updated and app restarted', 200
