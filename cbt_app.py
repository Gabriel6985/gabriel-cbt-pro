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
CSS += '.jamb-header{background-color:#0B2C4A;color:white;padding:18px 10px;border-radius:8px 8px 0 0;border:4px solid #FFD700;}'
CSS += '.jamb-header h1{color:white !important;font-size:42px !important;font-weight:900 !important;margin:0;text-align:center;text-transform:uppercase;letter-spacing:1px;-webkit-text-stroke:1.5px #FFD700;text-shadow:4px 4px 0px #000, 6px 6px 12px rgba(0,0,0,0.8);font-family:Arial Black, Arial, sans-serif !important;line-height:1.1;}'
CSS += '.jamb-header p{color:#FFD700 !important;text-align:center;font-size:15px;font-weight:900;margin:8px 0 0 0;letter-spacing:3px;}'
CSS += '.student-bar{background-color:#FFFFFF;border:2px solid #0B2C4A;border-top:none;padding:10px 14px;color:#0B2C4A !important;font-weight:900;font-size:15px;}'
CSS += '.card{background-color:#FFFFFF !important;padding:24px;border-radius:12px;margin-top:14px;border-top:6px solid #FFD700;}'
CSS += '.login-title{color:#0B2C4A !important;font-size:30px !important;font-weight:900 !important;text-align:center;text-transform:uppercase;margin:0;font-family:Arial Black, Arial, sans-serif;}'
CSS += '.login-sub{text-align:center;color:#444 !important;font-weight:700;font-size:14px;}'
CSS += '.field-label{color:#0B2C4A !important;font-weight:900 !important;font-size:18px !important;text-transform:uppercase;margin-top:14px;margin-bottom:2px;letter-spacing:0.5px;}'
CSS += '.select-role{color:#0B2C4A !important;font-weight:900 !important;font-size:20px !important;text-transform:uppercase;letter-spacing:1px;margin:0;}'
CSS += 'label{font-weight:900 !important;color:#0B2C4A !important;font-size:16px !important;}'
CSS += 'input,textarea,select{background-color:#fff !important;color:#000 !important;border:2.5px solid #0B2C4A !important;border-radius:8px !important;font-weight:800 !important;font-size:16px !important;}'
CSS += '.stButton>button{background-color:#0A9D58 !important;color:white !important;font-weight:900 !important;border-radius:8px;padding:12px;width:100%;text-transform:uppercase;font-size:18px !important;}'
CSS += '.footer{text-align:center;margin-top:20px;padding:14px;background-color:#0B2C4A;border-radius:8px;color:white !important;font-weight:700;}'
CSS += '.footer span{color:#FFD700 !important;}'
CSS += 'div[data-testid="stRadio"] label{color:#000 !important;font-size:21px !important;font-weight:800 !important;background:#fff !important;padding:14px 12px !important;border:2px solid #ddd !important;border-radius:8px !important;margin-bottom:10px !important;width:100% !important;display:flex !important;align-items:center !important;}'
CSS += 'div[data-testid="stRadio"] p{color:#000 !important;font-weight:800 !important;font-size:21px !important;}'
CSS += 'div[data-testid="stRadio"] > label{border:none !important;}'
CSS += '.success-box{background-color:#0A9D58;color:white !important;padding:18px;border-radius:12px;text-align:center;font-size:20px;font-weight:900;margin-top:14px;}'
CSS += '.student-card{background-color:#fff !important;padding:16px;border-radius:10px;margin-top:10px;border:2px solid #0B2C4A;}'
CSS += '.student-name{color:#0B2C4A !important;font-size:20px !important;font-weight:900 !important;text-align:center;text-transform:uppercase;margin:0;}'
CSS += '.student-detail{color:#333 !important;text-align:center;font-weight:700;}'
CSS += '[data-testid="stSidebar"]{background-color:#001A33 !important;} [data-testid="stSidebar"] *{color:white !important;}'
CSS += '</style>'
st.markdown(CSS, unsafe_allow_html=True)

ALL_SUBJECTS = ['Mathematics','English Language','Physics','Chemistry','Biology','Economics','Government','Literature in English','CRS','Geography','Commerce','Financial Accounting','Agricultural Science','Computer Studies / ICT','Social Studies','Basic Science','Civic Education','History','Business Studies']
ALL_CLASSES = ['JSS 1','JSS 2','JSS 3','SS 1','SS 2','SS 3']

