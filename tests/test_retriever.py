from qa.retriever import Retriever

def test_retrieve_top_k():
    chunks = [
        {'id': 'c1', 'text': 'Python es un lenguaje de programación.'},
        {'id': 'c2', 'text': 'JavaScript se usa para el frontend.'},
        {'id': 'c3', 'text': 'La pizza es deliciosa.'}
    ]
    retriever = Retriever()
    retriever.index(chunks)
    results = retriever.retrieve("¿Qué es Python?")
    assert len(results) > 0
    assert results[0]['id'] == 'c1'