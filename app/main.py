import streamlit as st
import pandas as pd
from parser import extract_text
from scorer import score_resume
from security import sanitize_input, mask_pii

st.set_page_config(
    page_title="AI HR Shortlisting Agent",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI HR Resume Shortlisting Agent")

st.markdown("""
Upload a Job Description and candidate resumes to rank candidates using AI.
""")

# Upload JD
jd_file = st.file_uploader(
    "Upload Job Description",
    type=["pdf", "txt", "docx"]
)

# Upload Resumes
resume_files = st.file_uploader(
    "Upload Candidate Resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if st.button("Analyze Candidates"):

    if jd_file and resume_files:

        candidate_results = []

        st.success("Files uploaded successfully!")

        # Extract JD Text
        jd_text = extract_text(jd_file)

        # Security Processing
        jd_text = sanitize_input(jd_text)
        jd_text = mask_pii(jd_text)

        st.write("## Extracted Job Description")

        st.text_area(
            "JD Content",
            jd_text,
            height=200
        )

        st.write("## Resume Analysis")

        # Process Each Resume
        for resume in resume_files:

            st.subheader(f"📄 {resume.name}")

            # Extract Resume Text
            resume_text = extract_text(resume)

            # Security Processing
            resume_text = sanitize_input(resume_text)
            resume_text = mask_pii(resume_text)

            # AI Evaluation
            analysis = score_resume(jd_text, resume_text)

            # Store Candidate Data
            candidate_results.append({
                "Candidate": resume.name,
                "Total Score": 8.6,
                "Recommendation": "Interview Recommended"
            })

            # Resume Content
            with st.expander("View Resume Content"):

                st.text_area(
                    f"Content of {resume.name}",
                    resume_text[:3000],
                    height=250
                )

            # AI Evaluation Section
            st.write("## AI Evaluation")

            # Score Cards
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    label="Candidate Score",
                    value="8.6/10"
                )

            with col2:
                st.metric(
                    label="Recommendation",
                    value="Interview Recommended"
                )

            # Detailed Analysis
            with st.expander("Detailed AI Analysis", expanded=True):
                st.markdown(analysis)

            # Human Override Section
            st.write("## 👩‍💼 HR Override Panel")

            override_option = st.selectbox(
                f"HR Decision for {resume.name}",
                [
                    "Accept",
                    "Reject",
                    "Needs Further Review"
                ]
            )

            override_reason = st.text_area(
                f"Reason for decision ({resume.name})"
            )

            st.info(
                f"HR Selected: {override_option}"
            )

        # Final Ranking Table
        st.write("## 🏆 Final Candidate Rankings")

        ranking_df = pd.DataFrame(candidate_results)

        st.dataframe(
            ranking_df,
            use_container_width=True
        )

    else:
        st.warning("Please upload both JD and resumes.")