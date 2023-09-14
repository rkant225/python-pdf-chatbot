import streamlit as st
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, StorageContext, load_index_from_storage
import os
from pathlib import Path
import openai
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Text to speech imports
from gtts import gTTS
from pygame import mixer
from googletrans import Translator

st.set_page_config(layout="centered")
ss = st.session_state

openai.api_key = os.getenv("OPENAI_API_KEY")

# Translator INIT
translator = Translator()
mixer.init()

# if "authentication_status" not in st.session_state:
#     st.session_state.authentication_status = None
#     st.session_state.name = None
#     st.session_state.username = None

# Authenticator
with open('./auth.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


languageDictonary = {
    'English': 'en',
    'Hindi': 'hi',
    'Arabic': 'ar',
    'Assamese': 'as',
    'Bengali': 'bn',
    'Chinese': 'zh',
    'French': 'fr',
    'German': 'de',
    'Gujarati': 'gu',
    'Kannada': 'kn',
    'Tamil': 'ta',
    'Telugu': 'te',
}

# Set initial message
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]


# Helper method to generate audio and play it
def createAudioFromTextAndPlayIt(text):

    # Remove the old audio file if it exists
    if os.path.isfile('assistant.mp3'):
        mixer.music.unload()
        os.remove("assistant.mp3")

    audio = gTTS(text=text, lang=languageDictonary[st.session_state.assistant_language])
    audio.save("assistant.mp3")
    mixer.music.load("assistant.mp3")
    mixer.music.play()

    # Uncomment below "while" loop if you want to wait for audio to be finished.
    # while mixer.music.get_busy():
    #     continue


def stopAudioPlayback():
    mixer.music.stop()

name, authentication_status, username = authenticator.login('RockWell Automation ChatBot Login', 'main')


if st.session_state.authentication_status == False:
    st.error('Username/password is incorrect')
    
# If user is not logged in then ask them to login first
if not st.session_state.authentication_status:
    st.error("You must log-in to chat with our chatbot!")
    st.stop()  # App won't run anything after this line



# Sidebar
with st.sidebar:
    # App title
    st.title('Rockwell Automation')

    # User detail and logout button
    st.header('Welcome "' + st.session_state.name + '"!')
    authenticator.logout('Logout', 'sidebar')

    # UI selection
    st.radio("Selected UI", ["Chatbot", "Chat History"] ,key="selectedUi",horizontal=False)

    st.selectbox(label="Text output and playback language", options=['English', 'Hindi', 'Arabic', 'Assamese', 'Bengali', 'Chinese', 'French', 'German', 'Gujarati', 'Kannada', 'Tamil', 'Telugu'], key="assistant_language")

    st.checkbox('Do you want your assistant to read out the answers?', key="with_text_to_speach")
    st.button('Stop assistant playback', on_click=stopAudioPlayback, disabled=not st.session_state.with_text_to_speach)

if st.session_state.selectedUi == "Chatbot":
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    help_text = ""
    if os.path.isdir('./index') and os.path.isfile("./index/docstore.json") and os.path.isfile("./index/graph_store.json") and os.path.isfile("./index/index_store.json") and os.path.isfile("./index/vector_store.json"):
        help_text = "Enter your query..."
    else:
        help_text = "Chatbot is not yet ready, please connect with Admin."

    # User Input
    if prompt := st.chat_input(disabled=not (os.path.isdir('./index') and os.path.isfile("./index/docstore.json") and os.path.isfile("./index/graph_store.json") and os.path.isfile("./index/index_store.json") and os.path.isfile("./index/vector_store.json")), placeholder=help_text):
        st.session_state.messages.append({"role": "user", "content": prompt})
        ss['query'] = prompt
        with st.chat_message("user"):
            st.write(prompt)


    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                loaded_index = load_index_from_storage(StorageContext.from_defaults(persist_dir="./index"))
                query_engine = loaded_index.as_query_engine()
                eng_response = query_engine.query(ss['query']).response # English
                
                translated_text = translator.translate(eng_response, dest=languageDictonary[st.session_state.assistant_language]) # Translated
                response = translated_text.text
                st.write(response)

        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)

        # Play the sound
        if st.session_state.with_text_to_speach:
            createAudioFromTextAndPlayIt(response)

    # Delete the mp3 file
    if not mixer.music.get_busy() and os.path.isfile('assistant.mp3'):
        mixer.music.unload()
        os.remove("assistant.mp3")



# Chat History
if st.session_state.selectedUi == "Chat History":
    st.header('Chat history')
    st.write(st.session_state.messages)