# app.py

import streamlit as st
import pdfplumber
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import os

# 1️ Set OpenAI API key

os.environ["OPENAI_API_KEY"] =  "Paste your openai_api_key"

st.set_page_config(page_title="Local RAG Chatbot - PDF", layout="wide")
st.title("RAG-Based Diabetes Guide Chatbot")

# 2️ Load PDF

pdf_file = "Diabetes Management Guide.pdf"

try:
    transcript_text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                transcript_text += text

    st.success(f" Loaded PDF: {pdf_file}")

    # 3️ Split text into chunks

    splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
    chunks = splitter.split_text(transcript_text)

    # 4️ Create embeddings & FAISS vector store

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(chunks, embeddings)

    # 5️ Create retriever & QA chain

    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0),
        retriever=retriever
    )

    # 6️ Ask questions

    query = st.text_input(f"Ask me anything about Diabetes :")
    if query:
        with st.spinner(" Thinking..."):
            answer = qa_chain.run(query)
        st.markdown(f"**Answer:** {answer}")

except FileNotFoundError:
    st.error(f"PDF file '{pdf_file}' not found in project folder.")
except Exception as e:
    st.error(f"Error reading PDF: {e}")
