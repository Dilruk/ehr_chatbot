import openai
import json
import os
from dotenv import load_dotenv
import re

# Define the required structure and default values
EXPECTED_JSON_STRUCTURE = {
    "query_type": "",
    "patient_id": "",
    "name": "",
    "email": "",
    "extraction_type": "generic",
    "tables": [],
    "merge_logic": [],
    "filtering_logic": []
}


def validate_llm_response(llm_response: str) -> dict:
    """
    Validates and standardizes the LLM response JSON.
    - Ensures all required keys exist.
    - Fills missing keys with default values.
    - Standardizes filtering logic to expected format.
    """
    try:
        # Parse JSON from the LLM response
        match = re.search(r'\{.*\}', llm_response, re.DOTALL)
        parsed_query = json.loads(match.group(0))
        # parsed_query = json.loads(llm_response)

        # Ensure all required keys exist, filling missing ones with defaults
        standardized_query = {key: parsed_query.get(key, default) for key, default in EXPECTED_JSON_STRUCTURE.items()}

        # Standardize filtering logic format
        if not isinstance(standardized_query["filtering_logic"], list):
            standardized_query["filtering_logic"] = []

        # Ensure table names are always in a list
        if not isinstance(standardized_query["tables"], list):
            standardized_query["tables"] = []

        # Ensure merge logic is a list of dictionaries
        if not isinstance(standardized_query["merge_logic"], list):
            standardized_query["merge_logic"] = []
        return {"status": "success", "message": standardized_query}
    except json.JSONDecodeError:
        return {"status": "error", "message": "No records found, check your query again!"}


def get_openai_client():
    load_dotenv()  # Load environment variables from .env file
    openai_api_key = os.getenv("OPENAI_API_KEY")  # Retrieve API Key securely
    if not openai_api_key:
        raise ValueError("Missing API Key! Ensure OPENAI_API_KEY is set in .env")

    openai_client = openai.OpenAI(api_key=openai_api_key)  # Use new OpenAI client

    return openai_client
