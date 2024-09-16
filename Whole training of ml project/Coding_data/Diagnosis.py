import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import requests
import json
import streamlit_shadcn_ui as ui
from streamlit_lottie import st_lottie
import joblib
from streamlit_card import card
import pandas as pd
def func1():
    model=joblib.load("General_Diseases.pkl")
    csv_training="C:\\Users\\goris\\OneDrive\\Documents\\Whole training of ml project\\general_diseases\\Training.csv"
    csv_medicine="C:\\Users\\goris\\OneDrive\\Documents\\Whole training of ml project\\general_diseases\\Output_drugs.csv"
    csv_doctors="C:\\Users\\goris\\OneDrive\\Documents\\Whole training of ml project\\general_diseases\\Output_drugs.csv"
    df_train=pd.read_csv(csv_training)
    label_prognosis_dict = pd.Series(df_train.prognosis.values, index=df_train.label).to_dict()
    df_medicine=pd.read_csv(csv_medicine)
    medicine_dict_1= pd.Series(df_medicine.Under_13.values, index=df_medicine.name).to_dict()
    medicine_dict_2= pd.Series(df_medicine.Above_13.values, index=df_medicine.name).to_dict()
    doctors= pd.Series(df_medicine.Doctors.values, index=df_medicine.name).to_dict()
    def get_prognosis(label):
        return label_prognosis_dict.get(label, "Label not found in the data")
    def medicine_get_13(med1):
        return medicine_dict_1.get(med1,"data not found")
    def medicine_get(med2):
        return medicine_dict_2.get(med2,"data not found")
    def doctors_diss(doc1):
        return doctors.get(doc1,"data not found")
    def load_lottieurl(url: str):
        r= requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_hello=load_lottieurl("https://lottie.host/5496551d-d836-46e8-a890-da76a9eebd20/jDxuHql8OQ.json")
    def diagnosiss(*texts):
        css = """
        @import url('https://fonts.googleapis.com/css2?family=Jersey+20&family=Pixelify+Sans:wght@400..700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Jersey+20&family=Jost:ital,wght@0,100..900;1,100..900&family=Pixelify+Sans:wght@400..700&display=swap');
        .diagnosis_typewriter {
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
        }
        .diagnosis_fonnt{
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
        }
        """
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
        
        for text in texts:
            st.markdown(f"<div class='diagnosis_typewriter'>{text}</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    st.markdown('<div style="color:red; font-size: 13px; margin-bottom: 5px">**Note: Our machine learning predictions are not a substitute for professional medical advice; consult a doctor for accurate diagnosis. Use our platform for educational purposes and as a secondary opinion only.</div>', unsafe_allow_html=True)
    with col1:
        diagnosiss("Symptom Analysis")
        diagnosiss("<div><p class='diagnosis_fonnt'>Choose from the cards below and</p><p class='diagnosis_fonnt'>select the symptoms that match how</p><p class='diagnosis_fonnt'>you're feeling.</p><p class='diagnosis_fonnt'>Once you've selected your symptoms,</p><p class='diagnosis_fonnt'>click the button below to see possible</p><p class='diagnosis_fonnt'>diagnoses and drug recommendations.</p></div>")
    with col2:
        st_lottie(
            lottie_hello,
            speed=1,
            reverse= False,
            loop=True,
            quality= "medium",
            height=430,
            width=700,
        )
    num_containers = 32
    cols = st.columns(4)
    listt=["Yes","Mild","No"]
    Sympp=[
        'Itching', 'Skin Rash', 'Nodal Skin Eruptions', 'Chills', 'Joint Pain',
        'Stomach Pain', 'Acidity', 'Ulcers On Tongue', 'Vomiting', 'Burning Micturition',
        'Spotting Urination', 'Fatigue', 'Weight_gain', 'Anxiety', 'Cold Hands And Feets',
        'Mood Swings', 'Weight Loss', 'Restlessness', 'Patches In Throat', 'Cough',
        'High Fever', 'Excessive Sweating', 'Dehydration', 'Indigestion', 'Headache', 'Back Pain',
        'Constipation', 'Abdominal pain', 'Swelling of Stomach', 'Redness Of Eyes',
        'Runny Nose', 'Chest Pain'
    ]

    ls=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    variables = []  

    for i in range(num_containers):
        col_index = i % 4
        col = cols[col_index]

        with col:
            with st.container(border=True):
                label = f"{i+1}. Are you experiencing {Sympp[i]} ??"  
                symptom = st.selectbox(label=label, options=listt, index=2)
                if symptom == "Yes":
                    var_value = 1
                elif symptom == "Mild":
                    var_value = 1
                elif symptom == "No":
                    var_value = 0
            # variable value in the list
            variables.append(var_value)
            countt= sum(variables)
    colw,colx,coly=st.columns([2.5,2,2.5])
    colA,colB,colC= st.columns([2.5,2,1.3])
    colD,colE,colF= st.columns(3)
    with colx:
        with st.container(border=True):
            age=st.checkbox("Is the patient younger than the age of 13??")
    with colB:
        button1=ui.button("Analyse for the results!!",key="abc",className="bg-orange-500 text-white",)
        if button1:
                ans=model.predict([variables])
                diss=get_prognosis(ans[0])
                doc= doctors_diss(diss)
                med_under_13=medicine_get_13(diss)
                med_over_13=medicine_get(diss)
                if variables==ls:
                    with colE:
                        card(
                            title="The Diagnosis is:",
                            text="You have no issues, that's great!",
                            image="https://htmlcolorcodes.com/assets/images/colors/bright-green-color-solid-background-1920x1080.png",
                            key="card1"
                            )

                elif countt<3:
                    with colE:
                        card(
                            title="Issue:",
                            text="You need to atleast select 3 symptoms for our model to work efficiently!!",
                            image="https://htmlcolorcodes.com/assets/images/colors/red-color-solid-background-1920x1080.png",
                            key="card1"
                            )                  
                elif age:
                    with colE:   
                        card(
                            title="The Diagnosis is:",
                            text=(f"There is the chance of: {diss}, according to your provided symptoms."),
                            image="https://media.istockphoto.com/id/1401811766/vector/a-cute-round-robot-wearing-a-stethoscope-new-technologies-and-lifestyle.jpg?s=612x612&w=0&k=20&c=KcnoJHezDoLSrUMXHpAP4KBjxMd2XECUHG0irdLyhmE=",
                            key="card1"
                            )
                    with colD:
                        card(
                            title="The Medicines prescribed are:",
                            text=(f"{med_under_13}"),
                            image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWPXS5vKwz4HrDYX68IvGRUoPnD7GtsW0sRrg0zkBrSA&s",
                            key="card2"
                            )     
                    with colF:
                            card(
                            title="The Doctors you should consult:",
                            text=(f"{doc}"),
                            image="https://images.rawpixel.com/image_social_square/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvdjg2OC1zYXNpLTA2LmpwZw.jpg",
                            key="card3"
                            )
                else:
                    with colE:   
                        card(
                            title="The Diagnosis is:",
                            text=(f"There is the chance of: {diss}, according to your provided symptoms."),
                            image="https://media.istockphoto.com/id/1401811766/vector/a-cute-round-robot-wearing-a-stethoscope-new-technologies-and-lifestyle.jpg?s=612x612&w=0&k=20&c=KcnoJHezDoLSrUMXHpAP4KBjxMd2XECUHG0irdLyhmE=",
                            key="card1"
                            )
                    with colD:
                        card(
                            title="The Medicines prescribed are:",
                            text=(f"{med_over_13}"),
                            image="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWPXS5vKwz4HrDYX68IvGRUoPnD7GtsW0sRrg0zkBrSA&s",
                            key="card2"
                            )     
                    with colF:
                            card(
                            title="The Doctors you should consult:",
                            text=(f"{doc}"),
                            image="https://images.rawpixel.com/image_social_square/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvdjg2OC1zYXNpLTA2LmpwZw.jpg",
                            key="card3"
                            ) 
def main():
    func1()
if __name__ == "__main__":
    main()
