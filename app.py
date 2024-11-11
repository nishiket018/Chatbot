import streamlit as st
from utils.query_handler import chatbot_response

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Sidebar navigation
st.sidebar.title("Navigation")
option = st.sidebar.radio("Select Query Type", ("CV", "Wiki", "Web"))

# Main chat interface
st.title("Chatbot")

# Display chat history
for entry in st.session_state.chat_history:
    if entry["sender"] == "user":
        st.markdown(f"<div style='text-align: right; background-color: #DCF8C6; padding: 8px; margin: 4px; border-radius: 8px;'>"
                    f"{entry['message']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='text-align: left; background-color: #E2E2E2; padding: 8px; margin: 4px; border-radius: 8px;'>"
                    f"{entry['message']}</div>", unsafe_allow_html=True)

# Handle different types of queries based on radio selection
if option == "CV":
    st.subheader("Upload Your Resume")
    uploaded_file = st.file_uploader("Upload your resume in PDF format", type="pdf")
    
    if uploaded_file:
        # Extract text from the uploaded resume
        from utils.cv_handler import extract_text_from_pdf, generate_career_insights
        resume_text = extract_text_from_pdf(uploaded_file)
        
        # Display extracted text (optional, for debugging)
        st.write("Extracted Resume Text:")
        st.write(resume_text)
        
        # Generate and display career insights
        career_insights = generate_career_insights(resume_text)
        st.subheader("Personalized Career Insights")
        st.write(career_insights)

# User input for chat (common for all options)
user_query = st.text_input("Type your message here...", value="")

# Send button functionality
if st.button("Send"):
    if user_query:
        # Check if the last user message is different from the current one
        if not st.session_state.chat_history or st.session_state.chat_history[-1]["message"] != user_query:
            # Append user message to chat history
            st.session_state.chat_history.append({"sender": "user", "message": user_query})
            
            # Get bot response based on query type
            from utils.query_handler import chatbot_response
            bot_response = chatbot_response(user_query, option)
            
            # Append bot response to chat history
            st.session_state.chat_history.append({"sender": "bot", "message": bot_response})
        
        # st.experimental_rerun()  # Rerun to update chat history and UI

