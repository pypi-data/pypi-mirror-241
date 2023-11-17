import os

import openai

import pandas as pd

from conv_anal.gnp_collection import *

from langchain.vectorstores import Chroma

import chromadb

from langchain.embeddings import GPT4AllEmbeddings, LlamaCppEmbeddings

def generate_doc_collection_chromadb(output_path, embedding_model=""):
    if embedding_model == "":
        embedding_model = "BERT"
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
    
    # Create vectorstore
    #chroma_client = chromadb.Client()
    chroma_client = chromadb.PersistentClient(output_path)
    
    ## Get documents
    documents = {"dotal_collection" : dotal_gnp,
                 "platino_collection" : platino_universal_GNP,
                 "privilegio_collection" : privilegio_universal_gnp,
                 "profesional_collection" : profesional_gnp,
                 "trasciende_collection" : trasciende_gnp,
                 "vision_collection" : vision_plus_gnp
                 }

    for doc_key in documents.keys():
        doc_collection = []
        doc = documents[doc_key]
        for section_key in doc.keys():
            section = doc[section_key]
            for subsection_key in section:
                subsection = section[subsection_key]
                # Can have a third level or not
                if isinstance(subsection, dict):
                    for paragraph_key in subsection:
                        paragraph = subsection[paragraph_key]
                        txt_document = '"""\n'
                        txt_document += f'{section_key}:\n'
                        txt_document += f'\t{subsection_key}:\n'
                        txt_document += f'\t\t{paragraph_key}:\n'
                        txt_document += f'\t\t\t{paragraph}\n'
                        txt_document += f'"""\n'
                        print(txt_document)
                        doc_collection.append(txt_document)
                else:
                    txt_document = '"""\n'
                    txt_document += f'{section_key}:\n'
                    txt_document += f'\t{subsection_key}:\n'
                    txt_document += f'\t\t{subsection}\n'
                    txt_document += f'"""\n'
                    print(txt_document)
                    doc_collection.append(txt_document)
        embedded_collection = embedding_fn.embed_documents(doc_collection)
        collection = chroma_client.create_collection(name=doc_key)
        collection.add(embeddings=embedded_collection,
                       documents=doc_collection,
                       ids=[str(i) for i in range(len(doc_collection))])


if __name__ == "__main__":
    generate_doc_collection_chromadb(os.path.join(os.path.expanduser("~"),
                                     ".cache/embeddings/data/gnp_collection"))
