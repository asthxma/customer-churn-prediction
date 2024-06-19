import streamlit as st
from PIL import Image
import numpy as np
from streamlit_extras.switch_page_button import switch_page 
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Churn Predition",
    page_icon=':money_with_wings:',
    layout="wide",
)

try:
    if st.session_state["authentication_status"]:
        st.sidebar.success(f'Welcome **{st.session_state["name"]}**!')
        st.sidebar.success('Select a Page')
    else:
        st.sidebar.success('Please Login to Access Pages')
except:
    st.sidebar.success('Please Login to Access Pages')

st.write("# Bank Customer Churn Prediction :sob:")
    
st.subheader('What is Dota 2?', divider='rainbow')
st.write("penjelasan mengenai blablablbala")