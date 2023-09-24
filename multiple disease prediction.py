# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 12:57:24 2023

@author: Chege
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the models
diabetes_model = pickle.load(open("diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("HeartDisease_model.sav", 'rb'))
parkinsons_model = pickle.load(open("Parkinsons_model.sav", 'rb'))


# sidebar for navigation

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart disease Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity', 'heart', 'person'],
                           
                           default_index = 0)
    
# Diabetes prediction page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    #columns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies	= st.text_input("Number of Pregnancies")
    with col2:
        Glucose	= st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")
    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")	
    with col2:
        Insulin = st.text_input("Insulin level")
    with col3:
        BMI = st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age	= st.text_input("Age of the Person")
    
    
    # Code for prediction
    diabetes_diagnosis = ''
    
    # creating a button for brediction
    
    if st.button("Diabetes Test Result"):
        diabetes_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        if (diabetes_prediction[0]==1):
            diabetes_diagnosis = 'The Person is Diabetic'
        else:
            diabetes_diagnosis = 'The person is not Diabetic'
            
    st.success(diabetes_diagnosis)
    
    
if (selected == 'Heart disease Prediction'):
    
    #page title
    st.title('Heart disease Prediction using ML')
    
    # getting the input data from the user
    #columns for input fields
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        age = st.text_input('Age of the person')
    with col2:
        sex = st.text_input('Sex of the person')
    with col3:
        cp = st.text_input('Type of chest pain')
    with col4:
        trestbps = st.text_input('Resting blood pressure')	
    with col1:
        chol = st.text_input('Serum cholesterol in mg/dl')
    with col2:
        fbs = st.text_input('Fasting blood sugar')
    with col3:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col4:
        thalach = st.text_input('Maximum heart rate achieved')
    with col1:
       exang = st.text_input('Exercise induced angina')	
    with col2:
       oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col3:
       slope = st.text_input('Slope of the peak exercise ST segment')
    with col4:
       ca = st.text_input('Number of major vessels(0-3) colored by flourosopy')
    with col1:
       thal = st.text_input('Thal: 3= normal, 6 =fixed defect,7 = reversable defect')
   
    
    # Code for prediction
    Heart_disease_diagnosis = ''
    
    # creating a button for brediction
    
    if st.button("Heart Disease Test Result"):
        Heart_disease_prediction = heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        if (Heart_disease_prediction[0]==1):
            Heart_disease_prediction = 'The person does not have a Heart Disease'
        else:
            diabetes_diagnosis = 'The person has a Heart Disease'
            
    st.success(Heart_disease_diagnosis)
    
if (selected == 'Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction using ML')
    
    
    # getting the input data from the user
    #columns for input fields
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        Fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        Fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        Flo = st.text_input('MDVP:Flo(Hz)')	
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')	
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')	
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
       RPDE = st.text_input('RPDE')
    with col3:
       DFA = st.text_input('DFA')	
    with col4:
       spread1 = st.text_input('spread1')
    with col5:
       spread2 = st.text_input('spread2')
    with col1:
       D2 = st.text_input('D2')
    with col2:
       PPE = st.text_input('PPE')
      
      
    
    # Code for prediction
    parkinsons_diagnosis = ''
    
    # creating a button for brediction
    
    if st.button("Heart Disease Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[Fo, Fhi, Flo, Jitter_percent,
                                                           Jitter_Abs, RAP, PPQ, DDP,Shimmer, 
                                                           Shimmer, APQ3, APQ5,APQ, DDA,
                                                           NHR, HNR,RPDE,DFA,spread1, spread2, D2, PPE]])
        if (parkinsons_prediction[0]==1):
            parkinsons_prediction = 'The person does not have a Parkinsons Disease'
        else:
            parkinsons_prediction = 'The person has a Parkinsons Disease'
            
    st.success(parkinsons_diagnosis)