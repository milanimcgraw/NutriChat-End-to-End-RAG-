from sentence_transformers import SentenceTransformer
import faiss
import openai
import numpy as np

class NutritionRAG:
    def __init__(self, df_nutrients, embeddings, openai_api_key):
        self.df_nutrients = df_nutrients
        self.embeddings = embeddings
        self.index = self.build_index(embeddings)
        openai.api_key = openai_api_key

    def build_index(self, embeddings):
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatL2(dimension)
        index.add(embeddings.astype('float32'))
        return index

    def retrieve(self, query, k=5):
        model = SentenceTransformer('all-MiniLM-L6-v2')
        query_embedding = model.encode([query])
        _, indices = self.index.search(query_embedding.astype('float32'), k)
        return self.df_nutrients.iloc[indices[0]]

    def generate_response(self, query):
        relevant_docs = self.retrieve(query)
        context = "\n".join(relevant_docs['description'].tolist())
        prompt = f"Context: {context}\nAnswer the following question: {query}"
        response = openai.Completion.create(model="gpt4o", prompt=prompt, max_tokens=100)
        return response.choices[0]['text']
