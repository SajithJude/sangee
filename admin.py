import os
import streamlit as st
import openai 
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_openai(source,initprompt):
    messages={"role": "system", "content": source}
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "user", "content": f"you are an interviewer who will ask 7 questions, (only one question at a time ), given in the following json list with sample answers :{initprompt}\n, if the users answer misses any information from the actual , then ask an additional question in a way that you hint the user to provide the missing information in the next answer before moving to the next questions "}]
        response = openai.ChatCompletion.create(
                                                    model="gpt-4-0314",
                                                    max_tokens=7000,
                                                    temperature=0.7,
                                                    messages = messages
                                                )
    st.session_state.messages.append(messages)
    response = openai.ChatCompletion.create(
        model="gpt-4-0314",
        max_tokens=7000,
        temperature=0.7,
        messages = st.session_state.messages
    )
    return response.choices[0].message['content']


def call_openaiturbo(source):
    message={"role": "user", "content": source}
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "user", "content": "You are a biology quiz bot that asks me questions and verify my answer and keep iterating till I say stop, Ask me questions about biology one after the other, one question at a time, and correct my responses before moving to the next question"}]
    st.session_state.messages.append(message)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=150,
        messages = st.session_state.messages
    )
    return response.choices[0].message['content']





def main():
    st.title("Pragmatic")

    promp = st.text_area("Background information")
    if st.button("Generate Answers"):
        response = call_openai(promp)
        jsonstr = json.loads(response)
        if "jsonstr" not in st.session_state:
            st.session_state.jsonstr = jsonstr
        st.write(st.session_state.jsonstr)
    conversation = st.empty()

    user_input = st.text_input("You:")

    if st.button("Send"):
        bot_response = call_openaiturbo(user_input,st.session_state.jsonstr)

        conversation.markdown(f'**You:** {user_input}')
        conversation.markdown(f'**Bot:** {bot_response}')

if __name__ == "__main__":
    main()
