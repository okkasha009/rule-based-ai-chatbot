from colorama import Fore

from chatbot.responses import get_response

from chatbot.utils import (
    typing_effect,
    current_time,
    current_date
)

from chatbot.config import EXIT_COMMANDS


class ChatBot:


    def process(self, user):

        user = user.lower().strip()

        if user in EXIT_COMMANDS:
            typing_effect("Goodbye 👋 Have a wonderful day!")
            return False

        if "time" in user:
            typing_effect(f"Current Time : {current_time()}")
            return True

        if "date" in user or "today" in user:
            typing_effect(f"Today's Date : {current_date()}")
            return True

        reply = get_response(user)

        if reply:
            typing_effect(reply)

        else:
            typing_effect(
                "Sorry, I don't understand that yet."
            )

        return True