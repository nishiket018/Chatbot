# utils/query_handler.py
import streamlit as st
from utils.cv_handler import extract_text_from_pdf, generate_career_insights
from utils.wikipedia_api import get_wikipedia_summary
from utils.web_search import search_web, identify_query_type, format_results

def chatbot_response(query, query_type):
    if query_type == "CV":
        st.subheader("Upload Your Resume")
        uploaded_file = st.file_uploader("Upload your resume in PDF format", type="pdf")
        
        if uploaded_file:
            # Extract text from the uploaded resume
            resume_text = extract_text_from_pdf(uploaded_file)
            
            # Display extracted text (optional, for debugging)
            st.write("Extracted Resume Text:")
            st.write(resume_text)
            
            # Generate and display career insights
            career_insights = generate_career_insights(resume_text)
            st.subheader("Personalized Career Insights")
            st.write(career_insights)
    elif query_type == "Wiki":
        return get_wikipedia_summary(query)
    elif query_type == "Web":
        query_type = identify_query_type(query)
        results = search_web(query)
        return format_results(results, query_type, query)
    else:
        return "Please select a valid tab."
