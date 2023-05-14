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

section1 , section2 = st.columns(2, gap="large")


context = section1.radio('Please select the context:', ['B2B', 'B2C'],horizontal=True)
col1, col2, col3, col4,col5 ,col6= section1.tabs(["Demographics","Roles","Company","Product","Generate","Pictures"])

# col1 = section1.expander("Demographic Information") 
# col2 = section1.expander("Professional Roles") 
# col3 = section1.expander("Company Information") 
# col4 = section1.expander("Product Descriptions")

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

nickname = section1.text_input('Nickname for the persona', value='John Doe')

if col5.button('Generate Persona'):

    persona_prompt = f"The user is a {role} in the {industry} industry. They work for a company called {company_name} which has approximately {company_size} employees. "\
    f"The company is located in {location} and can be described as follows: {company_description}. "\
    f"They are responsible for the product named {product_name}, which costs approximately {product_cost} and can be described as follows: {product_description}. "\
    f"The user's demographic information is as follows: They are {age} years old. "\
    f"The context for persona generation is {context}."

    persona = generate_persona(persona_prompt)
    if persona not in st.session_state:
        st.session_state.persona = persona
    personas[nickname] = persona

    with open("db.json", "w") as f:
        json.dump(personas, f)

    section1.write(persona)
    section1.success('Persona Saved successfully!')


col6.subheader('Persona related Images')
if col6.button('Generate Persona Image'):
    
    imagePrompt = f"a photo of how the following persona might look like: {st.session_state.persona}"
    image = openai.Image.create(
    prompt=imagePrompt,
    n=3,
    size="256x256"
    )
    for item in image["data"]:
        # image_url = image['data'][0]['url']
        col6.image(item["url"], caption=st.session_state.persona, width=100)
    # section2.write(image_url)



# Display the available personas in a dropdown
if personas:
    selected_persona = section2.selectbox("Select a persona to display", options=list(personas.keys()))
    old = section2.expander("Persona")

    persona_edit_prompt = section2.text_area("Enter your prompt")
    edit_persona = section2.button("Edit Persona")
    # if selected_persona:
    # with section2.expander("Persona"):
    old.write(personas[selected_persona])
    if edit_persona:
        edit_prompt= f"Evolve the following persona : {personas[selected_persona]}\n based on the new information obtained which is given bellow\n  new_information : {persona_edit_prompt}"
        edited_persona= generate_persona(edit_prompt)
        section2.write(edited_persona)

        personas[nickname] = edited_persona

        with open("db.json", "w") as f:
            json.dump(personas, f)
        section2.success('Persona Edited and saved successfully!')



else:
    section2.write("No personas available.")