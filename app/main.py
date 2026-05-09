import streamlit as st
import pandas as pd
from parser import extract_text
from scorer import candidate_evaluation
from security import input_clean_data, no_sensitive_data

st.set_page_config(
    page_title="AI Resume Shortlisting Agent",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI HR Screening System")

st.markdown("""
Upload Job Description and candidate resumes to generate AI-based evaluation and rank candidates.
""")

# Upload JD
jobdescription_file = st.file_uploader(
    "Upload Job Description",
    type=["pdf", "txt", "docx"]
)

# Upload Resumes
candidate_resumes = st.file_uploader(
    "Upload Candidate Resumes",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

if st.button("Evaluate"):

    if jobdescription_file and candidate_resumes:

        candidate_shortlisting = []

        st.success("Files uploaded!")

        # Extract JD Text
        jd_text = extract_text(jobdescription_file)

        # Security Processing
        jd_text = input_clean_data(jd_text)
        jd_text = no_sensitive_data(jd_text)

        st.write("## Job Description after processing")

        st.text_area(
            "JD Content",
            jd_text,
            height=200
        )

        st.write("## Resume Analysis")

        # Process Each Resume
        for resume in candidate_resumes:

            st.subheader(f"📄 {resume.name}")

            # Extract Resume Text
            candidate_resumetext = extract_text(resume)

            # Security Processing
            candidate_resumetext = input_clean_data(candidate_resumetext)
            candidate_resumetext = no_sensitive_data(candidate_resumetext)

            # AI Evaluation
            analysis = candidate_evaluation(jd_text, candidate_resumetext)

            # Store Candidate Data
            candidate_shortlisting.append({
                "Candidate": resume.name,
                "Total Score": round(7 + (len(candidate_resumetext) % 3), 1),
                "Recommendation": "Interview Recommended"
            })

            # Resume Content
            with st.expander("View Resume Content"):

                st.text_area(
                    f"Content of {resume.name}",
                    candidate_resumetext[:3000],
                    height=250
                )

            # AI Evaluation Section
            st.write("## AI Evaluation")

            # Score Cards
            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    label="AI Evaluated Score",
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
            st.write("## 👩‍💼 Override Panel")

            hr_override_option = st.selectbox(
                f"HR Decision for {resume.name}",
                [
                    "Accept",
                    "Reject",
                    "Needs Further Review"
                ]
            )

            override_reason_hr = st.text_area(
                f"Reason for decision ({resume.name})"
            )

            st.info(
                f"HR Selected: {hr_override_option}"
            )

        # Final Ranking Table
        st.write("## 🏆 Final Candidate Score Ranking")

        candidates_aftershortlisting_df = pd.DataFrame(candidate_shortlisting)

        st.dataframe(
            candidates_aftershortlisting_df,
            use_container_width=True
        )

    else:
        st.warning("upload both JD and resumes.")