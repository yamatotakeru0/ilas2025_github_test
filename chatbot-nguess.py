import os
from dotenv import load_dotenv
import chatgpt
import random

# nguess.pyより.
def nguess():
    answer = random.randint(1, 100)
    print('The answer is between 1 and 100.')
    print('If you want to end and talk with the AI, input 0.')
    print("If you have the AI guess, input 101.")
    guess = int(input('guess='))
    print('Your guess is', guess)
    truth = 0
    while truth == 0 :
        if guess == answer :#正解したとき.
            print('The answer is', answer)
            print('Good guess')
            truth = 1
        elif guess == 0 :#nguessをやめてAIと話すとき.
            print('The answer is', answer)
            truth = 1
        elif guess == 101 :#AIに推測してもらいたいとき.
            print('The answer is between 1 and 100.')
            print('If you want to end and talk with the AI, input 0.')
            print("AIに質問しました > '1から100の間の整数からランダムに私が選んだ数字を当ててください。'")
            gptGuess = chatbot.chat("1から100の間の整数からランダムに私が選んだ数字を当ててください。").strip()
            print("The AI's guess is", gptGuess)
            guess = int(input('guess='))
            print('Your guess is', guess)
        else :#不正解のとき.
            print("Bad guess")
            print('The answer is between 1 and 100.')
            print('If you want to end and talk with the AI, input 0.')
            print("If you have the AI guess, input 101.")
            guess = int(input('guess='))
            print('Your guess is', guess)

load_dotenv(".env")
chatbot = chatgpt.ChatBot(api_key = os.environ.get("OPENAI_API_KEY"))
system_setting = input("Please set system: ").strip()
chatbot.set_system_setting(system_setting)
print("Please input something after '>’")
while True:
    prompt = input("> ").strip()
    if prompt == "reset":
        chatbot.reset_message()
    elif prompt == "quit":
        break
    elif prompt == "nguess":
        nguess()
        print("Please input something after '>’")
    else:
        message = chatbot.chat(prompt)
        print(message)