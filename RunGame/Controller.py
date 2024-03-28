import json
import sendEmails

"""
eliminate player
"""
def eliminatePlayer(player, EliminatePlayerComboBox, RemovePlayerComboBox, Display_Game_Box):
    if player != '':
        f = open('../CreateGame/game.json')
        game = json.load(f)
        targetedBy = game[player]["targeted by"]
        target = game[player]["target"]

        game[player]["eliminated"] = "true"

        game[targetedBy]["target"] = target
        game[target]["targeted by"] = targetedBy
        game[targetedBy]["kills"] += 1

        game[player]["target"] = "N/A"
        game[player]["targeted by"] = "N/A"

        f.close()

        json_obj = json.dumps(game)
        with open('../CreateGame/game.json', 'w') as outfile:
            outfile.write(json_obj)

        sendEmails.sendNewAssignment(targetedBy)
        sendEmails.notifyRemoved(player)

        index = EliminatePlayerComboBox.findText(player)
        EliminatePlayerComboBox.removeItem(index)
        RemovePlayerComboBox.removeItem(index)

        displayGame(Display_Game_Box)


"""
remove player
"""
def removePlayer(player, RemovePlayerComboBox, EliminatePlayerComboBox, Display_Game_Box):
    if player != '':
        f = open('../CreateGame/game.json')
        game = json.load(f)
        targetedBy = game[player]["targeted by"]
        target = game[player]["target"]

        game[player]["eliminated"] = "removed"

        game[targetedBy]["target"] = target
        game[target]["targeted by"] = targetedBy

        game[player]["target"] = "N/A"
        game[player]["targeted by"] = "N/A"

        f.close()

        json_obj = json.dumps(game)
        with open('../CreateGame/game.json', 'w') as outfile:
            outfile.write(json_obj)

        sendEmails.sendNewAssignment(targetedBy)
        sendEmails.notifyRemoved(player)

        index = RemovePlayerComboBox.findText(player)
        RemovePlayerComboBox.removeItem(index)
        EliminatePlayerComboBox.removeItem(index)

        displayGame(Display_Game_Box)




"""
display players in game
"""
def displayGame(Display_Game_Box):

    # Opening JSON file
    f = open('../CreateGame/game.json')
    # returns JSON object as a dictionary
    game = json.load(f)

    text = 'Alive:\n'
    for player in game:
        if game[player]['eliminated'] == 'False':
            text += f'{player}:\n' \
                    f'Target: {game[player]["target"]}; Targeted by: {game[player]["targeted by"]}\n' \
                    f'Kills: {game[player]["kills"]}; Eliminated: {game[player]["eliminated"]}; Year: {game[player]["year"]}\n\n'
    text += '\nEliminated:\n'
    for player in game:
        if game[player]['eliminated'] != 'False':
            text += f'{player}:\n' \
                    f'Target: {game[player]["target"]}; Targeted by: {game[player]["targeted by"]}\n' \
                    f'Kills: {game[player]["kills"]}; Eliminated: {game[player]["eliminated"]}; Year: {game[player]["year"]}\n\n'

    f.close()

    Display_Game_Box.clear()
    Display_Game_Box.append(text)


"""
send initial assignments at beginning of game
"""
def emailInitialAssignments():
    sendEmails.sendInitialAssignments()

"""
update combo boxes
"""
def updateComboBoxes(EliminatePlayerComboBox, RemovePlayerComboBox):
    EliminatePlayerComboBox.clear()
    RemovePlayerComboBox.clear()

    f = open('../CreateGame/game.json')
    # returns JSON object as a dictionary
    game = json.load(f)

    for player in game:
        if game[player]['eliminated'] == 'False':
            EliminatePlayerComboBox.addItem(player)
            RemovePlayerComboBox.addItem(player)

    f.close()