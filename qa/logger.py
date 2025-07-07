import json
from datetime import datetime

def log_interaction(question, chunks, result, path="qa_history.jsonl"):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "context_ids": [c["id"] for c in chunks],
        "tokens_total": result.get("tokens"),
        "tokens_prompt": result.get("prompt_tokens"),
        "tokens_completion": result.get("completion_tokens"),
        "cost": result.get("cost"),
        "duration_sec": result.get("duration"),
        "answer": result.get("answer")
    }
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")