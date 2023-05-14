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

try:
    with open("db.json", "r") as f:
        personas = json.load(f)
except FileNotFoundError:
    personas = {}

st.title('AI-Powered Persona Generation Tool')

context = st.radio('Please select the context:', ['B2B', 'B2C'])

col1, col2, col3, col4 = st.columns(4)

col1.subheader('Demographic Information')
age = col1.number_input('Age', min_value=0, max_value=120, step=1, value=25)
location = col1.text_input('Location', value='New York')

col2.subheader('Professional Roles')
role = col2.text_input('Role', value='Product Manager')
industry = col2.text_input('Industry', value='Software')
company_size = col2.number_input('Company Size', min_value=1, step=1, value=100)

col3.subheader('Company Information')
company_name = col3.text_input('Company Name', value='ABC Corp')
company_description = col3.text_area('Company Description', max_chars=250, value='A leading software company.')

col4.subheader('Product Descriptions')
product_name = col4.text_input('Product Name', value='Project Management Tool')
product_description = col4.text_area('Product Description', max_chars=250, value='A tool for managing projects.')
product_cost = col4.number_input('Product Cost', format="%f", value=50.0)

nickname = st.text_input('Nickname for the persona', value='John Doe')

if st.button('Generate Persona'):

    persona_prompt = f"The user is a {role} in the {industry} industry. They work for a company called {company_name} which has approximately {company_size} employees. "\
    f"The company is located in {location} and can be described as follows: {company_description}. "\
    f"They are responsible for the product named {product_name}, which costs approximately {product_cost} and can be described as follows: {product_description}. "\
    f"The user's demographic information is as follows: They are {age} years old. "\
    f"The context for persona generation is {context}."

    persona = generate_persona(persona_prompt)
    personas[nickname] = persona

    with open("db.json", "w") as f:
        json.dump(personas, f)

    st.write(persona)
    st.success('Persona generated successfully!')




# Display the available personas in a dropdown
if personas:
    selected_persona = st.selectbox("Select a persona to display", options=list(personas.keys()))
    edit_persona = st.button("Edit Persona")
    if selected_persona:
        st.write(personas[selected_persona])
else:
    st.write("No personas available.")