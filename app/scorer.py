import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load model
model = genai.GenerativeModel("models/gemini-2.5-flash")


def score_resume(jd_text, resume_text):

    prompt = f"""
    You are an AI HR Recruiter.

    Compare the following resume with the job description.

    JOB DESCRIPTION:
    {jd_text}

    RESUME:
    {resume_text}

    Evaluate the candidate on:

    1. Skills Match (out of 10)
    2. Experience Relevance (out of 10)
    3. Education & Certifications (out of 10)
    4. Projects & Portfolio (out of 10)
    5. Communication Quality (out of 10)

    Also provide:
    - Total Score out of 10
    - Strengths
    - Weaknesses
    - Final Recommendation

    Format the output professionally.
    """

    response = model.generate_content(prompt)

    return response.text