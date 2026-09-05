import chromadb
from sentence_transformers import SentenceTransformer
from google import genai
model=SentenceTransformer('all-MiniLM-L6-v2')
def embedding(text):
    return model.encode(text).tolist()
documents=[
    "Aramesh Rafiee is currently learning artificial intelligence.",
    "Python is a popular programming language for AI development.",
    "RAG means combining document search with text generation by a language model."
]
embeddings=[embedding(doc) for doc in documents]
chroma_client=chromadb.Client()
collection=chroma_client.create_collection(name="my_knowledge")
collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=["doc1", "doc2", "doc3"]
)
gemini=genai.Client(api_key="YOUR_API_KEY")
chat=gemini.chats.create(model="gemini-2.5-flash")
def rag(question):
    query_embedding=embedding(question)
    results=collection.query(query_embeddings=[query_embedding],n_results=2)
    context="\n".join(results["documents"][0])
    prompt=f"""Answer the questrion based only on the context below.
Context:
    {context}
Question:{question}
Answer:"""
    respones=chat.send_message(prompt)
    return respones.text
answer=rag("What is RAG?")
print(answer)
