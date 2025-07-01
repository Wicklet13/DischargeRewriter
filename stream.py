from main import generate_response
import streamlit as st
import time

st.set_page_config(layout="wide")

st.title("LLM Chatbot")

st.write("")

explain_terms = st.checkbox("Explain medical terms", value=True)
reading_level = st.selectbox("Comprehension Level:", ["5th grade", "6th grade", "8th grade", "Young Adult"])

st.write("")


question_prompt = st.text_area("Enter Discharge Notes:", height=300)

if st.button("Submit"):
    res = generate_response(question_prompt, explain_terms, reading_level)
    
    # st.write(res)

    output = st.empty()

    current_text = ""
    for char in res:
        current_text += char
        output.markdown(current_text + "▌")  # ▌ cursor effect
        time.sleep(0.01)

    st.write(res)