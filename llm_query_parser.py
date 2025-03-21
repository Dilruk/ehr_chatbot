import re
import pandas as pd
import json
from dynamic_data_loader import load_structured_data
import Utils as Utils
import logging
logger = logging.getLogger(__name__)  # Get the existing logger

structured_data = load_structured_data()

PATIENT_IDENTIFIER_LIST = ["patient_id", "name", "email"]

def get_all_patient_identifiers(id_type, id_value):
    """
    Retrieves all available identifiers (patient_id, name, phone, email) using any known identifier.
    Uses case-insensitive and partial matching to handle variations in recorded names.
    Returns a dictionary containing all patient details including identifier type.
    """
    patients_df = structured_data.get("patients", None)

    if patients_df is None:
        return None  # No patient data available

    id_value = id_value.lower()
    # case-insensitive matching
    patients_df[id_type] = patients_df[id_type].astype(str).str.lower()
    match = patients_df[patients_df[id_type].str.contains(id_value, na=False)]
    if not match.empty:
        patient_details = match.iloc[0].to_dict()
        return {
            "patient_id": patient_details.get("patient_id"),
            "name": patient_details.get("name"),
            "phone": patient_details.get("phone"),
            "email": patient_details.get("email")
        }

    return None  # No matching patient found

def fetch_filtered_data(patient_id, query_details):
    """
    Retrieves requested data using robust merging and filtering logic.
    Handles complex queries, date conversions, and edge cases gracefully.
    """
    if not query_details.get("tables"):
        return {"status": "error", "message": "No tables specified in query details"}

    try:
        # Start with base table
        merged_df = structured_data[query_details["tables"][0]].copy()

        # Apply merge logic with conflict resolution
        for merge in query_details.get("merge_logic", []):
            right_df = structured_data[merge["right"]]
            # Identify overlapping columns (excluding join key), and renames overlapping columns in right_df
            conflicting_cols = set(merged_df.columns) & set(right_df.columns) - {merge["on"]}
            if conflicting_cols:
                right_df = right_df.rename(columns={col: f"{col}_{merge['right']}" for col in conflicting_cols})

            # Perform the merge
            merged_df = merged_df.merge(
                right_df,
                on=merge["on"],
                how=merge.get("how", "inner")
            )

        # Convert date columns to datetime objects
        date_columns = [col for col in merged_df.columns if 'date' in col.lower() or 'dob' in col.lower()]

        for col in date_columns:
            merged_df[col] = pd.to_datetime(merged_df[col], errors='coerce')

        # Apply patient ID filter if provided
        if patient_id:
            if 'patient_id' not in merged_df.columns:
                return {"status": "error", "message": "Patient ID column missing after merging"}
            merged_df = merged_df.query("patient_id == @patient_id")

        # Process advanced filtering logic
        if "filtering_logic" in query_details:
            for logic in query_details["filtering_logic"]:
                logic = str(logic).strip()
                try:
                    # Sorting logic
                    if "sort" in logic.lower() or "order" in logic.lower():
                        logic_split = logic.split(",")
                        col_name = ""
                        if len(logic_split) > 1:
                            col_name = logic_split[1]
                        ascending = True
                        if len(logic_split) > 2:
                            ascending = logic.split(",")[2] == "ascending"

                        if col_name in merged_df.columns:
                            merged_df = merged_df.sort_values(by=col_name, ascending=ascending)
                    elif "return" in logic.lower() or "limit" in logic.lower():
                        try:
                            logic_split = logic.split(",")
                            if len(logic_split) > 0:
                                limit = int(logic_split[1])
                                merged_df = merged_df.head(limit)
                        except ValueError:
                            pass
                    # Complex filtering
                    elif re.match(r'^filter:', logic, re.IGNORECASE):
                        if (match := re.match(r'filter:(.+)', logic, re.IGNORECASE)):
                            condition = match.group(1).strip()
                            # Tokenize condition by splitting on spaces while preserving quoted strings
                            # tokens = condition.split()
                            tokens = re.findall(r'\".*?\"|\S+', condition)
                            formatted_condition = []
                            i = 0
                            while i < len(tokens):
                                part = tokens[i]

                                # Check if the part is a column name
                                if part in merged_df.columns:
                                    col_name = part

                                    # Ensure the next part is a comparison operator
                                    if i + 1 < len(tokens) and tokens[i + 1] in {"==", "!=", ">=", "<=", ">", "<"}:
                                        operator = tokens[i + 1]
                                        value = tokens[i + 2] if i + 2 < len(tokens) else None

                                        # Ensure string values are quoted correctly
                                        if col_name in merged_df.select_dtypes(include=["object"]).columns:
                                            if value and not (value.startswith('"') and value.endswith('"')):
                                                value = f'"{value}"'

                                        formatted_condition.append(f"{col_name} {operator} {value}")
                                        i += 2  # Skip processed tokens
                                    else:
                                        formatted_condition.append(col_name)  # If not a condition, no changes.
                                elif part in {"AND", "OR", "(", ")"}:
                                    # Preserve logical operators and parentheses
                                    formatted_condition.append(part)
                                else:
                                    formatted_condition.append(part)

                                i += 1

                            # Join formatted condition
                            final_condition = " ".join(formatted_condition)

                            try:
                                merged_df = merged_df.query(final_condition)
                                logging.info(f"Applied filter: {final_condition}")
                            except Exception as e:
                                logging.error(f"Error applying filter '{final_condition}': {e}")

                except Exception as e:
                    print(f"Error processing '{logic}': {str(e)}")
                    continue

        return {"status": "success", "message": merged_df.to_dict(orient="records")} if not merged_df.empty else {"status": "error", "message": "No results found"}

    except KeyError as e:
        return {"status": "error", "message": f"Missing table or column: {str(e)}"}
    except Exception as e:
        return {"status": "error", "message": f"Unexpected error: {str(e)}"}

