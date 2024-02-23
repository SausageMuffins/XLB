# Format the output of the loaded documents and chunks
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def format_chunk(chunk, idx, separator):
    """Format a single chunk with its index and separator."""
    chunk_content = chunk.page_content 
    start_index = chunk.metadata.get('start_index', None)
    
    if start_index is not None:
        formatted_chunk = f"Chunk {idx} (Starts at {start_index}):\n{chunk_content}"
    else:
        formatted_chunk = f"Chunk {idx}:\n{chunk_content}"
    
    return formatted_chunk + "\n" + separator


# Writing the formatted material to a file
def format_and_write_docs(docs, file_path="visualizing_articles/loaded_docs.txt"):

    formatted_content = "\n\n".join(doc.page_content for doc in docs)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_content)
    print(f"Documents have been formatted and written to {file_path}.\n")
    
def format_and_write_chunks(chunks, file_path="visualizing_articles/chunks.txt"):
    separator = "-" * 50
    # Utilize list comprehension for formatting each chunk
    formatted_chunks = [format_chunk(chunk, idx, separator) for idx, chunk in enumerate(chunks, start=1)]

    # Joining formatted chunks, each already includes a separator at the end
    formatted_content = "\n\n".join(formatted_chunks)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_content)

    print(f"Chunks have been formatted and written to {file_path}.\n")



