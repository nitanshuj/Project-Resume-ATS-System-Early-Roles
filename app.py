from dotenv import load_dotenv
load_dotenv()

import base64
import streamlit as st
import os
import io

from PIL import Image

import pdf2image

import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response=model.generate_content([input, pdf_content[0], prompt])
    return response.text


def input_pdf_setup(uploaded_file):

    if uploaded_file is not None:
        
        # Convert the PDF to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())#, poppler_path = r"C:\Tools\poppler-23.11.0\Library\bin")
        
        first_page = images[0]

        # Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No PDF file uploaded")



# Streamlit App
# Prompt Template

st.set_page_config(page_title="ATS Resume Expert") #, page_icon="🔮", layout="wide")
st.header("ATS Resume Expert")

input_text = st.text_area("Job Description", key="input")
uploaded_file = st.file_uploader("Upload a Resume in PDF Format", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully!!")
    # pdf_content = input_pdf_setup(uploaded_file)


# submit1 = st.button("Resume Highlights")
# sumbit2 = st.button("How can I Improve my Skillet?")
submit3 = st.button("Percentage Match")

# input_prompt1 = """
#         You are experienced HR with tech experience in the field of Data Science, 
#         Data Analysis, Machine Learning Engineering, Full Stack Web Development, and Big Data Engineering. 
#         Your task is to review the resume and provide the highlights of the resume, 
#         based on the job description for these profiles.
#         You will analyze the resume of a candidate with around 1 year of work experience in a technical role.
#         Please share your professional evaluation of the resume on whether the candidate's profile aligns with the job description provided.
#         Highlight the weakness and strengths of the applicant in relation to the specified job role.
#         """


input_prompt3 = """
        You are a skilled Application Tracking System scanner with a deep understanding of the Data Science, Data Analysis, Machine Learning Engineering. 
        You will analyze the resume of a candidate with around 1 year of work experience in a technical role. You also have deep Application Tracking System (ATS) functionality.
        Your task is to review the resume and provide the percentage match of the resume to the job description for these profiles.
        You will have to give the missing keywords that are NOT present in the resume.
        You will also give the keywords that are not important, but are present in the resume.
        First the output should come as a percentage match, followed by the missing keywords and then finally the not important keywords.
        There should be 3 distinct paragraphs for each of the above.
        """

# if submit1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt1, pdf_content, input_text)
#         st.subheader("The response is:")
#         st.write(response)
#     else:
#         st.error("No PDF uploaded! Please upload a PDF file to continue.")

if submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The response is:")
        st.write(response)
    else:
        st.error("No PDF uploaded! Please upload a PDF file to continue.")

        