import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="EBUNTAYO SECONDARY SCHOOL - CBT Portal", page_icon="🎓", layout="centered")
SCHOOL_NAME = "EBUNTAYO SECONDARY SCHOOL"
ADMIN_PASS = "admin123"
TEACHER_PASS = "teacher123"
EXAM_PIN = "EBS2026"  # Change this - give to students

st.markdown("""
<style>
    .stApp { background-color: #0B2C4A !important; }
    .top-bar { background: linear-gradient(90deg, #001A33 0%, #0B2C4A 50%, #001A33 100%); padding: 28px 12px 22px 12px; border-radius: 12px; text-align: center; border: 3px solid #FFD700; margin-top: 5px; }
    .school-name { color: #FFFFFF !important; font-size: 46px !important; font-weight: 900 !important; font-family: 'Arial Black', Arial, sans-serif !important; text-transform: uppercase; -webkit-text-stroke: 1.5px #FFD700; text-shadow: 3px 3px 0px #000; margin: 0; line-height: 1.05; }
    .app-name { color: #FFD700 !important; font-size: 22px !important; font-weight: 900; margin: 8px 0 0 0; letter-spacing: 3px; }
    .subtitle { color: #FFFFFF !important; font-size: 12px; margin: 5px 0 0 0; letter-spacing: 2px; font-weight: 700; }
    .card { background-color: #FFFFFF !important; padding: 24px; border-radius: 14px; margin-top: 16px; border-top: 6px solid #FFD700; }
    .login-title { color: #0B2C4A !important; font-size: 28px !important; font-weight: 900 !important; text-align: center; text-transform: uppercase; font-family: 'Arial Black', sans-serif; margin:0; }
    .login-sub { text-align:center; color: #444 !important; font-size: 14px; font-weight: 600; }
    label { font-weight: 800 !important; color: #0B2C4A !important; font-size: 16px !important; }
    .stMarkdown p { color: white !important; } .card p, .card li, .card b { color: #0B2C4A !important; }
    input, textarea, select { background-color: #FFFFFF !important; color: #000 !important; border: 2.5px solid #0B2C4A !important; border-radius: 8px !important; font-weight: 700 !important; font-size: 16px !important; }
    div[data-baseweb="select"] > div { background-color: white !important; color: black !important; border: 2.5px solid #0B2C4A !important; }
    .stButton>button { background-color: #0A9D58 !important; color: white !important; font-size: 18px !important; font-weight: 900 !important; border-radius: 10px; padding: 12px; width: 100%; border: none; text-transform: uppercase; }
    .timer-box { background-color: #FF0000; color: white !important; padding: 14px; border-radius: 10px; text-align: center; font-size: 24px; font-weight: 900; margin: 10px 0; }
    .info-bar { background-color: #FFF3CD; padding: 12px; border-radius: 8px; border-left: 5px solid #FFD700; color: #0B2C4A !important; font-weight: 700; font-size: 14px; margin: 10px 0; }
    [data-testid="stSidebar"] { background-color: #001A33 !important; } [data-testid="stSidebar"] * { color: white !important; } [data-testid="stSidebar"] input { background-color: white !important; color: black !important; }
    .footer { text-align: center; margin-top: 28px; padding: 16px; background-color: #001A33; border-radius: 10px; border: 1px solid #FFD700; color: #FFFFFF !important; font-size: 13px; font-weight: 700; }
    .footer span { color: #FFD700 !important; }
    .instruction-box { background-color: #E8F0FE; padding: 14px; border-radius: 10px; border: 1px solid #0B2C4A; margin-top: 12px; }
    .field-label { color: #0B2C4A !important; font-weight: 900 !important; font-size: 15px !important; margin-top: 10px; }
    .question-card { background-color: #FFFFFF !important; padding: 24px; border-radius: 14px; margin-top: 12px; border-left: 6px solid #FFD700; }
    .question-card p { color: #0B2C4A !important; font-weight: 900 !important; font-size: 22px !important; line-height: 1.4; }
    div[data-testid="stRadio"] label { color: #000 !important; font-size: 21px !important; font-weight: 800 !important; background: #fff !important; padding: 16px !important; border: 3px solid #0B2C4A !important; border-radius: 12px !important; margin-bottom: 12px !important; width: 100% !important; display: flex !important; align-items: center !important; }
    div[data-testid="stRadio"] p { color: #000 !important; font-weight: 800 !important; font-size: 21px !important; }
    div[data-testid="stRadio"] > label { border: none !important; } div[data-testid="stRadio"] > label p { color: #0B2C4A !important; font-size: 17px !important; }
    div[data-testid="stRadio"] input[type="radio"] { transform: scale(1.7); margin-right: 10px !important; }
    .success-box { background-color: #0A9D58; color: white !important; padding: 18px; border-radius: 12px; text-align: center; font-size: 20px; font-weight: 900; margin-top: 14px; } .success-box p { color: white !important; }
    .student-card { background-color: #FFFFFF !important; padding: 18px; border-radius: 12px; margin-top: 12px; border: 2px solid #0B2C4A; }
    .student-name { color: #0B2C4A !important; font-size: 21px !important; font-weight: 900 !important; text-align: center; text-transform: uppercase; margin:0; }
    .student-detail { color: #333 !important; text-align: center; font-weight: 700; font-size: 14px; }
    .passage-box { background-color: #FFF8E1; padding: 16px; border-radius: 10px; border: 2px dashed #E65100; margin-bottom: 14px; } .passage-box p, .passage-box b { color: #0B2C4A !important; }
    .calc-box { background: #F1F1F1; padding: 12px; border-radius: 10px; border: 2px solid #0B2C4A; }
</style>
""", unsafe_allow_html=True)

