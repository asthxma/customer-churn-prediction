import pickle
from pathlib import Path
import pandas as pd
from PIL import Image

import streamlit as st
import streamlit_authenticator as stauth 
from streamlit_extras.switch_page_button import switch_page 
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Customer Data",
    page_icon='🖥️',
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
    st.write("# Dataset")
    st.write('<i> What dataset is being utilized? </i>', unsafe_allow_html=True)

    st.subheader('Base Dataset', divider='rainbow')
    st.write('Information about bank customers that includes various demographic, financial, and activity features.\
              These features are used to predict whether a customer will churn or retain.')
    df = pd.read_csv('dataset/base_dataset.csv')
    st.write(df)

    st.subheader('Processed Dataset', divider='violet')
    st.write('Dataset has been processed by removing irrelevant columns, converting categorical features to numeric,\
              feature scaling, and selecting significant features using ANOVA and Mutual Information, \
              resulting in high-quality data that is ready to be used to train machine learning \
              models to accurately predict customer churn.', unsafe_allow_html=True)
    df2 = pd.read_csv('dataset/modified_data.csv')
    st.write(df2)

try:
    if st.session_state["authentication_status"]:
        st.sidebar.success(f'You are logged in as **{st.session_state["name"]}**.')
        authenticator.logout("Logout", "sidebar")
    else:
        st.sidebar.success('Please Login to Access Pages')
except:
    st.sidebar.success('Please Login to Access Pages')