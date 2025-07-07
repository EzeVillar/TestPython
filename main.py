import argparse
import os
import sys
from qa.chunker import chunk_text
from qa.retriever import Retriever
from qa.prompt_builder import build_prompt
from qa.llm import ask_llm
from qa.logger import log_interaction

def parse_args():
    parser = argparse.ArgumentParser(description="Smart Doc QA - Preguntá sobre documentos de texto")
    parser.add_argument('--input', required=True, help='Ruta del archivo de texto (.txt)')
    parser.add_argument('--ask', help='Pregunta a realizar sobre el documento')
    return parser.parse_args()

def main():
    args = parse_args()

    if not os.path.exists(args.input):
        print(f" El archivo '{args.input}' no existe.")
        sys.exit(1)

    with open(args.input, 'r', encoding='utf-8') as f:
        document_text = f.read()

    chunks = chunk_text(document_text, method='paragraph')
    retriever = Retriever()
    retriever.index(chunks)

    if args.ask:
        top_chunks = retriever.retrieve(args.ask)
        prompt = build_prompt(args.ask, top_chunks)
        result = ask_llm(prompt)

        if "error" in result:
            print(f" Error al consultar el modelo: {result['error']}")
        else:
            print("\n Respuesta:")
            print(result["answer"])
            print("\n Citas:", ", ".join(c["id"] for c in top_chunks))
            print(f" Duracion: {result['duration']:.2f}s | Tokens: {result['tokens']} | Costo aprox: ${result['cost']:.6f}")
            log_interaction(args.ask, top_chunks, result)
    else:
        print(" Entrando en modo interactivo (escribi 'salir' para terminar)")
        while True:
            question = input(" Pregunta: ")
            if question.lower() in ['salir', 'exit', 'quit']:
                break
            top_chunks = retriever.retrieve(question)
            prompt = build_prompt(question, top_chunks)
            result = ask_llm(prompt)
            if "error" in result:
                print(f" Error: {result['error']}")
            else:
                print("\n Respuesta:")
                print(result["answer"])
                print("\n Citas:", ", ".join(c["id"] for c in top_chunks))
                print(f" Duracion: {result['duration']:.2f}s | Tokens: {result['tokens']} | Costo aprox: ${result['cost']:.6f}")
                log_interaction(question, top_chunks, result)

if __name__ == '__main__':
    main()