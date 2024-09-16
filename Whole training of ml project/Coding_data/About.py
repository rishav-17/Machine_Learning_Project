import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie
import streamlit_shadcn_ui as ui
import requests
import plotly.io as pio
def func4():
    css="""@import url('https://fonts.googleapis.com/css2?family=Jersey+20&family=Pixelify+Sans:wght@400..700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Jersey+20&family=Jost:ital,wght@0,100..900;1,100..900&family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&family=Pixelify+Sans:wght@400..700&display=swap');
    .typewriter {
          overflow: hidden;
          border-right: .15em solid transparent; 
          white-space: nowrap; 
          margin: 0 auto; 
          letter-spacing: .15em; 
          margin-left: 2%; /* Adjust as needed */
          font-size: 40px; 
          font-family: "Jersey 20", sans-serif;
          font-weight: 400;
          font-style: normal;
        }
    .fonnt{
         font-family: "Lato", sans-serif;
         font-optical-sizing: auto;
         font-size: 16px;
         font-weight: 400;
         font-style: italic;
         margin-left:2%;
         font-variation-settings:
         "slnt" 0,
         "CASL" 0,
         "CRSV" 0.5,
         "MONO" 0;
         align-text:center; 
        } 
    .linkk{
       color: white !important;  
        }  
    .linkk:hover {
        color:  #33FFFF !important;
        }
    .button-link {
        display: inline-block;
        background-color: #007bff;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        border-radius: 5px;
        cursor: pointer;
        color: white !important;
        border-radius: 12px;
        } 
    .button-link:hover{
        background-color: #0056b3; 
        text-decoration: none; 
    }
    """
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    conf_matrix_1 = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ]
    fig_1 = px.imshow(conf_matrix_1,  
                labels=dict(x="Real Values", y="Values Calculated by AI", color="Productivity"),
                x=['Jaundice', 'Paralysis', 'Hypothyroidism', 'Impetigo', 'Hepatitis A', 'Common Cold', 'Hypoglycemia','Allergy', 'Vertigo',"Hypoglycemia","Arthritis"],
                y=['Jaundice', 'Vertigo', 'Hypothyroidism', 'Acne', 'Hepatitis A', 'Common Cold', 'Hypoglycemia','Allergy', 'Vertigo',"Hypoglycemia","Arthritis"],
                text_auto=True,
                aspect="auto",
                color_continuous_scale='Viridis',
                )
    confusion_matrix_2=[[140,  10,   0,   0],
                        [  6, 133,   8,   6],
                        [  0,   0, 203,   0],
                        [  0,   1,   0, 149]]
    fig_2=    fig = px.imshow(confusion_matrix_2,  
                labels=dict(x="Real Values", y="Values Calculated by AI", color="Productivity"),
                x=["Pitutary","No Tumor","Meningioma","Glioma"],
                y=["Pitutary","No Tumor","Meningioma","Glioma"],
                text_auto=True,
                aspect="auto",
                color_continuous_scale='Viridis'
                )
    st.markdown("""
        <div style=" padding: 10px; border-radius: 10px;">
        <div class="typewriter">App's Mission</div>
        <p class="fonnt">Our mission is simple yet ambitious: to empower individuals with timely and accurate medical insights, enabling them to take proactive steps towards better health. Through our AI-driven platform, we aim to bridge the gap between medical expertise and patient care, ensuring that everyone has access to the information and support they need to make informed healthcare decisions.</p>
        <div class="typewriter">Values We Uphold</div>
        <ul>
        <li class="fonnt" style="margin-left:3%"><b>Innovation</b>: We are committed to pushing the boundaries of what's possible in healthcare technology, constantly exploring new avenues for improving diagnosis, treatment, and patient outcomes.</li>
        <li class="fonnt" style="margin-left:3%"><b>Accuracy</b>: Accuracy is at the core of everything we do. We prioritize precision in our AI models and strive to deliver reliable medical information that users can trust.</li>
        <li class="fonnt" style="margin-left:3%"><b>Empowerment</b>: We believe in empowering individuals to take control of their health. By providing personalized insights and actionable recommendations, we enable users to make informed choices about their well-being.</li>
        </ul>
        <div class="typewriter">Technologies</div>
        <ul>
        <p class="fonnt">Diagno AI harnesses the latest advancements in artificial intelligence and machine learning to provide users with accurate and efficient medical solutions. Our CNN model enables precise MRI analysis, while robust algorithms drive symptom evaluation and diagnosis. Also using the modern machine learning algorithms we focus upon providing the best outcome after getting symptoms of any particular disease</p>
        </ul>
        <div class="typewriter", style="font-size: 24px">For General Diagnosis system:</div>
        <ul>
        <li class="fonnt" style="margin-left:3%"><b>Algorithm Used</b>: The Machine model i have used is the Random Forest Classification. It is a popular machine learning algorithm used for both classification and regression tasks. It belongs to the ensemble learning family, meaning it combines multiple individual models to create a more robust and accurate final model. <a class="linkk" href="https://en.wikipedia.org/wiki/Random_forest"> For furthur reference, click here!!</a></li>
        <li class="fonnt" style="margin-left:3%"><b>Accuracy</b>: Before deploying any model in our platform, we conduct extensive validation and evaluation procedures to assess its accuracy and reliability. This includes testing the model on diverse datasets, performing cross-validation to ensure generalization, and comparing its predictions to ground truth labels provided by medical experts. The accuracy of the model used here is: 93.089%. <a class="linkk" href="https://github.com/gurmindero7/6months_drug_recommendation_rishav_gndu/blob/main/Whole%20training%20of%20ml%20project/general_diseases/Random_Forest_practice.ipynb"> To get the information about dataset and accuracy, click here!!</a></li>
        <li class="fonnt" style="margin-left:3%"><b>Confusion Matrix</b>: Ensuring the accuracy of our AI models is essential for providing you with reliable medical diagnoses and treatment recommendations. The confusion matrix allows us to quantitatively measure our model's performance, giving you confidence in the results you receive from Diagno.AI. Now the confusion matrix is provided below: </li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    st.plotly_chart(fig_1, use_container_width=True)
    st.markdown("""
    <div class="typewriter", style="font-size: 24px">For MRI Diagnosis System:</div>
    <ul>
    <li class="fonnt" style="margin-left:3%"><b>Model Used</b>: The Machine learning model i have used here is Convolutional Nural Networks (CNN). It is a deep learning model designed for image processing. They use layers of filters to scan images for patterns, reducing complexity through pooling layers. Fully connected layers then classify the image. CNNs excel at tasks like image recognition and object detection, emulating human visual processing. <a class="linkk" href="https://en.wikipedia.org/wiki/Convolutional_neural_network"> For furthur reference, click here!!</a></li>
    <li class="fonnt" style="margin-left:3%"><b>Accuracy</b>: Before deploying any model in our platform, we conduct extensive validation and evaluation procedures to assess its accuracy and reliability. This includes testing the model on diverse datasets, performing cross-validation to ensure generalization, and comparing its predictions to ground truth labels provided by medical experts. The accuracy of the model used here is: 97%. <a class="linkk" href="https://github.com/gurmindero7/6months_drug_recommendation_rishav_gndu/blob/main/Whole%20training%20of%20ml%20project/MRI_Brain/cnn-model-1.ipynb"> To get the information about dataset and accuracy, click here!!</a></li>
    <li class="fonnt" style="margin-left:3%"><b>Confusion Matrix</b>: Ensuring the accuracy of our AI models is essential for providing you with reliable medical diagnoses and treatment recommendations. The confusion matrix allows us to quantitatively measure our model's performance, giving you confidence in the results you receive from Diagno.AI. Now the confusion matrix is provided below: </li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    st.plotly_chart(fig_2, use_container_width=True)
    st.markdown("""
        <div style=" padding: 10px; border-radius: 10px;">
        <div class="typewriter">Continuous Improvement</div>
        <p class="fonnt">We're committed to continuous improvement, and the insights gained from the confusion matrix play a crucial role in that process. By leveraging this valuable tool, we're constantly refining our AI algorithms to deliver even more accurate and reliable medical insights.</p>
        """, unsafe_allow_html=True)
    cola, colb= st.columns(2)
    with cola:
            st.markdown("""
        <div style=" padding: 10px; border-radius: 10px;">
        <div class="typewriter" style="margin-left: 4.2%">Contact Us</div>""", unsafe_allow_html=True)
            st.write("---")
            st.markdown("""
        <div style=" padding: 10px; border-radius: 10px;">
        <p class="fonnt" style="font-size: 18px", "Margin-left=4.2%"> My name is Rishav Chopra. I am studying Bachelors in Computer science. I am pretty enthusiactic about the Data Science and Machine Learning field. This project would help me to understand the concepts of Artificial intelligence and the required Machine learning which would be beneficial for my further projects and study purposes. </p>
        <p class="fonnt" style="font-size: 18px;color: #00FFFF;","Margin-left=4.2%">For any inquiry or any feed back you can email me by clicking the button below:</p>
        <a href="https://mail.google.com/mail/?view=cm&fs=1&to=rishavchopra1080@gmail.com" class="button-link" style="margin-left:2%">E-Mail</a>
        """, unsafe_allow_html=True) 
               
    with colb:
        def load_lottieurl(url: str):
            r= requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        lottie_hello=load_lottieurl("https://lottie.host/147f93c1-ba2c-4f57-9c27-a06778eb8435/tZIkc3FV6E.json")
        st_lottie(
            lottie_hello,
            speed=1,
            reverse= False,
            loop=True,
            quality= "medium",
            height=430,
            width=700,
        )

def main():
    func4()

if __name__ == "__main__":
    main()