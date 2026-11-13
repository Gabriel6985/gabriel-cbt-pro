import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.set_page_config(page_title="Gabriel CBT Pro", page_icon="📝")

# --- PERFECT THEME - NO WHITE ---
st.markdown("""
<style>
    .stApp { background-color: #0A1A33 !important; }
    h1 { color: #FFD700 !important; text-align: center; }
    h3, p, label, span { color: white !important; }
    .stButton>button { background-color: #FF4500 !important; color: white !important; font-size: 18px; font-weight: bold; border-radius: 12px; padding: 12px; width: 100%; border: none; }
    .stButton>button:hover { background-color: #FFD700 !important; color: black !important; }
    [data-testid="stSidebar"] { background-color: #000B1E !important; }
    [data-testid="stSidebar"] * { color: #FFD700 !important; }
    input, textarea, select { background-color: #1E3A5F !important; color: white !important; border: 2px solid #FFD700 !important; border-radius: 10px !important; }
    [data-testid="stTextInput"] input { background-color: #1E3A5F !important; color: white !important; }
    [data-testid="stSelectbox"] div { background-color: #1E3A5F !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

ALL_SUBJECTS = ["Mathematics","English Language","Physics","Chemistry","Biology","Further Mathematics","Economics","Government","Literature in English","CRS","IRS","Geography","Commerce","Financial Accounting","Agricultural Science","Computer Studies / ICT","Social Studies","Basic Science","Basic Technology","Civic Education","History","Home Economics","Business Studies","French","Yoruba","Igbo","Hausa","Fine Arts","Music","Physical & Health Education"]

DEFAULT_QUESTIONS = [
    {"q": "What is the full meaning of ICT?", "options": ["Internet and Computer Technology","Information and Communication Technology","Information and Computer Technology","Internet Communication Tool"], "answer": "Information and Communication Technology", "subject": "Computer Studies / ICT"},
    {"q": "Which of these is an input device?", "options": ["Monitor","Printer","Keyboard","Speaker"], "answer": "Keyboard", "subject": "Computer Studies / ICT"},
    {"q": "What does CPU stand for?", "options": ["Central Processing Unit","Computer Personal Unit","Central Program Unit","Computer Processing Utility"], "answer": "Central Processing Unit", "subject": "Computer Studies / ICT"},
    {"q": "Which of these is used to store data permanently?", "options": ["RAM","Hard Disk","Cache","ROM"], "answer": "Hard Disk", "subject": "Computer Studies / ICT"},
    {"q": "Which program is used to browse the internet?", "options": ["Microsoft Word","Google Chrome","Microsoft Excel","Paint"], "answer": "Google Chrome", "subject": "Computer Studies / ICT"},
    {"q": "What is 2 + 2?", "options": ["3","4","5","6"], "answer": "4", "subject": "Mathematics"},
    {"q": "What is 5 x 3?", "options": ["10","15","20","25"], "answer": "15", "subject": "Mathematics"},
    {"q": "What is the capital of Nigeria?", "options": ["Lagos","Abuja","Kano","Ibadan"], "answer": "Abuja", "subject": "Social Studies"},
]

def show_pie_chart(correct, wrong, title):
    st.markdown(f"<h3 style='color:#FFD700; text-align:center;'>{title}</h3>", unsafe_allow_html=True)
    if correct + wrong == 0:
        st.write("No data yet for pie chart")
        return
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('#0A1A33')
    ax.set_facecolor('#0A1A33')
    labels = ['Correct ✅', 'Wrong ❌']
    sizes = [correct, wrong]
    colors = ['#00FF7F', '#FF4500']
    # If one is zero, avoid empty pie error
    if correct == 0 or wrong == 0:
        # Show single color
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'color':'white', 'fontsize':12, 'weight':'bold'})
    else:
        ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, textprops={'color':'white', 'fontsize':12, 'weight':'bold'})
    ax.axis('equal')
    st.pyplot(fig)

st.markdown("<h1>📝 Gabriel CBT Pro</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#FF4500 !important;'>Built by ACHONWA GABRIEL</h3>", unsafe_allow_html=True)
school_name = st.text_input("🏫 School Name (For Exam)", placeholder="e.g. Bright Future Secondary School")
if school_name:
    st.markdown(f"<h2 style='text-align:center; color:#00FF7F !important;'>{school_name.upper()}</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#00FF7F !important; font-weight:bold;'>Welcome to Your Online Exam Portal 🎓</p>", unsafe_allow_html=True)
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
    correct = st.sidebar.selectbox("Correct Answer", ["Option 1","Option 2","Option 3","Option 4"])
    if st.sidebar.button("Add Question"):
        opts = [o1,o2,o3,o4]
        ans = opts[["Option 1","Option 2","Option 3","Option 4"].index(correct)]
        if new_q and all(opts):
            st.session_state.questions.append({"q": new_q, "options": opts, "answer": ans, "subject": new_subject})
            st.sidebar.success("Question Added!")
        else:
            st.sidebar.error("Fill all fields!")
    st.sidebar.subheader("📊 All Results & Performance")
    if st.session_state.results:
        df = pd.DataFrame(st.session_state.results)
        st.sidebar.dataframe(df)
        csv = df.to_csv(index=False).encode('utf-8')
        st.sidebar.download_button("📥 Download Results as Excel/CSV", csv, "gabriel_cbt_results.csv", "text/csv")
        # ADMIN PIE CHART - Overall Pass/Fail
        total_correct = int(df['score'].sum())
        total_questions_all = int(df['total'].sum())
        total_wrong = total_questions_all - total_correct
        st.subheader("📊 Overall School Performance")
        show_pie_chart(total_correct, total_wrong, "📊 Overall Performance - All Students")
        # Show by Subject
        st.write("**Performance by Subject:**")
        for subj in df['subject'].unique():
            sub_df = df[df['subject']==subj]
            c = int(sub_df['score'].sum())
            t = int(sub_df['total'].sum())
            w = t - c
            st.write(f"{subj}: {c}/{t} Correct")
            show_pie_chart(c, w, f"🥧 {subj}")
    else:
        st.sidebar.write("No results yet - Pie chart will appear after first exam")

if not st.session_state.exam_started:
    st.markdown("<h3 style='color:#FFD700;'>👨‍🎓 Student Login</h3>", unsafe_allow_html=True)
    # Show last result pie chart if exists
    if st.session_state.last_score is not None:
        s, t = st.session_state.last_score
        st.success(f"Last Result: {s}/{t}")
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
    if info.get("school"):
        st.info(f"🏫 {info['school']} | Name: {info['name']} | Class: {info['class']} | Subject: {info['subject']} | Term: {info['term']}")
    else:
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
    st.markdown(f"<h3 style='color:#00FF7F;'>{info['subject']} - {info['term']} Exam</h3>", unsafe_allow_html=True)
    st.warning("⚠️ Do not leave this page or refresh. Your exam will be submitted.")
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
            wrong = len(filtered) - score
            st.success(f"🎉 {info['name']}, your score is {score}/{len(filtered)}")
            st.balloons()
            st.session_state.last_score = (score, len(filtered))
            st.session_state.results.append({"name": info["name"], "class": info["class"], "subject": info["subject"], "term": info["term"], "score": score, "total": len(filtered), "school": info.get("school","")})
            # STUDENT PIE CHART
            show_pie_chart(score, wrong, "🥧 Your Exam Performance")
    with col2:
        if st.button("Refresh Timer 🔄"):
            st.rerun()
    if st.button("Take Another Exam"):
        st.session_state.exam_started = False
        st.rerun()

st.markdown("---")
st.markdown("<center><h3 style='color:#FF4500;'>Built by ACHONWA GABRIEL ❤️</h3></center>", unsafe_allow_html=True)
