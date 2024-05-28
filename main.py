import streamlit as st
import manual_entry
import resume_parser
import chat_bot

st.title("Recruitment and HR Bot")

st.write("Q Bot: Hi! I'm your Q Bot. Please answer the following questions:")
choice = st.radio('Select an option:', ['Parse_Resume', 'Enter_Manually', 'Chat_Bot'])

if choice == 'Enter_Manually':
    manual_entry.manual_entry()

elif choice == 'Parse_Resume':
    uploaded_file = st.file_uploader("Upload PDF file", type="pdf")
    if uploaded_file is not None:
        resume_parser.parse_resume(uploaded_file)

elif choice == 'Chat_Bot':
    chat_bot.chat_bot()

else:
    st.write('Invalid Input')
