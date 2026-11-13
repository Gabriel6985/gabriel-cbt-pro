import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

st.set_page_config(page_title="EBUNTAYO SECONDARY SCHOOL - CBT", page_icon="🎓", layout="wide")
SCHOOL_NAME = "EBUNTAYO SECONDARY SCHOOL"
ADMIN_PASS = "admin123"
TEACHER_PASS = "teacher123"
EXAM_PIN = "EBS2026"

st.markdown("""
<style>
    .stApp { background-color: #F2F2F2 !important; }
    /* ===== JAMB HEADER LIKE YOUR PHOTO ===== */
    .jamb-header { background-color: #0B2C4A; color: white; padding: 12px 16px; border-radius: 8px 8px 0 0; border: 2px solid #0B2C4A; }
    .jamb-header h1 { color: white !important; font-size: 24px !important; font-weight: 900 !important; margin: 0; text-align: center; font-family: 'Arial Black', sans-serif; text-transform: uppercase; }
    .jamb-header p { color: #FFD700 !important; text-align: center; font-size: 13px; font-weight: 800; margin: 2px 0 0 0; letter-spacing: 2px; }
    .student-bar { background-color: #FFFFFF; border: 2px solid #0B2C4A; border-top: none; padding: 10px 14px; display: flex; justify-content: space-between; flex-wrap: wrap; color: #0B2C4A !important; font-weight: 800; font-size: 14px; }
    .student-bar span { color: #0B2C4A !important; }
    .timer-jamb { background-color: #FF0000; color: white !important; padding: 6px 14px; border-radius: 6px; font-weight: 900; font-size: 18px; }
    .subject-bar { background-color: #D9E2F3; border: 2px solid #0B2C4A; border-top: none; padding: 10px; display: flex; gap: 8px; flex-wrap: wrap; }
    .subject-active { background-color: #0B2C4A !important; color: white !important; padding: 8px 16px; border-radius: 6px; font-weight: 900; }
    .subject-inactive { background-color: white; color: #0B2C4A !important; padding: 8px 16px; border-radius: 6px; font-weight: 700; border: 1px solid #0B2C4A; }
    /* QUESTION + PALETTE SIDE BY SIDE */
    .exam-box { background-color: white; border: 2px solid #0B2C4A; border-top: none; padding: 0; }
    .q-left { padding: 20px; }
    .q-left p { color: #0B2C4A !important; font-size: 21px !important; font-weight: 800 !important; line-height: 1.5; }
    .palette-box { background-color: #F8F9FA; border-left: 2px solid #0B2C4A; padding: 16px; min-height: 420px; }
    .palette-title { color: #0B2C4A !important; font-weight: 900; font-size: 16px; text-align: center; border-bottom: 2px solid #0B2C4A; padding-bottom: 8px; }
    .legend { color: #0B2C4A !important; font-weight: 700; font-size: 13px; margin-top: 12px; }
    .legend span { font-size: 14px; }
    .card { background-color: #FFFFFF !important; padding: 22px; border-radius: 12px; margin-top: 14px; border-top: 6px solid #FFD700; box-shadow: 0 3px 10px rgba(0,0,0,0.15); }
    .login-title { color: #0B2C4A !important; font-size: 26px !important; font-weight: 900 !important; text-align: center; text-transform: uppercase; font-family: 'Arial Black', sans-serif; margin:0; }
    label { font-weight: 800 !important; color: #0B2C4A !important; }
    input, textarea, select { background-color: #fff !important; color: #000 !important; border: 2.5px solid #0B2C4A !important; border-radius: 8px !important; font-weight: 700 !important; }
    div[data-baseweb="select"] > div { background-color: white !important; color: black !important; border: 2.5px solid #0B2C4A !important; }
    .stButton>button { background-color: #0A9D58 !important; color: white !important; font-weight: 900 !important; border-radius: 8px; padding: 10px; width: 100%; text-transform: uppercase; }
    .footer { text-align: center; margin-top: 20px; padding: 14px; background-color: #0B2C4A; border-radius: 8px; color: white !important; font-weight: 700; }
    .footer span { color: #FFD700 !important; }
    /* BIG OPTIONS LIKE PHOTO */
    div[data-testid="stRadio"] label { color: #000 !important; font-size: 21px !important; font-weight: 800 !important; background: #fff !important; padding: 14px 12px !important; border: 2px solid #ddd !important; border-radius: 8px !important; margin-bottom: 10px !important; width: 100% !important; display: flex !important; align-items: center !important; }
    div[data-testid="stRadio"] p { color: #000 !important; font-weight: 800 !important; font-size: 21px !important; }
    div[data-testid="stRadio"] > label { border: none !important; } div[data-testid="stRadio"] > label p { color: #0B2C4A !important; font-size: 16px !important; }
    div[data-testid="stRadio"] input[type="radio"] { transform: scale(1.6); margin-right: 10px !important; }
    .success-box { background-color: #0A9D58; color: white !important; padding: 18px; border-radius: 12px; text-align: center; font-size: 20px; font-weight: 900; margin-top: 14px; } .success-box p { color: white !important; }
    .student-card { background-color: #fff !important; padding: 16px; border-radius: 10px; margin-top: 10px; border: 2px solid #0B2C4A; }
    .student-name { color: #0B2C4A !important; font-size: 20px !important; font-weight: 900 !important; text-align: center;
