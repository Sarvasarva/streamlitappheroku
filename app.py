# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:26:24 2023

@author: Lenovo
"""

import numpy as np
import pickle
import streamlit as st

#Load the saved model

load_model=pickle.load(open('C:/Users/Lenovo/Documents/Data Science1/Machin Learning/Support Vector Machines/ML_Deployment/trainedmodel.sav','rb'))

#Creating a function for prediction

def loan_prediction(input_data):
    

    #Changing i/p data to numpy array
    toarrays=np.asarray(input_data)

    #Reshape array as we are predicting for one instance
    reshapearray=toarrays.reshape(1,-1)

    prediction=load_model.predict(reshapearray)
    print(prediction)

    if (prediction[0]==0):
        return "No Loan"
    else:
        return "Yes Loan"
    
    
def main():
    
    # giving a title
    st.title("Loan Prediction web app")
    
    # getting the i/p data from user
    
    ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Gender_1', 'Married_Yes',
       'Dependents_1', 'Dependents_2', 'Dependents_3',
       'Education_NotGraduate', 'Self_Employed_Yes',
       'Property_Area_Semiurban', 'Property_Area_Urban']
    
    
    ApplicantIncome= st.text_input("Income of the applicant")
    CoapplicantIncome= st.text_input("Income of the Coapplicant")
    LoanAmount= st.text_input("Loan amount")
    Loan_Amount_Term= st.text_input("loan amount term")
    Credit_History= st.text_input("Credit history")
    Gender_1= st.text_input("applicant gender")
    Married_Yes= st.text_input("Maritial status")
    Dependents_1= st.text_input("first dependent")
    Dependents_2= st.text_input("second dependent")
    Dependents_3= st.text_input("third dependent")
    Education_NotGraduate= st.text_input("applicant education")
    Self_Employed_Yes= st.text_input("applicant is self employed")
    Property_Area_Semiurban= st.text_input("property in suburban")
    Property_Area_Urban= st.text_input("property in urban")
    
    # code for prediction
    loanprocess= ''
    
    #Creating a button for prediction
    # Here 'loan_prediction' function is taken from 'def loan_prediction(input_data):' above
    
    if st.button('Loan Status'):
        loanprocess= loan_prediction([ApplicantIncome, CoapplicantIncome, LoanAmount,
           Loan_Amount_Term, Credit_History, Gender_1, Married_Yes,
           Dependents_1, Dependents_2, Dependents_3,
           Education_NotGraduate, Self_Employed_Yes,
           Property_Area_Semiurban, Property_Area_Urban])
    
    st.success(loanprocess)
    
if __name__=='__main__':
    main()
        
    
    
    
    
    