ALL_SUBJECTS = ["Mathematics","English Language","Physics","Chemistry","Biology","Economics","Government","Literature in English","CRS","Geography","Commerce","Financial Accounting","Agricultural Science","Computer Studies / ICT","Social Studies","Basic Science","Civic Education","History","Business Studies"]
ALL_CLASSES = ["JSS 1","JSS 2","JSS 3","SS 1","SS 2","SS 3"]

DEFAULT_QUESTIONS = [
    {"q": "What is the full meaning of ICT?", "options": ["Internet and Computer Technology","Information and Communication Technology","Information and Computer Technology","Internet Communication Tool"], "answer": "Information and Communication Technology", "subject": "Computer Studies / ICT", "class": "JSS 1", "term": "First Term", "topic": "ICT Basics", "type": "Objective", "passage": ""},
    {"q": "Which of these is an input device?", "options": ["Monitor","Printer","Keyboard","Speaker"], "answer": "Keyboard", "subject": "Computer Studies / ICT", "class": "JSS 1", "term": "First Term", "topic": "Devices", "type": "Objective", "passage": ""},
    {"q": "What does CPU stand for?", "options": ["Central Processing Unit","Computer Personal Unit","Central Program Unit","Computer Processing Utility"], "answer": "Central Processing Unit", "subject": "Computer Studies / ICT", "class": "JSS 1", "term": "First Term", "topic": "CPU", "type": "Objective", "passage": ""},
    {"q": "A computer is an electronic device. True or False?", "options": ["True","False"], "answer": "True", "subject": "Computer Studies / ICT", "class": "JSS 1", "term": "First Term", "topic": "Basics", "type": "True/False", "passage": ""},
    {"q": "The full meaning of RAM is ______", "options": [], "answer": "Random Access Memory", "subject": "Computer Studies / ICT", "class": "JSS 1", "term": "First Term", "topic": "Memory", "type": "Fill-in-blank", "passage": ""},
    {"q": "Explain in your own words what a computer is and list 3 uses.", "options": [], "answer": "Teacher to mark", "subject": "Computer Studies / ICT", "class": "JSS 1", "term": "First Term", "topic": "Theory", "type": "Theory/Essay", "passage": ""},
    {"q": "What is 2 + 2?", "options": ["3","4","5","6"], "answer": "4", "subject": "Mathematics", "class": "JSS 1", "term": "First Term", "topic": "Addition", "type": "Objective", "passage": ""},
]

