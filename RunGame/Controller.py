import json

import sendEmails
from RunGame import WindowBuild


def eliminatePlayer(player):

    #remove player
    #send email for new assignment

    sendEmails.sendNewAssignment(player)


def removePlayer(player):
    return None


def displayGame():
    # Opening JSON file
    f = open('../CreateGame/game.json')
    # returns JSON object as a dictionary
    game = json.load(f)

    text = game.dump()

    f.close()
    return text

def emailInitialAssignments():
    sendEmails.sendInitialAssignments()