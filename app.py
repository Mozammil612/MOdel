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
Preg = st.number_input('Enter the Number of times pregnant: ')
Plasma = st.number_input('Enter the Plasma glucose concentration: ')
blood = st.number_input('Enter the Diastolic blood pressure: ')
Tri = st.number_input('Enter the Triceps skin fold thickness: ')
insulin = st.number_input('Enter the 2-Hour serum insulin: ')
mass = st.number_input('Enter the Body mass index: ')
fun = st.number_input('Enter the Diabetespe digree function: ')
age = st.number_input('Enter the Age: ')



btn_click = st.button('Predict')

if btn_click == True:
    if Preg and Plasma and blood and Tri and insulin and mass and fun and age:
        querry = np.array([Preg, Plasma, blood,Tri,insulin,mass, fun, age])
        quer = querry.reshape(1,-1)
        pred = model.predict(querry)
        st.success(pred)
        
    else:
        st.error("Enter the Values Properly")



