# import os
# import streamlit as st
# import pickle
# import time
# import langchain
# from langchain import OpenAI
# from langchain.chains import RetrievalQAWithSourcesChain
# from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.document_loaders import UnstructuredURLLoader
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS

# from dotenv import load_dotenv

# load_dotenv()

# st.title("Poly AI Research Insights 📚🤖")

# st.sidebar.title("Article URLs")

# with st.sidebar:
#     openai_api_key = "" #os.getenv("OPENAI_API_KEY") if os.getenv("OPENAI_API_KEY") is not None else ""  # only for development environment, otherwise it should return None
#     user_api_key = st.text_input("Introduce your OpenAI API Key (https://platform.openai.com/account/api-keys) 🔑", value=openai_api_key, type="password")
#     if user_api_key != "":
#         openai_api_key = user_api_key

    
    

# urls = []
# for i in range(2):
#     url = st.sidebar.text_input(f"URL {i+1} 🌐")
#     urls.append(url)


# process_url_clicked = st.sidebar.button("Process URLs 🚀")

# st.sidebar.write('### 👨‍💻 Developed by: [Sai Durga Prasad]("https://www.linkedin.com/in/saidurgaprasadbattula/")')

# file_path = "faiss_store_openai.pkl"


# main_placeholder = st.empty()
# try:
#     llm = OpenAI(temperature=0.6, max_tokens=500, openai_api_key=user_api_key)
# except Exception as e:
#     st.error(f"Error: {e}")

# if process_url_clicked:
#     loader = UnstructuredURLLoader(urls=urls)
#     main_placeholder.text("📋 Data Loading....Started....✅ ✅ ✅ ")
#     data = loader.load()

#     text_splitter = RecursiveCharacterTextSplitter(
#         separators=['\n\n', '\n','.',','],
#         chunk_size = 1000
#     )
#     main_placeholder.text("📜 Text Splitter....Started....✅ ✅ ✅ ")
#     docs = text_splitter.split_documents(data)

#     try:
#         embeddings = OpenAIEmbeddings()
#     except Exception as e:
#         st.error(f"Error: {e}")

#     vectorstore_openai = FAISS.from_documents(docs, embeddings)
#     main_placeholder.text("🔍 Embedding Vector Started Buliding.....✅ ✅ ✅ ")
#     time.sleep(2)

#     with open(file_path, "wb") as f:
#         pickle.dump(vectorstore_openai, f)


# query = main_placeholder.text_input("Question: 🤔")
# if query:
#     if os.path.exists(file_path):
#         with open(file_path, "rb") as f:
#             vectorstore = pickle.load(f)
#             chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
#             result = chain({"question": query}, return_only_outputs=True)
#             # result will be a dictionary of this format --> {"answer": "", "sources": [] }
#             st.header("Answer")
#             st.write(result["answer"])

#             # Display sources, if available
#             sources = result.get("sources", "")
#             if sources:
#                 st.subheader("Sources: 📚")
#                 sources_list = sources.split("\n")  # Split the sources by newline
#                 for source in sources_list:
#                     st.write(source)


# st.balloons()
# with open("docs.md", "r") as f:
#     st.success(f.read())


import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env (especially openai api key)

st.title("RockyBot: News Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_openai.pkl"

main_placeholder = st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)

if process_url_clicked:
    # load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")
    data = loader.load()
    # split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter...Started...✅✅✅")
    docs = text_splitter.split_documents(data)
    # create embeddings and save it to FAISS index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")
    time.sleep(2)

    # Save the FAISS index to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)

query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)
            # result will be a dictionary of this format --> {"answer": "", "sources": [] }
            st.header("Answer")
            st.write(result["answer"])

            # Display sources, if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")  # Split the sources by newline
                for source in sources_list:
                    st.write(source)