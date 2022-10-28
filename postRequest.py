import requests

"""
Makes a post request to my database.
"""

def addData(augment, rarity, stage, user, gameid):
    parameters = {"augment": augment, "rarity": rarity, "stage": stage, "username": user, "gameid": gameid}
    requests.post("https://apex.oracle.com/pls/apex/leonworkspace/new/augment", data=parameters)