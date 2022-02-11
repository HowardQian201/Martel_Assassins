import json
import sendEmails

"""
eliminate player
"""
def eliminatePlayer(player):
    f = open('../CreateGame/game.json')
    game = json.load(f)
    targetedBy = game[player]["targeted by"]
    target = game[player]["target"]

    game[player]["eliminated"] = "true"

    game[targetedBy]["target"] = target
    game[target]["targeted by"] = targetedBy
    game[targetedBy]["kills"] += 1

    f.close()

    sendEmails.sendNewAssignment(targetedBy)

"""
remove player
"""
def removePlayer(player):
    f = open('../CreateGame/game.json')
    game = json.load(f)
    targetedBy = game[player]["targeted by"]
    target = game[player]["target"]

    game[player]["eliminated"] = "removed"

    game[targetedBy]["target"] = target
    game[target]["targeted by"] = targetedBy

    f.close()

    sendEmails.sendNewAssignment(targetedBy)

"""
display players in game
"""
def displayGame():
    # Opening JSON file
    f = open('../CreateGame/game.json')
    # returns JSON object as a dictionary
    game = json.load(f)

    text = ''
    for player in game:
        if player['eliminated'] == 'False':
            text += f'{player}\n'

    for player in game:
        if player['eliminated'] != 'False':
            text += f'{player}\n'

    f.close()
    return text

#send initial assignments at beginning of game
def emailInitialAssignments():
    sendEmails.sendInitialAssignments()