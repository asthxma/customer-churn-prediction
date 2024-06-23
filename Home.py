from PIL import Image
import numpy as np

import streamlit as st
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

st.write("# Bank Customer Churn Prediction")
    
st.subheader('Customer Retention: A Crucial Aspect for Banking Sustainability and Growth', divider='blue')
st.write("Customer retention is a critical aspect for the sustainability and growth of banks. Loyal customers \
         provide a stable and more predictable source of revenue compared to new customers who may not be as loyal. \
         Additionally, the cost of acquiring new customers is significantly higher than the cost of retaining existing ones. \
         Therefore, focusing on customer retention can offer significant competitive advantages.")

st.write("A high churn rate, or customer turnover, is an indication of issues within the service, products, or customer relationships. \
        This can be detrimental to a bank in the long run, as losing customers can potentially decrease revenue and increase operational costs.\
        The main causes of churn can include customer dissatisfaction, poor service, uncompetitive products, or more attractive offers \
        from competitors.")