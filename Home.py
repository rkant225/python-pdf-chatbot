# Login imports
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# UI streamlit import
import streamlit as st
import base64 
st.set_page_config(layout="wide")

# Import and apply CSS
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


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

# Image 6
file_ = open("./assets/Features.png", "rb") 
contents = file_.read() 
Features_image = base64.b64encode(contents).decode("utf-8") 
file_.close() 

# Image 7
file_ = open("./assets/robotHi.gif", "rb") 
contents = file_.read() 
robotHi_image = base64.b64encode(contents).decode("utf-8") 
file_.close() 

# Image 8
file_ = open("./assets/logo.png", "rb") 
contents = file_.read() 
logo_image = base64.b64encode(contents).decode("utf-8") 
file_.close() 

# Image 10
file_ = open("./assets/chatbotBye.gif", "rb") 
contents = file_.read() 
chatbotBye_image = base64.b64encode(contents).decode("utf-8") 
file_.close() 

# Video 1
file_ = open("./assets/Vodeo_Combined.mp4", "rb") 
contents = file_.read() 
Vodeo_Combined_video = base64.b64encode(contents).decode("utf-8") 
file_.close() 

# Video 2
file_ = open("./assets/Video_Chatbot.mp4", "rb") 
contents = file_.read() 
Video_Chatbot_video = base64.b64encode(contents).decode("utf-8") 
file_.close() 

# Video 3
file_ = open("./assets/Video_Train.mp4", "rb") 
contents = file_.read() 
Video_Train_video = base64.b64encode(contents).decode("utf-8") 
file_.close() 

