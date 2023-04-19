import streamlit as st
import openai
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.enums import TA_JUSTIFY

# Set up the OpenAI API client
openai.api_key = st.secrets["openai_api_key"]

# Set up Streamlit app
st.title("Mini Project Report Generator")
project_name = st.text_input("Enter a project name:")

# Generate report using OpenAI API
if st.button("Generate Report"):
    prompt = f"Generate a mini project report for the project {project_name} with the following sections: Introduction, Literature Review, Methodology, Results, Discussion, Conclusion, References, Acknowledgements, and Appendix."
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      temperature=0.5,
      max_tokens=2048,
      n=1,
      stop=None,
      timeout=10,
    )
    report_text = response.choices[0].text

    # Create PDF file using reportlab
    doc = SimpleDocTemplate("mini_project_report.pdf", pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    report = []
    for line in report_text.split('\n'):
        report.append(Paragraph(line, styles["Justify"]))
        report.append(Spacer(1, 12))
    doc.build(report)

    # Create download button
    with open("mini_project_report.pdf", "rb") as f:
        bytes_data = f.read()
        st.download_button(
            label="Download Report",
            data=bytes_data,
            file_name="mini_project_report.pdf",
            mime="application/pdf",
        )
