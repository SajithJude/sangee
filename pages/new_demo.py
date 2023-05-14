import streamlit as st
import openai
import os 

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_persona(source):
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=source,
        temperature=0.56,
        max_tokens=2066,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0
    )
    return response.choices[0].text
# Title of your app
st.title('AI-Powered Persona Generation Tool')

# Radio button for B2B and B2C contexts
context = st.radio('Please select the context:', ['B2B', 'B2C'])

# Input fields for demographic information
st.subheader('Demographic Information')
age = st.number_input('Age', min_value=0, max_value=120, step=1)
location = st.text_input('Location')

# Input fields for professional roles
st.subheader('Professional Roles')
role = st.text_input('Role')
industry = st.text_input('Industry')
company_size = st.number_input('Company Size', min_value=1, step=1)

# Input fields for company information
st.subheader('Company Information')
company_name = st.text_input('Company Name')
company_description = st.text_area('Company Description', max_chars=250)

# Input fields for product descriptions
st.subheader('Product Descriptions')
product_name = st.text_input('Product Name')
product_description = st.text_area('Product Description', max_chars=250)
product_cost = st.number_input('Product Cost', format="%f")

# When user clicks this button, call your persona generation function with the provided inputs
if st.button('Generate Persona'):

    persona_prompt = f"The user is a {role} in the {industry} industry. They work for a company called {company_name} which has approximately {company_size} employees. "\
    f"The company is located in {location} and can be described as follows: {company_description}. "\
    f"They are responsible for the product named {product_name}, which costs approximately {product_cost} and can be described as follows: {product_description}. "\
    f"The user's demographic information is as follows: They are {age} years old. "\
    f"The context for persona generation is {context}."
    
    person_a = generate_persona(persona_prompt)
    st.write(person_a)


    # Call your persona generation function here
    # persona = generate_persona(context, age, location, role, industry, company_size, company_name, company_description, product_name, product_description, product_cost)
    st.success('Persona generated successfully!')