DEFAULT_QUESTIONS = [
    {'q': 'If 3x + 5 = 20, what is the value of 2x - 1?', 'options': ['7','9','11','15'], 'answer': '9', 'subject': 'Mathematics', 'class': 'SS 2', 'term': 'First Term', 'topic': 'Algebra', 'type': 'Objective', 'passage': ''},
    {'q': 'What is the full meaning of ICT?', 'options': ['Internet and Computer Technology','Information and Communication Technology','Information and Computer Technology','Internet Communication Tool'], 'answer': 'Information and Communication Technology', 'subject': 'Computer Studies / ICT', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'ICT Basics', 'type': 'Objective', 'passage': ''},
    {'q': 'Which of these is an input device?', 'options': ['Monitor','Printer','Keyboard','Speaker'], 'answer': 'Keyboard', 'subject': 'Computer Studies / ICT', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'Devices', 'type': 'Objective', 'passage': ''},
    {'q': 'What does CPU stand for?', 'options': ['Central Processing Unit','Computer Personal Unit','Central Program Unit','Computer Processing Utility'], 'answer': 'Central Processing Unit', 'subject': 'Computer Studies / ICT', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'CPU', 'type': 'Objective', 'passage': ''},
    {'q': 'A computer is an electronic device. True or False?', 'options': ['True','False'], 'answer': 'True', 'subject': 'Computer Studies / ICT', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'Basics', 'type': 'True/False', 'passage': ''},
    {'q': 'The full meaning of RAM is ______', 'options': [], 'answer': 'Random Access Memory', 'subject': 'Computer Studies / ICT', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'Memory', 'type': 'Fill-in-blank', 'passage': ''},
    {'q': 'Explain in your own words what a computer is and list 3 uses.', 'options': [], 'answer': 'Teacher to mark', 'subject': 'Computer Studies / ICT', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'Theory', 'type': 'Theory/Essay', 'passage': ''},
    {'q': 'What is 2 + 2?', 'options': ['3','4','5','6'], 'answer': '4', 'subject': 'Mathematics', 'class': 'JSS 1', 'term': 'First Term', 'topic': 'Addition', 'type': 'Objective', 'passage': ''},
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

st.markdown('<div class="jamb-header"><h1>EBUNTAYO SECONDARY SCHOOL</h1><p>FIRST TERM CBT EXAMINATION | GABRIEL CBT PRO</p></div>', unsafe_allow_html=True)

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

st.markdown('<p class="select-role">SELECT ROLE</p>', unsafe_allow_html=True)
role = st.radio('SELECT ROLE', ['STUDENT - WRITE EXAM', 'TEACHER - SET QUESTIONS', 'ADMIN - MONITOR & RESULTS'], horizontal=True, label_visibility='collapsed')

if role.startswith('TEACHER'):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="login-title">TEACHER LOGIN</p>', unsafe_allow_html=True)
    st.markdown('<p class="field-label">TEACHER PASSWORD</p>', unsafe_allow_html=True)
    tp = st.text_input('TEACHER PASSWORD', type='password', label_visibility='collapsed')
    if tp == TEACHER_PASS:
        st.success('Welcome Teacher!')
        st.markdown('<p class="field-label">QUESTION TYPE</p>', unsafe_allow_html=True)
        q_type = st.selectbox('QUESTION TYPE', ['Objective','True/False','Fill-in-blank','Theory/Essay'], label_visibility='collapsed')
        st.markdown('<p class="field-label">SUBJECT</p>', unsafe_allow_html=True)
        tq_subj = st.selectbox('SUBJECT', ALL_SUBJECTS, key='t_subj', label_visibility='collapsed')
        st.markdown('<p class="field-label">CLASS</p>', unsafe_allow_html=True)
        tq_class = st.selectbox('CLASS', ALL_CLASSES, key='t_class', label_visibility='collapsed')
        st.markdown('<p class="field-label">TERM</p>', unsafe_allow_html=True)
        tq_term = st.selectbox('TERM', ['First Term','Second Term','Third Term'], key='t_term', label_visibility='collapsed')
        st.markdown('<p class="field-label">TOPIC</p>', unsafe_allow_html=True)
        tq_topic = st.text_input('TOPIC', label_visibility='collapsed')
        st.markdown('<p class="field-label">PASSAGE (OPTIONAL)</p>', unsafe_allow_html=True)
        tq_passage = st.text_area('PASSAGE', label_visibility='collapsed')
        st.markdown('<p class="field-label">QUESTION</p>', unsafe_allow_html=True)
        tq_q = st.text_area('QUESTION', label_visibility='collapsed')
        if q_type == 'Objective':
            st.markdown('<p class="field-label">OPTION A</p>', unsafe_allow_html=True)
            o1 = st.text_input('OPTION A', label_visibility='collapsed')
            st.markdown('<p class="field-label">OPTION B</p>', unsafe_allow_html=True)
            o2 = st.text_input('OPTION B', label_visibility='collapsed')
            st.markdown('<p class="field-label">OPTION C</p>', unsafe_allow_html=True)
            o3 = st.text_input('OPTION C', label_visibility='collapsed')
            st.markdown('<p class="field-label">OPTION D</p>', unsafe_allow_html=True)
            o4 = st.text_input('OPTION D', label_visibility='collapsed')
            st.markdown('<p class="field-label">CORRECT ANSWER</p>', unsafe_allow_html=True)
            corr = st.selectbox('CORRECT', ['Option A','Option B','Option C','Option D'], label_visibility='collapsed')
            if st.button('Add Objective'):
                opts = [o1,o2,o3,o4]
                ans = opts[['Option A','Option B','Option C','Option D'].index(corr)]
                if tq_q and all(opts):
                    st.session_state.questions.append({'q': tq_q, 'options': opts, 'answer': ans, 'subject': tq_subj, 'class': tq_class, 'term': tq_term, 'topic': tq_topic, 'type': 'Objective', 'passage': tq_passage})
                    st.success('Added!')
        elif q_type == 'True/False':
            st.markdown('<p class="field-label">CORRECT ANSWER</p>', unsafe_allow_html=True)
            corr2 = st.selectbox('CORRECT', ['True','False'], label_visibility='collapsed')
            if st.button('Add True/False'):
                if tq_q:
                    st.session_state.questions.append({'q': tq_q, 'options': ['True','False'], 'answer': corr2, 'subject': tq_subj, 'class': tq_class, 'term': tq_term, 'topic': tq_topic, 'type': 'True/False', 'passage': tq_passage})
                    st.success('Added!')
        elif q_type == 'Fill-in-blank':
            st.markdown('<p class="field-label">CORRECT ANSWER</p>', unsafe_allow_html=True)
            ans_fill = st.text_input('CORRECT ANSWER', label_visibility='collapsed')
            if st.button('Add Fill-in-blank'):
                if tq_q:
                    st.session_state.questions.append({'q': tq_q, 'options': [], 'answer': ans_fill, 'subject': tq_subj, 'class': tq_class, 'term': tq_term, 'topic': tq_topic, 'type': 'Fill-in-blank', 'passage': tq_passage})
                    st.success('Added!')
        else:
            if st.button('Add Theory'):
                if tq_q:
                    st.session_state.questions.append({'q': tq_q, 'options': [], 'answer': 'Teacher to mark', 'subject': tq_subj, 'class': tq_class, 'term': tq_term, 'topic': tq_topic, 'type': 'Theory/Essay', 'passage': tq_passage})
                    st.success('Added!')
        st.markdown('---')
        st.subheader('Bulk Upload CSV')
        st.info('Columns: question,optionA,optionB,optionC,optionD,answer,subject,class,term,topic,type')
        up = st.file_uploader('Upload CSV', type=['csv'])
        if up is not None:
            try:
                df_up = pd.read_csv(up)
                for _, r in df_up.iterrows():
                    opts = [str(r.get('optionA','')), str(r.get('optionB','')), str(r.get('optionC','')), str(r.get('optionD',''))]
                    opts = [o for o in opts if o and o != 'nan']
                    st.session_state.questions.append({'q': str(r.get('question','')), 'options': opts, 'answer': str(r.get('answer','')), 'subject': str(r.get('subject','Mathematics')), 'class': str(r.get('class','JSS 1')), 'term': str(r.get('term','First Term')), 'topic': str(r.get('topic','')), 'type': str(r.get('type','Objective')), 'passage': ''})
                st.success('Uploaded!')
            except Exception as e:
                st.error(str(e))
        st.markdown('---')
        st.subheader('Question Bank')
        st.write('Total: ' + str(len(st.session_state.questions)))
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
        st.subheader('Session Recovery')
        st.markdown('<p class="field-label">ADD EXTRA TIME</p>', unsafe_allow_html=True)
        extra = st.selectbox('ADD EXTRA TIME', ['+5 Minutes','+10 Minutes','+15 Minutes','+30 Minutes'], label_visibility='collapsed')
        if st.button('Add Extra Time'):
            if st.session_state.start_time:
                st.session_state.start_time += timedelta(minutes=int(extra.split()[0].replace('+','')))
                st.success('Added!')
            else:
                st.info('No active exam')
        if st.button('Reset Frozen Session'):
            st.session_state.exam_started = False
            st.success('Reset Done')
        if st.session_state.results:
            df = pd.DataFrame(st.session_state.results)
            st.markdown('---')
            st.subheader('ADMIN REVIEW')
            st.dataframe(df)
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button('Download Results CSV', csv, 'ebuntayo_results.csv', 'text/csv')
            show_pie_chart(int(df['score'].sum()), int(df['total'].sum())-int(df['score'].sum()), 'Overall Performance')
            df['label'] = df.apply(lambda r: str(r['name']) + ' - ' + str(r['subject']) + ' - ' + str(r['class']), axis=1)
            st.markdown('<p class="field-label">SELECT STUDENT TO REVIEW</p>', unsafe_allow_html=True)
            sel = st.selectbox('SELECT STUDENT', df['label'].tolist(), label_visibility='collapsed')
            srow = df[df['label']==sel].iloc[0]
            sc = int(srow['score']); tt = int(srow['total'])
            st.markdown('<div class="student-card"><p class="student-name">' + str(srow['name']) + '</p><p class="student-detail">' + str(srow['subject']) + ' | ' + str(srow['class']) + ' | ' + str(sc) + '/' + str(tt) + '</p></div>', unsafe_allow_html=True)
            show_pie_chart(sc, tt-sc, str(srow['subject']) + ' Performance', student_name=str(srow['name']) + ' Performance')
            st.subheader('All Students - Each With Own Pie Chart')
            for _, row in df.iterrows():
                s = int(row['score']); t = int(row['total'])
                st.markdown('<div class="student-card"><p class="student-name">' + str(row['name']) + '</p><p class="student-detail">' + str(row['subject']) + ' | ' + str(row['class']) + ' | ' + str(s) + '/' + str(t) + '</p></div>', unsafe_allow_html=True)
                show_pie_chart(s, t-s, str(row['subject']), student_name=str(row['name']))
        else:
            st.info('No results yet.')
        st.write('Student PIN: ' + EXAM_PIN)
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
        st.markdown('<p class="field-label">FULL NAME *</p>', unsafe_allow_html=True)
        name = st.text_input('FULL NAME', placeholder='Enter your full name', key='s_name', label_visibility='collapsed')
        st.markdown('<p class="field-label">EXAM PIN *</p>', unsafe_allow_html=True)
        pin = st.text_input('EXAM PIN', type='password', placeholder='Ask teacher for PIN', key='s_pin', label_visibility='collapsed')
        st.markdown('<p class="field-label">SELECT SUBJECT</p>', unsafe_allow_html=True)
        subject = st.selectbox('SELECT SUBJECT', ALL_SUBJECTS, key='s_subj', label_visibility='collapsed')
        st.markdown('<p class="field-label">SELECT CLASS</p>', unsafe_allow_html=True)
        class_ = st.selectbox('SELECT CLASS', ALL_CLASSES, key='s_class', label_visibility='collapsed')
        st.markdown('<p class="field-label">SELECT TERM</p>', unsafe_allow_html=True)
        term = st.selectbox('SELECT TERM', ['First Term','Second Term','Third Term'], key='s_term', label_visibility='collapsed')
        st.markdown('<p class="field-label">EXAM TYPE</p>', unsafe_allow_html=True)
        exam_type = st.selectbox('EXAM TYPE', ['First Term Exam','Second Term Exam','Third Term Exam','Mock Exam','Promotion Exam','Test / Quiz'], key='s_type', label_visibility='collapsed')
        st.markdown('<p class="field-label">SELECT TIME</p>', unsafe_allow_html=True)
        exam_time = st.selectbox('SELECT TIME', ['10 Minutes','20 Minutes','30 Minutes','1 Hour'], key='s_time', label_visibility='collapsed')
        agree = st.checkbox('I have read instructions - Do NOT switch tab')
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
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<p class="login-title">PROFILE CHECK</p>', unsafe_allow_html=True)
        st.markdown('<p style="text-align:center;color:#0B2C4A;font-weight:800;">Student: ' + str(info['name']) + '<br>Class: ' + str(info['class']) + ' | Subject: ' + str(info['subject']) + '<br>Total Questions: ' + str(len(filt)) + ' | Time: ' + str(info['mins']) + ' Mins</p>', unsafe_allow_html=True)
        if st.button('CONFIRM & START EXAM'):
            shuffled = filt.copy()
            random.shuffle(shuffled)
            for qq in shuffled:
                if qq.get('options') and len(qq['options'])>2:
                    opts = qq['options'].copy(); random.shuffle(opts); qq['options'] = opts
            st.session_state.shuffled_q = shuffled
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
        subj_cols = st.columns(4)
        for i, subj in enumerate(['Mathematics','English Language','Physics','Chemistry']):
            is_active = (subj == info['subject'])
            label = subj + ' (Active)' if is_active else subj
            if subj_cols[i].button(label, key='subj_' + subj):
                new_filt = [q for q in st.session_state.questions if q.get('subject')==subj]
                if new_filt:
                    st.session_state.student_info['subject'] = subj
                    st.session_state.shuffled_q = new_filt
                    st.session_state.current_q = 0
                    st.rerun()
        with st.expander('Calculator - Click to Open'):
            c1,c2,c3 = st.columns(3)
            n1 = c1.number_input('First', value=0.0, key='calc1')
            op = c2.selectbox('Op', ['+','-','x','/'], key='calc_op')
            n2 = c3.number_input('Second', value=0.0, key='calc2')
            if op == '+': res = n1+n2
            elif op == '-': res = n1-n2
            elif op == 'x': res = n1*n2
            else: res = n1/n2 if n2 != 0 else 0
            st.success('Answer: ' + str(res))
        if total_sec <= 0:
            filt = st.session_state.shuffled_q
            score = 0; theory_txt = ''
            for i, qq in enumerate(filt):
                if qq.get('type')=='Theory/Essay': theory_txt += str(st.session_state.answers_dict.get(i,'')) + ' | '
                elif qq.get('type')=='Fill-in-blank':
                    if str(st.session_state.answers_dict.get(i,'')).strip().lower()==str(qq['answer']).strip().lower(): score += 1
                else:
                    if st.session_state.answers_dict.get(i)==qq['answer']: score += 1
            st.session_state.results.append({'name': info['name'], 'exam_no': '', 'class': info['class'], 'subject': info['subject'], 'term': info['term'], 'exam_type': info.get('exam_type',''), 'score': score, 'total': len(filt), 'school': SCHOOL_NAME, 'date': datetime.now().strftime('%Y-%m-%d %H:%M'), 'theory': theory_txt})
            st.session_state.active_students = [a for a in st.session_state.active_students if a['name']!=info['name']]
            st.session_state.exam_started = False; st.session_state.profile_ok = False; st.session_state.submitted_msg = True; st.rerun()
        else:
            st.markdown('<div style="background:#FF0000;color:white;text-align:center;padding:8px;font-weight:900;font-size:20px;border:2px solid #0B2C4A;border-top:none;">TIME: ' + str(total_sec//60).zfill(2) + ':' + str(total_sec%60).zfill(2) + '</div>', unsafe_allow_html=True)
        filtered = st.session_state.shuffled_q
        total_q = len(filtered)
        left, right = st.columns([3, 1])
        with left:
            q = filtered[st.session_state.current_q]
            st.markdown('<div style="background:white;border:2px solid #0B2C4A;border-top:none;padding:20px;min-height:300px;"><p style="color:#0B2C4A;font-weight:900;font-size:16px;">Question ' + str(st.session_state.current_q+1) + ' of ' + str(total_q) + '</p><p style="color:#0B2C4A;font-weight:800;font-size:21px;">' + str(q['q']) + '</p></div>', unsafe_allow_html=True)
            prev = st.session_state.answers_dict.get(st.session_state.current_q, None)
            if q.get('type') in ['Objective','True/False']:
                opts = q['options']; letters = ['A.','B.','C.','D.']
                opts_letter = [letters[i] + '  ' + opts[i] for i in range(len(opts))]
                d_idx = None
                if prev:
                    try: d_idx = opts.index(prev)
                    except: d_idx = None
                choice = st.radio('Select:', opts_letter, index=d_idx, key='radio_' + str(st.session_state.current_q), label_visibility='collapsed')
                if choice: st.session_state.answers_dict[st.session_state.current_q] = opts[letters.index(choice[:2])]
            elif q.get('type')=='Fill-in-blank':
                ans_fill = st.text_input('Type answer:', value=str(prev) if prev else '', key='fill_' + str(st.session_state.current_q))
                if ans_fill: st.session_state.answers_dict[st.session_state.current_q] = ans_fill
            else:
                if q.get('passage'): st.info('Passage: ' + str(q['passage']))
                ans_theory = st.text_area('Write answer:', value=str(prev) if prev else '', key='theory_' + str(st.session_state.current_q), height=120)
                if ans_theory: st.session_state.answers_dict[st.session_state.current_q] = ans_theory
            if st.button('FLAG QUESTION' if st.session_state.current_q not in st.session_state.flagged else 'UNFLAG QUESTION'):
                if st.session_state.current_q in st.session_state.flagged: st.session_state.flagged.remove(st.session_state.current_q)
                else: st.session_state.flagged.add(st.session_state.current_q)
                st.rerun()
        with right:
            st.markdown('<div style="background:#F8F9FA;border:2px solid #0B2C4A;border-top:none;padding:12px;min-height:300px;"><p style="text-align:center;font-weight:900;color:#0B2C4A;">QUESTION PALETTE</p></div>', unsafe_allow_html=True)
            for row_start in range(0, total_q, 5):
                pcols = st.columns(5)
                for j in range(5):
                    idx = row_start + j
                    if idx < total_q:
                        if idx in st.session_state.flagged: lab = 'FLAG ' + str(idx+1)
                        elif idx in st.session_state.answers_dict and st.session_state.answers_dict[idx] not in [None,'']: lab = 'DONE ' + str(idx+1)
                        else: lab = str(idx+1)
                        if idx == st.session_state.current_q: lab = '[' + str(idx+1) + '*]'
                        if pcols[j].button(lab, key='pal_' + str(idx)): st.session_state.current_q = idx; st.rerun()
            st.markdown('<div style="background:#F8F9FA;border:2px solid #0B2C4A;padding:10px;color:#0B2C4A;font-weight:700;font-size:13px;">LEGEND:<br>Answered = DONE<br>Unanswered = Number<br>Flagged = FLAG<br><br>Answered: ' + str(len([v for v in st.session_state.answers_dict.values() if v not in [None,'']])) + ' / ' + str(total_q) + '<br>Flagged: ' + str(len(st.session_state.flagged)) + '</div>', unsafe_allow_html=True)
        b1,b2,b3,b4 = st.columns(4)
        with b1:
            if st.button('< Previous'):
                if st.session_state.current_q>0: st.session_state.current_q -= 1; st.rerun()
        with b2:
            if st.button('Clear Selection'):
                if st.session_state.current_q in st.session_state.answers_dict: del st.session_state.answers_dict[st.session_state.current_q]
                st.rerun()
        with b3:
            if st.button('Next >'):
                if st.session_state.current_q<total_q-1: st.session_state.current_q += 1; st.rerun()
        with b4:
            if st.button('SUBMIT EXAM'):
                score = 0; theory_txt = ''
                for i, qq in enumerate(filtered):
                    if qq.get('type')=='Theory/Essay': theory_txt += str(st.session_state.answers_dict.get(i,'')) + ' | '
                    elif qq.get('type')=='Fill-in-blank':
                        if str(st.session_state.answers_dict.get(i,'')).strip().lower()==str(qq['answer']).strip().lower(): score += 1
                    else:
                        if st.session_state.answers_dict.get(i)==qq['answer']: score += 1
                st.session_state.results.append({'name': info['name'], 'exam_no': '', 'class': info['class'], 'subject': info['subject'], 'term': info['term'], 'exam_type': info.get('exam_type',''), 'score': score, 'total': len(filtered), 'school': SCHOOL_NAME, 'date': datetime.now().strftime('%Y-%m-%d %H:%M'), 'theory': theory_txt})
                st.session_state.active_students = [a for a in st.session_state.active_students if a['name']!=info['name']]
                st.session_state.exam_started = False; st.session_state.profile_ok = False; st.session_state.submitted_msg = True; st.session_state.current_q = 0; st.session_state.answers_dict = {}; st.session_state.flagged = set(); st.rerun()

st.markdown('<div class="footer">EBUNTAYO SECONDARY SCHOOL | GABRIEL CBT PRO<br>BUILT BY <span>ACHONWA GABRIEL</span> | Admin: admin123 | Teacher: teacher123 | PIN: EBS2026</div>', unsafe_allow_html=True)
