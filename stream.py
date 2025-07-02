from main import generate_response
import streamlit as st
import time

st.set_page_config(layout="wide")

st.title("")

st.write("")

reading_level = st.selectbox("Comprehension Level:", ["5th grader", "6th grader", "8th grader", "Young Adult", "Doctor"])
word_count = st.number_input("Word Count:", value=500)
explain_terms = st.checkbox("Explain medical terms", value=True)

st.write("")

question_prompt = st.text_area("Enter Discharge Notes:", height=300)

if st.button("Submit"):
    res = generate_response(question_prompt, explain_terms, word_count, reading_level)
    
    output = st.empty()

    current_text = ""
    for char in res:
        current_text += char
        output.markdown(current_text + "▌")  # ▌ cursor effect
        time.sleep(0.01)