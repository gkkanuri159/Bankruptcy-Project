#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 11:53:15 2023

@author: geetakanuri
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st

pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

def main():
    st.title("Bankruptcy Predictor")
    industrial_risk = st.text_input("Industrial Risk", "Type Here")
    management_risk = st.text_input("Management Risk", "Type Here")
    financial_flexibility = st.text_input("Financial Flexibility", "Type Here")
    credibility = st.text_input("Credibility", "Type Here")
    competitiveness = st.text_input("Competitiveness", "Type Here")
    operating_risk = st.text_input("Operating Risk", "Type Here")
    result = ""
    if st.button("Predict"):
        result = predict(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk)
        st.success('The output is {}'.format(result))
    if st.button("About"):
            st.text("Bankruptcy is 0,Non-Bankruptcy is 1")

def predict(industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk):
    prediction = classifier.predict([[industrial_risk, management_risk, financial_flexibility, credibility, competitiveness, operating_risk]])
    print(prediction)
    return prediction

if __name__ == '__main__':
    main()