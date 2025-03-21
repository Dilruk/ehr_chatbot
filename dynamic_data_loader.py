import pandas as pd

def load_structured_data():
    """
    Loads structured patient data from CSV files.
    """
    data_files = {
        "allergies": "allergies.csv",
        "diagnosis": "diagnosis.csv",
        "encounters": "encounters.csv",
        "labs": "labs.csv",
        "medications": "medications.csv",
        "notes": "notes.csv",
        "patients": "patients.csv",
        "procedures": "procedures.csv",
        "visits": "visits.csv"
    }

    structured_data = {}
    for key, file in data_files.items():
        try:
            structured_data[key] = pd.read_csv(f"data_2/{file}")
        except FileNotFoundError:
            print(f"Warning: {file} not found, skipping...")

    return structured_data


if __name__ == '__main__':
    structured_data = load_structured_data()
