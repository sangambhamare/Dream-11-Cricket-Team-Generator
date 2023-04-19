import streamlit as st
import openai
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from io import BytesIO

openai.api_key = "YOUR_API_KEY"

def generate_text(prompt):
    response = openai.Completion.create(
      engine="davinci",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.5,
    )

    return response.choices[0].text

def create_report(project_name):
    doc = SimpleDocTemplate(f"{project_name}.pdf", pagesize=letter)
    styles = getSampleStyleSheet()

    intro = generate_text(f"Introduction for {project_name}")
    lit_review = generate_text(f"Literature Review for {project_name}")
    methodology = generate_text(f"Methodology for {project_name}")
    results = generate_text(f"Results for {project_name}")
    discussion = generate_text(f"Discussion for {project_name}")
    conclusion = generate_text(f"Conclusion for {project_name}")
    references = generate_text(f"References for {project_name}")
    acknowledgement = generate_text(f"Acknowledgement for {project_name}")
    appendix = generate_text(f"Appendix for {project_name}")

    elements = []
    elements.append(Paragraph(intro, styles["Normal"]))
    elements.append(Paragraph(lit_review, styles["Normal"]))
    elements.append(Paragraph(methodology, styles["Normal"]))
    elements.append(Paragraph(results, styles["Normal"]))
    elements.append(Paragraph(discussion, styles["Normal"]))
    elements.append(Paragraph(conclusion, styles["Normal"]))
    elements.append(Paragraph(references, styles["Normal"]))
    elements.append(Paragraph(acknowledgement, styles["Normal"]))
    elements.append(Paragraph(appendix, styles["Normal"]))

    doc.build(elements)

    return f"{project_name}.pdf"

st.title("Mini Project Report Generator")

project_name = st.text_input("Enter the project name")
if project_name:
    st.write("Generating report...")
    report_filename = create_report(project_name)
    with open(report_filename, "rb") as f:
        pdf_data = f.read()
    st.write("Report generated!")
    st.download_button("Download Report", data=pdf_data, file_name=report_filename)
