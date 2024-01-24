import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template
## Streamlit App

st.set_page_config(page_title="ATS Resume EXpert")
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("Upload your resume(PDF)...",type=["pdf"])


if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")


import streamlit as st

# Define the buttons
submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("How Can I Improve My Skills")
submit3 = st.button("Percentage Match")

# Define the prompts
input_prompt1 = """
As an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
Based on missing technical skills, your mission is to provide thoughtful and personalized guidance on skill development, considering their unique journey and goals.
Review the provided information and craft a response that outlines specific recommendations for skill enhancement.
Identify areas for growth and suggest tailored strategies to advance their skills, aligning with their career aspirations.
"""

input_prompt3 = """
As a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. Provide the percentage match if the resume matches
the job description. First, the output should come as a percentage, followed by missing keywords, and lastly, final thoughts.
"""

# Main functionality
if submit1 or submit2 or submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_text(uploaded_file)
        if submit1:
            response = get_gemini_response(input_prompt1)
        elif submit2:
            response = get_gemini_response(input_prompt2)
        elif submit3:
            response = get_gemini_response(input_prompt3)

        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
