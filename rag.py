import chromadb
from sentence_transformers import SentenceTransformer
from google import genai

API_KEY = "YOUR_API_KEY"  # replace with your own Gemini API key

model = SentenceTransformer('all-MiniLM-L6-v2')


def embedding(text):
    return model.encode(text).tolist()


documents = [
    "Aramesh Rafiee is currently learning artificial intelligence.",
    "Python is a popular programming language for AI development.",
    "RAG means combining document search with text generation by a language model.",
]

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="my_knowledge")
collection.add(
    documents=documents,
    embeddings=[embedding(doc) for doc in documents],
    ids=[f"doc{i+1}" for i in range(len(documents))],
)

gemini_client = genai.Client(api_key=API_KEY)
chat = gemini_client.chats.create(model="gemini-2.5-flash")


def rag(question):
    query_embedding = embedding(question)
    results = collection.query(query_embeddings=[query_embedding], n_results=2)
    context = "\n".join(results["documents"][0])
    prompt = f"""Answer the question based only on the context below.
Context:
    {context}
Question: {question}
Answer:"""
    response = chat.send_message(prompt)
    return response.text


if __name__ == "__main__":
    answer = rag("What is RAG?")
    print(answer)
