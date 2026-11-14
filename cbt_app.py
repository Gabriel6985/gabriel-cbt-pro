import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title='EBUNTAYO SECONDARY SCHOOL - CBT', page_icon='🎓', layout='wide')
SCHOOL_NAME = 'EBUNTAYO SECONDARY SCHOOL'
ADMIN_PASS = 'admin123'
TEACHER_PASS = 'teacher123'
EXAM_PIN = 'EBS2026'

CSS = '<style>'
CSS += '.stApp{background-color:#F2F2F2 !important;}'
CSS += '.block-container{padding-top:0.8rem !important;padding-bottom:1rem !important;max-width:100% !important;}'
CSS += 'div[data-testid="stVerticalBlock"]{gap:0.6rem !important;}'
# BIG HEADER - TALLER NAVY, BIGGER BOLDER SCHOOL NAME
CSS += '.jamb-header{background-color:#0B2C4A;color:white;padding:34px 12px 28px 12px;border-radius:10px 10px 0 0;border:6px solid #FFD700;position:relative;overflow:hidden;min-height:150px;}'
CSS += '.cap-bg{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:260px;opacity:0.14;z-index:0;}'
CSS += '.jamb-header h1{color:white !important;font-size:72px !important;font-weight:900 !important;margin:0;text-align:center;text-transform:uppercase;-webkit-text-stroke:3.5px #FFD700;text-shadow:6px 6px 0px #000, 10px 10px 20px rgba(0,0,0,0.9);font-family:Arial Black, Arial, sans-serif !important;line-height:1.0;letter-spacing:2px;position:relative;z-index:1;}'
CSS += '.jamb-header p{color:#FFD700 !important;text-align:center;font-size:18px;font-weight:900;margin:14px 0 0 0;letter-spacing:3px;position:relative;z-index:1;}'
CSS += '.student-bar{background-color:#FFFFFF;border:2px solid #0B2C4A;border-top:none;padding:10px;color:#0B2C4A !important;font-weight:900;font-size:15px;text-align:center;}'
CSS += '.card{background-color:#FFFFFF !important;padding:22px;border-radius:10px;margin-top:12px;border-top:5px solid #FFD700;}'
CSS += '.login-title{color:#0B2C4A !important;font-size:28px !important;font-weight:900 !important;text-align:center;text-transform:uppercase;margin:0;font-family:Arial Black, Arial, sans-serif;}'
CSS += '.login-sub{text-align:center;color:#444 !important;font-weight:700;font-size:14px;}'
CSS += '.field-label{color:#0B2C4A !important;font-weight:900 !important;font-size:16px !important;text-transform:uppercase;margin-top:12px;margin-bottom:4px;}'
# SINGLE SELECT ROLE - CLEAN, NO DOUBLE
CSS += 'div[data-testid="stRadio"]{margin-top:8px !important;}'
CSS += 'div[data-testid="stRadio"] > label{font-size:20px !important;font-weight:900 !important;color:#0B2C4A !important;text-transform:uppercase !important;}'
CSS += 'label{font-weight:900 !important;color:#0B2C4A !important;font-size:15px !important;}'
CSS += 'input,textarea,select{background-color:#fff !important;color:#000 !important;border:2px solid #0B2C4A !important;border-radius:8px !important;font-weight:800 !important;font-size:15px !important;}'
CSS += '.stButton>button{background-color:#0A9D58 !important;color:white !important;font-weight:900 !important;border-radius:8px;padding:10px;width:100%;text-transform:uppercase;font-size:14px !important;}'
CSS += '.footer{text-align:center;margin-top:14px;padding:12px;background-color:#0B2C4A;border-radius:8px;color:white !important;font-weight:700;font-size:13px;}'
CSS += '.footer span{color:#FFD700 !important;}'
CSS += '.q-box{background-color:white;border:2px solid #0B2C4A;padding:18px 18px 14px 18px;border-radius:12px;margin-top:14px;margin-bottom:6px;}'
CSS += '.q-title{color:#0B2C4A !important;font-weight:900;font-size:16px;margin:0 0 10px 0;}'
CSS += '.q-text{color:#000 !important;font-weight:800;font-size:21px;line-height:1.5;margin:0 0 14px 0;}'
CSS += 'div[data-testid="stRadio"] label{color:#000 !important;font-size:17px !important;font-weight:700 !important;background:#F8F8F8 !important;padding:11px 12px !important;border:2px solid #0B2C4A !important;border-radius:10px !important;margin-bottom:8px !important;width:100% !important;display:flex !important;align-items:center !important;line-height:1.4 !important;}'
CSS += 'div[data-testid="stRadio"] p{color:#000 !important;font-weight:700 !important;font-size:17px !important;margin:0 !important;line-height:1.4 !important;}'
CSS += '.success-box{background-color:#0A9D58;color:white !important;padding:16px;border-radius:10px;text-align:center;font-size:18px;font-weight:900;margin-top:12px;}'
CSS += '.student-card{background-color:#fff !important;padding:14px;border-radius:10px;margin-top:10px;border:2px solid #0B2C4A;}'
CSS += '.student-name{color:#0B2C4A !important;font-size:18px !important;font-weight:900 !important;text-align:center;text-transform:uppercase;margin:0;}'
CSS += '.student-detail{color:#333 !important;text-align:center;font-weight:700;}'
CSS += '.palette-box{background-color:#FFFFFF;border:2px solid #0B2C4A;border-radius:10px;padding:12px;margin-top:12px;}'
CSS += '.palette-title{color:#0B2C4A !important;font-weight:900;font-size:15px;text-align:center;margin:0 0 8px 0;}'
CSS += '.danger-box{background-color:#FFEBEE;border:2px solid #FF0000;padding:12px;border-radius:10px;margin-top:12px;}'
CSS += '[data-testid="stSidebar"]{background-color:#001A33 !important;} [data-testid="stSidebar"] *{color:white !important;}'
CSS += '</style>'
st.markdown(CSS, unsafe_allow_html=True)

