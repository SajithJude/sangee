import streamlit as st

def main():
    st.title("Chat Interface")

    conversation = st.empty()

    user_input = st.text_input("You:")

    if st.button("Send"):
        # You should replace the lines below with your chatbot model's response generation code
        bot_response = "This is a dummy response" 

        conversation.markdown(f'**You:** {user_input}')
        conversation.markdown(f'**Bot:** {bot_response}')

if __name__ == "__main__":
    main()
