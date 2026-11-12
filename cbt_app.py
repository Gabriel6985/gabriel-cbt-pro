import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="Gabriel CBT Pro", page_icon="📝")

# --- COLOURS / DESIGN ---
st.markdown("""
<style>
    .main { background-color: #f0f8ff; }
    h1 { color: #1E90FF !important; text-align: center; }
    .stButton>button {
        background-color: #1E90FF;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
        width: 100%;
    }
    .stButton>button:hover { background-color: #FF4500; color: white; }
    [data-testid="stSidebar"] { background-color: #001F3F !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stSelectbox, .stTextInput { background-color: white; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

ALL_SUBJECTS = [
    "Mathematics", "English Language", "Physics", "Chemistry", "Biology",
    "Further Mathematics", "Economics", "Government", "Literature in English",
    "CRS", "IRS", "Geography", "Commerce", "Financial Accounting",
    "Agricultural Science", "Computer Studies / ICT", "Social Studies",
    "Basic Science", "Basic Technology", "Civic Education", "History",
    "Home Economics", "Business Studies", "French", "Yoruba", "Igbo",
    "Hausa", "Fine Arts", "Music", "Physical & Health Education",
]

# --- HEADER WITH COLOUR ---
st.markdown("<h1 style='color:#1E90FF;'>📝 Gabriel CBT Pro</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#FF4500;'>Built by ACHONWA GABRIEL</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:green; font-weight:bold;'>Welcome to Your Online Exam Portal 🎓</p>", unsafe_allow_html=True)
st.markdown("---")

if "questions" not in st.session_state:
    st.session_state.questions = [
        {"q": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": "4", "subject": "Mathematics"},
        {"q": "What is the capital of Nigeria?", "options": ["Lagos", "Abuja", "Kano", "Ibadan"], "answer": "Abuja", "subject": "Social Studies"},
        {"q": "What is 5 x 3?", "options": ["10", "15", "20", "25"], "answer": "15", "subject": "Mathematics"},
    ]
if "results" not in st.session_state:
    st.session_state.results = []
if "exam_started" not in st.session_state:
    st.session_state.exam_started = False
if "student_info" not in st.session_state:
    st.session_state.student_info = {}
if "start_time" not in st.session_state:
    st.session_state.start_time = None

# --- ADMIN PANEL ---
st.sidebar.title("🔐 Admin Panel")
password = st.sidebar.text_input("Admin Password", type="password")
is_admin = (password == "admin123")
if password and is_admin:
    st.sidebar.success("✅ Admin Logged In!")

if is_admin:
    st.sidebar.subheader("Add New Question")
    new_subject = st.sidebar.selectbox("Subject", ALL_SUBJECTS)
    new_q = st.sidebar.text_area("Question")
    o1 = st.sidebar.text_input("Option 1")
    o2 = st.sidebar.text_input("Option 2")
    o3 = st.sidebar.text_input("Option 3")
    o4 = st.sidebar.text_input("Option 4")
    correct = st.sidebar.selectbox("Correct Answer", ["Option 1", "Option 2", "Option 3", "Option 4"])
    if st.sidebar.button("Add Question"):
        opts = [o1, o2, o3, o4]
        ans = opts[["Option 1", "Option 2", "Option 3", "Option 4"].index(correct)]
        if new_q and all(opts):
            st.session_state.questions.append({"q": new_q, "options": opts, "answer": ans, "subject": new_subject})
            st.sidebar.success("Question Added!")
        else:
            st.sidebar.error("Fill all fields!")

    st.sidebar.subheader("All Results")
    if st.session_state.results:
        for r in st.session_state.results:
            st.sidebar.write(f"{r['name']} | {r['class']} | {r['subject']} | {r['term']} : {r['score']}/{r['total']}")
    else:
        st.sidebar.write("No results yet")

# --- STUDENT LOGIN ---
if not st.session_state.exam_started:
    st.markdown("<h3 style='color:purple;'>👨‍🎓 Student Login</h3>", unsafe_allow_html=True)
    name = st.text_input("Student Name")
    subject = st.selectbox("Select Subject", ALL_SUBJECTS)
    class_ = st.selectbox("Select Class", ["JSS 1", "JSS 2", "JSS 3", "SS 1", "SS 2", "SS 3"])
    term = st.selectbox("Select Term", ["First Term", "Second Term", "Third Term"])
    exam_time = st.selectbox("Select Time", ["10 Minutes", "20 Minutes", "30 Minutes", "1 Hour"])

    if st.button("Enter / Start Exam 🚀"):
        if not name:
            st.error("Please enter your name!")
        else:
            mins = int(exam_time.split()[0]) if "Hour" not in exam_time else 60
            st.session_state.student_info = {"name": name, "subject": subject, "class": class_, "term": term, "mins": mins}
            st.session_state.start_time = datetime.now()
            st.session_state.exam_started = True
            st.rerun()

# --- EXAM WITH TIMER ---
else:
    info = st.session_state.student_info
    st.info(f"Name: {info['name']} | Class: {info['class']} | Subject: {info['subject']} | Term: {info['term']}")

    end_time = st.session_state.start_time + timedelta(minutes=info['mins'])
    remaining = end_time - datetime.now()
    total_seconds = int(remaining.total_seconds())

    if total_seconds <= 0:
        st.error("⏰ TIME UP! Exam auto-submitted.")
        st.session_state.exam_started = False
        st.rerun()
    else:
        mins_left = total_seconds // 60
        secs_left = total_seconds % 60
        st.warning(f"⏰ Time Remaining: {mins_left:02d}:{secs_left:02d} / {info['mins']} mins")
        if mins_left <= 5:
            st.error("⚠️ Less than 5 minutes left!")

    st.markdown(f"<h3 style='color:green;'>{info['subject']} - {info['term']} Exam</h3>", unsafe_allow_html=True)
    filtered = [q for q in st.session_state.questions if q.get("subject") == info["subject"]]
    if not filtered:
        filtered = st.session_state.questions
        st.warning(f"No questions for {info['subject']} yet, showing all questions")
    st.write(f"Total Questions: {len(filtered)}")

    answers = {}
    for i, q in enumerate(filtered):
        answers[i] = st.radio(f"Q{i+1}. {q['q']}", q["options"], key=f"q{i}")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Submit Exam ✅"):
            score = sum(1 for i, q in enumerate(filtered) if answers[i] == q["answer"])
            st.success(f"🎉 {info['name']}, your score is {score}/{len(filtered)}")
            st.session_state.results.append({"name": info["name"], "class": info["class"], "subject": info["subject"], "term": info["term"], "score": score, "total": len(filtered)})
    with col2:
        if st.button("Refresh Timer 🔄"):
            st.rerun()

    if st.button("Take Another Exam"):
        st.session_state.exam_started = False
        st.rerun()

st.markdown("---")
st.markdown("<center><h3 style='color:#FF4500;'>Built by ACHONWA GABRIEL ❤️</h3></center>", unsafe_allow_html=True)
st.markdown("<center><p style='color:blue;'>© 2026 Gabriel CBT Pro - All Rights Reserved</p></center>", unsafe_allow_html=True)
