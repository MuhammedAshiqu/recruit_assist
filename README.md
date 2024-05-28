# Recruitment and HR Bot

This repository contains a Streamlit-based application for recruitment and HR tasks, including a chatbot, manual data entry, and resume parsing functionalities.

## Files

### chat_bot.py

This file contains the code for a chatbot powered by Generative AI. It allows users to interact with the bot, upload their resume, and receive responses based on their queries and uploaded resume content.

### manual_entry.py

This file provides a manual data entry interface where users can input their personal information such as name, email address, phone number, and skills.

### resume_parser.py

In this file, a resume parsing functionality is implemented. It extracts information such as name, email, phone number, and skills from uploaded resumes.

### main.py

This file serves as the main interface for the application. Users can choose between parsing a resume, manual data entry, or interacting with the chatbot.

## Usage

To run the application, ensure you have Streamlit installed (`pip install streamlit`) and then execute `streamlit run main.py` in your terminal.

Upon running the application, you will be presented with options to choose from:

- **Parse Resume**: Upload a resume to extract relevant information.
- **Enter Manually**: Manually input personal information and skills.
- **Chat Bot**: Interact with the chatbot powered by Generative AI.

Choose the desired option, follow the instructions, and interact with the application accordingly.

## Dependencies

- Streamlit
- PyPDF2
- Google Generative AI
- Pandas
- Spacy
- Fitz (PyMuPDF)

## Notes

- Ensure that you have the necessary API keys and credentials set up, especially for Google Generative AI, as specified in the code.
- Make sure to have the required CSV file (`job_skills.csv`) for skills matching functionality in the resume parsing section.

Feel free to explore, modify, and extend the functionality of the application according to your needs. If you encounter any issues or have suggestions for improvements, please don't hesitate to open an issue or submit a pull request. Happy recruiting!

##Output

