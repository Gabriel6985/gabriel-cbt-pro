import streamlit as st
import time, json, os, pandas as pd
from datetime import datetime

st.set_page_config(page_title="Gabriel CBT Pro", page_icon="🎓")

SUBJECTS = ["English","General mathematics","Civic education","Data processing","Marketing","Yoruba","Igbo","Hausa","Physics","Chemistry","Biology","Further mathematics","Agricultural science","Geography","Computer studies","Physical education","Health education","French","Literature-in-English","Government","Christian Religious studies (CRS)","Islamic studies (IRS)","History","Fine Arts","Economics","Commerce","Financial Accounting","Book keeping","Business Studies","Social studies","Food and nutrition","Animal husbandry","Basic science","Basic Technology","Music"]

# DEFAULT QUESTIONS - Sample, Admin can add more
DEFAULT_Q = {
 "Computer studies": [
  {"q":"What does CPU stand for?","options":["Central Processing Unit","Computer Personal Unit","Central Print Unit","Control Processing Unit"],"answer":"Central Processing Unit"},
  {"q":"What does HTML stand for?","options":["Hyper Text Markup Language","High Text Machine Language","Hyperlink Text Markup Language","Home Tool Markup Language"],"answer":"Hyper Text Markup Language"},
  {"q":"Which device is used to input data?","options":["Monitor","Keyboard","Printer","Speaker"],"answer":"Keyboard"},
  {"q":"What is 1 Byte equal to?","options":["8 Bits","4 Bits","16 Bits","1024 Bits"],"answer":"8 Bits"},
  {"q":"Which is an output device?","options":["Keyboard","Mouse","Printer","Scanner"],"answer":"Printer"},
 ],
 "English": [
  {"q":"Choose the correct plural: One box, two ___","options":["boxs","boxes","boxies","boxen"],"answer":"boxes"},
  {"q":"Which is a noun?","options":["Run","Beautiful","Happiness","Quickly"],"answer":"Happiness"},
  {"q":"She ___ to school everyday.","options":["go","goes","going","gone"],"answer":"goes"},
 ],
 "General mathematics": [
  {"q":"What is 12 + 15?","options":["25","27","28","26"],"answer":"27"},
  {"q":"What is 5 x 8?","options":["35","40","45","30"],"answer":"40"},
  {"q":"What is the square root of 144?","options":["10","12","14","16"],"answer":"12"},
 ],
 "Biology": [
  {"q":"What is the powerhouse of the cell?","options":["Nucleus","Mitochondria","Ribosome","Golgi body"],"answer":"Mitochondria"},
  {"q":"Photosynthesis takes place in the ___","options":["Root","Leaf","Stem","Flower"],"answer":"Leaf"},
 ],
 "Physics": [
  {"q":"What is the SI unit of force?","options":["Joule","Newton","Watt","Pascal"],"answer":"Newton"},
  {"q":"What is the speed of light?","options":["3x10^8 m/s","3x10^6 m/s","3x10^5 m/s","3x10^7 m/s"],"answer":"3x10^8 m/s"},
 ],
 "Chemistry": [
  {"q":"What is H2O?","options":["Salt","Water","Oxygen","Acid"],"answer":"Water"},
  {"q":"What is the chemical symbol for Gold?","options":["Ag","Au","Fe","Gd"],"answer":"Au"},
 ],
 "Economics": [
  {"q":"What is demand?","options":["Quantity willing to buy at a price","Quantity supplied","Total production","Government spending"],"answer":"Quantity willing to buy at a price"},
 ],
 "Government": [
  {"q":"Nigeria gained independence in which year?","options":["1960","1963","1970","1959"],"answer":"1960"},
 ],
}

def load_questions():
    if os.path.exists("questions.json"):
        with open("questions.json") as f:
            return json.load(f)
    return DEFAULT_Q

def save_questions(q):
    with open("questions.json","w") as f:
        json.dump(q,f)

if "started" not in st.session_state: st.session_state.started=False
if "submitted" not in st.session_state: st.session_state.submitted=False
if "start_time" not in st.session_state: st.session_state.start_time=0
if "questions" not in st.session_state: st.session_state.questions=load_questions()

st.title("🎓 Gabriel CBT Pro")
st.caption("Built by Achonwa Gabriel | For Secondary Schools in Nigeria | Any Subject, Any Exam")

# SIDEBAR ADMIN
st.sidebar.title("🔐 Admin / Teacher Panel")
admin_pass = st.sidebar.text_input("Admin Password", type="password")
if admin_pass == "gabriel123":
    st.sidebar.success("Welcome Admin Gabriel!")
    st.sidebar.subheader("➕ Add New Question")
    subj = st.sidebar.selectbox("Subject", SUBJECTS)
    new_q = st.sidebar.text_input("Question")
    opt1 = st.sidebar.text_input("Option A")
    opt2 = st.sidebar.text_input("Option B")
    opt3 = st.sidebar.text_input("Option C")
    opt4 = st.sidebar.text_input("Option D")
    correct = st.sidebar.selectbox("Correct Answer", ["Option A","Option B","Option C","Option D"])
    if st.sidebar.button("Add Question"):
        if new_q and opt1 and opt2 and opt3 and opt4:
            opts = [opt1,opt2,opt3,opt4]
            ans = opts[["Option A","Option B","Option C","Option D"].index(correct)]
            if subj not in st.session_state.questions: st.session_state.questions[subj]=[]
            st.session_state.questions[subj].append({"q":new_q,"options":opts,"answer":ans})
            save_questions(st.session_state.questions)
            st.sidebar.success("Question Added!")
        else:
            st.sidebar.error("Fill all fields")
    st.sidebar.divider()
    st.sidebar.subheader("📊 All Results")
    if os.path.exists("results.csv"):
        df = pd.read_csv("results.csv")
        st.sidebar.write(f"Total: {len(df)} students")
        st.sidebar.dataframe(df)
        st.sidebar.download_button("Download Results", df.to_csv(index=False), "gabriel_cbt_results.csv")
    else:
        st.sidebar.info("No results yet.")
