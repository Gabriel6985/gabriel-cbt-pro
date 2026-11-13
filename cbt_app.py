import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Gabriel CBT Pro - CBT Examination Portal", page_icon="🎓", layout="centered")

# --- PROFESSIONAL STYLE ---
st.markdown("""
<style>
    .stApp { background-color: #F2F4F7 !important; }
    .top-bar { background-color: #0A1A33; padding: 25px 15px 20px 15px; border-radius: 0px 0px 15px 15px; text-align: center; margin-top: -50px; }
    .school-name { color: #FFFFFF !important; font-size: 32px; font-weight: 800; letter-spacing: 1px; margin: 0; text-transform: uppercase; font-family: 'Segoe UI', sans-serif; }
    .app-name { color: #FFD700 !important; font-size: 20px; font-weight: 700; margin: 5px 0 0 0; letter-spacing: 2px; }
    .subtitle { color: #D9E2EC !important; font-size: 13px; margin: 5px 0 0 0; }
    .card { background-color: white; padding: 22px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.08); border-top: 4px solid #0A1A33; margin-top: 20px; }
    h3 { color: #0A1A33 !important; }
    p, label, span { color: #243B53 !important; }
    .stButton>button { background-color: #0A1A33 !important; color: white !important; font-size: 17px; font-weight: 700; border-radius: 8px; padding: 12px; width: 100%; border: none; }
    .stButton>button:hover { background-color: #FF4500 !important; }
    input, textarea, select { background-color: white !important; color: #102A43 !important; border: 1.5px solid #BCCCDC !important; border-radius: 8px !important; }
    [data-testid="stSidebar"] { background-color: #0A1A33 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    [data-testid="stSidebar"] input { background-color: white !important; color: black !important; }
    .footer { text-align: center; margin-top: 40px; padding: 15px; border-top: 1px solid #D9E2EC; color: #627D98 !important; font-size: 13px; font-weight: 600; letter-spacing: 1px; }
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
    st.markdown(f"<h3 style='text-align:center;'>{title}</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="display:flex; justify-content:center;">
        <div style="width:200px; height:200px; border-radius:50%; background: conic-gradient(#0A9D58 0% {pct_correct}%, #E65100 {pct_correct}% 100%); display:flex; align-items:center; justify-content:center;">
            <div style="width:90px; height:90px; background:white; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#0A1A33; font-weight:800; font-size:20px;">{pct_correct}%</div>
        </div>
    </div>
    <p style="text-align:center; margin-top:10px; font-weight:600;">Correct: {correct} ({pct_correct}%) &nbsp;&nbsp; | &nbsp;&nbsp; Wrong: {wrong} ({pct_wrong}%)</p>
    """, unsafe_allow_html=True)
    df = pd.DataFrame({"Result": ["Correct","Wrong"], "Count": [correct, wrong]})
    st.bar_chart(df.set_index("Result"))

# --- TOP HEADER: SCHOOL NAME IN CAPITAL LETTERS ---
# Default is EBUNTAYO SECONDARY SCHOOL, but Admin can change it
if "school_name_display" not in st.session_state:
    st.session_state.school_name_display = "EBUNTAYO SECONDARY SCHOOL"

school_input = st.text_input("School Name (For Display)", value=st.session_state.school_name_display)
# Always show in CAPITAL LETTERS
school_name_caps = school_input.upper().strip() if school_input else "EBUNTAYO SECONDARY SCHOOL"
st.session_state.school_name_display = school_name_caps

st.markdown(f"""
<div class="top-bar">
    <p class="school-name">{school_name_caps}</p>
    <p class="app-name">GABRIEL CBT PRO</p>
    <p class="subtitle">COMPUTER BASED TEST EXAMINATION PORTAL</p>
</div>
""", unsafe_allow_html=True)

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

