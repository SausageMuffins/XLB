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

from format_output import format_and_write_chunks, format_and_write_docs # for formatting and readability

DATA_PATH = "reference_articles"
dotenv.load_dotenv() # load in variables from .env file
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY") or getpass("Enter your OpenAI API key: ") # set the API key

# loading documents from a directory
def load_documents():
    loader = DirectoryLoader('./reference_articles', glob="**/*.pdf")
    docs = loader.load()
    return docs

def split_text(docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(docs) 
    print(f"Split {len(docs)} documents into {len(chunks)} chunks.\n")
    
    #print(chunks) - I found out that chunks are a list of Document objects
    return chunks

loaded_docs = load_documents()
chunks = split_text(loaded_docs)
#print(chunks)

# format and write the documents to the folder "visualizing_articles"
format_and_write_docs(loaded_docs)
format_and_write_chunks(chunks)




