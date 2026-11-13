import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Gabriel CBT Pro", page_icon="📝")

st.markdown("""
<style>
    .stApp { background-color: #0A1A33 !important; }
    h1 { color: #FFD700 !important; text-align: center; }
    h3, p, label, span { color: white !important; }
    .stButton>button { background-color: #FF4500 !important; color: white !important; font-size: 18px; font-weight: bold; border-radius: 12px; padding: 12px; width: 100%; border: none; }
    [data-testid="stSidebar"] { background-color: #000B1E !important; }
    [data-testid="stSidebar"] * { color: #FFD700 !important; }
    input, textarea, select { background-color: #1E3A5F !important; color: white !important; border: 2px solid #FFD700 !important; border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)

ALL_SUBJECTS = ["Mathematics","English Language","Physics","Chemistry","Biology","Economics","Government","Literature in English","CRS","Geography","Commerce","Financial Accounting","Agricultural Science","Computer Studies / ICT","Social Studies","Basic Science","Civic Education","History","Business Studies"]

DEFAULT_QUESTIONS = [
    {"q": "What is the full meaning of ICT?", "options": ["Internet and Computer Technology","Information and Communication Technology","Information and Computer Technology","Internet Communication Tool"], "answer": "Information and Communication Technology", "subject": "Computer Studies / ICT"},
    {"q": "Which of these is an input device?", "options": ["Monitor","Printer","Keyboard","Speaker"], "answer": "Keyboard", "subject": "Computer Studies / ICT"},
    {"q": "What does CPU stand for?", "options": ["Central Processing Unit","Computer Personal Unit","Central Program Unit","Computer Processing Utility"], "answer": "Central Processing Unit", "subject": "Computer Studies / ICT"},
    {"q": "Which of these is used to store data permanently?", "options": ["RAM","Hard Disk","Cache","ROM"], "answer": "Hard Disk", "subject": "Computer Studies / ICT"},
    {"q": "Which program is used to browse the internet?", "options": ["Microsoft Word","Google Chrome","Microsoft Excel","Paint"], "answer": "Google Chrome", "subject": "Computer Studies / ICT"},
    {"q": "What is 2 + 2?", "options": ["3","4","5","6"], "answer": "4", "subject": "Mathematics"},
    {"q": "What is the capital of Nigeria?", "options": ["Lagos","Abuja","Kano","Ibadan"], "answer": "Abuja", "subject": "Social Studies"},
]

def show_pie_chart(correct, wrong, title):
    total = correct + wrong
    if total == 0:
        st.write("No data yet")
        return
    pct_correct = int((correct/total)*100)
    pct_wrong = 100 - pct_correct
    st.markdown(f"<h3 style='text-align:center; color:#FFD700;'>{title}</h3>", unsafe_allow_html=True)
    # HTML Pie Chart - No library needed!
    st.markdown(f"""
    <div style="display:flex; justify-content:center;">
        <div style="width:200px; height:200px; border-radius:50%; background: conic-gradient(#00FF7F 0% {pct_correct}%, #FF4500 {pct_correct}% 100%); display:flex; align-items:center; justify-content:center;">
            <div style="width:90px; height:90px; background:#0A1A33; border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-weight:bold; font-size:20px;">{pct_correct}%</div>
        </div>
    </div>
    <p style="text-align:center; margin-top:10px;">🟩 Correct: {correct} ({pct_correct}%) &nbsp;&nbsp; 🟧 Wrong: {wrong} ({pct_wrong}%)</p>
    """, unsafe_allow_html=True)
    # Also Bar Chart - Built-in
    df = pd.DataFrame({"Result": ["Correct","Wrong"], "Count": [correct, wrong]})
    st.bar_chart(df.set_index("Result"))

st.markdown("<h1>📝 Gabriel CBT Pro</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#FF4500 !important;'>Built by ACHONWA GABRIEL</h3>", unsafe_allow_html=True)
school_name = st.text_input("🏫 School Name", placeholder="e.g. Bright Future Secondary School")
if school_name:
    st.markdown(f"<h2 style='text-align:center; color:#00FF7F !important;'>{school_name.upper()}</h2>", unsafe_allow_html=True)
st.markdown("---")

if "questions" not in st.session_state:
    st.session_state.questions = DEFAULT_QUESTIONS.copy()
if "results" not in st.session_state:
    st.session_state.results = []
if "exam_started" not in st.session_state:
    st.session_state.exam_started = False
if "student_info" not in st.session_state:
    st.session_state.student_info = {}
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "last_score" not in st.session_state:
    st.session_state.last_score = None

st.sidebar.title("🔐 Admin Panel")
password = st.sidebar.text_input("Admin Password", type="password")
is_admin = (password == "admin123")
if is_admin:
    st.sidebar.success("✅ Admin Logged In!")
    st.sidebar.subheader("Add New Question")
    new_subject = st.sidebar.selectbox("Subject", ALL_SUBJECTS)
    new_q = st.sidebar.text_area("Question")
    o1 = st.sidebar.text_input("Option 1")
    o2 = st.sidebar.text_input("Option 2")
    o3 = st.sidebar.text_input("Option 3")
    o4 = st.sidebar.text_input("Option 4")
    correct = st.sidebar.selectbox("Correct Answer", ["Option 1","Option 2","Option 3","Option 4"])
    if st.sidebar.button("Add Question"):
        opts = [o1,o2,o3,o4]
        ans = opts[["Option 1","Option 2","Option 3","Option 4"].index(correct)]
        if new_q and all(opts):
            st.session_state.questions.append({"q": new_q, "options": opts, "answer": ans, "subject": new_subject})
            st.sidebar.success("Question Added!")
        else:
            st.sidebar.error("Fill all fields!")
    st.sidebar.subheader("📊 All Results")
    if st.session_state.results:
        df = pd.DataFrame(st.session_state.results)
        st.sidebar.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')
        st.sidebar.download_button("📥 Download Results", csv, "gabriel_cbt_results.csv", "text/csv")
        st.subheader("📊 Overall School Performance")
        total_correct = int(df['score'].sum())
        total_all = int(df['total'].sum())
        show_pie_chart(total_correct, total_all - total_correct, "🥧 Overall Performance")

if not st.session_state.exam_started:
    st.markdown("<h3 style='color:#FFD700;'>👨‍🎓 Student Login</h3>", unsafe_allow_html=True)
    if st.session_state.last_score is not None:
        s, t = st.session_state.last_score
        show_pie_chart(s, t-s, "🥧 Your Last Exam Performance")
    name = st.text_input("Student Name")
    subject = st.selectbox("Select Subject", ALL_SUBJECTS)
    class_ = st.selectbox("Select Class", ["JSS 1","JSS 2","JSS 3","SS 1","SS 2","SS 3"])
    term = st.selectbox("Select Term", ["First Term","Second Term","Third Term"])
    exam_time = st.selectbox("Select Time", ["10 Minutes","20 Minutes","30 Minutes","1 Hour"])
    if st.button("Enter / Start Exam 🚀"):
        if not name:
            st.error("Please enter your name!")
        else:
            mins = int(exam_time.split()[0]) if "Hour" not in exam_time else 60
            st.session_state.student_info = {"name": name, "subject": subject, "class": class_, "term": term, "mins": mins, "school": school_name}
            st.session_state.start_time = datetime.now()
            st.session_state.exam_started = True
            st.rerun()
else:
    info = st.session_state.student_info
    st.info(f"Name: {info['name']} | Class: {info['class']} | Subject: {info['subject']} | Term: {info['term']}")
    end_time = st.session_state.start_time + timedelta(minutes=info['mins'])
    remaining = end_time - datetime.now()
    total_seconds = int(remaining.total_seconds())
    if total_seconds <= 0:
        st.error("⏰ TIME UP!")
        st.session_state.exam_started = False
        st.rerun()
    else:
        mins_left = total_seconds // 60
        secs_left = total_seconds % 60
        st.warning(f"⏰ Time Remaining: {mins_left:02d}:{secs_left:02d}")
    st.markdown(f"<h3 style='color:#00FF7F;'>{info['subject']} - {info['term']} Exam</h3>", unsafe_allow_html=True)
    filtered = [q for q in st.session_state.questions if q.get("subject") == info["subject"]]
    if not filtered:
        filtered = st.session_state.questions
    st.write(f"Total Questions: {len(filtered)}")
    answers = {}
    for i, q in enumerate(filtered):
        answers[i] = st.radio(f"Q{i+1}. {q['q']}", q["options"], key=f"q{i}")
    if st.button("Submit Exam ✅"):
        score = sum(1 for i, q in enumerate(filtered) if answers[i] == q["answer"])
        wrong = len(filtered) - score
        st.success(f"🎉 {info['name']}, your score is {score}/{len(filtered)}")
        st.balloons()
        st.session_state.last_score = (score, len(filtered))
        st.session_state.results.append({"name": info["name"], "class": info["class"], "subject": info["subject"], "term": info["term"], "score": score, "total": len(filtered), "school": info.get("school","")})
        show_pie_chart(score, wrong, "🥧 Your Exam Performance")
    if st.button("Take Another Exam"):
        st.session_state.exam_started = False
        st.rerun()

st.markdown("---")
st.markdown("<center><h3 style='color:#FF4500;'>Built by ACHONWA GABRIEL ❤️</h3></center>", unsafe_allow_html=True)
