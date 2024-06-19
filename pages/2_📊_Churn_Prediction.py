import pickle
from pathlib import Path

import streamlit as st
import streamlit_authenticator as stauth 

import joblib
from PIL import Image
import numpy as np
from streamlit_extras.switch_page_button import switch_page 
from streamlit.components.v1 import html


st.set_page_config(
    page_title="Churn Prediction",
    page_icon='📊',
    layout="wide",
)

names = ["Administrator"]
usernames = ["admin"]

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    cookie_name="database", key="abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    st.session_state['user_authenticated'] = True
    authenticator.logout("Logout", "sidebar")
    st.subheader("Customer Data Input", divider='violet')
    col1, col2= st.columns(2)
    with col1:
        Gender = st.radio("Choose your gender",["Male", "Female"],index=None)
        Age = st.number_input('Enter your age',value=None, placeholder="Ex: 21")
        country = st.radio("Enter your place of residence (country)",["France","Germany", "Spain"],index=None)
        CreditScore = st.number_input('Enter your credit score',value=None, placeholder="Ex: 670")
        Balance = st.number_input('Enter your account balance ($)',value=None, placeholder="Ex: 30000")
        Salary = st.number_input('Enter your yearly salary ($)',value=None, placeholder="Ex: 40000")
        IsActiveMember = st.radio("Are you an active bank member?",["Yes", "No"],index=None)
        NumOfProducts = st.number_input('How many of our products are you using?',value=None, placeholder="Ex: 3")
    with col2:
        st.write("")

    st.subheader("Churn Prediction", divider='blue')
    rf_loaded = joblib.load("gboost2.pkl")

    # Make a prediction
    if st.button('Predict'):
        CreditScore = float(CreditScore)
        Age = float(Age)
        Gender = 1 if Gender == "Male" else 0
        CreditAgeRatio = np.divide(CreditScore, Age, where=Age != 0, out=np.zeros_like(CreditScore, dtype=float))
        BalanceSalaryRatio = np.divide(Balance, Salary, where=Salary != 0, out=np.zeros_like(Balance, dtype=float))
        if country == "France":
            Germany = 0
            Spain = 0
        elif country == "Germany":
            Germany = 1
            Spain = 0
        else:
            Germany = 0
            Spain = 1
        IsActiveMember = 1 if IsActiveMember == "Yes" else 0
        input_data = np.array([[CreditScore, Gender, Age, Balance, NumOfProducts, IsActiveMember, CreditAgeRatio, BalanceSalaryRatio, Germany, Spain]])
        predictions = rf_loaded.predict(input_data)

    # Map predictions to retain or churn
        predictions_mapped = ["retain" if pred == 0 else "churn" for pred in predictions]
        st.write(f"Prediction: {predictions_mapped}")

try:
    if st.session_state["authentication_status"]:
        st.sidebar.success(f'You are logged in as **{st.session_state["name"]}**.')
        st.sidebar.success('Select a Page')
    else:
        st.sidebar.success('Please Login to Access Pages')
except:
    st.sidebar.success('Please Login to Access Pages')