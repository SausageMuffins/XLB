import os
import dotenv

import bs4
from langchain import hub
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from getpass import getpass

dotenv.load_dotenv() # load in variables from .env file
os.environ["OPENAI_API_KEY"] = os.getenv("API_KEY") or getpass("Enter your OpenAI API key: ") # set the API key

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def format_and_write_docs(docs, file_path='visualizing_articles/nytimes_article.txt'):
    formatted_content = "\n\n".join(doc.page_content for doc in docs)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_content)
    print(f"Documents have been formatted and written to {file_path}")