ALL_SUBJECTS = ['Mathematics','English Language','Physics','Chemistry','Biology','Economics','Government','Literature in English','CRS','Geography','Commerce','Financial Accounting','Agricultural Science','Computer Studies / ICT','Social Studies','Basic Science','Civic Education','History','Business Studies']
ALL_CLASSES = ['JSS 1','JSS 2','JSS 3','SS 1','SS 2','SS 3']

DEFAULT_QUESTIONS = [
    {'q': 'What is the full meaning of ICT?', 'options': ['Internet and Computer Technology','Information and Communication Technology','Information and Computer Technology','Internet Communication Tool'], 'answer': 'Information and Communication Technology', 'subject': 'Computer Studies / ICT', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'ICT Basics', 'type': 'Objective', 'passage': '', 'qno': 1},
    {'q': 'Which of these is an input device?', 'options': ['Monitor','Printer','Keyboard','Speaker'], 'answer': 'Keyboard', 'subject': 'Computer Studies / ICT', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'Devices', 'type': 'Objective', 'passage': '', 'qno': 2},
    {'q': 'What does CPU stand for?', 'options': ['Central Processing Unit','Computer Personal Unit','Central Program Unit','Computer Processing Utility'], 'answer': 'Central Processing Unit', 'subject': 'Computer Studies / ICT', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'CPU', 'type': 'Objective', 'passage': '', 'qno': 3},
    {'q': 'Which of these is used to store data permanently?', 'options': ['RAM','Hard Disk','Cache','ROM'], 'answer': 'Hard Disk', 'subject': 'Computer Studies / ICT', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'Memory', 'type': 'Objective', 'passage': '', 'qno': 4},
    {'q': 'Which program is used to browse the internet?', 'options': ['Microsoft Word','Google Chrome','Microsoft Excel','Paint'], 'answer': 'Google Chrome', 'subject': 'Computer Studies / ICT', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'Internet', 'type': 'Objective', 'passage': '', 'qno': 5},
    {'q': 'What is the full meaning of RAM?', 'options': ['Random Access Memory','Read Access Memory','Rapid Access Memory','Random And Memory'], 'answer': 'Random Access Memory', 'subject': 'Computer Studies / ICT', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'Memory', 'type': 'Objective', 'passage': '', 'qno': 6},
    {'q': 'Which of these is an output device?', 'options': ['Keyboard','Mouse','Monitor','Scanner'], 'answer': 'Monitor', 'subject': 'Computer Studies / ICT', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'Devices', 'type': 'Objective', 'passage': '', 'qno': 7},
    {'q': 'If 3x + 5 = 20, what is the value of 2x - 1?', 'options': ['7','9','11','15'], 'answer': '9', 'subject': 'Mathematics', 'class': 'SS 2', 'term': 'First Term', 'topic': 'Algebra', 'type': 'Objective', 'passage': '', 'qno': 1},
    {'q': 'What is 2 + 2?', 'options': ['3','4','5','6'], 'answer': '4', 'subject': 'Mathematics', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'Addition', 'type': 'Objective', 'passage': '', 'qno': 1},
    {'q': 'What is 10 x 5?', 'options': ['15','50','45','55'], 'answer': '50', 'subject': 'Mathematics', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'Multiplication', 'type': 'Objective', 'passage': '', 'qno': 2},
    {'q': 'What is the capital of Nigeria?', 'options': ['Lagos','Abuja','Kano','Ibadan'], 'answer': 'Abuja', 'subject': 'Social Studies', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'Capital', 'type': 'Objective', 'passage': '', 'qno': 1},
    {'q': 'Which arm of government makes laws?', 'options': ['Executive','Legislature','Judiciary','Police'], 'answer': 'Legislature', 'subject': 'Government', 'class': 'SS 2', 'term': 'First Term', 'topic': 'Government', 'type': 'Objective', 'passage': '', 'qno': 1},
    {'q': 'Who is the head of the Executive arm in Nigeria?', 'options': ['Senate President','Chief Justice','President','Governor'], 'answer': 'President', 'subject': 'Government', 'class': 'SS 2', 'term': 'First Term', 'topic': 'Government', 'type': 'Objective', 'passage': '', 'qno': 2},
]

