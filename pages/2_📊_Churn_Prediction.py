import pickle
from pathlib import Path
import joblib
import numpy as np

import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page 
from streamlit.components.v1 import html

def check_input(input_value, field_name):
    if input_value is None or (isinstance(input_value, str) and input_value.strip() == ''):
        st.warning(f"{field_name} is required.")
        return False
    return True

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
    st.write("# Customer Churn Prediction")
    st.write('<i>Predicting customer churn with precision, enabling strategic decisions and proactive measures.</i>', unsafe_allow_html=True)

    st.header("Customer Data Input", divider='rainbow')
    st.write("Enter customer data to predict churn with our algorithm!")

    col1, col2= st.columns(2)
    with col1:
        Gender = st.radio("Select the customer's gender",["Male", "Female"],index=None)
        Age = st.number_input("Input the customer's age",value=None, placeholder="Ex: 21")
        Country = st.radio("Specify the customer's country of residence",["France","Germany", "Spain"],index=None)
        CreditScore = st.number_input("Input the customer's credit score",value=None, placeholder="Ex: 670")
        Balance = st.number_input("Enter the customer's account balance (in $)",value=None, placeholder="Ex: 30000")
        Salary = st.number_input("Enter the customer's yearly salary (in $)",value=None, placeholder="Ex: 40000")
        IsActiveMember = st.radio("Is the customer an active bank member?",["Yes", "No"],index=None)
        NumOfProducts = st.number_input("How many of the bank's products is the customer using?",value=None, placeholder="Ex: 3")
    with col2:
        st.write("")

    st.subheader("Churn Prediction", divider='blue')
    modelpred = joblib.load("model.pkl")

    # Predict
    if st.button('Predict'):
        valid_input = True
        valid_input &= check_input(Gender, "Gender")
        valid_input &= check_input(Age, "Age")
        valid_input &= check_input(Country, "Country")
        valid_input &= check_input(CreditScore, "Credit Score")
        valid_input &= check_input(Balance, "Account Balance")
        valid_input &= check_input(Salary, "Yearly Salary")
        valid_input &= check_input(IsActiveMember, "Active Member Status")
        valid_input &= check_input(NumOfProducts, "Number of Products")

        if valid_input:
            try:
                Age = int(Age)
                CreditScore = float(CreditScore)
                Balance = float(Balance)
                Salary = float(Salary)
                Gender = 1 if Gender == "Male" else 0
                NumOfProducts = int(NumOfProducts)
                CreditAgeRatio = np.divide(CreditScore, Age, where=Age != 0, out=np.zeros_like(CreditScore, dtype=float))
                BalanceSalaryRatio = np.divide(Balance, Salary, where=Salary != 0, out=np.zeros_like(Balance, dtype=float))
                IsActiveMember = 1 if IsActiveMember == "Yes" else 0

                if Country == "France":
                    Germany = 0
                    Spain = 0
                elif Country == "Germany":
                    Germany = 1
                    Spain = 0
                else:
                    Germany = 0
                    Spain = 1

                input_data = np.array([[CreditScore, Gender, Age, Balance, NumOfProducts, IsActiveMember, CreditAgeRatio, BalanceSalaryRatio, Germany, Spain]])
                predictions = modelpred.predict(input_data)

                predictions_mapped = ["retain" if pred == 0 else "churn" for pred in predictions]
                if predictions == 0:
                    st.write('The customer is predicted to :green[<b>retain</b>].', unsafe_allow_html=True)
                    st.write("Recommendation: Offer a loyalty reward program to encourage continued engagement.")
                else:
                    st.write('The customer is predicted to :red[<b>churn</b>].', unsafe_allow_html=True)
                    st.write("Recommendation: Contact the customer to understand their needs better and offer personalized banking solutions \
                             or benefits to increase retention.")
            except ValueError:
                st.error("Please enter valid numeric values.")

try:
    if st.session_state["authentication_status"]:
        st.sidebar.success(f'You are logged in as **{st.session_state["name"]}**.')
        authenticator.logout("Logout", "sidebar")
    else:
        st.sidebar.success('Please Login to Access Pages')
except:
    st.sidebar.success('Please Login to Access Pages')