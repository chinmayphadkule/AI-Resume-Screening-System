import streamlit as st
from src.pdf_extractor import extract_text_from_pdf
from src.preprocess import preprocess
from src.matcher import get_match_score

st.title("AI Resume Screening System")

resume_file = st.file_uploader("Upload Resume (PDF)")
job_desc = st.text_area("Paste Job Description")

if st.button("Calculate Match Score"):
    if resume_file and job_desc:
        resume_text = extract_text_from_pdf(resume_file)
        resume_clean = preprocess(resume_text)
        jd_clean = preprocess(job_desc)

        score = get_match_score(resume_clean, jd_clean)

        st.success(f"Match Score: {round(score*100,2)}%")

        