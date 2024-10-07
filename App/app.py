import streamlit as st
import pandas as pd
import numpy as np
from assistant import NutritionRAG  # Make sure the assistant.py has your NutritionRAG class

st.title("Nutrition Facts Assistant")

# Load preprocessed data and FAISS index
df = pd.read_csv('preprocessed_nutrition_data.csv')
embeddings = np.load('nutrition_embeddings.npy')

# Initialize RAG system with the correct OpenAI API key
rag = NutritionRAG(df, embeddings, openai_api_key=st.secrets["OPENAI_API_KEY"])

# User input
query = st.text_input("Ask a nutrition question:", "")

if st.button("Submit"):
    if query:
        response = rag.generate_response(query)
        st.write(f"Response: {response}")
