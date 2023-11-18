import os
from conv_anal.chatgpt_memory import ChatGPTMemory

GPT_MODEL = "gpt-3.5-turbo"

def main():
    if os.getenv("OPENAI_API_HOST", None):
        gpt_model = "llama-13b"
    else:
        gpt_model = GPT_MODEL
    bot = ChatGPTMemory(gpt_model,
                        "You are a helpful assistant.",
                        max_tokens=500,
                        request_timeout=0)
    while True:
        question = input("> ")
        if question == "quit":
            break
        print("\n------------------------")
        response = bot.ask(question)
        print(response)
        print("------------------------\n")

if __name__ == "__main__":
    main()
