import streamlit as st
import openai
import weasyprint

openai.api_key = "YOUR_API_KEY_HERE"

st.title("Mini Project Creator")

project_name = st.text_input("Enter the name of your project:")

if st.button("Create Mini Project Report"):
    st.write("Generating mini project report...")

    intro = f"Introduction:\n\nThis project aims to {project_name}."
    lit_review = "Literature Review:\n\nWe conducted a thorough review of the existing literature in this field and found that..."
    methodology = "Methodology:\n\nTo achieve our objectives, we used the following methodology..."
    results = "Results:\n\nOur analysis revealed that..."
    discussion = "Discussion:\n\nWe interpret our findings as follows..."
    conclusion = "Conclusion:\n\nIn conclusion, our project provides valuable insights into..."
    references = "References:\n\n1. Author 1, et al. (Year). Title. Journal.\n2. Author 2, et al. (Year). Title. Journal."
    acknowledgement = "Acknowledgement:\n\nWe would like to express our gratitude to..."

    report = intro + "\n\n" + lit_review + "\n\n" + methodology + "\n\n" + results + "\n\n" + discussion + "\n\n" + conclusion + "\n\n" + references + "\n\n" + acknowledgement

    try:
        generated_text = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Generate a mini project report for a project titled '{project_name}' using the following structure:\n\n{report}",
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        ).choices[0].text

        st.write("Mini project report generated successfully!")
        st.write("Exporting report to PDF...")

        pdf = weasyprint.HTML(string=generated_text).write_pdf()

        st.download_button(
            label="Download PDF",
            data=pdf,
            file_name=f"{project_name}_report.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.error("Error generating mini project report.")
        st.error(str(e))
