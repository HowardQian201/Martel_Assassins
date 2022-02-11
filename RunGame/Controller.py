import json

import sendEmails

def eliminatePlayer(player):
    f = open('../CreateGame/game.json')
    game = json.load(f)
    targettedBy = game[player]["targetted by"]
    target = game[player]["target"]

    game[player]["eliminated"] = "true"

    game[targettedBy]["target"] = target
    game[target]["targetted by"] = targettedBy
    game[targettedBy]["kills"] += 1

    f.close()

    sendEmails.sendNewAssignment(targettedBy)


def removePlayer(player):
    f = open('../CreateGame/game.json')
    game = json.load(f)
    targettedBy = game[player]["targetted by"]
    target = game[player]["target"]

    game[player]["eliminated"] = "removed"

    game[targettedBy]["target"] = target
    game[target]["targetted by"] = targettedBy

    f.close()

    sendEmails.sendNewAssignment(targettedBy)


def displayGame():
    # Opening JSON file
    f = open('../CreateGame/game.json')
    # returns JSON object as a dictionary
    game = json.load(f)

    text = ''
    for player in game:
        if player['eliminated'] == 'False':
            text += f'{player}\n'

    f.close()
    return text

def emailInitialAssignments():
    sendEmails.sendInitialAssignments()