from sentence_transformers import SentenceTransformer, util

class Retriever:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        print(f"🧠 Cargando modelo de embeddings: {model_name}")
        self.model = SentenceTransformer(model_name)
        self.embeddings = []
        self.chunks = []

    def index(self, chunks):
        self.chunks = chunks
        texts = [c['text'] for c in chunks]
        self.embeddings = self.model.encode(texts, convert_to_tensor=True)
        print(f"📦 Indexados {len(chunks)} fragmentos.")

    def retrieve(self, question, top_k=3):
        question_embedding = self.model.encode(question, convert_to_tensor=True)
        hits = util.semantic_search(question_embedding, self.embeddings, top_k=top_k)[0]
        results = []
        for hit in hits:
            idx = hit['corpus_id']
            score = hit['score']
            chunk = self.chunks[idx]
            results.append({'id': chunk['id'], 'text': chunk['text'], 'score': score})
        return results