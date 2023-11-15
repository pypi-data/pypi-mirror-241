import os
import re

import openai

import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt

from conv_anal.infer_data import *
from conv_anal.time_series import *
from conv_anal.code_exec import check_for_code

from conv_anal.chatgpt_embeddings import num_tokens
from conv_anal.chatgpt_memory import ChatGPTMemory, num_tokens_from_messages

CURLY_REGEX = r"\{(.*?)\}"
GPT_MODEL = "gpt-3.5-turbo"

def discover_datasets(csv_folder="./conv_anal/data/bank"):
    csv_files = []
    for root, _, fnames in os.walk(csv_folder):
        for fname in fnames :
            if fname.endswith(".csv"):
                csv_files.append((fname, os.path.join(root, fname)))
    return csv_files

def load_csv_prompt(description):
    loading_prompt = f"{description} \n"
    loading_prompt += f"What can you tell me about this dataset?"
    return loading_prompt

def initial_prompt(selection, fnames):
    init_message = f"The following datasets are available to explore: {str(fnames)[1:-1]}\n"
    init_message += f"If the user answers: \"\"\"{selection}\"\"\"\n"
    init_message += f"Which dataset did he select? Put the filename in curly brackets."
    return init_message

def main(interactive=True):
    check_for_code("")
    system_message = "You answer questions about Pandas dataframes."
    introduction = 'Use the given dataframe information to answer questions. Any code answer must be given in Python.\n\n'
    bot = ChatGPTMemory(model=GPT_MODEL,
                        system_message=system_message)
    
    datasets = discover_datasets()
    fnames = [ds[0] for ds in datasets]
    
    datasets = dict(datasets)
    dataset_selected = False
    
    init_message = f"\nThe following datasets are available to explore: {str(fnames)[1:-1]}\n"
    init_message += f"Choose one to start."

    print(init_message)
    while interactive:
        print("\n")
        question = input("> ")
        print("\n")
        if question == "quit":
            interactive=False
            break
        if not dataset_selected:
            response = bot.out_of_context_question(initial_prompt(question, fnames))
            selected_fname = re.search(CURLY_REGEX, response).group(1)
            if selected_fname in fnames:
                dataset_selected = True
                print(f"Loading '{selected_fname}'...\n\n")
                df, description = analyse_dataset(datasets[selected_fname])
                print(description)
                import ipdb;ipdb.set_trace()
                #bot.set_introduction(introduction)
                # Save response to Memory
                response = bot.ask(load_csv_prompt(description))
                print(response)
            else:
                print("Sorry, I couldn't understand your answer.")
        else:
            response = bot.ask(question)
            has_code, code = check_for_code(response)
            if has_code:
                try:
                    exec(compile(code, "", "exec"))
                except:
                    print("Sorry, I can't do that.")
            else:
                print(response)


if __name__ == "__main__" :
    main()
