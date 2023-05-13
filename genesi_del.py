from ast import Constant
#do "pip install requests"
import requests
import os
import base64
import json
#do "pip install PyGithub"
from github import Github


ACCOUNTS = os.environ['GH_ACCOUNTS_B64']
ACCOUNTS = base64.b64decode(ACCOUNTS).decode("utf-8")
#print(ACCOUNTS)

data = json.loads(ACCOUNTS)


for item in data:
    print("ID: "        , item["id"])
    print("Account: "   , item["account"])
    #print("Token: "    , item["token"])

    try:
        # Instantiate the Github object using the access token
        g = Github(item["token"])

        # Delete all GH account repositories
        user = g.get_user()
        repos = user.get_repos()
        for repo in repos:
            repo.delete()
    except Exception as e:
        # If an error occurs, add the error message to the message string
        continue
