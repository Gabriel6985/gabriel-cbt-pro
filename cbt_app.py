import streamlit as st

st.set_page_config(page_title="Gabriel CBT Pro", layout="centered")
st.title("📚 Gabriel CBT Pro")

# --- DEFAULT QUESTIONS ---
if "questions" not in st.session_state:
    st.session_state.questions = [
        {"q": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4"},
        {"q": "What is the capital of Nigeria?", "options": ["Lagos", "Abuja", "Kano", "Ibadan"], "answer": "Abuja"},
        {"q": "What is 5 x 3?", "options": ["10", "15", "20", "8"], "answer": "15"},
    ]
if "results" not in st.session_state:
    st.session_state.results = []
if "started" not in st.session_state:
    st.session_state.started = False
if "answers" not in st.session_state:
    st.session_state.answers = {}

# --- SIDEBAR: ADMIN ---
st.sidebar.title("🔐 Admin Panel")
admin_pass = st.sidebar.text_input("Admin Password", type="password")
is_admin = (admin_pass == "admin123")

if is_admin:
    st.sidebar.success("Admin Logged In!")
    st.sidebar.subheader("Add New Question")
    new_q = st.sidebar.text_input("Question")
    opt1 = st.sidebar.text_input("Option 1")
    opt2 = st.sidebar.text_input("Option 2")
    opt3 = st.sidebar.text_input("Option 3")
    opt4 = st.sidebar.text_input("Option 4")
    correct = st.sidebar.selectbox("Correct Answer", ["Option 1", "Option 2", "Option 3", "Option 4"])
    if st.sidebar.button("Add Question"):
        opts = [opt1, opt2, opt3, opt4]
        ans_map = {"Option 1": opt1, "Option 2": opt2, "Option 3": opt3, "Option 4": opt4}
        if new_q and all(opts):
            st.session_state.questions.append({"q": new_q, "options": opts, "answer": ans_map[correct]})
            st.sidebar.success("Question Added!")
            st.rerun()
        else:
            st.sidebar.warning("Fill all fields")

    st.sidebar.subheader("All Results")
    if st.session_state.results:
        for r in st.session_state.results:
            st.sidebar.write(f"{r['name']}: {r['score']}/{r['total']}")
    else:
        st.sidebar.write("No results yet")

    if st.sidebar.button("Clear All Questions"):
        st.session_state.questions = []
        st.rerun()
    if st.sidebar.button("Reset Results"):
        st.session_state.results = []
        st.rerun()

# --- STUDENT EXAM ---
questions = st.session_state.questions

if not st.session_state.started:
    st.write(f"Welcome! Total Questions: {len(questions)}")
    name = st.text_input("Enter your name")
    if st.button("Start Exam", type="primary"):
        if name.strip() == "":
            st.warning("Please enter your name first")
        else:
            st.session_state.started = True
            st.session_state.name = name
            st.session_state.answers = {}
            st.rerun()
else:
    st.write(f"Student: **{st.session_state.get('name','')}**")
    for i, qq in enumerate(questions):
        st.subheader(f"Q{i+1}. {qq['q']}")
        st.session_state.answers[i] = st.radio("Choose one:", qq["options"], key=f"q{i}", index=None)
    if st.button("Submit Exam", type="primary"):
        score = 0
        for i, qq in enumerate(questions):
            if st.session_state.answers.get(i) == qq["answer"]:
                score += 1
        st.session_state.results.append({"name": st.session_state.name, "score": score, "total": len(questions)})
        st.success(f"Exam Finished! {st.session_state.name}, Score: {score}/{len(questions)}")
        if st.button("Take Exam Again"):
            st.session_state.started = False
            st.rerun()
