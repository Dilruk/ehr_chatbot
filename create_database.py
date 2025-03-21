import pandas as pd
import os

patient_001 = [{
  "patient": {
    "patient_id": "p_001",
    "name": "John A. Doe",
    "dob": "1965-04-12",
    "gender": "male",
    "address": "456 Elm Street, Springfield, USA",
    "contact": {
      "phone": "555-123-4567",
      "email": "johndoe@example.com"
    }
  }
}, {
  "encounters": [
    {
      "_id": "enc_1001",
      "resourceType": "Encounter",
      "status": "completed",
      "class": {
        "code": "EMER",
        "display": "Emergency"
      },
      "type": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "185349003",
              "display": "Emergency Department Visit"
            }
          ]
        }
      ],
      "patientId": "p_001",
      "participants": [
        {
          "individual": {
            "reference": "Practitioner/pract_100",
            "display": "Dr. Emily Richards"
          },
          "role": {
            "code": "ATND",
            "display": "Attending Physician"
          }
        }
      ],
      "reasonCode": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "267036007",
              "display": "Shortness of breath"
            }
          ]
        }
      ],
      "diagnosis": [
        {
          "reference": "Condition/cond_2001",
          "display": "Acute Exacerbation of Chronic Obstructive Pulmonary Disease"
        }
      ],
      "serviceProvider": {
        "reference": "Organization/org_001",
        "display": "Springfield General Hospital"
      },
      "location": [
        {
          "reference": "Location/loc_301",
          "display": "Emergency Room 1",
          "period": {
            "start": "2021-03-15T08:30:00Z",
            "end": "2021-03-15T10:00:00Z"
          }
        }
      ],
      "period": {
        "start": "2021-03-15T08:30:00Z",
        "end": "2021-03-15T10:00:00Z"
      },
      "relatedVisits": ["visit_5001"],
      "billing": {
        "lineItems": [
          {
            "sequence": 1,
            "productOrService": {
              "coding": [
                {
                  "system": "http://www.ama-assn.org/go/cpt",
                  "code": "99284",
                  "display": "Emergency department visit, moderate severity"
                }
              ]
            },
            "price": {
              "value": 750.00,
              "currency": "USD"
            }
          }
        ],
        "status": "billed"
      }
    },
    {
      "_id": "enc_1002",
      "resourceType": "Encounter",
      "status": "completed",
      "class": {
        "code": "AMB",
        "display": "Outpatient"
      },
      "type": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "185349003",
              "display": "Follow-up Visit"
            }
          ]
        }
      ],
      "patientId": "p_001",
      "participants": [
        {
          "individual": {
            "reference": "Practitioner/pract_101",
            "display": "Dr. Michael Thompson"
          },
          "role": {
            "code": "ATND",
            "display": "Attending Physician"
          }
        }
      ],
      "reasonCode": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "65363002",
              "display": "Lung Cancer Follow-up"
            }
          ]
        }
      ],
      "diagnosis": [
        {
          "reference": "Condition/cond_2002",
          "display": "Stage II Non-Small Cell Lung Cancer"
        }
      ],
      "serviceProvider": {
        "reference": "Organization/org_002",
        "display": "National Cancer Center"
      },
      "location": [
        {
          "reference": "Location/loc_302",
          "display": "Oncology Outpatient Clinic",
          "period": {
            "start": "2021-04-10T14:00:00Z",
            "end": "2021-04-10T15:00:00Z"
          }
        }
      ],
      "period": {
        "start": "2021-04-10T14:00:00Z",
        "end": "2021-04-10T15:00:00Z"
      },
      "relatedVisits": ["visit_5002"],
      "billing": {
        "lineItems": [
          {
            "sequence": 1,
            "productOrService": {
              "coding": [
                {
                  "system": "http://www.ama-assn.org/go/cpt",
                  "code": "99213",
                  "display": "Office or other outpatient visit for the evaluation and management of an established patient"
                }
              ]
            },
            "price": {
              "value": 150.00,
              "currency": "USD"
            }
          }
        ],
        "status": "billed"
      }
    },
    {
      "_id": "enc_1003",
      "resourceType": "Encounter",
      "status": "completed",
      "class": {
        "code": "INPT",
        "display": "Inpatient"
      },
      "type": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "18345009",
              "display": "Chemotherapy Session"
            }
          ]
        }
      ],
      "patientId": "p_001",
      "participants": [
        {
          "individual": {
            "reference": "Practitioner/pract_102",
            "display": "Dr. Sarah Lee"
          },
          "role": {
            "code": "ATND",
            "display": "Attending Physician"
          }
        }
      ],
      "reasonCode": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "58572004",
              "display": "Chemotherapy Treatment"
            }
          ]
        }
      ],
      "diagnosis": [
        {
          "reference": "Condition/cond_2002",
          "display": "Stage II Non-Small Cell Lung Cancer"
        }
      ],
      "serviceProvider": {
        "reference": "Organization/org_002",
        "display": "National Cancer Center"
      },
      "location": [
        {
          "reference": "Location/loc_303",
          "display": "Chemotherapy Unit",
          "period": {
            "start": "2021-06-01T09:00:00Z",
            "end": "2021-06-01T17:00:00Z"
          }
        }
      ],
      "period": {
        "start": "2021-06-01T09:00:00Z",
        "end": "2021-06-01T17:00:00Z"
      },
      "relatedVisits": ["visit_5003"],
      "billing": {
        "lineItems": [
          {
            "sequence": 1,
            "productOrService": {
              "coding": [
                {
                  "system": "http://www.ama-assn.org/go/cpt",
                  "code": "96413",
                  "display": "Chemotherapy administration, subcutaneous or intramuscular"
                }
              ]
            },
            "price": {
              "value": 500.00,
              "currency": "USD"
            }
          }
        ],
        "status": "billed"
      }
    }
  ]
},{
  "visits": [
    {
      "_id": "visit_5001",
      "resourceType": "Visit",
      "encounterID": ["enc_1001"],
      "patient_id": "p_001",
      "appointmentID": "app_9001",
      "status": "completed",
      "class": {
        "code": "EMER",
        "display": "Emergency"
      },
      "type": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "185349003",
              "display": "Emergency Department Visit"
            }
          ]
        }
      ],
      "serviceProvider": {
        "reference": "Organization/org_001",
        "display": "Springfield General Hospital"
      },
      "participant": {
        "individual": {
          "reference": "Practitioner/pract_100",
          "display": "Dr. Emily Richards"
        },
        "role": {
          "coding": [
            {
              "system": "http://terminology.hl7.org/CodeSystem/practitioner-role",
              "code": "attending",
              "display": "Attending Physician"
            }
          ]
        }
      },
      "diagnosis": [
        {
          "condition": {
            "coding": [
              {
                "system": "http://hl7.org/fhir/sid/icd-10",
                "code": "J44.1",
                "display": "Chronic obstructive pulmonary disease with (acute) exacerbation"
              }
            ]
          }
        }
      ],
      "location": {
        "reference": "Location/loc_301",
        "display": "Emergency Room 1",
        "period": {
          "start": "2021-03-15T08:30:00Z",
          "end": "2021-03-15T10:00:00Z"
        }
      },
      "reasonCode": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "267036007",
              "display": "Shortness of breath"
            }
          ]
        }
      ],
      "outcome": "Stabilized and discharged",
      "observation": [
        {
          "category": "vital-signs",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "8480-6",
                "display": "Systolic blood pressure"
              }
            ]
          },
          "valueQuantity": {
            "value": 150,
            "unit": "mmHg",
            "system": "http://unitsofmeasure.org",
            "code": "mm[Hg]"
          },
          "effectiveDateTime": "2021-03-15T09:00:00Z"
        }
      ],
      "billing": {
        "lineItems": [
          {
            "sequence": 1,
            "productOrService": {
              "coding": [
                {
                  "system": "http://www.ama-assn.org/go/cpt",
                  "code": "99284",
                  "display": "Emergency department visit, moderate severity"
                }
              ]
            },
            "price": {
              "value": 750.00,
              "currency": "USD"
            }
          }
        ],
        "status": "billed"
      }
    },
    {
      "_id": "visit_5002",
      "resourceType": "Visit",
      "encounterID": ["enc_1002"],
      "patient_id": "p_001",
      "appointmentID": "app_9002",
      "status": "completed",
      "class": {
        "code": "AMB",
        "display": "Outpatient"
      },
      "type": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "185349003",
              "display": "Follow-up Visit"
            }
          ]
        }
      ],
      "serviceProvider": {
        "reference": "Organization/org_002",
        "display": "National Cancer Center"
      },
      "participant": {
        "individual": {
          "reference": "Practitioner/pract_101",
          "display": "Dr. Michael Thompson"
        },
        "role": {
          "coding": [
            {
              "system": "http://terminology.hl7.org/CodeSystem/practitioner-role",
              "code": "attending",
              "display": "Attending Physician"
            }
          ]
        }
      },
      "diagnosis": [
        {
          "condition": {
            "coding": [
              {
                "system": "http://hl7.org/fhir/sid/icd-10",
                "code": "C34.1",
                "display": "Malignant neoplasm of upper lobe, bronchus or lung"
              }
            ]
          }
        }
      ],
      "location": {
        "reference": "Location/loc_302",
        "display": "Oncology Outpatient Clinic",
        "period": {
          "start": "2021-04-10T14:00:00Z",
          "end": "2021-04-10T15:00:00Z"
        }
      },
      "reasonCode": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "65363002",
              "display": "Lung Cancer Follow-up"
            }
          ]
        }
      ],
      "outcome": "Scheduled for chemotherapy",
      "observation": [
        {
          "category": "laboratory",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "2160-0",
                "display": "Hemoglobin [Mass/volume] in Blood"
              }
            ]
          },
          "valueQuantity": {
            "value": 13.5,
            "unit": "g/dL",
            "system": "http://unitsofmeasure.org",
            "code": "g/dL"
          },
          "effectiveDateTime": "2021-04-10T14:30:00Z"
        }
      ],
      "billing": {
        "lineItems": [
          {
            "sequence": 1,
            "productOrService": {
              "coding": [
                {
                  "system": "http://www.ama-assn.org/go/cpt",
                  "code": "99213",
                  "display": "Office or other outpatient visit for the evaluation and management of an established patient"
                }
              ]
            },
            "price": {
              "value": 150.00,
              "currency": "USD"
            }
          }
        ],
        "status": "billed"
      }
    },
    {
      "_id": "visit_5003",
      "resourceType": "Visit",
      "encounterID": ["enc_1003"],
      "patient_id": "p_001",
      "appointmentID": "app_9003",
      "status": "completed",
      "class": {
        "code": "INPT",
        "display": "Inpatient"
      },
      "type": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "18345009",
              "display": "Chemotherapy Session"
            }
          ]
        }
      ],
      "serviceProvider": {
        "reference": "Organization/org_002",
        "display": "National Cancer Center"
      },
      "participant": {
        "individual": {
          "reference": "Practitioner/pract_102",
          "display": "Dr. Sarah Lee"
        },
        "role": {
          "coding": [
            {
              "system": "http://terminology.hl7.org/CodeSystem/practitioner-role",
              "code": "attending",
              "display": "Attending Physician"
            }
          ]
        }
      },
      "diagnosis": [
        {
          "condition": {
            "coding": [
              {
                "system": "http://hl7.org/fhir/sid/icd-10",
                "code": "C34.1",
                "display": "Malignant neoplasm of upper lobe, bronchus or lung"
              }
            ]
          }
        }
      ],
      "location": {
        "reference": "Location/loc_303",
        "display": "Chemotherapy Unit",
        "period": {
          "start": "2021-06-01T09:00:00Z",
          "end": "2021-06-01T17:00:00Z"
        }
      },
      "reasonCode": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "58572004",
              "display": "Chemotherapy Treatment"
            }
          ]
        }
      ],
      "outcome": "Chemotherapy administered successfully",
      "observation": [
        {
          "category": "laboratory",
          "code": {
            "coding": [
              {
                "system": "http://loinc.org",
                "code": "718-7",
                "display": "White blood cells [#/volume] in Blood"
              }
            ]
          },
          "valueQuantity": {
            "value": 4.5,
            "unit": "10^3/uL",
            "system": "http://unitsofmeasure.org",
            "code": "10*3/uL"
          },
          "effectiveDateTime": "2021-06-01T12:00:00Z"
        }
      ],
      "billing": {
        "lineItems": [
          {
            "sequence": 1,
            "productOrService": {
              "coding": [
                {
                  "system": "http://www.ama-assn.org/go/cpt",
                  "code": "96413",
                  "display": "Chemotherapy administration, subcutaneous or intramuscular"
                }
              ]
            },
            "price": {
              "value": 500.00,
              "currency": "USD"
            }
          }
        ],
        "status": "billed"
      }
    }
  ]
}, {
  "procedures": [
    {
      "resourceType": "Procedure",
      "id": "proc_3001",
      "patient_id": "p_001",
      "status": "completed",
      "code": [
        {
          "system": "http://snomed.info/sct",
          "code": "73761001",
          "display": "Biopsy of lung"
        }
      ],
      "performedPeriod": {
        "start": "2020-02-20T10:00:00Z",
        "end": "2020-02-20T10:30:00Z"
      },
      "reasonCode": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "65363002",
              "display": "Lung mass evaluation"
            }
          ]
        }
      ],
      "performer": [
        {
          "actor": {
            "reference": "Practitioner/pract_103",
            "display": "Dr. Laura Kim"
          },
          "role": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/practitioner-role",
                "code": "surgeon",
                "display": "Surgeon"
              }
            ]
          }
        }
      ],
      "location": {
        "reference": "Location/loc_304",
        "display": "Surgical Suite 2"
      },
      "outcome": "Diagnosis confirmed as non-small cell lung carcinoma",
      "note": [
        {
          "text": "Procedure was well-tolerated. Tissue samples sent for histopathological analysis."
        }
      ],
      "relatedObservations": [
        {
          "reference": "Observation/obs_4001",
          "display": "Histopathology Report"
        }
      ],
      "radiologyDetails": {
        "imagingStudy": {
          "modality": "CT",
          "bodySite": {
            "coding": [
              {
                "system": "http://snomed.info/sct",
                "code": "51185008",
                "display": "Lung"
              }
            ]
          },
          "result": "Mass identified in upper lobe",
          "interpretation": {
            "coding": [
              {
                "system": "http://snomed.info/sct",
                "code": "281296001",
                "display": "Benign"
              }
            ]
          }
        }
      },
      "encounterID": ["enc_1004"]
    },
    {
      "resourceType": "Procedure",
      "id": "proc_3002",
      "patient_id": "p_001",
      "status": "completed",
      "code": [
        {
          "system": "http://snomed.info/sct",
          "code": "27447003",
          "display": "Chest CT Scan"
        }
      ],
      "performedPeriod": {
        "start": "2021-05-15T09:00:00Z",
        "end": "2021-05-15T10:00:00Z"
      },
      "reasonCode": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "65363002",
              "display": "Lung Cancer Follow-up"
            }
          ]
        }
      ],
      "performer": [
        {
          "actor": {
            "reference": "Practitioner/pract_104",
            "display": "Dr. Alan Walker"
          },
          "role": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/practitioner-role",
                "code": "radiologist",
                "display": "Radiologist"
              }
            ]
          }
        }
      ],
      "location": {
        "reference": "Location/loc_305",
        "display": "Radiology Department"
      },
      "outcome": "No evidence of metastasis",
      "note": [
        {
          "text": "CT scan performed without complications. No new lesions detected."
        }
      ],
      "relatedObservations": [
        {
          "reference": "Observation/obs_4002",
          "display": "Radiology Report - Chest CT"
        }
      ],
      "radiologyDetails": {
        "imagingStudy": {
          "modality": "CT",
          "bodySite": {
            "coding": [
              {
                "system": "http://snomed.info/sct",
                "code": "51185008",
                "display": "Chest"
              }
            ]
          },
          "result": "No new metastasis observed",
          "interpretation": {
            "coding": [
              {
                "system": "http://snomed.info/sct",
                "code": "129300006",
                "display": "No evidence of disease"
              }
            ]
          }
        }
      },
      "encounterID": ["enc_1002"]
    },
    {
      "resourceType": "Procedure",
      "id": "proc_3003",
      "patient_id": "p_001",
      "status": "completed",
      "code": [
        {
          "system": "http://snomed.info/sct",
          "code": "49550000",
          "display": "Lung Surgery"
        }
      ],
      "performedPeriod": {
        "start": "2022-08-20T07:00:00Z",
        "end": "2022-08-20T15:00:00Z"
      },
      "reasonCode": [
        {
          "coding": [
            {
              "system": "http://snomed.info/sct",
              "code": "65363002",
              "display": "Lung Cancer Treatment"
            }
          ]
        }
      ],
      "performer": [
        {
          "actor": {
            "reference": "Practitioner/pract_105",
            "display": "Dr. Karen White"
          },
          "role": {
            "coding": [
              {
                "system": "http://terminology.hl7.org/CodeSystem/practitioner-role",
                "code": "surgeon",
                "display": "Surgeon"
              }
            ]
          }
        }
      ],
      "location": {
        "reference": "Location/loc_306",
        "display": "Surgical Wing 3"
      },
      "outcome": "Successful resection of tumor",
      "note": [
        {
          "text": "Patient underwent lobectomy without complications. Post-operative recovery is progressing well."
        }
      ],
      "relatedObservations": [
        {
          "reference": "Observation/obs_4003",
          "display": "Surgical Report - Lobectomy"
        }
      ],
      "radiologyDetails": {
        "imagingStudy": {
          "modality": "MRI",
          "bodySite": {
            "coding": [
              {
                "system": "http://snomed.info/sct",
                "code": "51185008",
                "display": "Lung"
              }
            ]
          },
          "result": "Tumor successfully resected",
          "interpretation": {
            "coding": [
              {
                "system": "http://snomed.info/sct",
                "code": "281296001",
                "display": "Normal post-operative findings"
              }
            ]
          }
        }
      },
      "encounterID": ["enc_1005"]
    }
  ]
}, {
  "diagnosis": [
    {
      "_id": "cond_2001",
      "encounterID": "enc_1001",
      "patient_id": "p_001",
      "encounter_id": "enc_1001",
      "code": [
        {
          "system": "ICD-10",
          "code": "J44.1",
          "display": "Chronic obstructive pulmonary disease with (acute) exacerbation"
        }
      ],
      "onset_date": "2021-03-15",
      "notes": "Patient presented with acute shortness of breath and was diagnosed with COPD exacerbation."
    },
    {
      "_id": "cond_2002",
      "encounterID": "enc_1002",
      "patient_id": "p_001",
      "encounter_id": "enc_1002",
      "code": [
        {
          "system": "ICD-10",
          "code": "C34.1",
          "display": "Malignant neoplasm of upper lobe, bronchus or lung"
        }
      ],
      "onset_date": "2020-02-20",
      "notes": "Biopsy confirmed Stage II Non-Small Cell Lung Cancer."
    },
    {
      "_id": "cond_2003",
      "encounterID": "enc_1002",
      "patient_id": "p_001",
      "encounter_id": "enc_1002",
      "code": [
        {
          "system": "ICD-10",
          "code": "I10",
          "display": "Essential (primary) hypertension"
        }
      ],
      "onset_date": "2018-07-10",
      "notes": "Diagnosed during routine check-up. Managed with ACE inhibitors."
    },
    {
      "_id": "cond_2004",
      "encounterID": "enc_1003",
      "patient_id": "p_001",
      "encounter_id": "enc_1003",
      "code": [
        {
          "system": "ICD-10",
          "code": "E11.9",
          "display": "Type 2 diabetes mellitus without complications"
        }
      ],
      "onset_date": "2019-05-22",
      "notes": "Screened positive during hospitalization. Started on Metformin."
    }
  ]
}, {
  "labs": [
    {
      "patient_id": "p_001",
      "labName": "Complete Blood Count",
      "value": "Normal",
      "referenceRange": "Normal",
      "sampleCollectionDate": "2021-03-15",
      "code": [
        {
          "name": "loinc",
          "value": "57021-8"
        },
        {
          "name": "snomed",
          "value": "8648-8"
        }
      ],
      "reportedDate": "2021-03-15",
      "uom": "N/A"
    },
    {
      "patient_id": "p_001",
      "labName": "Hemoglobin A1c",
      "value": "6.8%",
      "referenceRange": "4.0-5.6%",
      "sampleCollectionDate": "2022-01-10",
      "code": [
        {
          "name": "loinc",
          "value": "4548-4"
        },
        {
          "name": "snomed",
          "value": "160773003"
        }
      ],
      "reportedDate": "2022-01-10",
      "uom": "%"
    },
    {
      "patient_id": "p_001",
      "labName": "Creatinine",
      "value": "1.1 mg/dL",
      "referenceRange": "0.6-1.2 mg/dL",
      "sampleCollectionDate": "2023-06-18",
      "code": [
        {
          "name": "loinc",
          "value": "2160-0"
        },
        {
          "name": "snomed",
          "value": "30331-1"
        }
      ],
      "reportedDate": "2023-06-18",
      "uom": "mg/dL"
    },
    {
      "patient_id": "p_001",
      "labName": "Liver Function Test",
      "value": "Elevated AST and ALT",
      "referenceRange": "Normal",
      "sampleCollectionDate": "2021-06-01",
      "code": [
        {
          "name": "loinc",
          "value": "48076-2"
        },
        {
          "name": "snomed",
          "value": "55530-1"
        }
      ],
      "reportedDate": "2021-06-01",
      "uom": "N/A"
    }
  ]
}, {
  "medications": [
    {
      "patient_id": "p_001",
      "genericName": "Lisinopril",
      "dosage": "10 mg",
      "frequency": "Once Daily",
      "route": "Oral",
      "startDate": "2018-07-10",
      "endDate": "2024-12-31",
      "code": [
        {
          "name": "RxNorm",
          "value": "LP653-10"
        },
        {
          "name": "NDC",
          "value": "00054-0055-20"
        }
      ]
    },
    {
      "patient_id": "p_001",
      "genericName": "Metformin",
      "dosage": "500 mg",
      "frequency": "Twice Daily",
      "route": "Oral",
      "startDate": "2019-05-22",
      "endDate": "2024-12-31",
      "code": [
        {
          "name": "RxNorm",
          "value": "860975"
        },
        {
          "name": "NDC",
          "value": "00591-0207-01"
        }
      ]
    },
    {
      "patient_id": "p_001",
      "genericName": "Etoposide",
      "dosage": "100 mg",
      "frequency": "Once Daily",
      "route": "Intravenous",
      "startDate": "2021-06-01",
      "endDate": "2021-06-15",
      "code": [
        {
          "name": "RxNorm",
          "value": "311602"
        },
        {
          "name": "NDC",
          "value": "00093-0741-01"
        }
      ]
    },
    {
      "patient_id": "p_001",
      "genericName": "Cisplatin",
      "dosage": "50 mg",
      "frequency": "Once Weekly",
      "route": "Intravenous",
      "startDate": "2021-06-01",
      "endDate": "2022-02-01",
      "code": [
        {
          "name": "RxNorm",
          "value": "310402"
        },
        {
          "name": "NDC",
          "value": "00093-0742-01"
        }
      ]
    }
  ]
}, {
  "allergies": [
    {
      "_id": "allergy_4001",
      "patient_id": "p_001",
      "allergenname": "Penicillin",
      "category": "Medication",
      "code": [
        {
          "name": "RxNorm",
          "value": "103470"
        },
        {
          "name": "NDC",
          "value": "00093-0007-02"
        }
      ],
      "reaction": {
        "reactionname": "Rash",
        "severity": "Mild",
        "code": [
          {
            "system": "http://snomed.info/sct",
            "code": "271807003",
            "display": "Rash"
          }
        ]
      },
      "recorded_date": "2017-11-05",
      "notes": "Develops rash upon administration of penicillin.",
      "source": "Patient Reported"
    },
    {
      "_id": "allergy_4002",
      "patient_id": "p_001",
      "allergenname": "Latex",
      "category": "Environmental",
      "code": [
        {
          "name": "RxNorm",
          "value": "Unknown"
        },
        {
          "name": "NDC",
          "value": "Unknown"
        }
      ],
      "reaction": {
        "reactionname": "Anaphylaxis",
        "severity": "Severe",
        "code": [
          {
            "system": "http://snomed.info/sct",
            "code": "235719002",
            "display": "Anaphylaxis"
          }
        ]
      },
      "recorded_date": "2019-08-12",
      "notes": "Severe allergic reaction to latex gloves used during surgery.",
      "source": "Medical Record"
    }
  ]
}, {
  "notes": [
    {
      "_id": "note_6001",
      "document_name": "Initial Diagnosis Note",
      "entered_date": "2020-02-20T11:00:00Z",
      "institution_code": "NCC",
      "sections": [
        {
          "key": "Chief Complaint",
          "text": "Persistent cough and chest pain."
        },
        {
          "key": "Diagnosis",
          "text": "Stage II Non-Small Cell Lung Cancer."
        },
        {
          "key": "Plan",
          "text": "Schedule for biopsy and initiate treatment protocol."
        }
      ],
      "generatedtext": "Patient presents with persistent cough and chest pain. Imaging suggests a mass in the upper lobe of the lung. Biopsy scheduled for further evaluation.",
      "generatedtextLoc": "/path/to/generated/file/Initial_Diagnosis_Note_2020-02-20.txt",
      "created_at": "2020-02-20T11:05:00Z",
      "updated_at": "2020-02-20T11:10:00Z"
    },
    {
      "_id": "note_6002",
      "document_name": "Biopsy Report",
      "entered_date": "2020-02-21T09:30:00Z",
      "institution_code": "NCC",
      "sections": [
        {
          "key": "Findings",
          "text": "Malignant cells consistent with non-small cell carcinoma."
        },
        {
          "key": "Conclusion",
          "text": "Diagnosis confirmed as Stage II Non-Small Cell Lung Cancer."
        }
      ],
      "generatedtext": "The biopsy reveals malignant cells indicative of non-small cell carcinoma. No evidence of metastasis at this stage.",
      "generatedtextLoc": "/path/to/generated/file/Biopsy_Report_2020-02-21.txt",
      "created_at": "2020-02-21T09:35:00Z",
      "updated_at": "2020-02-21T09:40:00Z"
    },
    {
      "_id": "note_6003",
      "document_name": "Treatment Plan Consult Note",
      "entered_date": "2020-03-01T10:00:00Z",
      "institution_code": "DMO",
      "sections": [
        {
          "key": "Treatment Options",
          "text": "Surgery followed by chemotherapy."
        },
        {
          "key": "Recommendations",
          "text": "Proceed with lobectomy to remove affected lung tissue."
        }
      ],
      "generatedtext": "After evaluating the patient's condition, it is recommended to proceed with a lobectomy followed by chemotherapy to ensure comprehensive treatment.",
      "generatedtextLoc": "/path/to/generated/file/Treatment_Plan_Consult_Note_2020-03-01.txt",
      "created_at": "2020-03-01T10:05:00Z",
      "updated_at": "2020-03-01T10:15:00Z"
    },
    {
      "_id": "note_6004",
      "document_name": "Radiology Follow-up Note",
      "entered_date": "2021-05-15T11:00:00Z",
      "institution_code": "DRO",
      "sections": [
        {
          "key": "Imaging Results",
          "text": "Chest CT shows no new metastasis."
        },
        {
          "key": "Assessment",
          "text": "Patient shows positive response to chemotherapy."
        }
      ],
      "generatedtext": "Recent chest CT indicates no new metastatic lesions. The patient is responding well to the current chemotherapy regimen.",
      "generatedtextLoc": "/path/to/generated/file/Radiology_Followup_Note_2021-05-15.txt",
      "created_at": "2021-05-15T11:05:00Z",
      "updated_at": "2021-05-15T11:10:00Z"
    },
    {
      "_id": "note_6005",
      "document_name": "Surgical Report",
      "entered_date": "2022-08-20T16:00:00Z",
      "institution_code": "Surgery",
      "sections": [
        {
          "key": "Procedure",
          "text": "Lobectomy performed successfully."
        },
        {
          "key": "Post-operative Plan",
          "text": "Continue chemotherapy and monitor recovery."
        }
      ],
      "generatedtext": "The patient underwent a successful lobectomy with no intraoperative complications. Post-operative recovery is progressing as expected.",
      "generatedtextLoc": "/path/to/generated/file/Surgical_Report_2022-08-20.txt",
      "created_at": "2022-08-20T16:05:00Z",
      "updated_at": "2022-08-20T16:15:00Z"
    },
    {
      "_id": "note_6006",
      "document_name": "Follow-up Consult Note",
      "entered_date": "2023-06-18T09:30:00Z",
      "institution_code": "NCC",
      "sections": [
        {
          "key": "Current Status",
          "text": "Patient reports no significant symptoms."
        },
        {
          "key": "Plan",
          "text": "Continue maintenance therapy and schedule next follow-up."
        }
      ],
      "generatedtext": "The patient is currently asymptomatic and tolerating maintenance therapy well. Next follow-up scheduled in three months.",
      "generatedtextLoc": "/path/to/generated/file/Followup_Consult_Note_2023-06-18.txt",
      "created_at": "2023-06-18T09:35:00Z",
      "updated_at": "2023-06-18T09:40:00Z"
    }
  ]
} ]
patient_002 = [
  {"patient":{
  "patient_id": "p_002",
  "name": {
    "given": "Karen",
    "family": "Wee"
  },
  "gender": "female",
  "birthDate": "1985-04-12",
  "contact": [
    {
      "system": "phone",
      "value": "+1-555-123-4567",
      "use": "mobile"
    },
    {
      "system": "email",
      "value": "karen.wee@example.com",
      "use": "home"
    }
  ],
  "address": {
    "line": ["123 Maple Street"],
    "city": "Springfield",
    "state": "IL",
    "postalCode": "62704",
    "country": "USA"
  }
}},
{"encounters": [
    {
  "_id": "enc_001",
  "resourceType": "Encounter",
  "status": "completed",
  "class": {
    "code": "AMB",
    "display": "Outpatient"
  },
  "type": [
    {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "185349003",
          "display": "Consultation"
        }
      ]
    }
  ],
  "patientId": "p_002",
  "participants": [
    {
      "individual": {
        "reference": "Practitioner/pract_001",
        "display": "Dr. Jane Smith"
      },
      "role": {
        "code": "ATND",
        "display": "Attending Physician"
      }
    }
  ],
  "reasonCode": [
    {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "254837009",
          "display": "Breast lump"
        }
      ]
    }
  ],
  "diagnosis": [
    {
      "reference": "Condition/cond_001",
      "display": "Malignant neoplasm of breast, left"
    }
  ],
  "serviceProvider": {
    "reference": "Organization/org_001",
    "display": "City Hospital"
  },
  "location": [
    {
      "reference": "Location/loc_101",
      "display": "Oncology Clinic - Room 201",
      "period": {
        "start": "2020-03-15T09:00:00Z",
        "end": "2020-03-15T10:30:00Z"
      }
    }
  ],
  "period": {
    "start": "2020-03-15T09:00:00Z",
    "end": "2020-03-15T10:30:00Z"
  },
  "relatedVisits": ["visit_1001"],
  "billing": {}
},
{
  "_id": "enc_002",
  "resourceType": "Encounter",
  "status": "completed",
  "class": {
    "code": "AMB",
    "display": "Outpatient"
  },
  "type": [
    {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "81846006",
          "display": "Chemotherapy Administration"
        }
      ]
    }
  ],
  "patientId": "p_002",
  "participants": [
    {
      "individual": {
        "reference": "Practitioner/pract_002",
        "display": "Dr. Alan Thompson"
      },
      "role": {
        "code": "ATND",
        "display": "Oncologist"
      }
    }
  ],
  "reasonCode": [
    {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "254837009",
          "display": "Breast cancer treatment"
        }
      ]
    }
  ],
  "diagnosis": [
    {
      "reference": "Condition/cond_001",
      "display": "Malignant neoplasm of breast, left"
    }
  ],
  "serviceProvider": {
    "reference": "Organization/org_001",
    "display": "City Hospital"
  },
  "location": [
    {
      "reference": "Location/loc_102",
      "display": "Chemotherapy Unit - Suite B",
      "period": {
        "start": "2021-06-20T10:00:00Z",
        "end": "2021-06-20T12:00:00Z"
      }
    }
  ],
  "period": {
    "start": "2021-06-20T10:00:00Z",
    "end": "2021-06-20T12:00:00Z"
  },
  "relatedVisits": ["visit_1002"],
  "billing": {}
}
]},
{"visits": [
    {
  "_id": "visit_1001",
  "resourceType": "Visit",
  "encounterID": ["enc_001"],
  "patient_id": "p_002",
  "appointmentID": "app_5001",
  "status": "completed",
  "class": {
    "code": "AMB",
    "display": "Outpatient"
  },
  "type": [
    {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "185349003",
          "display": "Follow-up Visit"
        }
      ]
    }
  ],
  "serviceProvider": {
    "reference": "Organization/NCC",
    "display": "National Cancer Center"
  },
  "participant": {
    "individual": {
      "reference": "Practitioner/pract_001",
      "display": "Dr. Jane Smith"
    },
    "role": {
      "coding": [
        {
          "system": "http://terminology.hl7.org/CodeSystem/practitioner-role",
          "code": "attending",
          "display": "Attending Physician"
        }
      ]
    }
  },
  "diagnosis": [
    {
      "condition": {
        "coding": [
          {
            "system": "http://hl7.org/fhir/sid/icd-10",
            "code": "C509",
            "display": "Malignant neoplasm of breast, unspecified"
          }
        ]
      }
    }
  ],
  "location": {
    "reference": "Location/dep_001",
    "display": "Pharmacy",
    "period": {
      "start": "2020-03-15T09:00:00Z",
      "end": "2020-03-15T11:30:00Z"
    }
  },
  "reasonCode": [
    {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "129300006",
          "display": "X-ray of chest"
        }
      ]
    }
  ],
  "outcome": "Follow-up appointment required",
  "observation": [
    {
      "category": "radiology",
      "code": {
        "coding": [
          {
            "system": "http://loinc.org",
            "code": "71045-1",
            "display": "Chest X-ray"
          }
        ]
      },
      "valueString": "No abnormalities detected",
      "effectiveDateTime": "2020-03-15T10:00:00Z"
    }
  ],
  "billing": {
    "lineItems": [
      {
        "sequence": 1,
        "productOrService": {
          "coding": [
            {
              "system": "http://www.ama-assn.org/go/cpt",
              "code": "71045",
              "display": "Chest X-ray, single view"
            }
          ]
        },
        "price": {
          "value": 200.00,
          "currency": "USD"
        }
      }
    ],
    "status": "billed"
  }
},
{
  "_id": "visit_1002",
  "resourceType": "Visit",
  "encounterID": ["enc_002"],
  "patient_id": "p_002",
  "appointmentID": "app_5002",
  "status": "completed",
  "class": {
    "code": "AMB",
    "display": "Outpatient"
  },
  "type": [
    {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "185349003",
          "display": "Follow-up Visit"
        }
      ]
    }
  ],
  "serviceProvider": {
    "reference": "Organization/NCC",
    "display": "National Cancer Center"
  },
  "participant": {
    "individual": {
      "reference": "Practitioner/pract_002",
      "display": "Dr. Alan Thompson"
    },
    "role": {
      "coding": [
        {
          "system": "http://terminology.hl7.org/CodeSystem/practitioner-role",
          "code": "attending",
          "display": "Attending Physician"
        }
      ]
    }
  },
  "diagnosis": [
    {
      "condition": {
        "coding": [
          {
            "system": "http://hl7.org/fhir/sid/icd-10",
            "code": "C509",
            "display": "Malignant neoplasm of breast, unspecified"
          }
        ]
      }
    }
  ],
  "location": {
    "reference": "Location/dep_002",
    "display": "Chemotherapy Unit",
    "period": {
      "start": "2021-06-20T10:00:00Z",
      "end": "2021-06-20T12:30:00Z"
    }
  },
  "reasonCode": [
    {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "129300006",
          "display": "Chemotherapy administration"
        }
      ]
    }
  ],
  "outcome": "Chemotherapy session completed",
  "observation": [
    {
      "category": "chemotherapy",
      "code": {
        "coding": [
          {
            "system": "http://loinc.org",
            "code": "8648-8",
            "display": "Chemotherapy administration"
          }
        ]
      },
      "valueString": "Session completed without complications",
      "effectiveDateTime": "2021-06-20T11:30:00Z"
    }
  ],
  "billing": {
    "lineItems": [
      {
        "sequence": 1,
        "productOrService": {
          "coding": [
            {
              "system": "http://www.ama-assn.org/go/cpt",
              "code": "96413",
              "display": "Chemotherapy administration"
            }
          ]
        },
        "price": {
          "value": 1500.00,
          "currency": "USD"
        }
      }
    ],
    "status": "billed"
  }
}
]},
{"procedures":[
    {
  "resourceType": "Procedure",
  "id": "proc_001",
  "patient_id": "p_002",
  "status": "completed",
  "code": [
    {
      "system": "http://snomed.info/sct",
      "code": "80146002",
      "display": "Lumpectomy"
    }
  ],
  "performedPeriod": {
    "start": "2020-04-10T08:30:00Z",
    "end": "2020-04-10T12:00:00Z"
  },
  "reasonCode": [
    {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "254837009",
          "display": "Breast lump"
        }
      ]
    }
  ],
  "performer": [
    {
      "actor": {
        "reference": "Practitioner/pract_003",
        "display": "Dr. Emily Clark"
      },
      "role": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/practitioner-role",
            "code": "surgeon",
            "display": "Surgeon"
          }
        ]
      }
    }
  ],
  "location": {
    "reference": "Location/loc_103",
    "display": "Surgical Suite 3"
  },
  "outcome": "Successful removal of tumor",
  "note": [
    {
      "text": "Patient tolerated the procedure well. No immediate complications observed."
    }
  ],
  "relatedObservations": [
    {
      "reference": "Observation/obs_002",
      "display": "Surgical pathology report"
    }
  ],
  "surgicalDetails": {
    "procedureType": "Lumpectomy",
    "bodySite": {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "51185008",
          "display": "Left Breast"
        }
      ]
    },
    "result": "Negative margins confirmed",
    "complications": "None"
  },
  "encounterID": ["enc_001"]
},
{
  "resourceType": "Procedure",
  "id": "proc_002",
  "patient_id": "p_002",
  "status": "completed",
  "code": [
    {
      "system": "http://snomed.info/sct",
      "code": "25781008",
      "display": "Bone marrow biopsy"
    }
  ],
  "performedPeriod": {
    "start": "2021-02-15T14:00:00Z",
    "end": "2021-02-15T14:45:00Z"
  },
  "reasonCode": [
    {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "386661006",
          "display": "Anemia"
        }
      ]
    }
  ],
  "performer": [
    {
      "actor": {
        "reference": "Practitioner/pract_004",
        "display": "Dr. Michael Lee"
      },
      "role": {
        "coding": [
          {
            "system": "http://terminology.hl7.org/CodeSystem/practitioner-role",
            "code": "hematologist",
            "display": "Hematologist"
          }
        ]
      }
    }
  ],
  "location": {
    "reference": "Location/loc_104",
    "display": "Hematology Lab"
  },
  "outcome": "Sample obtained successfully",
  "note": [
    {
      "text": "Patient experienced mild discomfort during the procedure."
    }
  ],
  "relatedObservations": [
    {
      "reference": "Observation/obs_003",
      "display": "Bone marrow biopsy results"
    }
  ],
  "hematologyDetails": {
    "procedureType": "Bone marrow biopsy",
    "bodySite": {
      "coding": [
        {
          "system": "http://snomed.info/sct",
          "code": "271442005",
          "display": "Posterior superior iliac spine"
        }
      ]
    },
    "result": "No evidence of metastasis",
    "complications": "Mild discomfort reported"
  },
  "encounterID": ["enc_003"]
}
]},
{"diagnosis":[
    {
  "_id": "diag_001",
  "encounterID": ["enc_001"],
  "patient_id": "p_002",
  "encounter_id": "enc_001",
  "code": [
    {
      "system": "ICD-10",
      "code": "C50.912",
      "display": "Malignant neoplasm of unspecified site of left female breast"
    }
  ],
  "onset_date": "2020-03-10",
  "notes": "Diagnosed with stage II breast cancer following biopsy and imaging studies."
},
{
  "_id": "diag_002",
  "encounterID": ["enc_001", "enc_002"],
  "patient_id": "p_002",
  "encounter_id": "enc_001",
  "code": [
    {
      "system": "ICD-10",
      "code": "I10",
      "display": "Essential (primary) hypertension"
    }
  ],
  "onset_date": "2018-07-20",
  "notes": "Patient has a history of hypertension, controlled with medication."
},
{
  "_id": "diag_003",
  "encounterID": ["enc_002"],
  "patient_id": "p_002",
  "encounter_id": "enc_002",
  "code": [
    {
      "system": "ICD-10",
      "code": "E11.9",
      "display": "Type 2 diabetes mellitus without complications"
    }
  ],
  "onset_date": "2019-11-05",
  "notes": "Diagnosed during routine check-up; HbA1c levels indicate controlled diabetes."
}
]},
{"labs":[
    {
  "patient_id": "p_002",
  "labName": "Complete Blood Count (CBC)",
  "value": "Hemoglobin: 13.5 g/dL, WBC: 6.2 x10^9/L, Platelets: 250 x10^9/L",
  "referenceRange": "Hemoglobin: 12-16 g/dL, WBC: 4-11 x10^9/L, Platelets: 150-450 x10^9/L",
  "sampleCollectionDate": "2021-06-20",
  "code": [
    {
      "name": "loinc",
      "value": "57021-8"
    },
    {
      "name": "snomed",
      "value": "3020004"
    }
  ],
  "reportedDate": "2021-06-20",
  "uom": "g/dL, x10^9/L"
},
{
  "patient_id": "p_002",
  "labName": "CREATININE",
  "value": "0.9 mg/dL",
  "referenceRange": "0.6-1.1 mg/dL",
  "sampleCollectionDate": "2024-08-26",
  "code": [
    {
      "name": "loinc",
      "value": "2160-0"
    },
    {
      "name": "snomed",
      "value": "1481-9"
    }
  ],
  "reportedDate": "2024-08-26",
  "uom": "mg/dL"
},
{
  "patient_id": "p_002",
  "labName": "Hemoglobin A1c",
  "value": "7.2%",
  "referenceRange": "4.0-5.6%",
  "sampleCollectionDate": "2023-09-15",
  "code": [
    {
      "name": "loinc",
      "value": "4548-4"
    },
    {
      "name": "snomed",
      "value": "3094-0"
    }
  ],
  "reportedDate": "2023-09-15",
  "uom": "%"
}
]},
{"medications":[
    {
  "patient_id": "p_002",
  "genericName": "Lisinopril",
  "dosage": "10 mg",
  "frequency": "Once daily",
  "route": "Oral",
  "startDate": "2018-07-25",
  "endDate": "Present",
  "code": [
    {
      "name": "RxNorm",
      "value": "310798"
    },
    {
      "name": "NDC",
      "value": "00093-1030-01"
    }
  ]
},
{
  "patient_id": "p_002",
  "genericName": "Metformin",
  "dosage": "500 mg",
  "frequency": "Twice daily",
  "route": "Oral",
  "startDate": "2019-11-10",
  "endDate": "Present",
  "code": [
    {
      "name": "RxNorm",
      "value": "860975"
    },
    {
      "name": "NDC",
      "value": "00093-0167-01"
    }
  ]
},
{
  "patient_id": "p_002",
  "genericName": "Lactulose",
  "dosage": "20 g",
  "frequency": "BID",
  "route": "Oral",
  "startDate": "2024-08-26",
  "endDate": "2024-09-30",
  "code": [
    {
      "name": "RxNorm",
      "value": "312961"
    },
    {
      "name": "NDC",
      "value": "00093-1031-01"
    }
  ]
}
]},
{"allergies":[
    {
  "_id": "allergy_001",
  "allergenname": "Penicillin",
  "category": "Antibiotic",
  "code": [
    {
      "name": "RxNorm",
      "value": "713880"
    },
    {
      "name": "NDC",
      "value": "00093-1000-01"
    }
  ],
  "reaction": {
    "reactionname": "Rash",
    "severity": "Mild",
    "code": [
      {
        "system": "http://snomed.info/sct",
        "code": "271807003",
        "display": "Rash"
      }
    ]
  },
  "recorded_date": "2019-04-10",
  "notes": "Patient developed a mild rash after taking amoxicillin.",
  "source": "Patient Reported"
},
{
  "_id": "allergy_002",
  "allergenname": "Lactulose",
  "category": "Laxative",
  "code": [
    {
      "name": "RxNorm",
      "value": "312961"
    },
    {
      "name": "NDC",
      "value": "00093-1031-01"
    }
  ],
  "reaction": {
    "reactionname": "None",
    "severity": "None",
    "code": []
  },
  "recorded_date": "2024-08-26",
  "notes": "No known adverse reactions.",
  "source": "Medical Record"
}
]},
{"notes":[
    {
  "_id": "cn_001",
  "document_name": "Initial Consult Note Oncology",
  "entered_date": "2020-03-15T10:45:00Z",
  "institution_code": "NCC",
  "sections": [
    {
      "key": "ECOG",
      "text": "1"
    },
    {
      "key": "Diagnosis",
      "text": "Stage II Malignant neoplasm of left breast"
    },
    {
      "key": "Plan",
      "text": "Schedule lumpectomy and initiate chemo protocol."
    }
  ],
  "generatedtext": "Patient presents with a palpable mass in the L breast. Mammogram and ultrasound confirm a 2.5 cm spiculated lesion. Biopsy results indicate invasive ductal carcinoma, ER+/PR+/HER2-. No distant mets on CT chest/abdomen/pelvis. ECOG performance status 1. Recommended lumpectomy followed by adjuvant chemotherapy. Discussed potential side effects and treatment timeline with patient.",
  "generatedtextLoc": "/documents/p_002/cn_001.txt",
  "created_at": "2020-03-15T10:50:00Z",
  "updated_at": "2020-03-15T11:00:00Z"
},
{
  "_id": "cn_002",
  "document_name": "Surgery Report - Lumpectomy",
  "entered_date": "2020-04-10T12:30:00Z",
  "institution_code": "SurgicalDept",
  "sections": [
    {
      "key": "Procedure",
      "text": "Lumpectomy performed on left breast."
    },
    {
      "key": "Findings",
      "text": "Tumor size 2.5 cm with clear margins."
    },
    {
      "key": "Post-Op Plan",
      "text": "Begin chemotherapy as scheduled."
    }
  ],
  "generatedtext": "The patient underwent a successful lumpectomy of the left breast under GA. Intraoperative findings reveal a 2.5 cm invasive ductal carcinoma with no lymphovascular invasion. Margins are clear, confirmed by frozen section. Sentinel lymph node biopsy performed; results pending. Estimated blood loss 50 mL. Patient tolerated the procedure well. Post-operative instructions provided. Plan to start adjuvant chemo next week.",
  "generatedtextLoc": "/documents/p_002/cn_002.txt",
  "created_at": "2020-04-10T12:45:00Z",
  "updated_at": "2020-04-10T13:00:00Z"
},
{
  "_id": "cn_003",
  "document_name": "Chemotherapy Session Note",
  "entered_date": "2021-06-20T12:15:00Z",
  "institution_code": "OncologyDept",
  "sections": [
    {
      "key": "Session",
      "text": "Second cycle of chemotherapy administered."
    },
    {
      "key": "Response",
      "text": "Patient tolerated the session well with no adverse effects."
    },
    {
      "key": "Next Steps",
      "text": "Continue with the planned chemotherapy regimen."
    }
  ],
  "generatedtext": "Karen Wee received her second cycle of AC (Doxorubicin and Cyclophosphamide) chemo today. Vital signs stable throughout the infusion. No episodes of febrile neutropenia, nausea, or vomiting reported. CBC prior to session: WBC 6.2 x10^9/L, Hgb 13.5 g/dL, Plt 250 x10^9/L. Anti-emetics administered as per protocol. Patient educated on potential delayed side effects and to report any unusual symptoms immediately. Next cycle scheduled in 3 weeks.",
  "generatedtextLoc": "/documents/p_002/cn_003.txt",
  "created_at": "2021-06-20T12:20:00Z",
  "updated_at": "2021-06-20T12:30:00Z"
},
{
  "_id": "cn_004",
  "document_name": "Radiology Report - Chest X-ray",
  "entered_date": "2024-10-15T10:30:00Z",
  "institution_code": "RadiologyDept",
  "sections": [
    {
      "key": "Imaging",
      "text": "Chest X-ray performed."
    },
    {
      "key": "Findings",
      "text": "No acute abnormalities detected."
    },
    {
      "key": "Conclusion",
      "text": "Normal chest X-ray."
    }
  ],
  "generatedtext": "PA and lateral views of the chest were obtained. Lungs are clear bilaterally with no evidence of consolidation, effusion, or pneumothorax. Heart size within normal limits. No mediastinal widening observed. No suspicious nodules or masses identified. No bony abnormalities noted. Impression: Normal CXR. No signs of metastatic disease in the thoracic cavity.",
  "generatedtextLoc": "/documents/p_002/cn_004.txt",
  "created_at": "2024-10-15T10:35:00Z",
  "updated_at": "2024-10-15T10:40:00Z"
},
{
  "_id": "cn_005",
  "document_name": "Endocrinology Follow-up Note",
  "entered_date": "2023-09-16T09:00:00Z",
  "institution_code": "EndocrinologyDept",
  "sections": [
    {
      "key": "Review",
      "text": "Reviewed HbA1c levels and blood glucose control."
    },
    {
      "key": "Assessment",
      "text": "Type 2 Diabetes mellitus is well-controlled with current medication."
    },
    {
      "key": "Plan",
      "text": "Continue Metformin. Schedule next HbA1c test in six months."
    }
  ],
  "generatedtext": "Patient presents for routine follow-up of T2DM. HbA1c today is 7.2%, down from 8.0% six months ago. Fasting BG levels consistently within target range. No hypoglycemic episodes reported. No signs of diabetic retinopathy or nephropathy on recent screening. Advised to maintain current diet and exercise regimen. Continue Metformin 500 mg BID. Next HbA1c scheduled for March 2024. Discussed importance of adherence to medication and lifestyle modifications.",
  "generatedtextLoc": "/documents/p_002/cn_005.txt",
  "created_at": "2023-09-16T09:05:00Z",
  "updated_at": "2023-09-16T09:15:00Z"
}
]}
]

