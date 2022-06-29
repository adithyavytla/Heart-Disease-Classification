# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('forest.pkl','rb'))

with st.sidebar:
    st.write('Let us help you diagnose your heart')
    html_temp='''<img src="https://cdn.pixabay.com/photo/2022/06/17/12/56/doctor-7267871_960_720.jpg" width=310 height=575> '''
    st.markdown(html_temp, unsafe_allow_html=True)

def predict_heart_disease(BMI,Smoking,AlcoholDrinking,Stroke,PhysicalHealth,MentalHealth,DiffWalking,Sex,AgeCategory,Race,Diabetic,PhysicalActivity,GenHealth,SleepTime,Asthma,KidneyDisease,SkinCancer):
    AgeCatVal={'18-24':0,'25-29':1,'30-34':2,'35-39':3,'40-44':4,'45-49':5,'50-54':6,'55-59':7,'60-64':8,'65-69':9,'70-74':10,'75-79':11,'80 or older':12}
    Ethinicity={'White':0,'Hispanic':1,'Black':2,'Asian':3,'American Indian/Alaskan Native':4,'Other':5}
    GenVal={'Excellent':0,'Very good':1,'Good':2,'Fair':3,'Poor':4}
    Smoking=1*(Smoking=='Yes')
    AlcoholDrinking=1*(AlcoholDrinking=='Yes')
    Stroke=1*(Stroke=='Yes')
    DiffWalking=1*(DiffWalking=='Yes')
    Sex=1*(Sex=='Female')
    AgeCategory=AgeCatVal[AgeCategory]
    Race=Ethinicity[Race]
    Diabetic=1*(Diabetic=='Yes')
    PhysicalActivity=1*(PhysicalActivity=='Yes')
    GenHealth=GenVal[GenHealth]
    Asthma=1*(Asthma=='Yes')
    KidneyDisease=1*(KidneyDisease=='Yes')
    SkinCancer=1*(SkinCancer=='Yes')
    Physical_MentalHealth=PhysicalHealth+MentalHealth
    PhysicalHealth_log=np.log1p(PhysicalHealth)
    MentalHealth_log=np.log1p(MentalHealth)
    prediction=model.predict([[BMI,Smoking,AlcoholDrinking,Stroke,PhysicalHealth,MentalHealth,DiffWalking,Sex,AgeCategory,Race,Diabetic,PhysicalActivity,GenHealth,SleepTime,Asthma,KidneyDisease,SkinCancer,Physical_MentalHealth,PhysicalHealth_log,MentalHealth_log]])
    print(prediction)
    return prediction

def main():
    html_temp = """
    <div style="background:#FF4B4B ;padding:10px">
    <h2 style="color:white;text-align:center;"> Heart Disease Prediction </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    st.write("Complete the information and submit")
    BMI = st.slider('What is your BMI?',min_value=13,max_value=60, step=None)
    Smoking = st.selectbox('Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]', ['Yes','No'])
    AlcoholDrinking = st.selectbox('Do you consume alcohol?', ['Yes','No'])
    Stroke = st.selectbox('(Ever told) (you had) a stroke?', ['Yes','No'])
    PhysicalHealth=st.slider('Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30 days was your physical health not good? (0-30 days)',min_value=0,max_value=30,step=None)
    MentalHealth=st.slider('Thinking about your mental health, for how many days during the past 30 days was your mental health not good? (0-30 days)',min_value=0,max_value=30,step=None)
    DiffWalking=st.selectbox('Do you have serious difficulty walking or climbing stairs?', ['Yes','No'])
    Sex=st.selectbox('Are you a male or female', ['Male','Female'])
    AgeCategory=st.selectbox('Which age category do you belong to?', ['18-24','25-29','30-34','35-39','40-44','45-49','50-54','55-59','60-64','65-69','70-74','75-79','80 or older'])
    Race=st.selectbox('Your Ethinicity', ['White','Hispanic','Black','Asian','American Indian/Alaskan Native','Other'])
    Diabetic=st.selectbox('(Ever told) (you had) diabetes?', ['Yes','No'])
    PhysicalActivity=st.selectbox('Did you exercise during the past 30 days other than your regular job', ['Yes','No'])
    GenHealth=st.selectbox('Would you say that in general your health is...', ['Excellent','Very good','Good','Fair','Poor'])
    SleepTime=st.slider('On average, how many hours of sleep do you get in a 24-hour period?',min_value=1,max_value=12,step=None)
    Asthma=st.selectbox('(Ever told) (you had) asthma?', ['Yes','No'])
    KidneyDisease=st.selectbox('Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?', ['Yes','No'])
    SkinCancer=st.selectbox('(Ever told) (you had) skin cancer?', ['Yes','No'])
    x=0
    result=""
    if st.button('Predict'):
        x=predict_heart_disease(BMI,Smoking,AlcoholDrinking,Stroke,PhysicalHealth,MentalHealth,DiffWalking,Sex,AgeCategory,Race,Diabetic,PhysicalActivity,GenHealth,SleepTime,Asthma,KidneyDisease,SkinCancer)
        if x==0:
            result="Great!You are healthy,Congratulations"
        else:
            result="You will be fine soon please visit a doctor"
    if x==0:
        st.success('{}'.format(result))
    else:
        st.error('{}'.format(result))

if __name__=="__main__":
    main()
