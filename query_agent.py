import llm_query_parser as llm_query_parser
import llm_response_parser as llm_response_parser
from dynamic_data_loader import load_structured_data  # Load structured patient data
import logging

# Load structured patient data
structured_data = load_structured_data()

# Configure logging once in the main script
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Logging configured successfully!")


def extract_patient_data(user_query):
    """
    Main function that extracts query intent, retrieves relevant data, and applies filtering.
    """
    response = llm_query_parser.parse_query_with_llm(user_query)

    if response["status"] == "success":
        structured_query = response["message"]
        print(f"\nStructured Query: {structured_query}")

        if structured_query['extraction_type'] == "single_user":
            json_sql_query = {
                "tables": structured_query["tables"],
                "merge_logic": structured_query["merge_logic"],
                "filtering_logic": structured_query["filtering_logic"],
                "query": "patient_id == @patient_id"
            }
            result = llm_query_parser.fetch_filtered_data(structured_query['patient_id'], json_sql_query)
        else:
            json_sql_query = {
                "tables": structured_query["tables"],
                "merge_logic": structured_query["merge_logic"],
                "filtering_logic": structured_query["filtering_logic"]
            }
            result = llm_query_parser.fetch_filtered_data(None, json_sql_query)
        logger.info(f"Processed Query Result:{result['message']}")
        return result
    else:
        logger.error(response["message"])
        return response


# Example Usage
if __name__ == "__main__":
    while True:
        user_query = input("\nAsk a question: ")
        if user_query.lower() in ["exit", "quit"]:
            break
        patient_data_response = extract_patient_data(user_query)

        if patient_data_response["status"] == "error":
            final_output = "<div><h1>Record not found, Please check your query and try again!</h1></div>"
        else:
            final_output = llm_response_parser.generate_user_friendly_response(user_query=user_query, extracted_patient_data=patient_data_response["message"])

        print(f"FINAL OUTPUT: \n{final_output}")
