# Login imports
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# UI streamlit import
import streamlit as st

st.set_page_config(layout="centered")


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


# Register UI
if authenticator.register_user('Register user', preauthorization=False):
    st.success('User registered successfully')
    with open('./auth.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)