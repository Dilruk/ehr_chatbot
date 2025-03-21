import re
import pandas as pd
import json
from dynamic_data_loader import load_structured_data
import Utils as Utils
import logging
logger = logging.getLogger(__name__)  # Get the existing logger

structured_data = load_structured_data()


def generate_user_friendly_response(user_query, extracted_patient_data):
    """
    Agent 2 takes the computed data output and the initial user query and generates a HTML summary.
    """
    prompt = f""" Consider the following patient related data: {extracted_patient_data}. 
    
    Now extract the most relevant information suitable for the following query: "{user_query}". Strictly use the given information to extract the relevant information.
    Only extract the most relevant information only. Provide the response strictly in HTML <DIV>. """

    response = Utils.get_openai_client().chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a medical report summarizer. Your job is to extract the most suitable answer from the given data and structure into an easy-to-read summary strictly in HTML <DIV> format."},
            {"role": "user", "content": prompt}
        ]
    )

    response_text = response.choices[0].message.content
    print(f"[Agent 2 Response]:\n{response_text}\n")

    return response_text
