import streamlit as st
import openai
import os
import json

from langchain import OpenAI

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader , ServiceContext, LLMPredictor
from llama_index import StorageContext, load_index_from_storage

# rebuild storage context
# load index


openai.api_key = os.getenv("OPENAI_API_KEY")
st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)


def call_gpt4(inpt,source):
    if "mssages" not in st.session_state:
        st.session_state.mssages= [{"role": "user", "content": f"you are a person with the following traits {source}, \n Given this information answer the questions asked in the next messages."}]
    message={"role": "user", "content": str(inpt)}
    st.session_state.mssages.append(message)
    response = openai.ChatCompletion.create(
        model="gpt-4-0314",
        max_tokens=200,
        messages = st.session_state.mssages
    )
    return response.choices[0].message['content']



def generate_persona(source):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=source,
        temperature=0.56,
        max_tokens=3066,
        top_p=1,
        frequency_penalty=0.35,
        presence_penalty=0
    )
    return response.choices[0].text

try:
    with open("db.json", "r") as f:
        personas = json.load(f)
except json.JSONDecodeError as e:
    personas = {}

st.title('AI-Powered Persona Generation Tool')

section1 , section2 = st.columns(2, gap="large")


context = section1.radio('Please select the context:', ['B2B', 'B2C'],horizontal=True)
col1,  col3, context_tab, col4,col5 ,col6= section1.tabs(["Demographics","Company","Additional Context","Product","Generate","Pictures"])


col1.subheader('Demographic Information')
age = col1.slider('Age', min_value=0, max_value=120, step=1, value=25)
location = col1.text_input('Location', value='New York')
industry = col1.text_input('Industry', value='Software')
company_size = col1.number_input('Company Size', min_value=1, step=1, value=100)
role = col1.text_input('Role', value='Product Manager')


context_tab.subheader('Context Information')
problems = context_tab.text_area('Problems', max_chars=250, value='Problem 1, Problem 2')
goals = context_tab.text_area('Goals', max_chars=250, value='Goal 1, Goal 2')
user_type = context_tab.radio('User Type', ['Sheep', 'Pioneer'])


col3.subheader('Company Information')
company_description = col3.text_area('Company Description', max_chars=250, value='A leading software company.')
client_base_size = col3.number_input('Size of Current Client Base', min_value=1, step=1, value=100)
client_base_industries = col3.text_area('Industries of Client Base', max_chars=250, value='Software, Information Technology')

col4.subheader('Product Descriptions')
product_name = col4.text_input('Product Name', value='Project Management Tool')
product_description = col4.text_area('Product Description', max_chars=250, value='A tool for managing projects.')
product_cost = col4.number_input('Product Cost', format="%f", value=50.0)
competitive_products = col4.text_area('Competitive Products', max_chars=250, value='Competitor Product A, Competitor Product B')

nickname = col5.text_input('Nickname for the persona', value='John Doe')

if col5.button('Generate Persona'):

    persona_prompt = f"Generate a persona for the user who is a {role} in the {industry} industry. They work for a company with approximately {company_size} employees. The company is described as follows: {company_description}. They have a client base of around {client_base_size} clients, operating in the following industries: {client_base_industries}. Their current problems include: {problems}. Their goals are: {goals}. The user is {age} years old, located in {location}, and identifies as a {user_type}. They are responsible for the product named {product_name}, which costs approximately {product_cost} and can be described as follows: {product_description}. They face competition from the following products: {competitive_products}."
    if "persona_prompt" not in st.session_state:
        st.session_state.persona_prompt= persona_prompt

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
    cols = col6.columns(3)
    imagePrompt = f"a photo of how the following person might look like in person: {st.session_state.persona}"
    image = openai.Image.create(
    prompt=imagePrompt,
    n=3,
    size="256x256"
    )
    for i, item in enumerate(image["data"]):
        cols[i].image(item["url"],width=100)



# Display the available personas in a dropdown
# if personas:
selected_persona = section2.selectbox("Select a persona to display", options=list(personas.keys()))
old = section2.expander("Persona")

