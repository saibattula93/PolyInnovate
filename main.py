import os
import streamlit as st
import pickle
import time
import langchain
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()

st.title("Poly Reas & Deve Tools")

st.sidebar.title("Article URLs")


urls = []
for i in range(2):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)


process_url_clicked = st.sidebar.button("Process URLs")

file_path = "faiss_store_openai.pkl"


main_placefolder = st.empty()

if process_url_clicked:
    loader = UnstructuredURLLoader(urls=urls)
    main_placefolder.text("Data Loading....Started....")
    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n','.',','],
        chunk_size = 1000
    )
    main_placefolder.text("Text Splitter....Started....")
    docs = text_splitter.split_documents(data)

    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placefolder.text("Embedding Vector Started Buliding.....")
    time.sleep(2)

    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)


