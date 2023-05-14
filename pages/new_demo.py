import streamlit as st
import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_persona(source):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=source,
        temperature=0.56,
        max_tokens=2066,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0
    )
    return response.choices[0].text

# Load existing personas or initialize an empty dictionary
try:
    with open("db.json", "r") as f:
        personas = json.load(f)
except FileNotFoundError:
    personas = {}

st.title('AI-Powered Persona Generation Tool')

context = st.radio('Please select the context:', ['B2B', 'B2C'])

col1, col2, col3, col4 = st.columns(4)

col1.subheader('Demographic Information')
age = col1.number_input('Age', min_value=0, max_value=120, step=1)
location = col1.text_input('Location')

col2.subheader('Professional Roles')
role = col2.text_input('Role')
industry = col2.text_input('Industry')
company_size = col2.number_input('Company Size', min_value=1, step=1)

col3.subheader('Company Information')
company_name = col3.text_input('Company Name')
company_description = col3.text_area('Company Description', max_chars=250)

col4.subheader('Product Descriptions')
product_name = col4.text_input('Product Name')
product_description = col4.text_area('Product Description', max_chars=250)
product_cost = col4.number_input('Product Cost', format="%f")

# Input field for nickname
nickname = st.text_input('Nickname for the persona')

if st.button('Generate Persona'):

    persona_prompt = f"The user is a {role} in the {industry} industry. They work for a company called {company_name} which has approximately {company_size} employees. "\
    f"The company is located in {location} and can be described as follows: {company_description}. "\
    f"They are responsible for the product named {product_name}, which costs approximately {product_cost} and can be described as follows: {product_description}. "\
    f"The user's demographic information is as follows: They are {age} years old. "\
    f"The context for persona generation is {context}."

    # Generate persona and save it under the given nickname
    persona = generate_persona(persona_prompt)
    personas[nickname] = persona

    # Save updated personas dictionary to db.json
    with open("db.json", "w") as f:
        json.dump(personas, f)

    st.write(persona)
    st.success('Persona generated successfully!')
