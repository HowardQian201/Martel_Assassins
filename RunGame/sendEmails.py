import smtplib
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendInitialAssignments():
    # Opening JSON file
    f = open('../CreateGame/game.json')
    # returns JSON object as a dictionary
    game = json.load(f)

    gmail_user = 'howard.h.qian@gmail.com'
    gmail_app_password = "cpmhimtjphknvach"

    for player in game:
        sent_from = gmail_user
        to = game[player]["email"]
        subject = "Your Assassins assignment"
        body = f"Your first assassins target is: {game[player]['target']}, a {game[game[player]['target']]['year']}. Good Luck!"

        message = MIMEMultipart()
        message['From'] = sent_from
        message['To'] = to
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))
        message = message.as_string()

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail_user, gmail_app_password)
            server.sendmail(sent_from, to, message)
            server.close()
            print(f'Email sent to {player}!')

        except Exception as e:
            print(e)
            print(f'Something went wrong while emailing {player}...')

    # Closing file
    f.close()


def sendNewAssignment(player):
    # Opening JSON file
    f = open('../CreateGame/game.json')
    # returns JSON object as a dictionary
    game = json.load(f)

    gmail_user = 'howard.h.qian@gmail.com'
    gmail_app_password = "cpmhimtjphknvach"

    sent_from = gmail_user
    to = game[player]["email"]
    subject = "Your New Assassins assignment"
    body = f"Your new assassins target is: {game[player]['target']}, a {game[game[player]['target']]['year']}. Good Luck!"

    message = MIMEMultipart()
    message['From'] = sent_from
    message['To'] = to
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    message = message.as_string()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # server.login(gmail_user, gmail_password)
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, to, message)
        server.close()
        print(f'Email sent to {player}!')

    except:
        print(f'Something went wrong while emailing {player}...')

    # Closing file
    f.close()

def notifyRemoved(player):
    # Opening JSON file
    f = open('../CreateGame/game.json')
    # returns JSON object as a dictionary
    game = json.load(f)

    gmail_user = 'howard.h.qian@gmail.com'
    gmail_app_password = "cpmhimtjphknvach"

    sent_from = gmail_user
    to = game[player]["email"]
    subject = "Assassins update"
    body = f"Unfortunately, you have been removed from the game. Better luck next time."

    message = MIMEMultipart()
    message['From'] = sent_from
    message['To'] = to
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    message = message.as_string()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # server.login(gmail_user, gmail_password)
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, to, message)
        server.close()
        print(f'Email sent to {player}!')

    except:
        print(f'Something went wrong while emailing {player}...')

    # Closing file
    f.close()