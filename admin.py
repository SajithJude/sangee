import os
import streamlit as st
import openai 
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_openai(source):
    # if "messages" not in st.session_state:
    messages=[{"role": "system", "content": f"You are the Buyer persona represents the following {source} given this information answer the following questions :\n What is this buyer persona’s most important job responsibilities and activities? • What are the top 5 obstacles that would interfere with this buyer persona’s career success? Where would this buyer persona look for information about products like BrandBuilder and other industry trends? • What role with this buyer persona play in the purchase process, would they define the need, evaluate different solutions, make the final purchase decision or some combination of those roles? • What other roles in the company would likely be part of the buying process and decision-making? • Why wouldn’t this buyer persona already have a product like Brandbuilder? • Are there related products that this buyer’s team uses that would need to integrate with Brandbuilder? • What concerns would this buyer have that might keep them from making the purchase decision? \n the response should consist of the questions and the answers "}]

    # messages = [ {"role": "user", "content": f"You are the Buyer persona represents the following {source} "}]
    # st.session_state.messages.append(message)
    response = openai.ChatCompletion.create(
        model="gpt-4-0314",
        max_tokens=7000,
        temperature=0.7,
        messages = messages
    )
    return response.choices[0].message['content']


def call_openaiturbo(inpt,source):
    
    if "messages" not in st.session_state:
        st.session_state.messages= [{"role": "user", "content": "you are an interviewer who will ask 7 questions about the user, (only one question at a time ), given in the following list with sample answers :\n"+str(source)+" \n, if the users answers contain similar information from the actual answer but still misses any information, then ask an additional follow up question that obtains a binary answer about the missing information, at the end of all questions create a buyer persona for the user who responded "}]
    message={"role": "user", "content": str(inpt)}
    st.session_state.messages.append(message)
    response = openai.ChatCompletion.create(
        model="gpt-4-0314",
        max_tokens=6800,
        messages = st.session_state.messages
    )
    return response.choices[0].message['content']





def main():
    st.title("Pragmatic")

    promp = st.text_area("Background information")
    if st.button("Generate Answers"):
        response = call_openai(promp)
        # jsonstr = json.loads(response)
        if "response" not in st.session_state:
            st.session_state.response = str(response)
        st.write(st.session_state.response)
    conversation = st.empty()

    user_input = st.text_input("You:")

    if st.button("Send"):
        bot_response = call_openaiturbo(user_input,str(st.session_state.response))

        conversation.markdown(f'**You:** {user_input}')
        conversation.markdown(f'**Bot:** {bot_response}')

if __name__ == "__main__":
    main()
    if st.session_state.response is not None:
        st.write(st.session_state.response)

