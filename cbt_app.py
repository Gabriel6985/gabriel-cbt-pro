import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="EBUNTAYO SECONDARY SCHOOL - CBT Portal", page_icon="🎓", layout="centered")

SCHOOL_NAME = "EBUNTAYO SECONDARY SCHOOL"

# --- REAL CBT COLOURS - FIXED VISIBILITY ---
st.markdown("""
<style>
    .stApp { background-color: #0B2C4A !important; }
    /* TOP HEADER - SCHOOL NAME SUPER BOLD */
    .top-bar { background: linear-gradient(90deg, #001A33 0%, #0B2C4A 50%, #001A33 100%); padding: 30px 12px 24px 12px; border-radius: 12px; text-align: center; border: 3px solid #FFD700; box-shadow: 0 6px 25px rgba(0,0,0,0.6); margin-top: 5px; }
    .school-name { color: #FFFFFF !important; font-size: 48px !important; font-weight: 900 !important; letter-spacing: 1px; margin: 0; line-height: 1.05; font-family: 'Arial Black', Arial, sans-serif !important; text-transform: uppercase; -webkit-text-stroke: 1.5px #FFD700; text-shadow: 3px 3px 0px #000, 5px 5px 10px rgba(0,0,0,0.8); }
    .app-name { color: #FFD700 !important; font-size: 24px !important; font-weight: 900; margin: 10px 0 0 0; letter-spacing: 3px; text-shadow: 2px 2px 4px #000; }
    .subtitle { color: #FFFFFF !important; font-size: 12px; margin: 6px 0 0 0; letter-spacing: 2px; font-weight: 700; }
    /* CARDS - WHITE AND CLEAR */
    .card { background-color: #FFFFFF !important; padding: 26px; border-radius: 14px; box-shadow: 0 6px 20px rgba(0,0,0,0.4); margin-top: 18px; border-top: 6px solid #FFD700; }
    .card h3, .card h2 { color: #0B2C4A !important; }
    /* LOGIN TITLE - VERY BOLD AND VISIBLE */
    .login-title { color: #0B2C4A !important; font-size: 30px !important; font-weight: 900 !important; text-align: center; margin: 0 0 5px 0; text-transform: uppercase; letter-spacing: 1px; font-family: 'Arial Black', sans-serif; }
    .login-sub { text-align:center; color: #444 !important; font-size: 14px; font-weight: 600; margin-bottom: 18px; }
    /* LABELS - THIS WAS THE PROBLEM, NOW FIXED TO BLACK ON WHITE CARD */
    label { font-weight: 800 !important; color: #0B2C4A !important; font-size: 16px !important; }
    /* ALSO MAKE ALL TEXT OUTSIDE CARD WHITE */
    .stMarkdown p { color: white !important; }
    .card .stMarkdown p, .card p { color: #0B2C4A !important; }
    input, textarea, select { background-color: #FFFFFF !important; color: #000000 !important; border: 2.5px solid #0B2C4A !important; border-radius: 8px !important; font-weight: 700 !important; font-size: 16px !important; }
    div[data-baseweb="select"] > div { background-color: white !important; color: black !important; border: 2.5px solid #0B2C4A !important; }
    /* BUTTONS - START EXAM GREEN */
    .stButton>button { background-color: #0A9D58 !important; color: white !important; font-size: 19px !important; font-weight: 900 !important; border-radius: 10px; padding: 14px; width: 100%; border: none; box-shadow: 0 4px 10px rgba(0,0,0,0.3); letter-spacing: 1px; text-transform: uppercase; }
    .stButton>button:hover { background-color: #078A4C !important; }
    .timer-box { background-color: #FF0000; color: white !important; padding: 14px; border-radius: 10px; text-align: center; font-size: 24px; font-weight: 900; letter-spacing: 2px; margin: 10px 0; }
    .info-bar { background-color: #FFF3CD; padding: 12px; border-radius: 8px; border-left: 5px solid #FFD700; color: #0B2C4A !important; font-weight: 700; font-size: 14px; margin: 10px 0; }
    [data-testid="stSidebar"] { background-color: #001A33 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    [data-testid="stSidebar"] input { background-color: white !important; color: black !important; }
    .footer { text-align: center; margin-top: 30px; padding: 18px; background-color: #001A33; border-radius: 10px; border: 1px solid #FFD700; color: #FFFFFF !important; font-size: 13px; font-weight: 700; letter-spacing: 1px; }
    .footer span { color: #FFD700 !important; }
    .instruction-box { background-color: #E8F0FE; padding: 15px; border-radius: 10px; border: 1px solid #0B2C4A; margin-top: 12px; }
    .instruction-box b, .instruction-box li { color: #0B2C4A !important; }
    .question-card { background-color: white; padding: 18px; border-radius: 10px; margin-top: 12px; border-left: 5px solid #0B2C4A; box-shadow: 0 2px 8px rgba(0,0,0,0.15); }
    .question-card p { color: #0B2C4A !important; font-weight: 700; }
    .field-label { color: #0B2C4A !important; font-weight: 900 !important; font-size: 15px !important; margin-bottom: 2px; margin-top: 10px; }
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
    st.markdown(f"<h3 style='text-align:center; color:#0B2C4A;'>{title}</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="display:flex; justify-content:center;">
        <div style="width:210px; height:210px; border-radius:50%; background: conic-gradient(#0A9D58 0% {pct_correct}%, #E65100 {pct_correct}% 100%); display:flex; align-items:center; justify-content:center; box-shadow: 0 4px 12px rgba(0,0,0,0.2);">
            <div style="width:95px; height:95px; background:white; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#0B2C4A; font-weight:900; font-size:22px;">{pct_correct}%</div>
        </div>
    </div>
    <p style="text-align:center; margin-top:12px; font-weight:700; color:#0B2C4A;">Correct: {correct} ({pct_correct}%) &nbsp;|&nbsp; Wrong: {wrong} ({pct_wrong}%)</p>
    <div style="display:flex; gap:10px; justify-content:center; margin-top:8px;">
        <span style="background:#0A9D58; color:white; padding:6px 14px; border-radius:20px; font-weight:700; font-size:13px;">CORRECT {pct_correct}%</span>
        <span style="background:#E65100; color:white; padding:6px 14px; border-radius:20px; font-weight:700; font-size:13px;">WRONG {pct_wrong}%</span>
    </div>
    """, unsafe_allow_html=True)
    df = pd.DataFrame({"Result": ["Correct","Wrong"], "Count": [correct, wrong]})
    st.bar_chart(df.set_index("Result"))

