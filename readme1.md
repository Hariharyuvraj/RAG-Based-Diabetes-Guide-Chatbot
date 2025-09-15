# DiabetesCare ChatBot 

A Retrieval-Augmented Generation (RAG) based chatbot that provides accurate information and support for diabetes management by leveraging authoritative medical documents and guidelines.

##  Project Overview

This project implements a RAG (Retrieval-Augmented Generation) system specifically designed to answer questions about diabetes symptoms, precautions, diet recommendations, exercise guidelines, and general management strategies. The chatbot grounds its responses in verified medical information to reduce hallucinations and provide reliable answers.

##  Features

- **Document-Based Responses**: Answers questions using information from trusted diabetes guidelines and resources
- **Source Citation**: Shows which documents were used to generate each response
- **Multi-Document Support**: Processes PDFs, TXT files, and web-based resources
- **User-Friendly Interface**: Simple chat interface built with Streamlit
- **Medical Accuracy Focus**: Designed to provide reliable information with appropriate disclaimers

##  Architecture
DiabetesCare ChatBot
│
1) Diabetes Management Guide.pdf - information abt Diabetes (PDFs, text files)
2) vector_db/ - FAISS vector store (created automatically)
3) data_processing.py - Document loading and chunking
4) mbedding_model.py - Vector embeddings setup
5) rag_chain.py - Core RAG implementation
6) Diabetes_care_chatbot.py - Streamlit web application
