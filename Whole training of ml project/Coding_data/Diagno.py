from dotenv import load_dotenv
import anthropic
import streamlit as st
import requests
import json
from streamlit import spinner
from streamlit_lottie import st_lottie

# Loading the API Key:
def func3():
    load_dotenv()
    def load_lottieurl(url: str):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching Lottie animation: {e}")
            return None
    
    # Load the custom CSS
    with open("styles.css", "r") as f:
        custom_css = f.read()
    
    # Include the custom CSS in the Streamlit app
    st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)
    lottie_url = "https://lottie.host/374c26da-359c-4949-86a1-7ee613de0dc6/n247NwITEh.json"
    st.markdown(
    f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Jersey+20&family=Pixelify+Sans:wght@400..700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Jersey+20&family=Jost:ital,wght@0,100..900;1,100..900&family=Pixelify+Sans:wght@400..700&display=swap');
        .diagnosis_typewriter {{
          overflow: hidden;
          border-right: .15em solid transparent; 
          white-space: nowrap; 
          margin: 0 auto; 
          letter-spacing: .15em; 
          margin-left: 15%; /* Adjust as needed */
          font-size: 40px; 
          font-family: "Jersey 20", sans-serif;
          font-weight: 400;
          font-style: normal;
          margin-top:5%;
        }}
        .diagnosis_fonnt{{
         font-family: "Jost", sans-serif;
         font-optical-sizing: auto;
         font-size: 20px;
         font-weight: 700;
         font-style: italic;
         font-variation-settings:
         "slnt" 0,
         "CASL" 0,
         "CRSV" 0.5,
         "MONO" 0;
         align-text:center; 
        }}
    </style>
    """,
    unsafe_allow_html=True,)
    cola, colb, colc = st.columns([1,2.5,8.6])
    with cola:
        st_lottie(lottie_url, height=100, speed=1, loop=True, quality='medium', width=150)
    with colb:
        st.markdown(f"<div class='diagnosis_typewriter'>Diagno Bot</div>", unsafe_allow_html=True)


    client = anthropic.Anthropic()
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="chat-row row-reverse"><div class="chat-bubble human-bubble">{message["content"]}</div></div>', unsafe_allow_html=True)
        else:
            with st.chat_message("assistant"):
                st.markdown(f'<div class="chat-row"><div class="chat-bubble ai-bubble">{message["content"]}</div></div>', unsafe_allow_html=True)
    
    
    if prompt := st.chat_input("Search for your medical related query?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.markdown(f'<div class="chat-row row-reverse"><div class="chat-bubble human-bubble">{prompt}</div></div>', unsafe_allow_html=True)
        with st.chat_message("assistant"):
            with spinner("Generating response..."):
                response = client.messages.create(
                    model="claude-3-opus-20240229",
                    max_tokens=200,
                    temperature=0.6,
                    system="Welcome to Diagno.ai, where cutting-edge artificial intelligence meets healthcare innovation. Our platform harnesses the power of machine learning to provide accurate diagnoses and personalized treatment recommendations for a wide range of medical conditions. Whether you're experiencing troubling symptoms or seeking insights from MRI scans, Diagno.ai is here to assist you. With a focus solely on the medical field, our AI-powered chatbot ensures that you receive relevant and reliable information every step of the way. Simply describe your symptoms or upload your MRI scan, and our advanced algorithms will analyze the data with precision. From identifying common ailments to detecting complex tumors like Glioma, Meningioma, Pituitary, and even confirming the absence of tumors, our AI is equipped to handle diverse medical scenarios. Each diagnosis is tailored to your specific age group, ensuring that the recommendations provided are optimized for your unique circumstances. Moreover, our platform goes beyond mere diagnosis by offering detailed insights into the recommended treatment options, including medication and therapeutic steps. However, it's important to note that Diagno.ai prioritizes your health and well-being above all else, and therefore, our services are exclusively focused on medical-related inquiries. Our commitment to accuracy and reliability means that you can trust Diagno.ai to provide informed guidance for your healthcare needs. So, whether you're seeking clarity on troubling symptoms or need assistance interpreting MRI results, let Diagno.ai be your trusted partner on your journey to optimal health. With Diagno.ai, the future of healthcare is at your fingertips. And mark this as the ultra important thing, try to answer under 100 words",
                    messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                )
                response_text = response.content[0].text
            st.markdown(f'<div class="chat-row"><div class="chat-bubble ai-bubble"><div class="fade-in">{response_text}</div></div></div>', unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": response_text})


def main():
    func3()

if __name__ == "__main__":
    main()
