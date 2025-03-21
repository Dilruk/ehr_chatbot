import streamlit as st
import streamlit.components.v1 as components
from query_agent import extract_patient_data
from llm_response_parser import generate_user_friendly_response

theme_color = "#f8f9fa" if st.get_option("theme.base") == "light" else "#222"
# Custom CSS to increase text input size
st.markdown(
    """
    <style>
    .stTextInput > div > div > input {
        font-size: 18px !important;
        padding: 12px !important;
        height: 45px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("EHR Chatbot")
user_query = st.text_input("Ask a question about a patient:")

if user_query:
    # result = extract_patient_data(user_query)
    # st.write("Response:")
    # if isinstance(result, list) and result and "error" in result[0]:
    #     st.warning(result[0]["error"])
    # elif isinstance(result, dict) and "error" in result:
    #     st.warning(result["error"])
    # else:
    #     st.json(result)


    patient_data_response = extract_patient_data(user_query)
    if patient_data_response.get("status") == "error":
        final_output = "<div><h1>Record not found, Please check your query and try again!</h1></div>"
    else:
        final_output = generate_user_friendly_response(user_query=user_query, extracted_patient_data=patient_data_response["message"])

    # st.markdown(final_output, unsafe_allow_html=True)
    # components.html(final_output, height=800, scrolling=True)

    html_wrapper = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <style>
        body {{
          font-family: Arial, sans-serif;
          background-color: transparent;
          color: {theme_color}; /* Adjusts dynamically */
          padding: 20px;
        }}
      </style>
    </head>
    <body>
      {final_output}
    </body>
    </html>
    """

    components.html(html_wrapper, height=800, scrolling=True)