htmlString = f"""
                <div>
                    <div style='display:flex; justify-content:space-between; align-items:center; gap:1rem;'>
                        <div style='display:flex;'>
                            <img src="data:image/gif;base64,{logo_image}" height="80" alt="ChatbotFlow_imagea" style='border-radius:.5rem;'></img>
                        </div>
                        <div style='text-align:right;'>
                            <img src="data:image/gif;base64,{robotHi_image}" height="150" alt="ChatbotFlow_imagea" style='border-radius:.5rem;'></img>
                        </div>
                    </div>
                    <section>
                        <div>
                            <div style='display:flex; justify-content:space-between;align-items:center; gap:1rem;'>
                                <div>
                                    <div style='font-size: 2rem; font-weight: 600;'>Welcome to to our brand new Chatbot</div>
                                    <p style=''>At RockWell Automation, we recognize the paramount significance of efficiency and precision within the realm of industrial automation. This innovative tool has been meticulously crafted and fine-tuned to serve as your primary resource for addressing all your automation-related inquiries and concerns. Whether you are a seasoned expert seeking specific technical insights or someone relatively new to the complexities of industrial automation, our Chatbot is poised to cater to your needs. This innovative tool has been meticulously crafted and fine-tuned to serve as your primary resource for addressing all your automation-related inquiries and concerns. This innovative tool has been meticulously crafted and fine-tuned to serve as your primary resource for addressing all your automation-related inquiries and concerns. We have harnessed the power of technology to bring you a responsive and comprehensive solution, effectively reducing the time and effort traditionally required to access vital information and guidance.</p>
                                </div>
                                <div>
                                    <video height="280"  style='border-radius:83% 17% 79% 21% / 36% 51% 49% 64%; border: 5px solid rgb(250,50,40);' loop muted="true" autoplay="" playsinline="" src="data:video/mp4;base64,{Vodeo_Combined_video}" type="video/mp4"></video>
                                </div>
                            </div>
                        </div>
                    </section>
                    <section>
                        <div style='display:flex; justify-content:center; align-items:center; gap:1rem;'>
                            <div>
                                <video height="350" style='border-radius:1rem; border: 5px solid rgb(250,50,40); padding: 0rem .5rem;' loop muted="true" autoplay="" playsinline="" src="data:video/mp4;base64,{Video_Chatbot_video}" type="video/mp4"></video>
                            </div>
                            <div>
                                <div style='font-size: 2rem; font-weight: 600;'>How our Chatbot works?</div>
                                <p style=''>Our Chatbot is engineered to provide you with detailed explanations and solutions by leveraging an extensive library of training documents and device manuals. Whether you're a seasoned engineer or new to the world of industrial automation, our Chatbot is here to assist you at every step. Our chatbot is trained with multiple documents and manuals which leverages NLP models to understand user input, retrieve relevant information from its training data, and generate contextually appropriate responses. The goal is to provide users with accurate and helpful information, making it a valuable tool for various applications, including customer support, information retrieval, and automation assistance.</p>
                            </div>
                        </div>
                    </section>
                    <section>
                        <div style='display:flex; justify-content:center; align-items:center; gap:1rem;'>
                            <div>
                                <div style='font-size: 2rem; font-weight: 600;'>How to re-train Chatboat?</div>
                                <p style=''>Our Chatbot is highly flexible, We can always re-train our chatbot whenever we get new manual or document which we want to feed to our chatboat so that it can be added to it's knowledge base. To re-train the chatbot just login as Admin and navigate to 'Train Model (Admin)' menu. Here you have 3 simple steps. First upload your new documents and check weather they are available in Step 2. And finaly click on 'Generete index out of latest documents' button to re-train the model.</p>
                            </div>
                            <div>
                                <video height="350" style='border-radius:1rem; border: 5px solid rgb(250,50,40); padding: 0rem .5rem;' loop muted="true" autoplay="" playsinline="" src="data:video/mp4;base64,{Video_Train_video}" type="video/mp4"></video>
                            </div>
                        </div>
                    </section>
                    <section>
                        <div style='font-size: 2rem; font-weight: 600;'>Features of our chatbot</div>
                        <p>Our chatbot combines these features to deliver a valuable and efficient conversational experience, making it a valuable asset for customer support, information retrieval, and automation in various industries.</p>
                        <div style='display:flex; justify-content:center; align-items:center; gap:1rem;'>
                            <div>
                                <ul>
                                    <li><b>Context Awareness : </b>  Our chatbot maintain context throughout a conversation, remembering previous interactions and user queries to provide relevant responses.</li>
                                    <li><b>Multilingual Support  : </b>  Our chatbot supports multiple languages user can select there desired language from the sidebar. The output from the chatbot will be displayed to user in selected language. </li>
                                    <li><b>Continuous Learning and Training : </b>  Our chatbot have mechanisms for ongoing training and improvement, incorporating user feedback and new data to enhance its responses. </li>
                                    <li><b>User-Friendly Interface : </b>  User Interface of our chatbot is very simple and user-friendly. Here user can navigate through different section of application from the side-tab. Some features require user to be logged-in into the application. </li>
                                    <li><b>Supports user with different privileges : </b>  Our application supports multiple users with different privileges. Some Admin features will be restricted to user who don't have Admin rights. Admin user can re-train the model with new documents and manuals. </li>
                                    <li><b>Speech based output : </b>  Our application supports the speech bases chatbot output as well. Also user can sellect the desired language of speech output. </li>
                                </ul>
                            </div>
                            <div>
                                <img src="data:image/gif;base64,{Features_image}" height="450" alt="ChatbotFlow_imagea" style='border-radius:.5rem; margin: auto; display: block; padding:0.35rem; border: 5px solid rgb(250,50,40);'></img>
                            </div>
                        </div>
                    </section>
                    <section>
                        <div style='display:flex; justify-content:center; align-items:center; gap:1rem;'>
                            <div>
                                <img src="data:image/gif;base64,{chatbotBye_image}" height="250" alt="ChatbotFlow_imagea" style='border-radius:.5rem;'></img>
                            </div>
                            <div>
                                <div style='font-size: 2rem; font-weight: 600;'>Contact Us</div>
                                <p>At RockWell Automation, we're committed to providing you with the best possible support and assistance through our innovative chatbot. However, we understand that there may be times when you need to connect with a human expert for more complex inquiries or personalized assistance. We're here to help in every way we can. Have questions or need assistance beyond what the Chatbot can provide? Our customer support team is here to help. Contact us anytime for personalized assistance.</p>
                                <ul>
                                    <li><b>Phone : </b> +1-800-555-ROCK (7625)</li>
                                    <li><b>Email : </b> support@rockwellautomation.com</li>
                                </ul>
                            </div>
                        </div>
                    </section>
                </div>
            """

st.markdown(htmlString, unsafe_allow_html=True)


# Sidebar
with st.sidebar:
    if(st.session_state.name):
        st.header('Welcome "' + st.session_state.name + '"!')
        authenticator.logout('Logout', 'sidebar')