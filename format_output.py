def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def format_and_write_docs(docs, file_path="visualizing_articles/loaded_docs.txt"):

    formatted_content = "\n\n".join(doc.page_content for doc in docs)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_content)
    print(f"Documents have been formatted and written to {file_path}")
    
def format_and_write_chunks(chunks, file_path="formatted_chunks.txt"):
    formatted_chunks = []
    separator = "-" * 50
    for idx, chunk in enumerate(chunks, start=1):
        chunk_content = chunk.page_content 
        
        # Accessing the start_index from the metadata dictionary within the Document object
        start_index = chunk.metadata.get('start_index', None)  # get() for safe access to the dictionary

        if start_index is not None:
            formatted_chunk = f"Chunk {idx} (Starts at {start_index}):\n{chunk_content}"
        else:
            formatted_chunk = f"Chunk {idx}:\n{chunk_content}"
        
        # Add the separator line below each chunk
        formatted_chunks.append(formatted_chunk + "\n" + separator)

    formatted_content = "\n\n".join(formatted_chunks)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

    print(f"Chunks have been formatted and written to {file_path}")