def parse_query_with_llm(user_query):
    """
    Uses an LLM to understand and format the query into structured JSON.
    Includes the full database schema to ensure LLM maps queries correctly.
    """
    schema_info = """
    Here is the database schema:

    1.**patients Table**: [Contains basic information about each user]
       - `patient_id` (PK): Unique ID for the patient.
       - `name`: Full name of the patient.
       - `dob`: Birth date.
       - `gender`: Gender.
       - `phone`: Contact number.
       - `email`: Email address.
       - `address`: Physical address.
       
    2.**diagnosis Table**: [Contains diagnosis information about each patient]
       - `_id` (PK): Unique identifier for each diagnosis.
       - `patient_id` (FK → patients.patient_id): References a patient.
       - `encounter_id` (FK → encounters._id): References the encounter.
       - `onset_date`: Date of diagnosis.
       - `notes`: Additional information.

    3.**medications Table**: [Contains medication information about each patient]
       - `patient_id` (FK → patients.patient_id): References a patient.
       - `genericName`: Name of the medication.
       - `dosage`: Dosage details.
       - `frequency`: How often the medication is taken.
       - `route`: How the medication is given (Oral or Intravenous).
       - `startDate`: When medication was started.
       - `endDate`: When medication was stopped.
       - `rxnorm_code`: Medication RxNorm Code.
       - `ndc_code`: Medication NDC Code.

    4. **procedures Table**: [Contains procedures information of each patient]
       - `id` (PK): Unique identifier for each procedure.
       - `patient_id` (FK → patients.patient_id): References a patient.
       - `status`: Indicates if the procedure is completed.
       - `performedPeriod`: Duration of the procedure.
       - `reasonCode`: Reason for procedure.
       - `performer`: Who performed the procedure.
       - `location`: Hospital location of the procedure.
       - `outcome`: Outcome of the procedure.
       - `note`: Details of the procedure.
       - `relatedObservations`: Reports of the procedure.
       - `radiologyDetails`: Radiology observations of the procedure.
       - `surgicalDetails`: Surgical observations of the procedure.
       - `hematologyDetails`: Hematology details observations of the procedure.

    5. **allergies Table**: [Contains allergies of each patient]
       - `id` (PK): Unique identifier for each allergy.
       - `patient_id` (FK → patients.patient_id): References a patient.
       - `allergenname`: Name of the allergen.
       - `category`: Category of the allergen.
       - `reaction`: Reaction of the patient to the allergen.
       - `recorded_date`: Date allergy was recorded.
       - `notes`: Observations related to allergen administration.
       - `source`: How the observations in the notes column were discovered.
       - `rxnorm_code`: Medication RxNorm Code.
       - `ndc_code`: Medication NDC Code.

    6. **labs Table**: [Contains laboratory tests and results information of each patient]
       - `patient_id` (FK → patients.patient_id): References a patient.
       - `labName`: Name of the lab test.
       - `value`: Test result value.
       - `referenceRange`: Normal range for the test.
       - `uom`: Unit of measure.
       - `sampleCollectionDate`: Date test was performed.
       - `reportedDate`: Date test results were reported.

    7. **visits Table**: [Contains hospital and clinical visit information and observations of each patient]
       - `id` (PK): Unique identifier for each patient visit to the hospital.
       - `patient_id` (FK → patients.patient_id): References a patient.
       - `appointmentID`: Appointment ID for the visit.
       - `status`: is visit completed or not.
       - `class`: Visit class (e.g., inpatient, outpatient).
       - `type`: Reason to visit.
       - `serviceProvider`: Hospital name.
       - `participant`: Information of the doctor or clinical staff attended.
       - `diagnosis`: Diagnosis of the patient.
       - `location`: Visited hospital or clinic location.
       - `reasonCode`: Reason to visit.
       - `outcome`: Outcome of the patient visit.
       - `observation`: Observations from the patient visit.
       - `billing`: Price and billing information of the patient visit.
       
    8. **notes Table**: [Contains clinical condition information about each patient's condition] 
       - `id` (PK): Unique identifier for each note.
       - `patient_id` (FK → patients.patient_id): References a patient.
       - `document_name`: Name of the document.
       - `created_at`: First notes entered date.
       - `updated_at`: Notes last updated date.
       - `institution_code`: Department of the hospital.
       - `generatedtext`: Note content detailing patient conditions and observations.
    """

    prompt = f"""
    Consider the following database schema containing 8 tables with their columns and primary and foreign key reference information.
    {schema_info}
    
    Now help me process the following query: "{user_query}"
    
    **Ensure your response follows this JSON format, and provide most efficient and highly accurate queries with minimum table merges:**
    {{
        "query_type": "<query_intent>",
        "patient_id": "<patient_id_if_available>",
        "name": "<patient_name_if_available>",
        "email": "<patient_email_if_available>",
        "extraction_type": "single_user" or "generic",
        "tables": ["<table_1>", "<table_2>", ...],
        "merge_logic": [{{"left": "<table_1>", "right": "<table_2>", "on": "patient_id"}}, ...],
        "filtering_logic": [
        "order_by,<column_name>,[ascending|descending]",
        "return,<N>",
        "limit,<N>",
        "filter:onset_date >= 'YYYY-MM-DD'"
    ]    }}
    """
    response = Utils.get_openai_client().chat.completions.create(
        model="gpt-4-1106-preview",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a query formatting assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    formatted_query = response.choices[0].message.content
    print(f"formatted_query: {formatted_query}")
    try:
        parsed_query = Utils.validate_llm_response(formatted_query)
        if parsed_query["status"] == "success":
            # Identify the extraction type: Individual or otherwise
            parsed_query = parsed_query["message"]
            if parsed_query['extraction_type'] == "single_user":
                # Identify what patient-related information is provided
                available_identifiers = {key: parsed_query[key] for key in PATIENT_IDENTIFIER_LIST if key in parsed_query and parsed_query[key]}

                # If a patient ID is required but missing, retrieve ID first
                if "patient_id" not in available_identifiers:
                    patient_identifiers = None
                    for key in ["name", "email"]:
                        if key in parsed_query and parsed_query[key]:
                            patient_identifiers = get_all_patient_identifiers(key, parsed_query[key])
                            if patient_identifiers:
                                parsed_query.update(patient_identifiers)  # Merge all patient details into parsed_query
                                break
                    if not patient_identifiers:
                        return {"status": "error", "message": "No records found, check your query again!"}
            return {"status": "success", "message": parsed_query}
        else:
            return parsed_query
    except json.JSONDecodeError:
        return {"status": "error", "message": "Invalid response format from LLM"}
