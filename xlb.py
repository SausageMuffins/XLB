import os
import dotenv

import bs4
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from getpass import getpass

from format_output import format_and_write_chunks, format_and_write_docs, format_and_write_results # for formatting and readability

dotenv.load_dotenv() # load in variables from .env file
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY") or getpass("Enter your OpenAI API key: ") # set the API key

# loading documents from a directory
def load_documents(folder_name):
    directory = "reference_articles/" + folder_name
    loader = DirectoryLoader(directory, glob="**/*.pdf")
    docs = loader.load()
    return docs

def split_text(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(docs) 
    print(f"Split {len(docs)} documents into {len(chunks)} chunks.\n")
    
    #print(chunks) - I found out that chunks are a list of Document objects
    return chunks

model = ChatOpenAI()
embeddings = OpenAIEmbeddings()

query = "What should I know about Covid-19 now?"
sep = "-" * 50

# Loop through directories and query each topic
for root, directory, files in os.walk("reference_articles"):
    for folder in directory: # Repeat for each topic - JN1 or Vaccines
        print(f"{sep} + \n + Processing {folder}...")
        loaded_docs = load_documents(folder)
        chunks = split_text(loaded_docs)
        
        # record down for visualizing what was loaded and split.
        format_and_write_docs(loaded_docs, file_path=f"visualizing_articles/{folder}/{folder}_loaded_docs.txt")
        format_and_write_chunks(chunks, file_path=f"visualizing_articles/{folder}/{folder}_chunks.txt")
        
        db = Chroma.from_documents(chunks, embeddings) # create a new vector store each time to avoid keeping the old context
        retriever = db.as_retriever(search_type="mmr", search_kwargs={"k": 8}) # mmr, top 8 results
        results = retriever.get_relevant_documents(query) 
        retrieved_results = ""
        
        
        for ranking, doc in enumerate(results):
            retrieved_results += f"Ranking {ranking + 1}: {doc.metadata} \n{doc.page_content}\n"
            retrieved_results += "\n" + sep + "\n\n"
        
        format_and_write_results(retrieved_results, file_path=f"visualizing_articles/{folder}/{folder}_results.txt")