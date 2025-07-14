from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_into_chunks(text, chunk_size=800, chunk_overlap=100):
    """
    Split text into overlapping chunks to preserve context.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)
