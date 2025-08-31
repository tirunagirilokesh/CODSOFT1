import re
import random
import datetime


faq_responses = {
    "who are you": "I am your rule-based chatbot assistant 🤖",
    "what is your purpose": "My purpose is to help you with basic tasks and have a friendly chat!",
    "where are you from": "I live inside your computer 💻",
    "who created you": "I was created by a developer using Python 🐍"
}


jokes = [
    "Why don’t programmers like nature? Too many bugs 🐛",
    "Why do Java developers wear glasses? Because they don’t see sharp 👓",
    "What do you call a factory that makes good products? A satisfactory."
]


commands_list = [
    "hi / hello / hey → Greet the bot",
    "how are you → Small talk",
    "who are you / where are you from / who created you → FAQs",
    "time → Get current time",
    "date → Get today's date",
    "joke → Hear a random joke",
    "math expressions (like 5+3, 10*2, 9/3) → Solve simple math",
    "bye / exit → End the chat",
    "help / options → Show this help menu"
]

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    
    if user_input in ["help", "options", "commands"]:
        return "Here are some things you can ask me:\n- " + "\n- ".join(commands_list)

    
    if re.search(r"\b(hi|hello|hey|hola)\b", user_input):
        return "Hello there! 👋 How can I help you?"

    
    elif "how are you" in user_input:
        return "I’m doing awesome! Thanks for asking. How about you?"

    
    for question, answer in faq_responses.items():
        if question in user_input:
            return answer

    
    if "time" in user_input:
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')} ⏰"
    elif "date" in user_input:
        return f"Today's date is {datetime.datetime.now().strftime('%Y-%m-%d')} 📅"

    
    if "joke" in user_input:
        return random.choice(jokes)

    
    match = re.search(r"(\d+)\s*([\+\-\*/])\s*(\d+)", user_input)
    if match:
        num1, operator, num2 = int(match.group(1)), match.group(2), int(match.group(3))
        if operator == '+':
            return f"The result is {num1 + num2}"
        elif operator == '-':
            return f"The result is {num1 - num2}"
        elif operator == '*':
            return f"The result is {num1 * num2}"
        elif operator == '/':
            return f"The result is {num1 / num2 if num2 != 0 else 'undefined (division by zero)'}"

    
    if re.search(r"\b(bye|goodbye|exit|quit)\b", user_input):
        return "Goodbye! Have a fantastic day! 👋"

    
    return "I’m not sure about that 🤔 Try typing 'help' to see what I can do."


print("🤖 Smart Rule-Based ChatBot is online! Type 'help' to see options or 'bye' to exit.\n")
while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("Bot:", response)

    if "bye" in user_input.lower() or "exit" in user_input.lower():
        break
