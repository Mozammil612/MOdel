import streamlit as st
import numpy as np
from pickle import load
import pickle

#Loading pretrained classifier from pickle file
model = pickle.load(open('knn_model.pkl', 'rb'))
scaler = pickle.load(open('scaler_model.pkl', 'rb'))
#model = pickle.load(open('knn_model.pkl', 'rb'))
#model = pickle.load(open(r'C:\Users\mozammil\OneDrive\Desktop\models\knn_model.pkl', 'rb'))

# Display user input fields

Preg = st.number_input('Enter the Number of times pregnant: ',min_value=0.0, max_value=1000.0, step=0.1e-6)
Plasma = st.number_input('Enter the Plasma glucose concentration: ',min_value=0.0, max_value=1000.0, step=0.1e-6)
blood = st.number_input('Enter the Diastolic blood pressure: ',min_value=0.0, max_value=1000.0, step=0.1e-6)
Tri = st.number_input('Enter the Triceps skin fold thickness: ',min_value=0.0, max_value=1000.0, step=0.1e-6)
insulin = st.number_input('Enter the 2-Hour serum insulin: ',min_value=0.0, max_value=1000.0, step=0.1e-6)
mass = st.number_input('Enter the Body mass index: ',min_value=0.0, max_value=1000.0, step=0.1e-6)
fun = st.number_input('Enter the Diabetespe digree function: ',min_value=0.0, max_value=1000.0, step=1.,format="%.2f")
age = st.number_input('Enter the Age: ',min_value=0.0, max_value=1000.0, step=0.1e-6)



btn_click = st.button('Predict')

if btn_click == True:
    if Preg and Plasma and blood and Tri and insulin and mass and fun and age:
        querry = np.array([Preg, Plasma, blood,Tri,insulin,mass, fun, age])
        quer = querry.reshape(1,-1)
        pred = model.predict(querry)
        st.success(pred)
        
    else:
        st.error("Enter the Values Properly")



