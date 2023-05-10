import os
import streamlit as st
import openai 

openai.api_key = os.getenv("OPENAI_API_KEY")

def call_openai(source):
    messages=[{"role": "user", "content": source}]

    response = openai.ChatCompletion.create(
        model="gpt-4-0314",
        max_tokens=150,
        temperature=0.7,
        messages = messages
    )
    return response.choices[0].message['content']

def main():
    st.title("Chat Interface")

    conversation = st.empty()

    user_input = st.text_input("You:")

    if st.button("Send"):
        bot_response = call_openai(user_input)

        conversation.markdown(f'**You:** {user_input}')
        conversation.markdown(f'**Bot:** {bot_response}')

if __name__ == "__main__":
    main()
