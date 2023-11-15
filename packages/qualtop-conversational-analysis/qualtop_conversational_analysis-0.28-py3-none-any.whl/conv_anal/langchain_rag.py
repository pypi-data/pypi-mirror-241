import os
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

from langchain.embeddings import GPT4AllEmbeddings, LlamaCppEmbeddings


def generate_single_doc_db(file_path, embedding_model="llamacpp"):
    assert os.path.exists(file_path)
    if "pdf" in file_path:
        doc_loader = PyPDFLoader(file_path)
    else:
        doc_loader = TextLoader(file_path)
    print(f"Loading document...")
    documents = doc_loader.load()
    
    print(f"\nStarting document splitting...")
    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, 
                                                   chunk_overlap=100)
    documents = text_splitter.split_documents(documents)
    
    print(f"\nCreating {embedding_model} embeddings...")
    home_folder = os.path.expanduser("~")
    if embedding_model == "llamacpp":
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

    # Embed
    persist_directory = os.path.join(os.path.expanduser("~"),
                                     ".cache/embeddings",
                                     "data/gnp_single")
    vect_db = Chroma.from_documents(documents, 
                                    embedding=embedding_fn, 
                                    persist_directory=persist_directory)
    vect_db.persist()


def generate_vector_db(pdf_folder, embedding_model="llamacpp"):
    assert os.path.exists(pdf_folder)
    documents = []
    for root, folder, filenames in os.walk(pdf_folder):
        i=1
        for fname in filenames:
            file_path = os.path.join(root, fname)
            if file_path.endswith("txt"):
                doc_loader = TextLoader(file_path)
            else:
                doc_loader = PyPDFLoader(file_path)
            try:
                docs = doc_loader.load()
            except:
                print(file_path)
                continue
            documents.extend(doc_loader.load())
            print(f"Loaded document {i}...")
            i += 1

    print(f"\nStarting document splitting...")
    # Split documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, 
                                                   chunk_overlap=100)
    documents = text_splitter.split_documents(documents)
    
    print(f"\nCreating {embedding_model} embeddings...")
    home_folder = os.path.expanduser("~")
    if embedding_model == "llamacpp":
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

    print(f"\nCreating mistral embeddings...")
    
    # Embed
    persist_directory = os.path.join(os.path.expanduser("~"),
                                     ".cache/embeddings",
                                     "data/gnp")
    vect_db = Chroma.from_documents(documents, 
                                    embedding=embedding_fn, 
                                    persist_directory=persist_directory)
    vect_db.persist()


if __name__ == "__main__":
    generate_single_doc_db(os.path.join(os.path.expanduser("~"), 
                                        "temp/gnp",
                                        "example.txt"))
    generate_vector_db(os.path.join(os.path.expanduser("~"), 
                                    "temp/gnp"))
