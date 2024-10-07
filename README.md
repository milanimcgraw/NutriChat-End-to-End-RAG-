# 🤖 Nutrition Facts Chat Assistant

## ⚙️ Project Overview

The Nutrition Facts Chat Assistant is an advanced, AI-powered application that leverages Retrieval-Augmented Generation (RAG) to answer questions and provide accurate and contextual nutritional information. This project demonstrates the practical application of cutting-edge natural language processing techniques in the field of nutrition and dietary information. The USDA FoodData Central dataset was used for comprehensive nutritional information.

## ⚙️ Technical Stack

- **Python**: Core programming language
- **Sentence Transformers**: For text embedding and similarity calculations
- **OpenAI GPT Models**: For generating human-like responses and evaluations
- **Pandas**: For efficient data manipulation and processing
- **Matplotlib & Seaborn**: For data visualization
- **Streamlit**: For creating the interactive web interface and monitoring dashboard

> #### ⚙️ Querying the Assistant
>>**The system will use a combination of FAISS and GPT-4o to retrieve and generate accurate, contextually relevant responses.The Nutrition Facts Assistant allows users to ask nutrition-related questions like:**
>*"What are the nutritional benefits of kale?"*
>*"How much protein is in chicken breast?"*
>*"Compare the fat content of whole milk and skim milk."*
>*The system will use a combination of FAISS and GPT-4o to retrieve and generate accurate, contextually relevant responses."*

## ⚙️ Key Features

- **RAG-based Information Retrieval**: Utilizes a sophisticated RAG system witgh a FAISS index to fetch and generate relevant nutritional information from a comprehensive database.
- **Interactive User Interface**: Offers a user-friendly interface for querying nutritional information, built with Streamlit for seamless interaction and containerized with Docker for easy deployment. 
- **High-Accuracy Responses**: Employs state-of-the-art language models to ensure accurate and contextually appropriate answers to nutritional queries.
- **Performance Evaluation**: Implements rigorous evaluation metrics including Ground Truth Evaluation,Text-Based Evaluation, Vector-Based Evaluation, Cosine Similarity, and LLM-as-a-judge to assess the quality of generated responses.
- **Data Visualization**: Features insightful visualizations of system performance and nutritional data distributions.
- **Automated Data Ingestion**: Includes a robust pipeline for ingesting and processing new nutritional data, ensuring the system stays up-to-date.
- **Real-time Monitoring**: Provides a dashboard for monitoring system usage and performance and user interactions in real-time. View system performance, including response times and user ratings, via the integrated dashboard.
- **User Feedback**: Users can rate the responses (1-5), and the ratings will be stored and displayed in the dashboard.

## ⚙️ Evaluation and Metrics

This project employs a two-pronged approach to evaluate the performance of the chat assistant:

1. **Cosine Similarity**: Measures the similarity between the generated answers and the ground truth from our nutrition database.
2. **LLM-as-a-Judge**: Utilizes a language model to provide a qualitative assessment of the generated answers, classifying them as RELEVANT, PARTLY_RELEVANT, or NON_RELEVANT.

## ⚙️ Getting Started

>### Prerequisites

>Ensure you have the following software installed:
>- **Git**: Version control to clone the repository.
>- **Docker**: To containerize and run the application.
>- **Python 3.9**: Required for running Python-based scripts locally.
>- **Clone the repository**:
```git clone https://github.com/your-repo/nutrition-facts-assistant.git cd nutrition-facts-assistant```

1. **Install dependencies**:
- Ensure you're in the project's root directory and run the following: ```pip install -r requirements.txt```
2. **Run the application**:
- This project is designed to run using Docker. To start the application, run: ```docker-compose up```
3. **Open the interface**:
- Open your browser and navigate to: ```http://localhost:8501```
- You will be able to interact with the Nutrition Assistant from the Streamlit interface.

## ⚙️ GitHub Codespaces Setup
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

## ⚙️ Deployment

This project is deployed on Hugging Face Spaces. Visit [will link space] to interact with the live demo.
### ⚙️ Local Deployment

1. Set up your environment using the steps mentioned in the "Getting Started" section.
2. Ensure Docker is running on your machine.
3. Use the following command to run the app: ```docker-compose up``` 
4. You can access the app via http://localhost:8501.

### ⚙️ Deployment to Hugging Face Spaces

1. **Create a Space**:
- Go to Hugging Face Spaces and create a new space.
- Select the appropriate framework (Streamlit) and link your GitHub repository.
2. **Configure Environment Variables**:
Set the required environment variables, such as OPENAI_API_KEY, directly in the Hugging Face Space settings.
3. **Push the Repository**:
- Push the repository to Hugging Face Spaces for deployment.
- The system will automatically deploy the Streamlit application.
4. **Access the App**:
- Once deployed, users can access the live app through the Hugging Face Space.

## ⚙️ Project Structure
- **nutrition_facts_assistant.ipynb**: The Jupyter Notebook that contains the code for experimenting with data ingestion, embedding generation, vector search, and performance evaluation metrics for the RAG system. It documents the entire development process step-by-step and can be used to test changes to the system. This notebook is useful for documentation, testing, and validating each component of the system during development. It's also an excellent resource for understanding the flow of the project, from ingestion to evaluation.
- **app.py**: The Streamlit application responsible for providing the user interface. Users can input their nutrition-related queries, and this file handles the interaction with the NutritionRAG system (via assistant.py). It displays responses from the RAG system and collects user feedback.
- **assistant.py**: Core assistant code that implements the NutritionRAG class, which handles retrieval from the FAISS index and generates responses using OpenAI's GPT model. It includes the RAG pipeline, vector search with FAISS, and prompt building for GPT-4o. Responsible for retrieving relevant documents and generating nutrition-based responses.
- **db.py**: Core assistant code that implements the NutritionRAG class, which handles retrieval from the FAISS index and generates responses using OpenAI's GPT model. It includes the RAG pipeline, vector search with FAISS, and prompt building for GPT-4o. Responsible for retrieving relevant documents and generating nutrition-based responses.
- **generate_data.py**: Script responsible for processing the nutritional data and generating embeddings using Sentence Transformers. Creates a FAISS index for fast retrieval during the query phase. This script should be run when preprocessing the nutrition dataset, ensuring it is ready for querying.
- **requirements.txt**:  Lists all the Python dependencies required for the project, ensuring the environment is set up with the correct libraries and versions. Includes packages such as pandas, sentence-transformers, faiss-cpu, and openai to power the RAG pipeline.
- **docker-compose.yaml**: Defines the services necessary to run the project in a containerized environment using Docker. Sets up the Streamlit application to run on port 8501 and enables easy container management. Provides instructions for managing the environment with Docker Compose.
- **Dockerfile**: Builds a Docker image for the application, including all necessary dependencies and Python packages. Ensures that the application can be deployed in a consistent, reproducible environment. The entry point is set to run the Streamlit app (app.py).

## ⚙️ License

This project is released under MIT license. 

## ⚙️ Acknowledgements


---

This project was developed as part of the LLM Zoomcamp course, demonstrating practical applications of large language models and retrieval-augmented generation in the field of nutritional information systems.
