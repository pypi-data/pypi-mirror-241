import os

import openai

import pandas as pd

import pickle

from conv_anal.chatgpt_embeddings import calculate_embeddings

from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.vectorstores import Chroma
import chromadb

from langchain.embeddings import GPT4AllEmbeddings, LlamaCppEmbeddings

def generate_single_doc_db(file_path, output_file, embedding_model=""):
    print(f"\nCreating {embedding_model} embeddings...")
    home_folder = os.path.expanduser("~")
    if embedding_model == "mistral-7b":
        embedding_model_path = os.path.join(home_folder,
                                            ".cache/gpt4all",
                                            "mistral-7b-instruct-v0.1.Q4_0.gguf")
        
        embedding_fn = LlamaCppEmbeddings(model_path=embedding_model_path,
                                          n_gpu_layers=80,
                                          n_batch=1024,
                                          n_ctx=4096,
                                          f16_kv=True)
    else:
        embedding_fn = GPT4AllEmbeddings()

    # Load input file
    with open(file_path, "rb") as fp:
        df = pd.read_pickle(fp)
   
    # Number of index (level) columns
    l_cols = [col_name for col_name in df.columns if col_name.startswith("l_")]
    n_levels = len(l_cols)
    
    # Get context documents
    context_documents = []
    for i in range(df.shape[0]):
        context_documents.append(", ".join(df.loc[i][l_cols].values))

    ## Keep only unique prefixes
    #context_documents = list(set(context_documents))
    content_documents = df["text"].values.tolist()
    
    vectorizable_docs = []
    for i in range(len(content_documents)):
        vectorizable_docs.append(": ".join([context_documents[i], content_documents[i]]))
    
    context_embeddings = calculate_embeddings(vectorizable_docs,
                                              embedding_model=embedding_model,
                                              batch_size=50)

    try:
        os.makedirs(os.path.dirname(output_file))
    except:
        pass
    context_embeddings.to_pickle(output_file, compression="infer")


def generate_single_doc_chromadb(file_path, output_path, embedding_model=""):
    print(f"\nCreating {embedding_model} embeddings...")
    home_folder = os.path.expanduser("~")
    if embedding_model == "mistral-7b":
        embedding_model_path = os.path.join(home_folder,
                                            ".cache/gpt4all",
                                            "mistral-7b-instruct-v0.1.Q4_0.gguf")
        
        embedding_fn = LlamaCppEmbeddings(model_path=embedding_model_path,
                                          n_gpu_layers=80,
                                          n_batch=1024,
                                          n_ctx=4096,
                                          f16_kv=True)
    else:
        embedding_fn = GPT4AllEmbeddings()

    # Load input file
    with open(file_path, "rb") as fp:
        df = pd.read_pickle(fp)
   
    # Number of index (level) columns
    l_cols = [col_name for col_name in df.columns if col_name.startswith("l_")]
    n_levels = len(l_cols)
    
    # Get context documents
    context_documents = []
    for i in range(df.shape[0]):
        context_documents.append(", ".join(df.loc[i][l_cols].values))

    ## Keep only unique prefixes
    #context_documents = list(set(context_documents))
    content_documents = df["text"].values.tolist()
    
    vectorizable_docs = []
    for i in range(len(content_documents)):
        vectorizable_docs.append(": ".join([context_documents[i], content_documents[i]]))
    
    context_embeddings = calculate_embeddings(vectorizable_docs,
                                              embedding_model=embedding_model,
                                              batch_size=50)

    chroma_client = chromadb.PersistentClient(output_path)
    collection = chroma_client.create_collection(name="context_collection")

    collection.add(
            embeddings=context_embeddings["embedding"].values.tolist(),
            documents=content_documents,
            ids=[str(j) for j in range(len(vectorizable_docs))]
    )

    vecdb = Chroma(
                client=chroma_client,
                collection_name="context_collection",
                embedding_function=embedding_fn,
                persist_directory=output_path,
            )
    vecdb.persist()

def generate_single_doc_contextless_chromadb(file_path, output_path, embedding_model=""):
    print(f"\nCreating {embedding_model} embeddings...")
    home_folder = os.path.expanduser("~")
    if embedding_model == "mistral-7b":
        embedding_model_path = os.path.join(home_folder,
                                            ".cache/gpt4all",
                                            "mistral-7b-instruct-v0.1.Q4_0.gguf")
        
        embedding_fn = LlamaCppEmbeddings(model_path=embedding_model_path,
                                          n_gpu_layers=80,
                                          n_batch=1024,
                                          n_ctx=4096,
                                          f16_kv=True)
    else:
        embedding_fn = GPT4AllEmbeddings()

    # Load input file
    with open(file_path, "rb") as fp:
        df = pd.read_pickle(fp)
   
    ## Get documents
    content_documents = df["text"].values.tolist()
    
    content_embeddings = calculate_embeddings(content_documents,
                                              embedding_model=embedding_model,
                                              batch_size=50)

    chroma_client = chromadb.PersistentClient(output_path)
    collection = chroma_client.create_collection(name="contextless_collection")

    collection.add(
            embeddings=content_embeddings["embedding"].values.tolist(),
            documents=content_documents,
            ids=[str(j) for j in range(len(content_documents))]
    )

    vecdb = Chroma(
                client=chroma_client,
                collection_name="contextless_collection",
                embedding_function=embedding_fn,
                persist_directory=output_path,
            )
    vecdb.persist()


if __name__ == "__main__":
    # Setup openai
    openai_api_host = os.getenv("OPENAI_API_HOST", None)
    if openai_api_host:
        openai.api_base = openai_api_host
        openai.api_key = ""
        gpt_model = "mistral-7b"
    else:
        openai_key = os.getenv("OPENAI_API_KEY", "")
        openai.api_key = openai_key
        gpt_model = GPT_MODEL
    
    generate_single_doc_contextless_chromadb(os.path.join(os.path.expanduser("~"), 
                                        "temp/gnp",
                                        "df_pages.bin"),
                                 os.path.join(os.path.expanduser("~"),
                                              ".cache/embeddings/data/gnp_single")
                                 )
