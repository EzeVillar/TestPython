from qa.chunker import chunk_text

def test_chunk_paragraphs():
    text = "Párrafo 1.\n\nPárrafo 2.\n\nPárrafo 3."
    chunks = chunk_text(text, method='paragraph')
    assert len(chunks) == 3
    assert chunks[0]['text'] == "Párrafo 1."

def test_chunk_sentences():
    text = "Esto es una oración. Esto es otra."
    chunks = chunk_text(text, method='sentence')
    assert len(chunks) == 2