import streamlit as st
import openai

# Set up the OpenAI API client
openai.api_key = st.secrets["openai_api_key"]

# Set up Streamlit app
st.title("Mini Project Report Generator")
project_name = st.text_input("Enter a project name:")

def generate_intro(project_name):
    intro_prompt = f"Write an introduction for the project in 1000 words'{project_name}'."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=intro_prompt,
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text

if project_name:
    intro = generate_intro(project_name)
    st.header("Introduction")
    st.write(intro)
