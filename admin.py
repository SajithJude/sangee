import os
import streamlit as st
import openai 
import json

openai.api_key = os.getenv("OPENAI_API_KEY")
st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="expanded", menu_items=None)
def call_openai(source):
    # if "messages" not in st.session_state:
    messages=[{"role": "system", "content": f"You are the Buyer persona represents the following {source} given this information answer the following questions :\n What is your most important job responsibilities and activities? • What are the top 5 obstacles that would interfere with your career success? Where would you look for information about products like your company and other industry trends? • What role do you play in the purchase process, would they define the need, evaluate different solutions, make the final purchase decision or some combination of those roles? • What other roles in the company would likely be part of the buying process and decision-making? • Why wouldn’t you already have a product like yours? • Are there related products that this buyer’s team uses that would need to integrate with your product? • What concerns would you have that might keep them from making the purchase decision? \n the response should consist of the questions and the answers "}]

    # messages = [ {"role": "user", "content": f"You are the Buyer persona represents the following {source} "}]
    # st.session_state.messages.append(message)
    response = openai.ChatCompletion.create(
        model="gpt-4-0314",
        max_tokens=7000,
        temperature=0.7,
        messages = messages
    )
    return response.choices[0].message['content']



def main():
    if "response" not in st.session_state:
        st.session_state.response = ""

    st.title("Marketing Admin")

    promp = st.text_area("Background information of buyer")
    if st.button("Generate"):
        response = call_openai(promp)
        # jsonstr = json.loads(response)
        st.session_state.response = str(response)
        # st.write(st.session_state.response)



    if st.session_state.response != "":
        email = st.text_input("Enter the email of the Buyer")
        send_email_button = st.button("Send email")
        with st.expander("Sample persona answers"):
            st.write(st.session_state.response)

if __name__ == "__main__":
    main()
    
