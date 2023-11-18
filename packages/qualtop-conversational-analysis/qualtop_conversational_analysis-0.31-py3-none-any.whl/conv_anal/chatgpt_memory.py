import os
from datetime import datetime
import os
import openai
import tiktoken

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613", verbose=False):
    """Return the number of tokens used by a list of messages."""
    try:
        if "llama" in model:
            encoding = tiktoken.encoding_for_model("gpt2")
        else:
            encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        if verbose:
            print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        "gpt-3.5-turbo-0613",
        "gpt-3.5-turbo-16k-0613",
        "gpt-4-0314",
        "gpt-4-32k-0314",
        "gpt-4-0613",
        "gpt-4-32k-0613",
        "llama-13b",
        "llama-13b_code",
        "mistral-7b_code",
        "llama2-13b",
        "codellama-13b",
        "mistral-7b",
        }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif "gpt-3.5-turbo" in model:
        if verbose:
            print("Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613.")
        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0613")
    elif "gpt-4" in model:
        if verbose:
            print("Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613.")
        return num_tokens_from_messages(messages, model="gpt-4-0613")
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens


class ChatGPTMemory(object):

    def __init__(self, model, system_message, 
                 max_tokens=500,
                 token_budget=4096-1000,
                 temperature=0, 
                 request_timeout=60,
                 open_ai_base=None,
                 verbose=False,
                 *args, **kwargs):
        assert isinstance(system_message, str)
        
        # Setup openai (or other provider)
        if open_ai_base:
            print(f"Looking at server {open_ai_base}\n")
            openai.api_base = open_ai_base
            openai_key = ""
        else:
            openai_key= os.getenv("OPENAI_API_KEY", "")
        
        openai.api_key = openai_key
       
        self.model = model
        self.max_tokens = max_tokens
        self.token_budget = token_budget
        self.system_message = system_message
        self.temperature = temperature
        self.request_timeout = request_timeout
        self.messages = [
                {"role": "system", "content": system_message}
                ]
        self.verbose = verbose

    def insert_response(self, response):
        assert isinstance(response, str)

        self.messages.append({"role" : "assistant",
                              "content" : response})

    def insert_message(self, message):
        assert isinstance(message, dict)
        assert "role" in message.keys() and "content" in message.keys()
        self.messages.append(message)

    def is_below_token_budget(self):
        total_tokens = num_tokens_from_messages(self.messages, 
                                                self.model,
                                                self.verbose)
        return total_tokens < self.token_budget

    def free_memory(self):
        while not self.is_below_token_budget() :
            # Remove second question and its response
            # e.g.
            # messages[0] -> system
            # messages[1] -> initial_context + first_question
            # messages[2] -> assistant
            # messages[3] -> user (second question)
            # messages[4] -> user (second answer)
            self.messages.pop(3)
            self.messages.pop(3) # indexes slide

    def ask(self, query):
        assert isinstance(query, str)

        self.messages.append({"role" : "user", 
                              "content" : query})
    
        if not self.is_below_token_budget():
            self.free_memory()
        if self.verbose: 
            print(f"Starts api call {datetime.now().strftime('%y-%m-%d %H:%M')}")
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            request_timeout=self.request_timeout
        )
        if self.verbose: 
            print(f"Ends api call {datetime.now().strftime('%y-%m-%d %H:%M')}")

        response_message = response["choices"][0]["message"]["content"]
        self.insert_response(response_message)
        return response_message
    
    def print_history(self):
        for message in self.messages:
            print(message["role"] + ": \n")
            print("\t" + message["content"] + "\n\n")

    def out_of_context_question(self, query):
        messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": query},
        ]

        if self.verbose: 
            print(f"Starts api call {datetime.now().strftime('%y-%m-%d %H:%M')}")
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            request_timeout=self.request_timeout
        )
        if self.verbose: 
            print(f"Ends api call {datetime.now().strftime('%y-%m-%d %H:%M')}")

        response_message = response["choices"][0]["message"]["content"]
        return response_message
