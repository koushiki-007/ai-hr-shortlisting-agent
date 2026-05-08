# AI HR Resume Shortlisting Agent

## Overview of the project

It is an AI-powered HR Resume Shortlisting system that I have built using Python, Streamlit, and Gemini AI API key.

This project helps to simplify the screening process of a resume for HR teams. The system compares the uploaded resume with job description and generate AI-based candidate evaluations for the candidate, instead of manually doing the process.

The system:
- extracts text from candidate resumes
- analyze profiles for each resume
- generatea score based on the outcome
- ranks the candidates according to score
- allow HR make their decision override

In the project I have also tried to add some security features like PII masking and input sanitization because handling security measures is an important part of the entire process

---

# Features

## Core Features

- HR uploads a job description
- Next resume upload and parsing 
- Evaluation of the resumes by AI
- Candidates are given a rank table
- HR Override
- Resume content viewer also added
- Sanitization of the input
- PII Masking

---

# Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| LLM | Gemini 2.5 Flash |
| AI SDK | Google Generative AI |
| Resume Parsing | PyPDF + python-docx |
| Data Processing | Pandas |
| Security | Regex-based sanitization |

---

# Project Workflow

1. HR uploads Job Description and candidate resume
2. Resume text parsed and extracted
3. Sanitization of input applied
4. AI-based evaluation of resumes
5. Scores for the candidates and recommendation generated
6. HR override part starts
7. Final candidate ranks displayed in table

---

# Project Architecture

```text
Job Description + Resumes
            ↓
Document Parser
            ↓
Security Layer
(Input Sanitization + PII Masking)
            ↓
Gemini AI Evaluation
            ↓
Candidate Scoring
            ↓
HR Override Panel
            ↓
Final Ranking Table
```

---

# Installation Steps

## Clone Repository

```bash
git clone <repository-link>
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
GOOGLE_API_KEY=your_api_key_here
```

---

# Run Project

```bash
streamlit run app/main.py
```

---

# Security Mitigations

## Prompt Injection Protection
- If any suspiscious intruction present, those are filtered from uploaded text.
- Input santizations happens before AI-based evaluation 

## PII Protection
- Emails and phone numbers masked for safety 

## API Key Security
- API key stored in `.env` and added to `.gitignore` for safety

## Human-in-the-Loop Safety
- Final decisions made by HR, not entirely dependent on AI

---

# LLM & Framework Choice

## LLM Used
Gemini 2.5 Flash

### Why Gemini?
- Faster response, reasoning capability, easy integration, works best for text evaluation tasks

## Framework Used
Streamlit + Google Generative AI SDK

### Why Streamlit?
- Easy UI development, better interaction

---

# Challenges Faced

- Resume file formats can be different, and handling all of the files is a task
- Gemini Key model compatibility issue during integration
- Evaluation output structuring issue
- Implementation of security measures

---

# Future Improvements

- Dynamic score extraction
- Embedding-based using similarty
- Vector database implementation
- Export the pdf report
- System authentication

---

# Author

Koushiki Das  
B.Tech CSE (AI & ML)