persona_option = section2.radio('what do you wanna do with this persona:', ['edit', 'chat'],horizontal=True)

if persona_option == "edit":
    persona_edit_prompt = section2.text_area("What new information do you have about this persona?")
    edit_persona = section2.button("Edit Persona")
    old.write(personas[selected_persona])
    if edit_persona:
        edit_prompt= f"Evolve the following persona : {personas[selected_persona]}\n based on the new information obtained which is given bellow\n  new_information : {persona_edit_prompt}"
        edited_persona= generate_persona(edit_prompt)
        section2.write(edited_persona)

        personas[nickname] = edited_persona

        with open("db.json", "w") as f:
            json.dump(personas, f)
        section2.success('Persona Edited and saved successfully!')

elif persona_option == "chat":
    chat_input = section2.text_input("What's your question?")
    ask_button = section2.button("Ask")

    # Create a string or list to hold the conversation if it doesn't exist
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    if ask_button:
        reply = call_gpt4(chat_input, personas[selected_persona])
        section2.info(reply)
        # Append the user's question and the generated response to the conversation
        st.session_state.conversation.append(('User', chat_input))
        st.session_state.conversation.append(('Persona', reply))
        # Display the conversation
        for speaker, text in st.session_state.conversation:
            pers = st.sidebar.expander("Persona")
            if speaker == 'User':
                st.sidebar.write(f'{speaker}: {text}')
            else:
                pers.write(text)
                  # speaker == 'AI'
                # with section2.expander(f'{speaker}:'):
                #     section2.text(text)

# else:
#     section2.write("No personas available.")

but = st.button("jsnjs ")
if but:

    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=3500))
    service_context = ServiceContext.from_defaults(llm_predictor=llm_predictor)

    folder_name = "data"
    path = os.path.join(".", folder_name)

    documents = SimpleDirectoryReader(path).load_data()
    index = GPTVectorStoreIndex.from_documents(documents,service_context=service_context)
    index.storage_context.persist()
    storage_context = StorageContext.from_defaults(persist_dir="./storage")


    index = load_index_from_storage(storage_context)
    query_engine = index.as_query_engine()
    response = query_engine.query(f"Generate a Persona document for the following information, exclude names: {st.session_state.persona_prompt}")

    st.write(response)

















# import os
# import streamlit as st
# import openai 
# import json

# openai.api_key = os.getenv("OPENAI_API_KEY")
# st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="expanded", menu_items=None)
# def call_openai(source):
#     # if "messages" not in st.session_state:
#     messages=[{"role": "system", "content": f"You are the Buyer persona represents the following {source} given this information answer the following questions :\n What is your most important job responsibilities and activities? • What are the top 5 obstacles that would interfere with your career success? Where would you look for information about products like your company and other industry trends? • What role do you play in the purchase process, would they define the need, evaluate different solutions, make the final purchase decision or some combination of those roles? • What other roles in the company would likely be part of the buying process and decision-making? • Why wouldn’t you already have a product like yours? • Are there related products that this buyer’s team uses that would need to integrate with your product? • What concerns would you have that might keep them from making the purchase decision? \n the response should consist of the questions and the answers "}]

#     # messages = [ {"role": "user", "content": f"You are the Buyer persona represents the following {source} "}]
#     # st.session_state.messages.append(message)
#     response = openai.ChatCompletion.create(
#         model="gpt-4-0314",
#         max_tokens=7000,
#         temperature=0.7,
#         messages = messages
#     )
#     return response.choices[0].message['content']



# def main():
#     if "response" not in st.session_state:
#         st.session_state.response = ""

#     st.title("Marketing Admin")

#     promp = st.text_area("Background information of buyer")
#     if st.button("Generate"):
#         response = call_openai(promp)
#         # jsonstr = json.loads(response)
#         st.session_state.response = str(response)
#         # st.write(st.session_state.response)



#     if st.session_state.response != "":
#         email = st.text_input("Enter the email of the Buyer")
#         send_email_button = st.button("Send email")
#         with st.expander("Sample persona answers"):
#             st.write(st.session_state.response)

# if __name__ == "__main__":
#     main()
    
