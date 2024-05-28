import streamlit as st
import pandas as pd

def manual_entry():
    st.write("Q Bot: Hi! I'm your Q Bot. Please answer the following questions:")
    questions = ["What is your name?", "Your Email Address?", "Mobile Number?", "What are your Skills"]
    user_data = []

    for i, question in enumerate(questions):
        st.write("Q Bot:", question)
        if i == 3:
            selected_skills = st.multiselect("Select your skills:", ['Python', 'Numpy', 'Pandas', 'Machine Learning', 'Deep Learning'])
            user_data.append(selected_skills)
        else:
            answer = st.text_input(f"Answer {i + 1}:")
            user_data.append(answer)

    if st.button("Submit"):
        st.write("Name:", user_data[0])
        st.write("Email:", user_data[1])
        st.write("Phone:", user_data[2])
        st.write("Skills:", ", ".join(user_data[3]))

        data = pd.read_csv('path_of_file')
        data['job_skills'] = data['job_skills'].str.lower().fillna('').apply(lambda x: ','.join(sorted(skill.strip().replace(' ', '') for skill in x.split(','))))

        check = (user_data[3])

        sorted_check = [','.join(sorted(skill.lower().replace(' ', '') for skill in check))]

        for string in sorted_check:
            indices = data[data['job_skills'] == string].index
            if not indices.empty:
                print(f"Indices for '{string}': {indices}")
            else:
                print(f"'{string}' not found in Column2")
