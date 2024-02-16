## Overview

This project seeks to investigate the possibility of biases in generated answers when using Retrieval Augmented Generation (RAG) techniques with Language Models (LLMs).

Language Models Tested:
- ChatGPT 3.5 Turbo

## Set-up

Follow the steps below to set up the necessary dependencies. LangChain quickstart guide [here](https://python.langchain.com/docs/use_cases/question_answering/quickstart).

Install Dependencies
```
%pip install --upgrade --quiet  langchain langchain-community langchainhub langchain-openai chromadb bs4
```

Make sure to create your own .env file to store the necessary information for the APIs. The .env file should minimally look like: 
```
API_KEY=insert_here
```

