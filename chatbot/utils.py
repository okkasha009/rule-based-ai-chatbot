import time

from datetime import datetime

from colorama import Fore


def typing_effect(message):

    print(Fore.CYAN + "Bot: ", end="")

    for char in message:
        print(char, end="", flush=True)
        time.sleep(0.02)

    print()


def current_time():

    return datetime.now().strftime("%I:%M %p")


def current_date():

    return datetime.now().strftime("%d %B %Y")