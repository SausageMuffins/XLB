def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def format_and_write_docs(docs, file_path='visualizing_articles/nytimes_article.txt'):

    formatted_content = "\n\n".join(doc.page_content for doc in docs)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_content)
    print(f"Documents have been formatted and written to {file_path}")