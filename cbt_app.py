import streamlit as st
import time

st.set_page_config(page_title="Gabriel CBT Pro", layout="centered")
st.title("Gabriel CBT Pro")

if "started" not in st.session_state:
    st.session_state.started = False
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "start_time" not in st.session_state:
    st.session_state.start_time = None

questions = [
    {"q": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
    {"q": "What is the capital of Nigeria?", "options": ["Lagos", "Abuja", "Kano", "Ibadan"], "answer": "Abuja"},
    {"q": "What is 5 x 3?", "options": ["10", "15", "20", "8"], "answer": "15"},
]

if not st.session_state.started:
    st.write("Welcome! Click Start to begin your exam.")
    name = st.text_input("Enter your name")
    if st.button("Start Exam"):
        if name.strip() == "":
            st.warning("Please enter your name first")
        else:
            st.session_state.started = True
            st.session_state.start_time = time.time()
            st.session_state.name = name
            st.rerun()
else:
    st.write(f"Student: {st.session_state.get('name','')}")
    for i, qq in enumerate(questions):
        st.subheader(f"Q{i+1}. {qq['q']}")
        st.session_state.answers[i] = st.radio(
            "Choose one:", qq["options"],
            key=f"q{i}",
            index=None
        )
    if st.button("Submit Exam"):
        score = 0
        for i, qq in enumerate(questions):
            if st.session_state.answers.get(i) == qq["answer"]:
                score += 1
        st.success(f"Exam Finished! Score: {score}/{len(questions)}")
        if st.button("Restart"):
            st.session_state.started = False
            st.session_state.answers = {}
            st.rerun()
