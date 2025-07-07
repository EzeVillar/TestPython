from qa.prompt_builder import build_prompt

def test_prompt_contains_question_and_context():
    question = "¿Qué es Python?"
    chunks = [{'id': 'chunk_0', 'text': 'Python es un lenguaje.'}]
    prompt = build_prompt(question, chunks)
    assert "Python es un lenguaje." in prompt
    assert question in prompt