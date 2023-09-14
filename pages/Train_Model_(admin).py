import streamlit as st
from llama_index import SimpleDirectoryReader, GPTVectorStoreIndex, StorageContext, load_index_from_storage
import os
from pathlib import Path
import openai
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(layout="centered")

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

name, authentication_status, username = authenticator.login('RoclWell Automation ChatBot Login', 'main')


if st.session_state.authentication_status == False:
    st.error('Username/password is incorrect')

# If user is not logged in then ask them to login first
if not st.session_state.authentication_status:
    st.error("You must log-in as Admin to see the content of this sensitive page!")
    st.stop()  # App won't run anything after this line



def loadPdfsAndGenerateIndex():
    with st.spinner("Creating Index from Train documents...."):
        documents = SimpleDirectoryReader('./train_docs').load_data()
        index = GPTVectorStoreIndex(documents)
        index.storage_context.persist(persist_dir="./index")


# Sidebar
# with st.sidebar:


def upload(uploaded_file):
    cwd = os.getcwd()
    completePath = Path(cwd, "train_docs", uploaded_file.name)
    with open(completePath, mode='wb') as w:
        w.write(uploaded_file.getvalue())


def updateFileList():
    cwd = os.getcwd()
    fileNames = os.listdir(Path(cwd, "train_docs"))
    st.session_state.file_List = fileNames

def renderFileList():
    # listHTMLString = ""
    cwd = os.getcwd()
    fileNames = os.listdir(Path(cwd, "train_docs"))
    # for file in fileNames:
    #     listHTMLString = listHTMLString + "<li>" + file + "<button> x </button>" + "</li>"
    # st.markdown(listHTMLString, unsafe_allow_html=True)
   

    for index,file in enumerate(fileNames):
        cwd = os.getcwd()
        emp = st.empty()
        col1, col2 = st.columns([7, 5])

        col1.markdown('<b>'+ file + '</b>', unsafe_allow_html=True)

        if col2.button("Del", key=index):
            fileToBeDeleted = Path(cwd, "train_docs", file)
            if os.path.isfile(fileToBeDeleted):
                os.remove(fileToBeDeleted)
                st.experimental_rerun()

        else:
            emp.empty()


# Sidebar
with st.sidebar:
    authenticator.logout('Logout', 'sidebar')

if st.session_state.username == "admin":

    st.title('Rockwell Automation (Admin)')

    st.header('Welcome "' + st.session_state.name + '"!')
    # authenticator.logout('Logout', 'main')

    st.header("1. Select and save your new User manual to training folder.")

    with st.form("my-form", clear_on_submit=True):
        uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
        submitted = st.form_submit_button("Store this file to '/train_docs' for training")
        if submitted and uploaded_file:
            upload(uploaded_file)

    # uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])
    # if uploaded_file:
    #     upload(uploaded_file)

    # st.button("Store this file to '/train_docs'", on_click=upload, disabled=not uploaded_file)

    st.header("2. List of current training documents/manual.")
    updateFileList()
    renderFileList()

    st.header("3. Finaly generate index out of training documents.")
    st.markdown("<i>The button located below serves a crucial function in our system - it's the key to generating an index from your PDF documents. By clicking on this button, you initiate a process that will extract essential information and organize it into a comprehensive index. This feature can save you valuable time and effort when you need to quickly access specific content within your PDFs. So, whenever you're ready to create an index from your documents, simply click on the button below to get started!</i>", unsafe_allow_html=True)
    st.button('Generete index out of latest documents', on_click=loadPdfsAndGenerateIndex)
else:
    st.error("You can't access this restricted page as you are not an Admin.")