st.markdown(f"""
<div class="top-bar">
    <p class="school-name">{SCHOOL_NAME}</p>
    <p class="app-name">★ GABRIEL CBT PRO ★</p>
    <p class="subtitle">COMPUTER BASED TEST &nbsp;|&nbsp; EXAMINATION PORTAL</p>
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
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "answers_dict" not in st.session_state:
    st.session_state.answers_dict = {}

st.sidebar.title("Admin Panel")
password = st.sidebar.text_input("Admin Password", type="password")
is_admin = (password == "admin123")
if is_admin:
    st.sidebar.success("Admin Logged In")
    st.sidebar.subheader("Add New Question")
    new_subject = st.sidebar.selectbox("Subject", ALL_SUBJECTS)
    new_q = st.sidebar.text_area("Question")
    o1 = st.sidebar.text_input("Option A")
    o2 = st.sidebar.text_input("Option B")
    o3 = st.sidebar.text_input("Option C")
    o4 = st.sidebar.text_input("Option D")
    correct = st.sidebar.selectbox("Correct Answer", ["Option A","Option B","Option C","Option D"])
    if st.sidebar.button("Add Question"):
        opts = [o1,o2,o3,o4]
        ans = opts[["Option A","Option B","Option C","Option D"].index(correct)]
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
        st.sidebar.download_button("Download Results", csv, "ebuntayo_cbt_results.csv", "text/csv")
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Overall School Performance")
        total_correct = int(df['score'].sum())
        total_all = int(df['total'].sum())
        show_pie_chart(total_correct, total_all - total_correct, "Overall Performance")
        st.markdown('</div>', unsafe_allow_html=True)

if not st.session_state.exam_started:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<p class='login-title'>STUDENT LOGIN</p>", unsafe_allow_html=True)
    st.markdown("<p class='login-sub'>Enter your details to begin your examination</p>", unsafe_allow_html=True)
    if st.session_state.last_score is not None:
        s, t = st.session_state.last_score
        show_pie_chart(s, t-s, "Your Last Exam Performance")
    st.markdown("<p class='field-label'>FULL NAME *</p>", unsafe_allow_html=True)
    name = st.text_input("Full Name", label_visibility="collapsed", placeholder="Enter your full name")
    st.markdown("<p class='field-label'>EXAM NUMBER / ADMISSION NO</p>", unsafe_allow_html=True)
    exam_no = st.text_input("Exam Number", label_visibility="collapsed", placeholder="e.g. EBS/001")
    st.markdown("<p class='field-label'>SELECT SUBJECT</p>", unsafe_allow_html=True)
    subject = st.selectbox("Select Subject", ALL_SUBJECTS, label_visibility="collapsed")
    st.markdown("<p class='field-label'>SELECT CLASS</p>", unsafe_allow_html=True)
    class_ = st.selectbox("Select Class", ["JSS 1","JSS 2","JSS 3","SS 1","SS 2","SS 3"], label_visibility="collapsed")
    st.markdown("<p class='field-label'>SELECT TERM</p>", unsafe_allow_html=True)
    term = st.selectbox("Select Term", ["First Term","Second Term","Third Term"], label_visibility="collapsed")
    st.markdown("<p class='field-label'>EXAM TYPE</p>", unsafe_allow_html=True)
    exam_type = st.selectbox("Exam Type", ["First Term Exam","Second Term Exam","Third Term Exam","Mock Exam","Promotion Exam","Test / Quiz"], label_visibility="collapsed")
    st.markdown("<p class='field-label'>SELECT TIME</p>", unsafe_allow_html=True)
    exam_time = st.selectbox("Select Time", ["10 Minutes","20 Minutes","30 Minutes","1 Hour"], label_visibility="collapsed")
    st.markdown("""
    <div class="instruction-box">
        <b>EXAMINATION INSTRUCTIONS:</b>
        <ul>
            <li>Read each question carefully before answering</li>
            <li>Each question has only ONE correct answer</li>
            <li>Do NOT refresh the page during the exam</li>
            <li>Exam will submit AUTOMATICALLY when time is up</li>
            <li>Click SUBMIT EXAM when you finish</li>
            <li>Malpractice is NOT allowed</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    agree = st.checkbox("I have read and understood the instructions")
    if st.button("START EXAM"):
        if not name:
            st.error("Please enter your full name!")
        elif not agree:
            st.error("Please tick 'I have read the instructions' to continue!")
        else:
            mins = int(exam_time.split()[0]) if "Hour" not in exam_time else 60
            st.session_state.student_info = {"name": name, "exam_no": exam_no, "subject": subject, "class": class_, "term": term, "exam_type": exam_type, "mins": mins, "school": SCHOOL_NAME}
            st.session_state.start_time = datetime.now()
            st.session_state.exam_started = True
            st.session_state.current_q = 0
            st.session_state.answers_dict = {}
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
else:
    info = st.session_state.student_info
    st.markdown(f"<div class='info-bar'>Name: {info['name']} | {SCHOOL_NAME} | {info['subject']} | {info['class']} | {info['term']} | {info.get('exam_type','')}</div>", unsafe_allow_html=True)
    end_time = st.session_state.start_time + timedelta(minutes=info['mins'])
    remaining = end_time - datetime.now()
    total_seconds = int(remaining.total_seconds())
    if total_seconds <= 0:
        st.error("TIME UP! Submitting automatically...")
        st.session_state.exam_started = False
        st.rerun()
    else:
        mins_left = total_seconds // 60
        secs_left = total_seconds % 60
        st.markdown(f"<div class='timer-box'>TIME REMAINING: {mins_left:02d}:{secs_left:02d}</div>", unsafe_allow_html=True)
        st.progress(1 - (total_seconds / (info['mins']*60)))
    filtered = [q for q in st.session_state.questions if q.get("subject") == info["subject"]]
    if not filtered:
        filtered = st.session_state.questions
    total_q = len(filtered)
    answered = len([v for v in st.session_state.answers_dict.values() if v])
    st.markdown(f"<div class='info-bar'>Question {st.session_state.current_q+1} of {total_q} | Answered: {answered} | Remaining: {total_q - answered}</div>", unsafe_allow_html=True)
    st.progress(answered/total_q if total_q>0 else 0)
    st.write("Question Palette: Click a number to jump")
    cols = st.columns(5)
    for idx in range(total_q):
        is_done = idx in st.session_state.answers_dict
        label = f"{'✅ ' if is_done else ''}{idx+1}"
        if cols[idx % 5].button(label, key=f"pal_{idx}"):
            st.session_state.current_q = idx
            st.rerun()
    q = filtered[st.session_state.current_q]
    st.markdown('<div class="question-card">', unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:18px;'>Q{st.session_state.current_q+1}. {q['q']}</p>", unsafe_allow_html=True)
    prev_ans = st.session_state.answers_dict.get(st.session_state.current_q, None)
    options_with_letters = [f"A. {q['options'][0]}", f"B. {q['options'][1]}", f"C. {q['options'][2]}", f"D. {q['options'][3]}"]
    default_idx = None
    if prev_ans:
        try:
            default_idx = q['options'].index(prev_ans)
        except:
            default_idx = None
    choice = st.radio("Select your answer:", options_with_letters, index=default_idx, key=f"radio_{st.session_state.current_q}")
    if choice:
        chosen_raw = q['options'][["A.","B.","C.","D."].index(choice[:2])]
        st.session_state.answers_dict[st.session_state.current_q] = chosen_raw
    st.markdown('</div>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("PREVIOUS"):
            if st.session_state.current_q > 0:
                st.session_state.current_q -= 1
                st.rerun()
    with c2:
        if st.button("NEXT"):
            if st.session_state.current_q < total_q-1:
                st.session_state.current_q += 1
                st.rerun()
    st.write("---")
    if st.button("SUBMIT EXAM"):
        score = sum(1 for i, qq in enumerate(filtered) if st.session_state.answers_dict.get(i) == qq["answer"])
        wrong = total_q - score
        st.success(f"{info['name']}, your score is {score}/{total_q}")
        st.balloons()
        st.session_state.last_score = (score, total_q)
        st.session_state.results.append({"name": info["name"], "exam_no": info.get("exam_no",""), "class": info["class"], "subject": info["subject"], "term": info["term"], "exam_type": info.get("exam_type",""), "score": score, "total": total_q, "school": SCHOOL_NAME, "date": datetime.now().strftime("%Y-%m-%d %H:%M")})
        show_pie_chart(score, wrong, "Your Exam Performance")
        pct = (score/total_q*100) if total_q>0 else 0
        grade = "A - Excellent!" if pct>=70 else "B - Very Good!" if pct>=60 else "C - Good" if pct>=50 else "D - Fair" if pct>=40 else "F - Try Again"
        st.info(f"Percentage: {pct:.1f}% | Grade: {grade}")
    if st.button("Take Another Exam"):
        st.session_state.exam_started = False
        st.session_state.current_q = 0
        st.session_state.answers_dict = {}
        st.rerun()

st.markdown(f"""
<div class="footer">
    {SCHOOL_NAME} &nbsp;|&nbsp; GABRIEL CBT PRO<br><br>
    BUILT BY <span>ACHONWA GABRIEL</span>
</div>
""", unsafe_allow_html=True)
