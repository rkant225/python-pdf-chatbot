import streamlit as st
import os
import openai
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(layout="centered")

openai.api_key = os.getenv("OPENAI_API_KEY")

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

name, authentication_status, username = authenticator.login('RoclWell Automation ChatBot Login', 'main')


if st.session_state.authentication_status == False:
    st.error('Username/password is incorrect')
    
# If user is not logged in then ask them to login first
if not st.session_state.authentication_status:
    st.error("You must log-in to see User details!")
    st.stop()  # App won't run anything after this line


# Sidebar
with st.sidebar:
    authenticator.logout('Logout', 'sidebar')

userDetailsMarkdown = f""" 
    ### Name
        {st.session_state.name}
    ### Username
        {st.session_state.username}
    ### IsAuthenticated
        {st.session_state.authentication_status}
"""
st.markdown(userDetailsMarkdown)