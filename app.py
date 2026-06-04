import streamlit as st
import random

st.title("AI Interview Coach")

# User name
name = st.text_input("Enter your name")

if name:
    st.sidebar.success(f"Logged in as: {name}")

question_bank = {
    "Python": [
        "What is a list in Python?",
        "What is the difference between a list and a tuple?",
        "What is a dictionary?"
    ],

    "HR": [
        "Tell me about yourself.",
        "What are your strengths?",
        "Why should we hire you?"
    ],

    "SSB": [
        "Why do you want to join the Armed Forces?",
        "Tell me about a leadership experience.",
        "How do you handle pressure?"
    ]
}

category = st.selectbox(
    "Select Interview Type",
    list(question_bank.keys())
) 

if st.button("Generate Interview Question"):
   question = random.choice(question_bank[category])
   st.session_state["question"] = question

if "question" in st.session_state:
    st.write("### Interview Question")
    st.write(st.session_state["question"])

    answer = st.text_area("Your Answer")

    if st.button("Submit Answer"):
        st.success("Answer Submitted!")
        st.write("Your answer:")
        st.write(answer)