# --- ADMIN ---
st.sidebar.title("Admin Panel")
password = st.sidebar.text_input("Admin Password", type="password")
is_admin = (password == "admin123")
if is_admin:
    st.sidebar.success("Admin Logged In")
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
    st.sidebar.subheader("All Results")
    if st.session_state.results:
        df = pd.DataFrame(st.session_state.results)
        st.sidebar.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')
        st.sidebar.download_button("Download Results", csv, "gabriel_cbt_results.csv", "text/csv")
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Overall School Performance")
        total_correct = int(df['score'].sum())
        total_all = int(df['total'].sum())
        show_pie_chart(total_correct, total_all - total_correct, "Overall Performance")
        st.markdown('</div>', unsafe_allow_html=True)

# --- STUDENT LOGIN / EXAM ---
if not st.session_state.exam_started:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<h3>Student Login</h3>", unsafe_allow_html=True)
    if st.session_state.last_score is not None:
        s, t = st.session_state.last_score
        show_pie_chart(s, t-s, "Your Last Exam Performance")
    name = st.text_input("Student Name")
    subject = st.selectbox("Select Subject", ALL_SUBJECTS)
    class_ = st.selectbox("Select Class", ["JSS 1","JSS 2","JSS 3","SS 1","SS 2","SS 3"])
    term = st.selectbox("Select Term", ["First Term","Second Term","Third Term"])
    exam_time = st.selectbox("Select Time", ["10 Minutes","20 Minutes","30 Minutes","1 Hour"])
    if st.button("Start Exam"):
        if not name:
            st.error("Please enter your name!")
        else:
            mins = int(exam_time.split()[0]) if "Hour" not in exam_time else 60
            st.session_state.student_info = {"name": name, "subject": subject, "class": class_, "term": term, "mins": mins, "school": school_name_caps}
            st.session_state.start_time = datetime.now()
            st.session_state.exam_started = True
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
else:
    info = st.session_state.student_info
    st.info(f"Name: {info['name']} | Class: {info['class']} | Subject: {info['subject']} | Term: {info['term']}")
    end_time = st.session_state.start_time + timedelta(minutes=info['mins'])
    remaining = end_time - datetime.now()
    total_seconds = int(remaining.total_seconds())
    if total_seconds <= 0:
        st.error("TIME UP!")
        st.session_state.exam_started = False
        st.rerun()
    else:
        mins_left = total_seconds // 60
        secs_left = total_seconds % 60
        st.warning(f"Time Remaining: {mins_left:02d}:{secs_left:02d}")
    st.markdown(f"<h3>{info['subject']} - {info['term']} Exam</h3>", unsafe_allow_html=True)
    filtered = [q for q in st.session_state.questions if q.get("subject") == info["subject"]]
    if not filtered:
        filtered = st.session_state.questions
    st.write(f"Total Questions: {len(filtered)}")
    answers = {}
    for i, q in enumerate(filtered):
        st.markdown('<div class="card">', unsafe_allow_html=True)
        answers[i] = st.radio(f"Q{i+1}. {q['q']}", q["options"], key=f"q{i}")
        st.markdown('</div>', unsafe_allow_html=True)
    if st.button("Submit Exam"):
        score = sum(1 for i, q in enumerate(filtered) if answers[i] == q["answer"])
        wrong = len(filtered) - score
        st.success(f"{info['name']}, your score is {score}/{len(filtered)}")
        st.balloons()
        st.session_state.last_score = (score, len(filtered))
        st.session_state.results.append({"name": info["name"], "class": info["class"], "subject": info["subject"], "term": info["term"], "score": score, "total": len(filtered), "school": info.get("school","")})
        show_pie_chart(score, wrong, "Your Exam Performance")
    if st.button("Take Another Exam"):
        st.session_state.exam_started = False
        st.rerun()

# --- FOOTER: WITHOUT LOVE EMOJI ---
st.markdown(f"""
<div class="footer">
    {school_name_caps} &nbsp;|&nbsp; GABRIEL CBT PRO<br><br>
    BUILT BY ACHONWA GABRIEL
</div>
""", unsafe_allow_html=True)
