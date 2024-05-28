# import re
# import fitz  # PyMuPDF
# import streamlit as st
# import pandas as pd

# def extract_text_from_pdf(pdf_file):
#     text = ""
#     with fitz.open(pdf_file) as doc:
#         for page_num in range(len(doc)):
#             page = doc.load_page(page_num)
#             text += page.get_text()
#     return text

# def extract_name(text):
#     name = re.findall(r"([A-Z][a-z]+(?: [A-Z][a-z]+)?)", text)
#     return name[0] if name else None

# def extract_email(text):
#     email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
#     return email[0] if email else None

# def extract_phone_number(text):
#     phone = re.findall(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]", text)
#     return phone[0] if phone else None

# def extract_skills(text):
#     skills = re.findall(r"(?i)\b(?:skills|expertise)\b[\s\S]*?(?=\b(?:education|qualification|experience)\b)", text)
#     if skills:
#         return ", ".join([s.strip() for s in skills[0].split(":")[-1].split(",")])
#     else:
#         return None

# def parse_resume(uploaded_file):
#     resume_text = extract_text_from_pdf(uploaded_file)

#     resume_sections = {
#         "name": extract_name(resume_text),
#         "email": extract_email(resume_text),
#         "phone": extract_phone_number(resume_text),
#         "skills": extract_skills(resume_text),
#     }

#     st.write("Name:", resume_sections["name"])
#     st.write("Email:", resume_sections["email"])
#     st.write("Phone:", resume_sections["phone"])
#     st.write("Skills:", resume_sections["skills"])

#     data = pd.read_csv('job_skills.csv')
#     data['job_skills'] = data['job_skills'].str.lower().fillna('').apply(lambda x: ','.join(sorted(skill.strip().replace(' ', '') for skill in x.split(','))))

#     check = ['communicationskills']
#     # if isinstance(check, str):
#     #     check = [skill.strip() for skill in check.split(',')]

#     # sorted_check = [','.join(sorted(skill.lower().replace(' ', '') for skill in check))]


#     for string in check:
#         indices = data[data['job_skills'] == string].index
#         if not indices.empty:
#             for i in indices:
#                 st.write(data['job_link'][i])
#         else:
#             st.write(f"'{string}' not found in Column2")

# # Streamlit UI
# # #uploaded_file = st.file_uploader("Upload Resume", type=['pdf'])

# # if uploaded_file is not None:
# #     parse_resume(uploaded_file)

import re
import fitz  # PyMuPDF
import streamlit as st
import pandas as pd
import spacy

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(pdf_file) as doc:
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
    return text

def extract_name(text):
    # Split text into lines and consider only the first few lines
    lines = text.split('\n')[:10]
    name_candidates = []

    for line in lines:
        # Strip whitespace and check if the line could be a name
        stripped_line = line.strip()
        if re.match(r"^[A-Z][a-z]+(?: [A-Z][a-z]+)+$", stripped_line):
            name_candidates.append(stripped_line)
        # Additionally, look for names in uppercase (some resumes use uppercase for names)
        elif re.match(r"^[A-Z]+(?: [A-Z]+)+$", stripped_line):
            name_candidates.append(stripped_line.title())

    if name_candidates:
        # Assume the first valid candidate is the name
        return name_candidates[0]
    return None

def extract_email(text):
    doc = nlp(text)
    for token in doc:
        if token.like_email:
            return token.text
    return None

def extract_phone_number(text):
    phone_pattern = re.compile(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]")
    match = phone_pattern.search(text)
    return match.group(0) if match else None

def extract_skills(text):
    doc = nlp(text)
    skills_section = None
    for sent in doc.sents:
        if 'skills' in sent.text.lower():
            skills_section = sent
            break

    if skills_section:
        skills = []
        for token in skills_section:
            if token.is_alpha and not token.is_stop:
                skills.append(token.text)
        return ", ".join(skills)
    return None

def extract_experience(text):
    experience_keywords = ['experience', 'work experience', 'professional experience', 'employment history']
    experience_section = None

    lines = text.split('\n')
    for i, line in enumerate(lines):
        for keyword in experience_keywords:
            if keyword in line.lower():
                experience_section = lines[i:]
                break
        if experience_section:
            break

    if experience_section:
        experience_text = '\n'.join(experience_section)
        return experience_text
    return None


def parse_resume(uploaded_file):
    resume_text = extract_text_from_pdf(uploaded_file)

    resume_sections = {
        "name": extract_name(resume_text),
        "email": extract_email(resume_text),
        "phone": extract_phone_number(resume_text),
        "skills": extract_skills(resume_text),
    }

    st.write("Name:", resume_sections["name"])
    st.write("Email:", resume_sections["email"])
    st.write("Phone:", resume_sections["phone"])
    st.write("Skills:", resume_sections["skills"])

    data = pd.read_csv('path_of_file')
    data['job_skills'] = data['job_skills'].str.lower().fillna('').apply(lambda x: ','.join(sorted(skill.strip().replace(' ', '') for skill in x.split(','))))

    check = ['communicationskills']

    for string in check:
        indices = data[data['job_skills'] == string].index
        if not indices.empty:
            for i in indices:
                st.write(data['job_link'][i])
        else:
            st.write(f"'{string}' not found in job_skills")

