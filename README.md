# Poly AI Research Insights 📚🤖

Poly AI Research bot is a user-friendly news research tool designed for effortless information retrieval. Users can input article URLs and ask questions to receive relevant insights from the market trends and financial domain.


![Poly Bot](https://github.com/saibattula93/PolyInnovate/blob/main/Poly%20Bot.png)


## 📊 Features
- Load URLs or upload text files containing URLs to fetch article content.
- Process article content through LangChain's UnstructuredURL Loader
- Construct an embedding vector using OpenAI's embeddings and leverage FAISS, a powerful similarity search library, to enable swift and effective retrieval of relevant information
- Interact with the LLM's (Chatgpt) by inputting queries and receiving answers along with source URLs


## Tech Stack
**Streamlit**: Powers the frontend, providing a seamless user interface. **LangChain**: Acts as the foundation for integrating the LLM into the web app. **OpenAI**: AI research and technology, powering natural language processing.

## How to use Application
### Website link:
Go through [Here](https://polyinnovate-52xkrhwtx8wn5pmh56wk3e.streamlit.app/)

### Local Setup:

1. **Clone this repository to your local machine using:**

```git clone https://github.com/saibattula93/PolyInnovate.git```

2. **Set Up a Virtual Environment:**

  ```#For Windows:```

  ```python -m venv venv```

3. **Activate the Virtual Environment:**

```#For Windows:```

```venv\Scripts\activate```

4. **Install Required Dependencies:**

```pip install -r requirements.txt```

5. **Set up your OpenAI API key** by creating a .env file in the project root and adding your API:

```openai_api_key = "OPEN AI API KEY"```

6. **Run Poly AI Bot:**

```streamlit run Home.py```

After running the command, Streamlit will provide a local URL ```http://localhost:8501/``` which you can open in your web browser to access Poly AI Bot.

## The web app will open in your browser.

On the sidebar, you can input URLs directly.

- Initiate the data loading and processing by clicking "Process URLs."

- Observe the system as it performs text splitting, generates embedding vectors, and efficiently indexes them using FAISS.

- The embeddings will be stored and indexed using FAISS, enhancing retrieval speed.

- The FAISS index will be saved in a local file path in pickle format for future use.

- One can now ask a question and get the answer based on those news articles


## Project Structure

- Home.py: The main Streamlit application script.
- requirements.txt: A list of required Python packages for the project.
- faiss_store_openai.pkl: A pickle file to store the FAISS index.
- .env: Configuration file for storing your OpenAI API key.
