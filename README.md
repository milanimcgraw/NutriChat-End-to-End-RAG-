# 🤖 Nutrition Facts Chat Assistant

## ⚙️ Project Overview

The Nutrition Facts Chat Assistant is an advanced, AI-powered application that leverages Retrieval-Augmented Generation (RAG) to answer questions and provide accurate and contextual nutritional information. This project demonstrates the practical application of cutting-edge natural language processing techniques in the field of nutrition and dietary information. The dataset (nutrients_csvfile.csv) is used for comprehensive nutritional information and is sourced from Kaggle (Link:https://www.kaggle.com/datasets/niharika41298/nutrition-details-for-most-common-foods)

## ⚙️ Technical Stack

- **LLM**: OpenAI (GPT 4o)
- **RAG Evaluation**: Cosine Similarity, LLM as a Judge
- **Retrieval Evaluation**: Text and Vector Evaluations with Hit Rate, MRR 
- **Ingestion Pipeline**: Elastic Sesarch, MinSearch, PostGresSQL 
- **Interface**: Streamlit 
- **Monitoring**: Python script
- **Containerization**: Docker
- **Hybrid Search**: Langchain


> #### ⚙️ Querying the Assistant
>>**The system will use GPT-4o to retrieve and generate accurate, contextually relevant responses.The Nutrition Facts Assistant allows users to ask nutrition-related questions like:**
>*"What are the nutritional benefits of kale?"*
>*"How much protein is in chicken breast?"*
>*"Compare the fat content of whole milk and skim milk."*

## ⚙️ Evaluation Metrics

1. **Mean Reciprocal Rank (MRR)**:
   - Evaluates the rank position of the first relevant document.
   - Formula: `MRR = (1 / |Q|) * Σ (1 / rank_i)` for i = 1 to |Q|

2. **F1 Score**:
   - Harmonic mean of precision and recall.
   - Formula: `F1 = 2 * (Precision * Recall) / (Precision + Recall)`

3. **Hit Rate (HR) or Recall at k**:
   - Measures the proportion of queries for which at least one relevant document is retrieved in the top k results.
   - Formula: `HR@k = (Number of queries with at least one relevant document in top k) / |Q|`

4.  **Cosine Similarity**: Measures the similarity between the generated answers and the ground truth from our nutrition database.

5.  **LLM-as-a-Judge**: Utilizes a language model to provide a qualitative assessment of the generated answers, classifying them as RELEVANT, PARTLY_RELEVANT, or NON_RELEVANT.


## ⚙️ Reproducibility

#### Running Elastic Search 

```bash
docker run -it \
    --rm \
    --name elasticsearch \
    -m 4GB \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

If the previous command doesn't work (i.e. you see "error pulling image configuration"), try to run ElasticSearch directly from Docker Hub:

```bash
docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    elasticsearch:8.4.3
```

#### Prerequisites

Ensure you have the following software installed:
- **Git**: Version control to clone the repository.
- **Docker**: To containerize and run the application.
- **Python 3.9**: Required for running Python-based scripts locally.
- **Clone the repository**:
```git clone https://github.com/your-repo/nutrition-facts-assistant.git cd nutrition-facts-assistant```

1. **Install dependencies**:
- Ensure you're in the project's root directory and run the following: ```pip install -r requirements.txt```
2. **Run the application**:
- This project is designed to run using Docker. To start the application, run: ```docker-compose up```
3. **Open the interface**:
- Open your browser and navigate to: ```http://localhost:8501```
- You will be able to interact with the Nutrition Assistant from the Streamlit interface.

#### ⚙️ GitHub Codespaces Setup
For a seamless experience, you can run this project directly in GitHub Codespaces, which provides a cloud-based development environment.

1. **Create a Codespace**:
- Navigate to your repository on GitHub.
- Click the "Code" button, then select "Open with Codespaces".
- Create a new Codespace by selecting your desired configuration.
2. **Install Dependencies**:
- Once the Codespace is running, open the terminal within Codespaces and run: ```pip install -r requirements.txt```
3. **Run the Application**:
- Use Docker Compose to bring up the services. In the terminal, run: ```docker-compose up```
4. **Access the Application**: 
- GitHub Codespaces will provide a preview URL, or you can access it via port forwarding to view the Streamlit app.

#### ⚙️ Local Deployment

1. Set up your environment using the steps mentioned in the "Getting Started" section.
2. Ensure Docker is running on your machine.
3. Use the following command to run the app: ```docker-compose up``` 
4. You can access the app via http://localhost:8501.

## ⚙️ License

This project is released under MIT license. 

## ⚙️ Acknowledgements
---

This project was developed as part of the LLM Zoomcamp course, demonstrating practical applications of large language models and retrieval-augmented generation in the field of nutritional information systems.
