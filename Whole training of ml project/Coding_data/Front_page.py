import streamlit as st
import Diagnosis
import Mri
import Diagno
import About
from streamlit_option_menu import option_menu
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.exceptions import (LoginError,
                                                          RegisterError,) 
st.set_page_config(layout="wide", initial_sidebar_state="expanded")
#THE PAGE 1 CONTENT IS HERE:-
def page1():
    with open('C:\\Users\\goris\\OneDrive\\Documents\\Whole training of ml project\\Coding_data\\config.yaml') as file:
            config =  yaml.load(file, Loader=SafeLoader)

    # Creating the authenticator object
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['pre-authorized']
    )

        # Function to display a video background
    def display_video_background(video_url):
        video_html = f"""
        <video autoplay muted loop playsinline width="100%">
            <source src="{video_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        """
        css_code = """
        <style>
        video {
            position: fixed;
            top: 0%;
            left: 0%;
            min-width: 100%;
            min-height: 100%;
            height: auto;
        }
        </style>
        """
        # Display the video background and the Streamlit app content
        st.markdown(video_html + css_code, unsafe_allow_html=True)
    # Function to display animated text
    def display_animated_text(*texts):
        css = """
        @import url('https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400..700&display=swap'); 
        @keyframes typing {
          from { width: 0 }
          to { width: 100% }
        }
        .typewriter {
          overflow: hidden;
          border-right: .15em solid transparent; 
          white-space: nowrap; 
          margin: 0 auto; 
          letter-spacing: .15em; 
          animation: typing 4.8s steps(45, end); 
          animation-fill-mode: forwards;
          margin: 0; 
          margin-left:35%;
          left: 10pxpx; 
          font-size: 65px; 
          font-family: "Pixelify Sans", sans-serif;
          font-weight: 700;
          font-style: normal;
        }
        """
        # Render CSS styles
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
        # Display animated text
        for text in texts:
         st.markdown(f"<div class='typewriter'>{text}</div>", unsafe_allow_html=True)
    def display_glass_card(*cards):
        css = """
        @import url('https://fonts.googleapis.com/css2?family=Recursive:wght@300..1000&display=swap');
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(-10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .glass-morphism-card {
            animation-name: fadeIn;
            animation-duration: 1s;
            animation-timing-function: ease-in;
            animation-fill-mode: both;
            animation-delay: 2s;
            background: rgba(7, 25, 40, 0.45); 
            border-radius: 10px; 
            backdrop-filter: blur(10px);
            border: 1px solid rgba( 255, 255, 255, 0.18 );
            padding: 20px;
            position: relative; 
            z-index: 1;
        }
        .fonnt{
         font-family: "Recursive", sans-serif;
         font-optical-sizing: auto;
         font-size: 20px;
         font-weight: 700;
         font-style: normal;
         font-variation-settings:
         "slnt" 0,
         "CASL" 0,
         "CRSV" 0.5,
         "MONO" 0;
        }
        .fonnt2{
         font-family: "Recursive", sans-serif;
         font-optical-sizing: auto;
         font-weight: 400;
         font-style: normal;
         font-variation-settings:
         "slnt" 0,
         "CASL" 0,
         "CRSV" 0.5,
         "MONO" 0;
        }
        """
        # Render CSS styles
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
        # Create a container to hold the glass div and button
        st.markdown('<div style="position: relative;">', unsafe_allow_html=True)
        # Display the glass div
        for card in cards:
            st.markdown(f"<div class='glass-morphism-card'>{card}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        # Close the container
        st.markdown('</div>', unsafe_allow_html=True)
    def main():
        # Display video background
        video_url = "https://cdn.discordapp.com/attachments/1219334215708053546/1237280442349125733/TensorPix_-_Untitled_video_-_Made_with_Clipchamp.mp4?ex=663b12b5&is=6639c135&hm=3ed4cf51503af4b5372f11d399c708e4489ddff9b4c123e4aa2aa23f70d5c7d6&"
        display_video_background(video_url)
        # Display animated text
        display_animated_text("Diagno.AI")
        # Display card with button
        display_glass_card("<div><p class='fonnt'>What is Diagno.AI</p><p class='fonnt2'>At Diagno.ai, we harness the power of Artificial Intelligence to revolutionize healthcare. Our cutting-edge machine learning models, including predictive disease diagnosis and personalized medicine recommendations, are paving the way for a healthier future.</p><p class='fonnt'>Predictive Disease Diagnosis</p><p class=fonnt2>Our AI-powered platform analyzes medical data with unparalleled accuracy, providing timely predictions of potential diseases based on symptoms and patient history. From common ailments to rare conditions, Diagno.ai offers insights that empower informed decision-making and proactive healthcare management.</p><p class='fonnt'>Personalized Medicine Recommendations</p><p class='fonnt2'>Every individual is unique, and so are their healthcare needs. Diagno.ai leverages AI to tailor treatment recommendations, considering factors such as genetic predispositions,age and medication responses. With personalized medicine, we strive to optimize patient outcomes and enhance quality of life.</p><p class='fonnt'>MRI Detection AI Model</p><p class='fonnt2'>In addition to predictive diagnosis and personalized treatment, Diagno.ai pioneers the use of AI in MRI analysis. Our advanced algorithms can detect subtle abnormalities in medical imaging, aiding radiologists and clinicians in early detection and precise diagnosis.</p><p class='fonnt'>Get Started Today</p><p class='fonnt2'>Register or log in to unlock the full potential of Diagno.ai. Together, let's redefine healthcare for a brighter, healthier tomorrow.</p></div>")
    if __name__ == "__main__":
        main()
    #Side-bar
    def toggle_sidebar():
        # Get the current state of the sidebar
        is_expanded = not st.session_state.sidebar_expanded
        # Toggle the state
        st.session_state.sidebar_expanded = is_expanded
    # Initialize the state variable to control sidebar expansion
    if 'sidebar_expanded' not in st.session_state:
        st.session_state.sidebar_expanded = False
    #coding for the sidebar:
    col1,col2,col3= st.columns(3)
        # Add the button inside the column
    with col2:
            button_container = st.empty()
            with button_container.container():
                if st.button("Login or Register", use_container_width=True,type="primary"):
                        toggle_sidebar()
    # Conditionally display content based on sidebar state
    if st.session_state.sidebar_expanded:
        with st.sidebar:
            selected = option_menu("Register/Login", ["Register", 'Login','Logout'], 
                                    icons=['box-arrow-in-right', 'door-open-fill','box-arrow-in-left'], 
                                    menu_icon="file-person-fill")
        if selected == "Register":
            with st.sidebar:   
                try:
                    (email_of_registered_user,
                    username_of_registered_user,
                    name_of_registered_user) = authenticator.register_user(pre_authorization=False)
                    if email_of_registered_user:
                        st.success('User registered successfully!!')
                        st.markdown('<h6 style="color:White; font-size: 16px"> **you can go to the login page and enter the site</h6>', unsafe_allow_html=True)
                except RegisterError as e:
                    st.error(e)
        if selected == "Login":
            with st.sidebar:
                try:
                    authenticator.login()
                except LoginError as e:
                    st.error(e)
                if st.session_state["authentication_status"]:
                     st.markdown('<h6 style="color:#0add08; font-size: 17px">The user has logged in, you can enter the site now!!</h6>', unsafe_allow_html=True)
                     if st.button("Double click to enter the site!", use_container_width=True):
                            st.session_state.current_function = "page2"
                elif st.session_state["authentication_status"] is False:
                    st.error('Username/password is incorrect')
        if selected == "Logout":
            with st.sidebar:
                if st.session_state["authentication_status"]:
                    with st.container(border=True):
                        st.subheader('Logout')
                        st.checkbox(f'Are you sure you want to log out, {st.session_state["name"]}?', key='verify_logout')
                        if st.session_state.verify_logout:
                            authenticator.logout()
                else:
                    st.success("User is logged out")

    # Saving config file
    with open('C:\\Users\\goris\\OneDrive\\Documents\\Whole training of ml project\\Coding_data\\config.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(config, file, default_flow_style=False)

##THE PAGE 2 CONTENT IS HERE:-
def page2():
    defaultindex = 0
    selected2 = option_menu(f"welcome in, {st.session_state["name"]}", ["MRI-Diagnosis", "General-Diagnosis", "Diagno Bot", "About"], 
                                    icons=["upc scan", "prescription2","robot","info-circle-fill"], default_index=defaultindex,
                                    menu_icon="person-square", orientation="horizontal", styles={
                                        'container':{'font-size':'18px',"margin-left":"0%","margin-right":"0%"}
                                        })
    if selected2=="General-Diagnosis":
        Diagnosis.main()
    elif selected2=="MRI-Diagnosis":
        Mri.main()
    elif selected2=="Diagno Bot":
        Diagno.main()
    elif selected2=="About":
        About.main()
        #if st.button("Double click to go back to front page"):
        #    st.session_state.current_function="page1"

def main():
    if "current_function" not in st.session_state:
        st.session_state.current_function = "page1"
    if st.session_state.current_function == "page1":
        page1()
    elif st.session_state.current_function == "page2":
        page2()

if __name__ == "__main__":
    main()