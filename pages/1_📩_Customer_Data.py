import pickle
from pathlib import Path
import pandas as pd
from PIL import Image
from streamlit_extras.switch_page_button import switch_page 
from streamlit.components.v1 import html
import streamlit as st
import streamlit_authenticator as stauth 

st.set_page_config(
    page_title="Dota 2 GA - Dataset",
    page_icon='📩',
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
    st.write("# Dataset")
    st.write('<i> What dataset is being utilized?</i>', unsafe_allow_html=True)
    df = pd.read_csv('dataset/base_dataset.csv')
    st.write(df)