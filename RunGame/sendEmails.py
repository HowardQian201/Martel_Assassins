import smtplib
import json

def sendInitialAssignments():
    # Opening JSON file
    f = open('../CreateGame/game.json')
    # returns JSON object as a dictionary
    game = json.load(f)

    gmail_user = 'hhq1@rice.edu'
    gmail_password = ''

    for player in game:
        sent_from = gmail_user
        to = game[player]["email"]
        subject = 'New Assassins Target'
        body = f"Your new assassins target is: {game[player]['target']}, a {game[game[player]['target']]['year']}. Good Luck!"

        email_text = """\
            From: %s
            To: %s
            Subject: %s
    
            %s
            """ % (sent_from, ", ".join(to), subject, body)

        try:
            server = smtplib.SMTP_SSL('smtp@gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
            server.close()

            print(f'Email sent to {player}!')
        except:
            print(f'Something went wrong while emailing {player}...')

    # Closing file
    f.close()


def sendNewAssignment(player):
    # Opening JSON file
    f = open('../CreateGame/game.json')
    # returns JSON object as a dictionary
    game = json.load(f)

    gmail_user = 'hhq1@gmail.com'
    gmail_password = ''

    sent_from = gmail_user
    to = game[player]["email"]
    subject = 'New Assassins Target'
    body = f"Your new assassins target is: {game[player]['target']}, a {game[game[player]['target']]['year']}. Good Luck!"

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')

    # Closing file
    f.close()