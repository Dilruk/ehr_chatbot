# 🏥 EHR Chatbot

An AI-powered chatbot designed to interact with **Electronic Health Records (EHR)** to help healthcare professionals retrieve patient information, summarize medical history, and answer clinical questions using **natural language**.

---

## 📜 Overview

The EHR Chatbot enables **efficient retrieval and summarization** of patient data stored in EHR systems. It follows a structured pipeline to process queries, extract relevant data, and generate meaningful responses.

---

## 🛠️ System Architecture

The chatbot's architecture follows a modular approach:

1. **Data Storage Module**: Stores structured EHR data.
2. **User Query**: A healthcare provider submits a question.
3. **Query Parser Agent**: Interprets the query and converts it into a structured format.
4. **Data Extractor Module**: Retrieves relevant data from storage.
5. **Data Storage Interaction**: Fetches necessary records.
6. **Response Generator Agent**: Constructs a natural language response.
7. **Response Sent to User**: The chatbot delivers the final answer.