# Sample input data
patients = [patient_001, patient_002]  # Assuming these are lists of dictionaries

DATA_DIR = "data_2"
os.makedirs(DATA_DIR, exist_ok=True)


# Define structured data containers
structured_data = {
    "patients": [],
    "encounters": [],
    "visits": [],
    "procedures": [],
    "diagnosis": [],
    "labs": [],
    "medications": [],
    "allergies": [],
    "notes": [],
}


def extract_structured_data():
    """
    Extracts structured patient data and saves it as CSV files.
    """
    for patient in patients:
        patient_data = patient[0]["patient"]

        # Process patient name (handle different formats)
        if isinstance(patient_data["name"], dict):
            full_name = f"{patient_data['name'].get('given', '')} {patient_data['name'].get('family', '')}".strip()
        else:
            full_name = patient_data["name"]

        # Process contact details
        phone, email = None, None
        if "contact" in patient_data:
            if isinstance(patient_data["contact"], list):
                for contact in patient_data["contact"]:
                    if contact.get("system") == "phone":
                        phone = contact["value"]
                    elif contact.get("system") == "email":
                        email = contact["value"]
            elif isinstance(patient_data["contact"], dict):
                phone = patient_data["contact"].get("phone")
                email = patient_data["contact"].get("email")

        # Extract patient details
        structured_data["patients"].append({
            "patient_id": patient_data["patient_id"],
            "name": full_name,
            "dob": patient_data.get("dob") or patient_data.get("birthDate"),
            "gender": patient_data["gender"],
            "phone": phone,
            "email": email,
            "address": patient_data["address"]
        })

        # Extract remaining sections while ensuring data consistency
        for section in patient[1:]:
            for key, records in section.items():
                if key in structured_data:
                    for record in records:
                        record["patient_id"] = patient_data["patient_id"]
                        # Extract Medications (RxNorm & NDC codes)
                        if "code" in record and isinstance(record["code"], list):
                            record["rxnorm_code"] = next((c["value"] for c in record["code"] if c.get("name") == "RxNorm"), None)
                            record["ndc_code"] = next((c["value"] for c in record["code"] if c.get("name") == "NDC"), None)
                            del record["code"]

                        # Convert note sections into list format if necessary
                        if "sections" in record and isinstance(record["sections"], dict):
                            record["sections"] = [{"key": k, "text": v} for k, v in record["sections"].items()]

                        structured_data[key].append(record)

    # Save structured data as CSV
    for key, data in structured_data.items():
        df = pd.DataFrame(data)
        df.to_csv(f"{DATA_DIR}/{key}.csv", index=False)
        print(f"Saved: {DATA_DIR}/{key}.csv")


if __name__ == "__main__":

  extract_structured_data()
  # extract_notes()