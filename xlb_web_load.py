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

# Custom function to use with SoupStrainer
# def filter_by_name(tag):
#     return tag.name == "section" and tag.get("name") == "articleBody"

# Using the custom function in SoupStrainer
# bs4_strainer = bs4.SoupStrainer(filter_by_name)
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def format_and_write_docs(docs, file_path='visualizing_articles/nytimes_article.txt'):
    formatted_content = "\n\n".join(doc.page_content for doc in docs)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_content)
    print(f"Documents have been formatted and written to {file_path}")

loader = WebBaseLoader(
    web_paths=("https://www.nytimes.com/2024/02/13/briefing/covid-boosters-children-cdc.html",),
    # bs_kwargs={"parse_only": bs4_strainer},
)

docs = loader.load()

# After loading documents
print("Loaded Documents:")
format_and_write_docs(docs)


text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# result = rag_chain.invoke("Give me a detailed summary of the article?")
# print(result)

# cleanup
vectorstore.delete_collection()