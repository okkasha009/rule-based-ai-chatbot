from colorama import init
from colorama import Fore

from chatbot.engine import ChatBot

init(autoreset=True)

print(Fore.GREEN)

print("=" * 55)

print("          RULE-BASED AI CHATBOT")

print("=" * 55)

print()

print("Type 'help' to see commands.")

print("Type 'exit' anytime to quit.")

print()

bot = ChatBot()

while True:

    user = input(Fore.YELLOW + "You : ")

    if not bot.process(user):
        break