def show_pie_chart(correct, wrong, title, student_name=""):
    total = correct + wrong
    if total == 0: st.write("No data yet"); return
    pct = int((correct/total)*100)
    if student_name: st.markdown(f"<p class='student-name'>{student_name}</p>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='text-align:center; color:#0B2C4A;'>{title}</h3>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="display:flex; justify-content:center;"><div style="width:200px; height:200px; border-radius:50%; background: conic-gradient(#0A9D58 0% {pct}%, #E65100 {pct}% 100%); display:flex; align-items:center; justify-content:center;"><div style="width:90px; height:90px; background:white; border-radius:50%; display:flex; align-items:center; justify-content:center; color:#0B2C4A; font-weight:900; font-size:22px;">{pct}%</div></div></div>
    <p style="text-align:center; margin-top:10px; font-weight:700; color:#0B2C4A;">Correct: {correct} ({pct}%) | Wrong: {wrong} ({100-pct}%)</p>
    """, unsafe_allow_html=True)
    st.bar_chart(pd.DataFrame({"Result": ["Correct","Wrong"], "Count": [correct, wrong]}).set_index("Result"))

st.markdown(f"""<div class="top-bar"><p class="school-name">{SCHOOL_NAME}</p><p class="app-name">★ GABRIEL CBT PRO ★</p><p class="subtitle">COMPUTER BASED TEST | ADMIN - TEACHER - STUDENT | JAMB / WAEC STANDARD</p></div>""", unsafe_allow_html=True)

# --- SESSION ---
for k,v in [("questions", DEFAULT_QUESTIONS.copy()),("results",[]),("exam_started",False),("student_info",{}),("start_time",None),("current_q",0),("answers_dict",{}),("flagged",set()),("submitted_msg",False),("profile_ok",False),("shuffled_q",[]),("theory_answers",{}),("active_students",[]),("calc_val","")]:
    if k not in st.session_state: st.session_state[k]=v

# --- ROLE SELECTOR - TOP ---
st.markdown('<div class="card">', unsafe_allow_html=True)
role = st.radio("WHO ARE YOU? Select Your Workspace:", ["🎓 Student - Write Exam", "👩‍🏫 Teacher - Set Questions", "🛡️ Admin - Monitor & Results"], horizontal=True)
st.markdown('</div>', unsafe_allow_html=True)

# ========== TEACHER MODULE ==========
if role.startswith("👩"):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<p class='login-title'>TEACHER LOGIN</p>", unsafe_allow_html=True)
    tp = st.text_input("Teacher Password", type="password", help="Default: teacher123")
    if tp == TEACHER_PASS:
        st.success("Welcome Teacher!")
        st.subheader("1. Add One Question - All Formats")
        q_type = st.selectbox("Question Type", ["Objective","True/False","Fill-in-blank","Theory/Essay"])
        tq_subj = st.selectbox("Subject", ALL_SUBJECTS, key="t_subj")
        tq_class = st.selectbox("Class", ALL_CLASSES, key="t_class")
        tq_term = st.selectbox("Term", ["First Term","Second Term","Third Term"], key="t_term")
        tq_topic = st.text_input("Topic", placeholder="e.g. Fractions, ICT Basics")
        tq_passage = st.text_area("Passage / Comprehension (Optional - for English)", placeholder="Paste passage here if question needs it")
        tq_q = st.text_area("Question")
        if q_type == "Objective":
            o1 = st.text_input("Option A"); o2 = st.text_input("Option B"); o3 = st.text_input("Option C"); o4 = st.text_input("Option D")
            corr = st.selectbox("Correct Answer", ["Option A","Option B","Option C","Option D"])
            if st.button("Add Objective Question"):
                opts=[o1,o2,o3,o4]; ans=opts[["Option A","Option B","Option C","Option D"].index(corr)]
                if tq_q and all(opts):
                    st.session_state.questions.append({"q":tq_q,"options":opts,"answer":ans,"subject":tq_subj,"class":tq_class,"term":tq_term,"topic":tq_topic,"type":"Objective","passage":tq_passage}); st.success("Added!")
        elif q_type == "True/False":
            corr2 = st.selectbox("Correct Answer", ["True","False"])
            if st.button("Add True/False"):
                if tq_q: st.session_state.questions.append({"q":tq_q,"options":["True","False"],"answer":corr2,"subject":tq_subj,"class":tq_class,"term":tq_term,"topic":tq_topic,"type":"True/False","passage":tq_passage}); st.success("Added!")
        elif q_type == "Fill-in-blank":
            ans_fill = st.text_input("Correct Answer (for auto-marking)")
            if st.button("Add Fill-in-blank"):
                if tq_q: st.session_state.questions.append({"q":tq_q,"options":[],"answer":ans_fill,"subject":tq_subj,"class":tq_class,"term":tq_term,"topic":tq_topic,"type":"Fill-in-blank","passage":tq_passage}); st.success("Added!")
        else:
            if st.button("Add Theory Question"):
                if tq_q: st.session_state.questions.append({"q":tq_q,"options":[],"answer":"Teacher to mark","subject":tq_subj,"class":tq_class,"term":tq_term,"topic":tq_topic,"type":"Theory/Essay","passage":tq_passage}); st.success("Added! Theory goes to Teacher Marking.")
        st.markdown("---")
        st.subheader("2. Bulk Upload - Excel / CSV (No Typing One by One)")
        st.info("CSV Format: question, optionA, optionB, optionC, optionD, answer, subject, class, term, topic, type")
        up = st.file_uploader("Upload CSV File", type=["csv"])
        if up is not None:
            try:
                df_up = pd.read_csv(up)
                for _, r in df_up.iterrows():
                    opts = [str(r.get("optionA","")), str(r.get("optionB","")), str(r.get("optionC","")), str(r.get("optionD",""))]
                    opts = [o for o in opts if o and o!="nan"]
                    st.session_state.questions.append({"q":str(r.get("question","")),"options":opts,"answer":str(r.get("answer","")),"subject":str(r.get("subject","Mathematics")),"class":str(r.get("class","JSS 1")),"term":str(r.get("term","First Term")),"topic":str(r.get("topic","")),"type":str(r.get("type","Objective")),"passage":""})
                st.success(f"Uploaded {len(df_up)} questions!")
            except Exception as e: st.error(f"Error: {e}")
        st.markdown("---")
        st.subheader("3. Question Bank - Filter by Class / Subject / Term / Topic")
        f_subj = st.selectbox("Filter Subject", ["All"]+ALL_SUBJECTS, key="f_subj")
        f_class = st.selectbox("Filter Class", ["All"]+ALL_CLASSES, key="f_class")
        f_term = st.selectbox("Filter Term", ["All","First Term","Second Term","Third Term"], key="f_term")
        f_type = st.selectbox("Filter Type", ["All","Objective","True/False","Fill-in-blank","Theory/Essay"], key="f_type")
        qdf = pd.DataFrame(st.session_state.questions)
        if f_subj!="All": qdf=qdf[qdf['subject']==f_subj]
        if f_class!="All": qdf=qdf[qdf['class']==f_class]
        if f_term!="All": qdf=qdf[qdf['term']==f_term]
        if f_type!="All": qdf=qdf[qdf['type']==f_type]
        st.write(f"Total Questions in Bank: {len(st.session_state.questions)} | Showing: {len(qdf)}")
        st.dataframe(qdf)
        st.markdown("---")
        st.subheader("4. Mark Theory / Essay - Hybrid Grading")
        st.info("Objective = Auto-marked. Theory = You mark here.")
        # Show theory answers submitted (stored in results theory field)
        theory_list = [r for r in st.session_state.results if r.get("theory")]
        if theory_list:
            for r in theory_list:
                st.write(f"{r['name']} - {r['subject']} - Theory: {r.get('theory')}")
                mark = st.number_input(f"Mark for {r['name']}", 0, 10, key=f"mark_{r['name']}_{r['subject']}")
                if st.button(f"Save Mark {r['name']}", key=f"btn_{r['name']}_{r['subject']}"):
                    r['theory_mark']=mark; st.success("Saved!")
        else: st.write("No theory answers yet.")
        st.markdown("---")
        st.subheader("5. Exam Scheduling & Batching")
        st.write(f"Current Exam PIN for Students: **{EXAM_PIN}** | Tell students this PIN")
        st.write("Assign: JSS 1 - 10:00AM Batch A, SS 1 - 11:00AM Batch B (You can announce batches)")
    elif tp: st.error("Wrong Teacher Password")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== ADMIN MODULE ==========
if role.startswith("🛡️"):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("<p class='login-title'>ADMIN LOGIN</p>", unsafe_allow_html=True)
    ap = st.text_input("Admin Password", type="password")
    if ap == ADMIN_PASS:
        st.success("Admin Logged In")
        # LIVE MONITOR
        st.subheader("🔴 LIVE MONITOR - Who Is Writing Now?")
        if st.session_state.active_students:
            st.dataframe(pd.DataFrame(st.session_state.active_students))
        else: st.info("No student is writing now. When a student starts, they appear here.")
        # SESSION RECOVERY
        st.subheader("🛠️ Session Recovery - Add Extra Time")
        st.write("If a student's PC fails, add time here. (Applies to current exam)")
        extra = st.selectbox("Add Extra Time", ["+5 Minutes","+10 Minutes","+15 Minutes","+30 Minutes"])
        if st.button("Add Extra Time to Current Exam"):
            mins_extra = int(extra.split()[0].replace("+",""))
            if st.session_state.start_time:
                st.session_state.start_time += timedelta(minutes=mins_extra)
                st.success(f"Added {mins_extra} mins!")
            else: st.info("No active exam now.")
        if st.button("Reset Frozen Session"):
            st.session_state.exam_started=False; st.session_state.answers_dict={}; st.success("Session Reset - Answers saved in results if submitted")
        # REVIEW
        if st.session_state.results:
            df = pd.DataFrame(st.session_state.results)
            st.markdown("---"); st.subheader("🔍 ADMIN REVIEW - Per-Student Pie Chart")
            st.dataframe(df)
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Results - Excel/CSV (Broadsheet)", csv, "ebuntayo_results.csv", "text/csv")
            total_c = int(df['score'].sum()); total_a = int(df['total'].sum())
            show_pie_chart(total_c, total_a-total_c, "Overall School Performance")
            df['label'] = df.apply(lambda r: f"{r['name']} - {r['subject']} - {r['class']} - {r.get('date','')}", axis=1)
            sel = st.selectbox("Select Student to Review", df['label'].tolist())
            srow = df[df['label']==sel].iloc[0]
            sc=int(srow['score']); tt=int(srow['total']); pct=(sc/tt*100) if tt else 0
            st.markdown(f"<div class='student-card'><p class='student-name'>{srow['name']}</p><p class='student-detail'>{srow['subject']} | {srow['class']} | Score {sc}/{tt} | {pct:.1f}% | Theory: {srow.get('theory','-')}</p></div>", unsafe_allow_html=True)
            show_pie_chart(sc, tt-sc, f"{srow['subject']} Performance", student_name=f"{srow['name']}'s Performance")
            st.subheader("📋 All Students - Each With Own Pie Chart + Name")
            for _, row in df.iterrows():
                s=int(row['score']); t=int(row['total'])
                st.markdown(f"<div class='student-card'><p class='student-name'>{row['name']}</p><p class='student-detail'>{row['subject']} | {row['class']} | {s}/{t}</p></div>", unsafe_allow_html=True)
                show_pie_chart(s, t-s, f"{row['subject']}", student_name=f"{row['name']}")
        else: st.info("No results yet.")
        st.subheader("👥 User & Role Management")
        st.write("Admin: admin123 | Teacher: teacher123 | Student: Uses Exam PIN + Name + Admission No")
        st.write(f"Student Exam PIN: {EXAM_PIN}")
    elif ap: st.error("Wrong Admin Password")
    st.markdown('</div>', unsafe_allow_html=True)

# ========== STUDENT MODULE ==========
if role.startswith("🎓"):
    if not st.session_state.exam_started and not st.session_state.profile_ok:
        if st.session_state.submitted_msg:
            st.markdown("<div class='success-box'><p>✅ EXAM SUBMITTED SUCCESSFULLY!</p><p style='font-size:15px;'>Your answers saved. Next student can login.</p></div>", unsafe_allow_html=True)
            st.session_state.submitted_msg=False
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("<p class='login-title'>STUDENT LOGIN</p>", unsafe_allow_html=True)
        st.markdown("<p class='login-sub'>Secure Login - Admission No + Exam PIN</p>", unsafe_allow_html=True)
        st.markdown("<p class='field-label'>FULL NAME *</p>", unsafe_allow_html=True)
        name = st.text_input("Full Name", label_visibility="collapsed", placeholder="Enter full name", key="s_name")
        st.markdown("<p class='field-label'>ADMISSION NO / REGISTRATION ID *</p>", unsafe_allow_html=True)
        exam_no = st.text_input("Admission No", label_visibility="collapsed", placeholder="e.g. EBS/001", key="s_no")
        st.markdown("<p class='field-label'>EXAM PIN / ACCESS CODE *</p>", unsafe_allow_html=True)
        pin = st.text_input("Exam PIN", label_visibility="collapsed", placeholder="Ask teacher for PIN", type="password", key="s_pin")
        st.markdown("<p class='field-label'>SELECT SUBJECT</p>", unsafe_allow_html=True)
        subject = st.selectbox("Subject", ALL_SUBJECTS, label_visibility="collapsed", key="s_subj")
        st.markdown("<p class='field-label'>SELECT CLASS</p>", unsafe_allow_html=True)
        class_ = st.selectbox("Class", ALL_CLASSES, label_visibility="collapsed", key="s_class")
        st.markdown("<p class='field-label'>SELECT TERM</p>", unsafe_allow_html=True)
        term = st.selectbox("Term", ["First Term","Second Term","Third Term"], label_visibility="collapsed", key="s_term")
        st.markdown("<p class='field-label'>EXAM TYPE</p>", unsafe_allow_html=True)
        exam_type = st.selectbox("Exam Type", ["First Term Exam","Second Term Exam","Third Term Exam","Mock Exam","Promotion Exam","Test / Quiz"], label_visibility="collapsed", key="s_type")
        st.markdown("<p class='field-label'>SELECT TIME</p>", unsafe_allow_html=True)
        exam_time = st.selectbox("Time", ["10 Minutes","20 Minutes","30 Minutes","1 Hour"], label_visibility="collapsed", key="s_time")
        st.markdown("<div class='instruction-box'><b>INSTRUCTIONS:</b><ul><li>Do NOT switch tab / copy / right-click - Anti-Malpractice</li><li>Questions are shuffled for each student</li><li>Result NOT shown to you - Only Admin sees it</li><li>Auto-save: Your answers save immediately</li></ul></div>", unsafe_allow_html=True)
        agree = st.checkbox("I have read instructions")
        if st.button("CONTINUE TO PROFILE CHECK"):
            if not name or not exam_no: st.error("Enter Name + Admission No!")
            elif pin != EXAM_PIN: st.error("Wrong Exam PIN! Ask your teacher. Hint: EBS2026")
            elif not agree: st.error("Tick instructions!")
            else:
                mins = int(exam_time.split()[0]) if "Hour" not in exam_time else 60
                st.session_state.student_info={"name":name,"exam_no":exam_no,"subject":subject,"class":class_,"term":term,"exam_type":exam_type,"mins":mins,"school":SCHOOL_NAME}
                st.session_state.profile_ok=True; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    elif not st.session_state.exam_started and st.session_state.profile_ok:
        # PROFILE CHECK
        info = st.session_state.student_info
        filt = [q for q in st.session_state.questions if q.get("subject")==info["subject"] and q.get("class")==info["class"]]
        if not filt: filt = [q for q in st.session_state.questions if q.get("subject")==info["subject"]]
        if not filt: filt = st.session_state.questions
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("<p class='login-title'>PROFILE CHECK</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:center; color:#0B2C4A; font-weight:800;'>Name: {info['name']}<br>Admission: {info['exam_no']}<br>Subject: {info['subject']}<br>Class: {info['class']} | Term: {info['term']}<br>Total Questions: {len(filt)} | Time: {info['mins']} Mins<br>Exam Type: {info['exam_type']}</p>", unsafe_allow_html=True)
        st.warning("Check your details! Once you click START, timer begins and cannot be paused.")
        if st.button("✅ CONFIRM & START EXAM"):
            # SHUFFLE - Anti-malpractice
            shuffled = filt.copy(); random.shuffle(shuffled)
            # Shuffle options for objective
            for qq in shuffled:
                if qq.get("options") and len(qq["options"])>2:
                    # Keep answer value, shuffle order
                    opts = qq["options"].copy(); random.shuffle(opts); qq["options"]=opts
            st.session_state.shuffled_q = shuffled
            st.session_state.start_time=datetime.now(); st.session_state.exam_started=True; st.session_state.current_q=0; st.session_state.answers_dict={}; st.session_state.flagged=set()
            # Add to live monitor
            st.session_state.active_students.append({"name":info['name'],"subject":info['subject'],"class":info['class'],"start":datetime.now().strftime("%H:%M"),"status":"Writing"})
            st.rerun()
        if st.button("⬅ Back to Login"): st.session_state.profile_ok=False; st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # EXAM SCREEN
        info = st.session_state.student_info
        st.markdown(f"<div class='info-bar'>Name: {info['name']} | {SCHOOL_NAME} | {info['subject']} | {info['class']} | DO NOT SWITCH TAB</div>", unsafe_allow_html=True)
        end_time = st.session_state.start_time + timedelta(minutes=info['mins'])
        remaining = end_time - datetime.now(); total_sec=int(remaining.total_seconds())
        # CALCULATOR - Built-in Tool
        with st.expander("🧮 CALCULATOR - Click to Open"):
            st.markdown('<div class="calc-box">', unsafe_allow_html=True)
            c1,c2,c3 = st.columns(3)
            n1 = c1.number_input("First Number", value=0.0, key="calc1")
            op = c2.selectbox("Operation", ["+","-","×","÷"], key="calc_op")
            n2 = c3.number_input("Second Number", value=0.0, key="calc2")
            if op=="+": res=n1+n2
            elif op=="-": res=n1-n2
            elif op=="×": res=n1*n2
            else: res=n1/n2 if n2!=0 else 0
            st.success(f"Answer: {res}")
            st.markdown('</div>', unsafe_allow_html=True)
        if total_sec <= 0:
            # Auto-submit
            filt = st.session_state.shuffled_q
            score = 0; theory_txt=""
            for i, qq in enumerate(filt):
                if qq.get("type")=="Theory/Essay": theory_txt+=str(st.session_state.answers_dict.get(i,""))+" | "
                elif qq.get("type")=="Fill-in-blank":
                    if str(st.session_state.answers_dict.get(i,"")).strip().lower()==str(qq["answer"]).strip().lower(): score+=1
                else:
                    if st.session_state.answers_dict.get(i)==qq["answer"]: score+=1
            st.session_state.results.append({"name":info["name"],"exam_no":info.get("exam_no",""),"class":info["class"],"subject":info["subject"],"term":info["term"],"exam_type":info.get("exam_type",""),"score":score,"total":len(filt),"school":SCHOOL_NAME,"date":datetime.now().strftime("%Y-%m-%d %H:%M"),"theory":theory_txt})
            st.session_state.exam_started=False; st.session_state.profile_ok=False; st.session_state.submitted_msg=True; st.session_state.answers_dict={}; st.rerun()
        else:
            st.markdown(f"<div class='timer-box'>TIME REMAINING: {total_sec//60:02d}:{total_sec%60:02d}</div>", unsafe_allow_html=True)
            st.progress(1-(total_sec/(info['mins']*60)))
        filtered = st.session_state.shuffled_q
        total_q=len(filtered); answered=len([v for v in st.session_state.answers_dict.values() if v not in [None,""]])
        st.markdown(f"<div class='info-bar'>Question {st.session_state.current_q+1} of {total_q} | Answered: {answered} | Flagged: {len(st.session_state.flagged)} | Remaining: {total_q-answered}</div>", unsafe_allow_html=True)
        st.write("Question Palette: 🟢 Answered | 🟡 Flagged | ⚪ Not Answered")
        cols = st.columns(5)
        for idx in range(total_q):
            if idx in st.session_state.flagged: lab=f"🟡 {idx+1}"
            elif idx in st.session_state.answers_dict and st.session_state.answers_dict[idx] not in [None,""]: lab=f"🟢 {idx+1}"
            else: lab=f"⚪ {idx+1}"
            if cols[idx%5].button(lab, key=f"pal_{idx}"): st.session_state.current_q=idx; st.rerun()
        q = filtered[st.session_state.current_q]
        st.markdown('<div class="question-card">', unsafe_allow_html=True)
        if q.get("passage"): st.markdown(f"<div class='passage-box'><b>📖 PASSAGE:</b><p>{q['passage']}</p></div>", unsafe_allow_html=True)
        st.markdown(f"<p>Q{st.session_state.current_q+1}. [{q.get('type','Objective')}] {q['q']}</p>", unsafe_allow_html=True)
        prev = st.session_state.answers_dict.get(st.session_state.current_q, None)
        if q.get("type") in ["Objective","True/False"]:
            opts = q["options"]
            letters=["A.","B.","C.","D."]
            opts_letter=[f"{letters[i]} {opts[i]}" for i in range(len(opts))]
            d_idx=None
            if prev:
                try: d_idx=opts.index(prev)
                except: d_idx=None
            choice=st.radio("Select your answer:", opts_letter, index=d_idx, key=f"radio_{st.session_state.current_q}")
            if choice:
                # Auto-save immediately
                chosen = opts[letters.index(choice[:2])]
                st.session_state.answers_dict[st.session_state.current_q]=chosen
        elif q.get("type")=="Fill-in-blank":
            ans_fill = st.text_input("Type your answer here:", value=str(prev) if prev else "", key=f"fill_{st.session_state.current_q}")
            if ans_fill: st.session_state.answers_dict[st.session_state.current_q]=ans_fill
        else:
            ans_theory = st.text_area("Write your Theory / Essay answer:", value=str(prev) if prev else "", key=f"theory_{st.session_state.current_q}", height=150)
            if ans_theory: st.session_state.answers_dict[st.session_state.current_q]=ans_theory
        st.markdown('</div>', unsafe_allow_html=True)
        c1,c2,c3 = st.columns(3)
        with c1:
            if st.button("PREVIOUS"):
                if st.session_state.current_q>0: st.session_state.current_q-=1; st.rerun()
        with c2:
            if st.button("🚩 FLAG / UNFLAG"):
                if st.session_state.current_q in st.session_state.flagged: st.session_state.flagged.remove(st.session_state.current_q)
                else: st.session_state.flagged.add(st.session_state.current_q)
                st.rerun()
        with c3:
            if st.button("NEXT"):
                if st.session_state.current_q<total_q-1: st.session_state.current_q+=1; st.rerun()
        st.write("---")
        if st.button("SUBMIT EXAM"):
            score=0; theory_txt=""
            for i, qq in enumerate(filtered):
                if qq.get("type")=="Theory/Essay": theory_txt+=str(st.session_state.answers_dict.get(i,""))+" | "
                elif qq.get("type")=="Fill-in-blank":
                    if str(st.session_state.answers_dict.get(i,"")).strip().lower()==str(qq["answer"]).strip().lower(): score+=1
                else:
                    if st.session_state.answers_dict.get(i)==qq["answer"]: score+=1
            st.session_state.results.append({"name":info["name"],"exam_no":info.get("exam_no",""),"class":info["class"],"subject":info["subject"],"term":info["term"],"exam_type":info.get("exam_type",""),"score":score,"total":len(filtered),"school":SCHOOL_NAME,"date":datetime.now().strftime("%Y-%m-%d %H:%M"),"theory":theory_txt})
            # Remove from live monitor
            st.session_state.active_students=[a for a in st.session_state.active_students if a["name"]!=info["name"]]
            st.session_state.exam_started=False; st.session_state.profile_ok=False; st.session_state.submitted_msg=True; st.session_state.current_q=0; st.session_state.answers_dict={}; st.session_state.flagged=set(); st.rerun()

st.markdown(f"""<div class="footer">{SCHOOL_NAME} | GABRIEL CBT PRO<br>BUILT BY <span>ACHONWA GABRIEL</span> | Admin: admin123 | Teacher: teacher123 | Student PIN: EBS2026</div>""", unsafe_allow_html=True)
