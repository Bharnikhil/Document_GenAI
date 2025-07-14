import fitz  # PyMuPDF

def extract_text_from_file(file):
    """
    Extract text from uploaded PDF or TXT file.
    """
    if file.name.endswith('.pdf'):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    elif file.name.endswith('.txt'):
        return file.read().decode('utf-8')

    else:
        raise ValueError("Unsupported file format")
