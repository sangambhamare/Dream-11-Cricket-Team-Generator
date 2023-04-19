import streamlit as st
import openai

# Set up the OpenAI API client
openai.api_key = st.secrets["openai_api_key"]

# Set up Streamlit app
st.title("Mini Project Report Generator")
project_name = st.text_input("Enter a project name:")

def generate_intro(project_name):
    intro_prompt = f"Write an introduction for the project'{project_name}'."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=intro_prompt,
        max_tokens=2048,
        n=10,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text + response.choices[1].text + response.choices[2].text + response.choices[3].text + response.choices[4].text + response.choices[5].text + response.choices[6].text + response.choices[7].text + response.choices[8].text + response.choices[9].text

if project_name:
    intro = generate_intro(project_name)
    st.header("Introduction")    
    st.write(intro)
    
    
def generate_lit_survey(project_name):
    lit_survey_prompt = f"Write a literature survey for the project '{project_name}'."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=lit_survey_prompt,
        max_tokens=2048,
        n=10,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text + response.choices[1].text + response.choices[2].text + response.choices[3].text + response.choices[4].text + response.choices[5].text + response.choices[6].text + response.choices[7].text + response.choices[8].text + response.choices[9].text

if project_name:
    lit_survey = generate_lit_survey(project_name)
    st.header("Literature Survey")
    st.write(lit_survey)
    
    
def generate_methodology(project_name):
    methodology_prompt = f"Write a methodology for the project '{project_name}'."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=methodology_prompt,
        max_tokens=2048,
        n=10,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text + response.choices[1].text + response.choices[2].text + response.choices[3].text + response.choices[4].text + response.choices[5].text + response.choices[6].text + response.choices[7].text + response.choices[8].text + response.choices[9].text

if project_name:
    methodology = generate_methodology(project_name)
    st.header("Methodology")
    st.write(methodology)