def show_pie_chart(correct, wrong, title, student_name=''):
    total = correct + wrong
    if total == 0:
        st.write('No data yet')
        return
    pct = int((correct/total)*100)
    if student_name:
        st.markdown('<p class="student-name">' + student_name + '</p>', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align:center;color:#0B2C4A;">' + title + '</h3>', unsafe_allow_html=True)
    pie_html = '<div style="display:flex;justify-content:center;"><div style="width:200px;height:200px;border-radius:50%;background: conic-gradient(#0A9D58 0% ' + str(pct) + '%, #E65100 ' + str(pct) + '% 100%);display:flex;align-items:center;justify-content:center;"><div style="width:90px;height:90px;background:white;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#0B2C4A;font-weight:900;font-size:22px;">' + str(pct) + '%</div></div></div><p style="text-align:center;font-weight:700;color:#0B2C4A;">Correct: ' + str(correct) + ' (' + str(pct) + '%) | Wrong: ' + str(wrong) + '</p>'
    st.markdown(pie_html, unsafe_allow_html=True)
    st.bar_chart(pd.DataFrame({'Result': ['Correct','Wrong'], 'Count': [correct, wrong]}).set_index('Result'))

st.markdown('<div class="jamb-header"><div class="cap-bg">🎓</div><h1>🎓 EBUNTAYO SECONDARY SCHOOL 🎓</h1><p>FIRST TERM CBT EXAMINATION | GABRIEL CBT PRO | LANDSCAPE MODE</p></div>', unsafe_allow_html=True)

if 'questions' not in st.session_state: st.session_state.questions = DEFAULT_QUESTIONS.copy()
if 'results' not in st.session_state: st.session_state.results = []
if 'exam_started' not in st.session_state: st.session_state.exam_started = False
if 'student_info' not in st.session_state: st.session_state.student_info = {}
if 'start_time' not in st.session_state: st.session_state.start_time = None
if 'current_q' not in st.session_state: st.session_state.current_q = 0
if 'answers_dict' not in st.session_state: st.session_state.answers_dict = {}
if 'flagged' not in st.session_state: st.session_state.flagged = set()
if 'submitted_msg' not in st.session_state: st.session_state.submitted_msg = False
if 'profile_ok' not in st.session_state: st.session_state.profile_ok = False
if 'shuffled_q' not in st.session_state: st.session_state.shuffled_q = []
if 'active_students' not in st.session_state: st.session_state.active_students = []

is_in_exam = st.session_state.exam_started or st.session_state.profile_ok
if not is_in_exam:
    # FIXED: ONLY ONE SELECT ROLE - NO DOUBLE, NO EXTRA MARKDOWN
    role = st.radio('SELECT ROLE', ['STUDENT - WRITE EXAM', 'TEACHER - SET QUESTIONS', 'ADMIN - MONITOR & RESULTS'], horizontal=True, key='role_select')
else:
    role = 'STUDENT - WRITE EXAM'
    if st.button('LOGOUT / BACK TO LOGIN - End This Exam'):
        st.session_state.exam_started = False
        st.session_state.profile_ok = False
        st.session_state.answers_dict = {}
        st.session_state.flagged = set()
        st.session_state.current_q = 0
        st.session_state.active_students = []
        st.rerun()

if role.startswith('TEACHER'):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="login-title">TEACHER LOGIN</p>', unsafe_allow_html=True)
    st.markdown('<p class="field-label">TEACHER PASSWORD</p>', unsafe_allow_html=True)
    tp = st.text_input('TEACHER PASSWORD', type='password', label_visibility='collapsed')
    if tp == TEACHER_PASS:
        st.success('Welcome Teacher! Set Questions Q1 to Q50')
        st.markdown('<div class="danger-box">', unsafe_allow_html=True)
        st.markdown('<p style="color:#FF0000 !important;font-weight:900;text-align:center;">START FRESH - DELETE SAMPLE QUESTIONS</p>', unsafe_allow_html=True)
        if st.button('DELETE ALL SAMPLE QUESTIONS - START FRESH'):
            st.session_state.questions = []
            st.success('Deleted! Bank is 0. Start from Q1.')
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('---')
        st.subheader('TEACHER QUESTION PALETTE - Q1 TO Q50')
        st.markdown('<p class="field-label">CHOOSE SUBJECT / CLASS TO SET FOR</p>', unsafe_allow_html=True)
        tq_subj_p = st.selectbox('SUBJECT FOR PALETTE', ALL_SUBJECTS, key='t_subj_pal', label_visibility='collapsed')
        tq_class_p = st.selectbox('CLASS FOR PALETTE', ALL_CLASSES, key='t_class_pal', label_visibility='collapsed')
        tq_term_p = st.selectbox('TERM FOR PALETTE', ['First Term','Second Term','Third Term'], key='t_term_pal', label_visibility='collapsed')
        filt_pal = [q for q in st.session_state.questions if q.get('subject')==tq_subj_p and q.get('class')==tq_class_p and q.get('term')==tq_term_p]
        done_nos = set([q.get('qno',0) for q in filt_pal])
        st.markdown('<div class="palette-box"><p class="palette-title">QUESTION PALETTE - ' + tq_subj_p + ' | ' + tq_class_p + ' | ' + str(len(done_nos)) + ' / 50 DONE</p></div>', unsafe_allow_html=True)
        for rs in range(0, 50, 10):
            pcols = st.columns(10)
            for j in range(10):
                qn = rs + j + 1
                lab = 'DONE ' + str(qn) if qn in done_nos else str(qn)
                if pcols[j].button(lab, key='t_pal_' + str(qn)):
                    st.session_state.selected_qno = qn
                    st.rerun()
        st.progress(len(done_nos)/50)
        st.markdown('---')
        st.subheader('ADD / EDIT QUESTION - Q1 TO Q50')
        if 'selected_qno' not in st.session_state: st.session_state.selected_qno = 1
        st.markdown('<p class="field-label">QUESTION NUMBER (1 TO 50)</p>', unsafe_allow_html=True)
        qno = st.selectbox('QUESTION NUMBER', list(range(1, 51)), index=st.session_state.selected_qno-1, key='qno_select', label_visibility='collapsed')
        st.session_state.selected_qno = qno
        existing = None
        for q in filt_pal:
            if q.get('qno')==qno: existing = q; break
        if existing:
            st.info('Q' + str(qno) + ' already exists: ' + str(existing['q'])[:100])
        else:
            st.warning('Q' + str(qno) + ' is EMPTY - Add it now.')
        st.markdown('<p class="field-label">TOPIC</p>', unsafe_allow_html=True)
        tq_topic = st.text_input('TOPIC', value=existing['topic'] if existing else '', label_visibility='collapsed')
        st.markdown('<p class="field-label">QUESTION</p>', unsafe_allow_html=True)
        tq_q = st.text_area('QUESTION', value=existing['q'] if existing else '', label_visibility='collapsed')
        st.markdown('<p class="field-label">OPTION A</p>', unsafe_allow_html=True)
        o1 = st.text_input('OPTION A', value=existing['options'][0] if existing and len(existing['options'])>0 else '', label_visibility='collapsed')
        st.markdown('<p class="field-label">OPTION B</p>', unsafe_allow_html=True)
        o2 = st.text_input('OPTION B', value=existing['options'][1] if existing and len(existing['options'])>1 else '', label_visibility='collapsed')
        st.markdown('<p class="field-label">OPTION C</p>', unsafe_allow_html=True)
        o3 = st.text_input('OPTION C', value=existing['options'][2] if existing and len(existing['options'])>2 else '', label_visibility='collapsed')
        st.markdown('<p class="field-label">OPTION D</p>', unsafe_allow_html=True)
        o4 = st.text_input('OPTION D', value=existing['options'][3] if existing and len(existing['options'])>3 else '', label_visibility='collapsed')
        st.markdown('<p class="field-label">CORRECT ANSWER</p>', unsafe_allow_html=True)
        corr = st.selectbox('CORRECT', ['Option A','Option B','Option C','Option D'], label_visibility='collapsed')
        if st.button('SAVE QUESTION Q' + str(qno)):
            opts = [o1,o2,o3,o4]
            ans = opts[['Option A','Option B','Option C','Option D'].index(corr)]
            if tq_q and all(opts):
                st.session_state.questions = [q for q in st.session_state.questions if not (q.get('subject')==tq_subj_p and q.get('class')==tq_class_p and q.get('term')==tq_term_p and q.get('qno')==qno)]
                st.session_state.questions.append({'q': tq_q, 'options': opts, 'answer': ans, 'subject': tq_subj_p, 'class': tq_class_p, 'term': tq_term_p, 'topic': tq_topic, 'type': 'Objective', 'passage': '', 'qno': qno})
                st.success('Q' + str(qno) + ' Saved!')
                st.session_state.selected_qno = qno+1 if qno<50 else 50
                st.rerun()
            else:
                st.error('Fill all fields!')
        st.markdown('---')
        st.subheader('BULK UPLOAD CSV - Q1 TO Q50 AT ONCE')
        st.info('Columns: question,optionA,optionB,optionC,optionD,answer,subject,class,term,topic')
        up = st.file_uploader('Upload CSV', type=['csv'])
        if up is not None:
            try:
                df_up = pd.read_csv(up)
                for idx2, (_, r) in enumerate(df_up.iterrows()):
                    opts = [str(r.get('optionA','')), str(r.get('optionB','')), str(r.get('optionC','')), str(r.get('optionD',''))]
                    opts = [o for o in opts if o and o != 'nan']
                    st.session_state.questions.append({'q': str(r.get('question','')), 'options': opts, 'answer': str(r.get('answer','')), 'subject': str(r.get('subject',tq_subj_p)), 'class': str(r.get('class',tq_class_p)), 'term': str(r.get('term',tq_term_p)), 'topic': str(r.get('topic','')), 'type': 'Objective', 'passage': '', 'qno': idx2+1})
                st.success('Uploaded!')
            except Exception as e:
                st.error(str(e))
        st.markdown('---')
        st.subheader('QUESTION BANK')
        st.write('Total: ' + str(len(st.session_state.questions)))
        if len(st.session_state.questions)>0:
            st.dataframe(pd.DataFrame(st.session_state.questions))
    elif tp:
        st.error('Wrong Password')
    st.markdown('</div>', unsafe_allow_html=True)

if role.startswith('ADMIN'):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="login-title">ADMIN LOGIN</p>', unsafe_allow_html=True)
    st.markdown('<p class="field-label">ADMIN PASSWORD</p>', unsafe_allow_html=True)
    ap = st.text_input('ADMIN PASSWORD', type='password', label_visibility='collapsed')
    if ap == ADMIN_PASS:
        st.success('Admin Logged In')
        st.subheader('LIVE MONITOR')
        if st.session_state.active_students:
            st.dataframe(pd.DataFrame(st.session_state.active_students))
        else:
            st.info('No student writing now.')
        st.markdown('<p class="field-label">ADD EXTRA TIME</p>', unsafe_allow_html=True)
        extra = st.selectbox('ADD EXTRA TIME', ['+5 Minutes','+10 Minutes','+15 Minutes','+30 Minutes'], label_visibility='collapsed')
        if st.button('Add Extra Time'):
            if st.session_state.start_time:
                st.session_state.start_time += timedelta(minutes=int(extra.split()[0].replace('+','')))
                st.success('Added!')
        if st.button('Reset Frozen Session'):
            st.session_state.exam_started = False; st.session_state.profile_ok = False; st.success('Reset Done'); st.rerun()
        if st.session_state.results:
            df = pd.DataFrame(st.session_state.results)
            st.markdown('---'); st.subheader('ADMIN REVIEW'); st.dataframe(df)
            csv = df.to_csv(index=False).encode('utf-8'); st.download_button('Download Results CSV', csv, 'ebuntayo_results.csv', 'text/csv')
            show_pie_chart(int(df['score'].sum()), int(df['total'].sum())-int(df['score'].sum()), 'Overall Performance')
            df['label'] = df.apply(lambda r: str(r['name']) + ' - ' + str(r['subject']) + ' - ' + str(r['class']), axis=1)
            st.markdown('<p class="field-label">SELECT STUDENT TO REVIEW</p>', unsafe_allow_html=True)
            sel = st.selectbox('SELECT STUDENT', df['label'].tolist(), label_visibility='collapsed')
            srow = df[df['label']==sel].iloc[0]; sc = int(srow['score']); tt = int(srow['total'])
            st.markdown('<div class="student-card"><p class="student-name">' + str(srow['name']) + '</p><p class="student-detail">' + str(srow['subject']) + ' | ' + str(srow['class']) + ' | ' + str(sc) + '/' + str(tt) + '</p></div>', unsafe_allow_html=True)
            show_pie_chart(sc, tt-sc, str(srow['subject']) + ' Performance', student_name=str(srow['name']) + ' Performance')
            st.subheader('All Students - Each With Own Pie Chart')
            for _, row in df.iterrows():
                s = int(row['score']); t = int(row['total'])
                st.markdown('<div class="student-card"><p class="student-name">' + str(row['name']) + '</p><p class="student-detail">' + str(row['subject']) + ' | ' + str(row['class']) + ' | ' + str(s) + '/' + str(t) + '</p></div>', unsafe_allow_html=True)
                show_pie_chart(s, t-s, str(row['subject']), student_name=str(row['name']))
        else:
            st.info('No results yet.')
    elif ap:
        st.error('Wrong Password')
    st.markdown('</div>', unsafe_allow_html=True)

if role.startswith('STUDENT'):
    if not st.session_state.exam_started and not st.session_state.profile_ok:
        if st.session_state.submitted_msg:
            st.markdown('<div class="success-box"><p>EXAM SUBMITTED SUCCESSFULLY!</p><p style="font-size:15px;">Next student can login.</p></div>', unsafe_allow_html=True)
            st.session_state.submitted_msg = False
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="login-title">STUDENT LOGIN</p>', unsafe_allow_html=True)
        st.markdown('<p class="login-sub">Secure Login - Full Name + Exam PIN</p>', unsafe_allow_html=True)
        lc1, lc2 = st.columns(2)
        with lc1:
            st.markdown('<p class="field-label">FULL NAME *</p>', unsafe_allow_html=True)
            name = st.text_input('FULL NAME', placeholder='Enter your full name', key='s_name', label_visibility='collapsed')
            st.markdown('<p class="field-label">SELECT SUBJECT</p>', unsafe_allow_html=True)
            subject = st.selectbox('SELECT SUBJECT', ALL_SUBJECTS, key='s_subj', label_visibility='collapsed')
            st.markdown('<p class="field-label">SELECT TERM</p>', unsafe_allow_html=True)
            term = st.selectbox('SELECT TERM', ['First Term','Second Term','Third Term'], key='s_term', label_visibility='collapsed')
            st.markdown('<p class="field-label">SELECT TIME</p>', unsafe_allow_html=True)
            exam_time = st.selectbox('SELECT TIME', ['10 Minutes','20 Minutes','30 Minutes','1 Hour'], key='s_time', label_visibility='collapsed')
        with lc2:
            st.markdown('<p class="field-label">EXAM PIN *</p>', unsafe_allow_html=True)
            pin = st.text_input('EXAM PIN', type='password', placeholder='Ask teacher for PIN', key='s_pin', label_visibility='collapsed')
            st.markdown('<p class="field-label">SELECT CLASS</p>', unsafe_allow_html=True)
            class_ = st.selectbox('SELECT CLASS', ALL_CLASSES, key='s_class', label_visibility='collapsed')
            st.markdown('<p class="field-label">EXAM TYPE</p>', unsafe_allow_html=True)
            exam_type = st.selectbox('EXAM TYPE', ['First Term Exam','Second Term Exam','Third Term Exam','Mock Exam','Promotion Exam','Test / Quiz'], key='s_type', label_visibility='collapsed')
            st.markdown('<p class="field-label">AGREE</p>', unsafe_allow_html=True)
            agree = st.checkbox('I have read instructions')
        if st.button('CONTINUE TO PROFILE CHECK'):
            if not name:
                st.error('Enter Your Full Name!')
            elif pin != EXAM_PIN:
                st.error('Wrong PIN! Hint: EBS2026')
            elif not agree:
                st.error('Tick instructions!')
            else:
                mins = int(exam_time.split()[0]) if 'Hour' not in exam_time else 60
                st.session_state.student_info = {'name': name, 'exam_no': '', 'subject': subject, 'class': class_, 'term': term, 'exam_type': exam_type, 'mins': mins, 'school': SCHOOL_NAME}
                st.session_state.profile_ok = True
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    elif not st.session_state.exam_started and st.session_state.profile_ok:
        info = st.session_state.student_info
        filt = [q for q in st.session_state.questions if q.get('subject')==info['subject'] and q.get('class')==info['class']]
        if not filt: filt = [q for q in st.session_state.questions if q.get('subject')==info['subject']]
        if not filt: filt = st.session_state.questions
        filt = [q for q in filt if q.get('options') and len(q.get('options'))>=2]
        filt = sorted(filt, key=lambda x: x.get('qno', 999))
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="login-title">PROFILE CHECK</p>', unsafe_allow_html=True)
        st.markdown('<p style="text-align:center;color:#0B2C4A;font-weight:800;">Student: ' + str(info['name']) + '<br>Class: ' + str(info['class']) + ' | Subject: ' + str(info['subject']) + '<br>Total Questions: ' + str(len(filt)) + ' | Time: ' + str(info['mins']) + ' Mins</p>', unsafe_allow_html=True)
        if st.button('CONFIRM & START EXAM'):
            st.session_state.shuffled_q = filt.copy()
            st.session_state.start_time = datetime.now()
            st.session_state.exam_started = True
            st.session_state.current_q = 0
            st.session_state.answers_dict = {}
            st.session_state.flagged = set()
            st.session_state.active_students.append({'name': info['name'], 'subject': info['subject'], 'class': info['class'], 'start': datetime.now().strftime('%H:%M'), 'status': 'Writing'})
            st.rerun()
        if st.button('Back'):
            st.session_state.profile_ok = False
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        info = st.session_state.student_info
        st.markdown('<div class="student-bar">Student: ' + str(info['name']) + ' | Class: ' + str(info['class']) + ' | Subject: ' + str(info['subject']) + '</div>', unsafe_allow_html=True)
        end_time = st.session_state.start_time + timedelta(minutes=info['mins'])
        remaining = end_time - datetime.now()
        total_sec = int(remaining.total_seconds())
        if total_sec <= 0:
            filt = st.session_state.shuffled_q
            score = 0
            for i, qq in enumerate(filt):
                if st.session_state.answers_dict.get(i)==qq['answer']: score += 1
            st.session_state.results.append({'name': info['name'], 'exam_no': '', 'class': info['class'], 'subject': info['subject'], 'term': info['term'], 'exam_type': info.get('exam_type',''), 'score': score, 'total': len(filt), 'school': SCHOOL_NAME, 'date': datetime.now().strftime('%Y-%m-%d %H:%M'), 'theory': ''})
            st.session_state.active_students = [a for a in st.session_state.active_students if a['name']!=info['name']]
            st.session_state.exam_started = False; st.session_state.profile_ok = False; st.session_state.submitted_msg = True; st.rerun()
        else:
            st.markdown('<div style="background:#FF0000;color:white;text-align:center;padding:8px;font-weight:900;font-size:18px;border:2px solid #0B2C4A;border-top:none;">TIME: ' + str(total_sec//60).zfill(2) + ':' + str(total_sec%60).zfill(2) + ' | Questions ' + str(st.session_state.current_q+1) + '-' + str(min(st.session_state.current_q+2, len(st.session_state.shuffled_q))) + ' of ' + str(len(st.session_state.shuffled_q)) + '</div>', unsafe_allow_html=True)
        filtered = st.session_state.shuffled_q
        total_q = len(filtered)
        idx_list = [st.session_state.current_q, st.session_state.current_q+1]
        for idx in idx_list:
            if idx < total_q:
                q = filtered[idx]
                st.markdown('<div class="q-box"><p class="q-title">Question ' + str(idx+1) + ' of ' + str(total_q) + ' | ' + str(info['subject']) + '</p><p class="q-text">' + str(q['q']) + '</p>', unsafe_allow_html=True)
                prev = st.session_state.answers_dict.get(idx, None)
                opts = q['options']; letters = ['A.','B.','C.','D.']
                while len(opts) < 4: opts = opts + ['-']
                opts_letter = [letters[i] + '  ' + opts[i] for i in range(min(4, len(opts)))]
                d_idx = None
                if prev:
                    try: d_idx = opts.index(prev)
                    except: d_idx = None
                choice = st.radio('Select Q' + str(idx+1), opts_letter, index=d_idx, key='radio_' + str(idx), label_visibility='collapsed')
                if choice: st.session_state.answers_dict[idx] = opts[letters.index(choice[:2])]
                cc1, cc2 = st.columns(2)
                with cc1:
                    if st.button('CLEAR Q' + str(idx+1), key='clear_' + str(idx)):
                        st.session_state.answers_dict.pop(idx, None)
                        st.rerun()
                with cc2:
                    if st.button('FLAG Q' + str(idx+1) if idx not in st.session_state.flagged else 'UNFLAG Q' + str(idx+1), key='flag_' + str(idx)):
                        if idx in st.session_state.flagged: st.session_state.flagged.remove(idx)
                        else: st.session_state.flagged.add(idx)
                        st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="palette-box"><p class="palette-title">QUESTION PALETTE - CLICK NUMBER TO JUMP | Answered: ' + str(len([v for v in st.session_state.answers_dict.values() if v not in [None,'']])) + ' / ' + str(total_q) + ' | Flagged: ' + str(len(st.session_state.flagged)) + '</p></div>', unsafe_allow_html=True)
        for row_start in range(0, total_q, 10):
            pcols = st.columns(10)
            for j in range(10):
                idx = row_start + j
                if idx < total_q:
                    if idx in st.session_state.flagged: lab = 'FLAG ' + str(idx+1)
                    elif idx in st.session_state.answers_dict and st.session_state.answers_dict[idx] not in [None,'']: lab = 'DONE ' + str(idx+1)
                    else: lab = str(idx+1)
                    if idx in idx_list: lab = '[' + str(idx+1) + '*]'
                    if pcols[j].button(lab, key='pal_' + str(idx)):
                        st.session_state.current_q = idx if idx % 2 == 0 else idx-1
                        st.rerun()
        b1,b2,b3,b4 = st.columns(4)
        with b1:
            if st.button('< Previous'):
                if st.session_state.current_q>=2: st.session_state.current_q -= 2; st.rerun()
        with b2:
            if st.button('CLEAR ALL'):
                st.session_state.answers_dict = {}
                st.rerun()
        with b3:
            if st.button('Next >'):
                if st.session_state.current_q+2 < total_q: st.session_state.current_q += 2; st.rerun()
        with b4:
            if st.button('SUBMIT EXAM'):
                score = 0
                for i, qq in enumerate(filtered):
                    if st.session_state.answers_dict.get(i)==qq['answer']: score += 1
                st.session_state.results.append({'name': info['name'], 'exam_no': '', 'class': info['class'], 'subject': info['subject'], 'term': info['term'], 'exam_type': info.get('exam_type',''), 'score': score, 'total': len(filtered), 'school': SCHOOL_NAME, 'date': datetime.now().strftime('%Y-%m-%d %H:%M'), 'theory': ''})
                st.session_state.active_students = [a for a in st.session_state.active_students if a['name']!=info['name']]
                st.session_state.exam_started = False; st.session_state.profile_ok = False; st.session_state.submitted_msg = True; st.session_state.current_q = 0; st.session_state.answers_dict = {}; st.session_state.flagged = set(); st.rerun()

st.markdown('<div class="footer">🎓 EBUNTAYO SECONDARY SCHOOL | GABRIEL CBT PRO<br>BUILT BY <span>ACHONWA GABRIEL UCHECHUKWU</span> | Exam PIN: EBS2026</div>', unsafe_allow_html=True)
