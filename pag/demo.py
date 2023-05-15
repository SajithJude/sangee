import streamlit as st
import os
import openai 
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
st.set_page_config(page_title=None, page_icon=None, layout="wide", initial_sidebar_state="collapsed", menu_items=None)


def call_openai(source):
    # if "messages" not in st.session_state:
    messages=[{"role": "system", "content": f"You are the Buyer persona represents the following {source} given this information answer the following questions :\n What is your most important job responsibilities and activities? • What are the top 5 obstacles that would interfere with your career success? Where would you look for information about products like your company and other industry trends? • What role do you play in the purchase process, would they define the need, evaluate different solutions, make the final purchase decision or some combination of those roles? • What other roles in the company would likely be part of the buying process and decision-making? • Why wouldn’t you already have a product like ours? • Are there related products that this buyer’s team uses that would need to integrate with your product? • What concerns would you have that might keep them from making the purchase decision? \n the response should consist of the questions and the answers "}]

    response = openai.ChatCompletion.create(
        model="gpt-4-0314",
        max_tokens=7000,
        temperature=0.7,
        messages = messages
    )
    return response.choices[0].message['content']




def call_openai_bp(source):
    # if "messages" not in st.session_state:
    messages=[{"role": "system", "content": f"generate a buyer persona based on this interview conversation {source}"}]

    response = openai.ChatCompletion.create(
        model="gpt-4-0314",
        max_tokens=7000,
        temperature=0.7,
        messages = messages
    )
    return response.choices[0].message['content']



def call_openaiturbo(inpt,source):
    
    if "messages" not in st.session_state:
        st.session_state.messages= [{"role": "user", "content": "you are an interviewer who will ask 7 questions about the user, (only one question at a time ), given in the following list with sample answers :\n"+str(source)+" \n, if the users answer for a particular question contains similar information from the actual answer to that question but misses any information from the actual answer, then ask an additional follow up question that reminds him about the missing information, and if the user still gives the same answer then move on to the next question, Once the questionarie is complete greet the user saying thank you. If the user asks any additional questions tell him to contact the company's sales team. "}]
    message={"role": "user", "content": str(inpt)}
    st.session_state.messages.append(message)
    response = openai.ChatCompletion.create(
        model="gpt-4-0314",
        max_tokens=6800,
        messages = st.session_state.messages
    )
    return response.choices[0].message['content']


if "qa_pairs" not in st.session_state:
    st.session_state.qa_pairs = []


mcol , buyercol = st.columns(2, gap="large")

if "response" not in st.session_state:
        st.session_state.response =""





mcol.title("Marketing Admin")


marketcol, personacol = mcol.tabs(["Stimulate Sample Persona", "View Actual Persona"])


promp = marketcol.text_area("Background information of buyer")
if marketcol.button("Stimulate"):
    response = call_openai(promp)
    # jsonstr = json.loads(response)
    st.session_state.response = str(response)
    # st.write(st.session_state.response)

if personacol.button("Generate"):
    bp_variable = str(st.session_state.qa_pairs)
    bp_res = call_openai_bp(bp_variable)
    personacol.write(bp_res)



if st.session_state.response != "":
    with marketcol.expander("Stimulted Persona"):
        marketcol.write(st.session_state.response)



buyercol.title("Pragmatic Questionnare")

conversation = buyercol.empty()


mescol , butcol = buyercol.columns([10,2])
user_input = mescol.text_input("Buyer:", placeholder="Type start and click send to initiate the quetsionare")
butcol.write("")
butcol.write("")

if butcol.button("Send"):
    bot_response = call_openaiturbo(user_input,str(st.session_state.response))
   
    st.session_state.qa_pairs.append((user_input, bot_response))

    conversation.markdown(f'**You:** {user_input}')
    conversation.info(f'**Interviewer:** {bot_response}')
