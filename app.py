import streamlit as st
import time
from assistant import GenericAssistant

st.title("Chatbot for best team ❤️")


assistant = GenericAssistant('intents.json', model_name="chatbot_model")
# assistant.train_model()
# assistant.save_model()
assistant.load_model()



def get_chat_response(text):
    bot_message = assistant.request(text)
    return bot_message

# Streamed response emulator
def response_generator(text):
    response = get_chat_response(text)
    
    for word in response.split():
        yield word + " "
        time.sleep(0.06)



# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})