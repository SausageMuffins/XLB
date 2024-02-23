## Overview

This project seeks to investigate the possibility of biases in generated answers when using Retrieval Augmented Generation (RAG) techniques with Language Models (LLMs).

Language Models Tested:
- ChatGPT 3.5 Turbo

Embedding Models Tested:
- text-embedding-3-small
## Set-up

Follow the steps below to set up the necessary dependencies. LangChain quickstart guide [here](https://python.langchain.com/docs/use_cases/question_answering/quickstart).

Install Dependencies
```
pip install -r requirements.txt
```

Make sure to create your own .env file to store the necessary information for the APIs. The .env file should minimally look like: 
```
API_KEY=insert_api_token_here
```
Your OpenAPI key can be created [here](https://platform.openai.com/api-keys). Make sure to top up the balance to use the api key. 

---

## Relevant Files

format_output.py is mainly for formatting and visualizing outputs at different stages of the pipeline (loading, splitting, retrieving etc.). The visualized files are under the folder "visualizing_articles".

Note: The reference articles are news articles with various topics (e.g. Covid-19, Climate Change). The articles will be used to in the main file (xlb) to perform RAG on.
