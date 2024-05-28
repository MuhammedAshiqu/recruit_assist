# import streamlit as st
# import google.generativeai as genai

# API_KEY = 'AIzaSyBZ2rlDmsKIxHKlHm5TfChaUrflOSkns7I'

# genai.configure(
#     api_key=API_KEY
# )

# model = genai.GenerativeModel('gemini-pro')
# chat = model.start_chat(history=[])

# # Initialize session state messages if not already done
# if 'messages' not in st.session_state:
#     st.session_state.messages = []

# if prompt := st.chat_input("Type Here?"):
#     # Display user message in chat message container
#     st.chat_message("user").markdown(prompt)
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     out = chat.send_message(prompt)
    
#     # Extract response content
#     response_content = out.candidates[0].content.parts[0].text
    
#     response = f"Bot: {response_content}"
#     # Display assistant response in chat message container
#     with st.chat_message("assistant"):
#         st.markdown(response)
#     # Add assistant response to chat history
#     st.session_state.messages.append({"role": "assistant", "content": response})







import streamlit as st
from PyPDF2 import PdfReader
import google.generativeai as genai

# Configure the Generative AI API
API_KEY = 'AIzaSyBZ2rlDmsKIxHKlHm5TfChaUrflOSkns7I'
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def chat_bot():
    # Initialize session state for messages if not already done
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    # Initialize session state for resume text if not already done
    if 'resume_text' not in st.session_state:
        st.session_state.resume_text = ""

    user_input = st.text_input("You:")

    if user_input:
        # Display the user's message in the chat
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        if "resume" in user_input.lower():
            # Handle resume upload
            uploaded_file = st.file_uploader("Upload your resume", type="pdf")

            if uploaded_file is not None:
                try:
                    pdf_reader = PdfReader(uploaded_file)
                    pdf_text = ""
                    for page in pdf_reader.pages:
                        pdf_text += page.extract_text()

                    # Store the PDF content in session state
                    if pdf_text:
                        st.session_state.resume_text = pdf_text
                        with st.expander("View Resume"):
                            st.write(pdf_text)
                        st.chat_message("assistant").markdown("Resume uploaded successfully.")
                    else:
                        st.chat_message("assistant").markdown("No text could be extracted from the PDF. Please try another file.")
                except Exception as e:
                    st.chat_message("assistant").markdown(f"An error occurred while reading the PDF: {e}")

        # If resume has been uploaded, allow user to enter job description
        if st.session_state.resume_text:
            what_to_do = st.text_input('What do you want to do?')

            if what_to_do:
                job_description = st.text_input("Enter job description")

                if job_description:
                    # Combine resume text and job description
                    combined_text = st.session_state.resume_text + "\n\n" + what_to_do + '\n\n' + job_description

                    # Send combined text to the generative model
                    try:
                        out = chat.send_message(combined_text)

                        # Extract response content
                        response_content = out.candidates[0].content.parts[0].text if out.candidates else "No response from the model."

                        # Display assistant response
                        response = f"Bot: {response_content}"
                        st.chat_message("assistant").markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})
                    except Exception as e:
                        st.chat_message("assistant").markdown(f"An error occurred while generating the response: {e}")
        else:
            # Process general chat input
            try:
                out = chat.send_message(user_input)
                response_content = out.candidates[0].content.parts[0].text if out.candidates else "No response from the model."
                response = f"Bot: {response_content}"
                st.chat_message("assistant").markdown(response)
            except Exception as e:
                st.chat_message("assistant").markdown(f"An error occurred while generating the response: {e}")

# Run the chat bot function
if __name__ == "__main__":
    chat_bot()
