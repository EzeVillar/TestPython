import re

def chunk_text(text, method='paragraph'):
    chunks = []
    if method == 'paragraph':
        raw_chunks = text.split('\n\n')
    elif method == 'sentence':
        raw_chunks = re.split(r'(?<=[.!?]) +', text)
    else:
        raise ValueError("El método debe ser 'paragraph' o 'sentence'")
    for idx, chunk in enumerate(raw_chunks):
        clean = chunk.strip()
        if clean:
            chunks.append({'id': f'chunk_{idx}', 'text': clean})
    return chunks