elif admin_pass:
    st.sidebar.error("Wrong password")

# STUDENT LOGIN
if not st.session_state.started:
    st.subheader("Student Login")
    name = st.text_input("Full Name")
    school = st.text_input("School Name")
    student_class = st.selectbox("Class", ["JSS1","JSS2","JSS3","SS1","SS2","SS3"])
    subject = st.selectbox("Choose Subject", SUBJECTS)
    exam_type = st.selectbox("Exam Type", ["1st Term Exam","2nd Term Exam","3rd Term Exam","Mock Exam","Test / Assignment","JAMB Practice"])
    # Show count
    count = len(st.session_state.questions.get(subject,[]))
    st.info(f"Subject: **{subject}** | Questions Available: **{count}** | Time: **15 Minutes**")
    if st.button("Start Exam 🚀", use_container_width=True):
        if name and school:
            if count==0:
                st.error(f"No questions yet for {subject}. Ask your teacher to add questions in Admin Panel.")
            else:
                st.session_state.name=name; st.session_state.school=school; st.session_state.student_class=student_class; st.session_state.subject=subject; st.session_state.exam_type=exam_type
                st.session_state.started=True; st.session_state.start_time=time.time()
                st.rerun()
        else:
            st.warning("Enter Name and School")
    st.stop()

# TIMER
if not st.session_state.submitted:
    elapsed = int(time.time()-st.session_state.start_time)
    remaining = 900 - elapsed
    if remaining<=0:
        st.session_state.submitted=True; st.rerun()
    mins,secs = divmod(remaining,60)
    st.warning(f"⏰ Time Left: {mins:02d}:{secs:02d} | {st.session_state.name} | {st.session_state.subject} | {st.session_state.exam_type}")
    time.sleep(1); st.rerun()

# EXAM
if st.session_state.started and not st.session_state.submitted:
    st.write(f"Good luck **{st.session_state.name}** - {st.session_state.student_class} | {st.session_state.school}")
    qs = st.session_state.questions.get(st.session_state.subject,[])
    answers={}
    for i,q in enumerate(qs):
        st.write(f"**Q{i+1}. {q['q']}**")
        answers[i]=st.radio(f"Q{i+1}", q["options"], key=f"q{i}", index=None)
    if st.button("Submit Exam ✅", use_container_width=True):
        st.session_state.answers=answers; st.session_state.submitted=True; st.rerun()

# RESULT
if st.session_state.submitted:
    qs = st.session_state.questions.get(st.session_state.subject,[])
    answers = st.session_state.get("answers",{})
    score=0
    for i,q in enumerate(qs):
        if answers.get(i)==q["answer"]: score+=1
    percent = (score/len(qs)*100) if qs else 0
    st.success(f"🎉 Result for {st.session_state.name}")
    st.write(f"### Subject: {st.session_state.subject} | Exam: {st.session_state.exam_type}")
    st.write(f"### Score: {score}/{len(qs)}")
    st.write(f"### Percentage: {percent:.1f}%")
    if percent>=70: st.balloons(); st.write("**Grade: A - Excellent!**")
    elif percent>=60: st.write("**Grade: B - Very Good**")
    elif percent>=50: st.write("**Grade: C - Good**")
    elif percent>=40: st.write("**Grade: D - Pass**")
    else: st.write("**Grade: F - Try Again**")
    new_row={"Name":st.session_state.name,"School":st.session_state.school,"Class":st.session_state.student_class,"Subject":st.session_state.subject,"Exam":st.session_state.exam_type,"Score":f"{score}/{len(qs)}","Percent":f"{percent:.1f}%","Date":datetime.now().strftime("%Y-%m-%d %H:%M")}
    if os.path.exists("results.csv"):
        df=pd.read_csv("results.csv"); df=pd.concat([df,pd.DataFrame([new_row])],ignore_index=True)
    else: df=pd.DataFrame([new_row])
    df.to_csv("results.csv",index=False)
    st.write("### Review:")
    for i,q in enumerate(qs):
        ua=answers.get(i,"No answer")
        if ua==q["answer"]: st.write(f"Q{i+1} ✅ {q['answer']}")
        else: st.write(f"Q{i+1} ❌ Your: {ua} | Correct: {q['answer']}")
    if st.button("Take Another Exam 🔄"):
        for k in list(st.session_state.keys()):
            if k!="questions": del st.session_state[k]
        st.session_state.started=False; st.session_state.submitted=False; st.rerun()
