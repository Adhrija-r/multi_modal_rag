import json
from src.retriever.retriever import retrieve
from src.generation.qa_generator import generate_answer

def run_eval(queries_file="src/eval/eval_queries.json"):
    with open(queries_file, "r", encoding="utf-8") as f:
        queries = json.load(f)
    results = []
    for q in queries:
        qry = q["query"]
        retrieved = retrieve(qry, k=5)
        ans = generate_answer(qry, retrieved)
        results.append({"query": qry, "answer": ans})
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    run_eval()