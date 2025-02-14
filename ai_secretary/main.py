from openai import OpenAI
from assistant import Assistant
from action_module import ActionModule
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = OpenAI()

if __name__ == "__main__":
    action_module = ActionModule()
    assistant = Assistant(client, action_module)

    while True:
        question = input("Your message: ")

        if question == "close":
            break
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"timestamp: {timestamp} | message: {question}"
        
        answer = assistant.generate_response(formatted_message)
        
        print("Assistant response: " + answer)