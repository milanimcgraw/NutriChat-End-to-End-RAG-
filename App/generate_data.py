import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

# Load the preprocessed dataset
df = pd.read_csv('preprocessed_nutrition_data.csv')

# Load the transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
embeddings = model.encode(df['description'].astype(str).tolist())

# Save embeddings
np.save('nutrition_embeddings.npy', embeddings)

# Create a FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings.astype('float32'))

# Save FAISS index
faiss.write_index(index, 'nutrition_faiss.index')
print("Embeddings and FAISS index saved.")