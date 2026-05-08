from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(pdf_file):
    text = ""

    pdf_reader = PdfReader(pdf_file)

    for page in pdf_reader.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted + "\n"

    return text


def extract_text_from_docx(docx_file):
    doc = Document(docx_file)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text


def extract_text(uploaded_file):

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)

    elif file_name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)

    elif file_name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    else:
        return ""