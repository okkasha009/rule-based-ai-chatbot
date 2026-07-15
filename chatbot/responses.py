import random

responses = {

    "hello": [
        "Hello 👋",
        "Hi there!",
        "Greetings!"
    ],

    "hi": [
        "Hello!",
        "Hi 👋"
    ],

    "how are you": [
        "I'm doing great!",
        "Doing awesome 😄"
    ],

    "your name": [
        "My name is RuleBot."
    ],

    "who are you": [
        "I'm a Rule-Based AI Chatbot."
    ],

    "python": [
        "Python is a beginner-friendly programming language."
    ],

    "artificial intelligence": [
        "Artificial Intelligence enables machines to perform tasks that normally require human intelligence."
    ],

    "machine learning": [
        "Machine Learning allows computers to learn from data."
    ],

    "thanks": [
        "You're welcome!",
        "Happy to help!"
    ],

    "help": [
        """
Available Commands

• hello
• hi
• how are you
• who are you
• your name
• python
• artificial intelligence
• machine learning
• time
• date
• thanks
• exit
"""
    ]
}


def get_response(intent):

    if intent in responses:
        return random.choice(responses[intent])

    return None