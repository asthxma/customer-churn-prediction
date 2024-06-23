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

st.write("# Welcome to Your Simple Solution for Banking Insights!")

st.subheader('Unlock the Power of Prediction with Ease', divider='rainbow')
st.write("At our platform, we simplify the way you understand your customers. Our user-friendly interface \
         allows bank administrators to effortlessly input customer details and generate accurate predictions about \
         customer behaviors, needs, and trends. No complex integrations or technical expertise required.")
image = Image.open('bank.jpg')
st.image(image, caption='Visualizing Customer Churn in Banking (Credit: Pijar Foundation)')

st.subheader('Why Choose Us?', divider='violet')
st.markdown(
"""
- Simplicity: Easily add customer details and get instant predictions without any technical hassle.
- Accuracy: Our advanced machine learning models ensure precise and reliable insights.
- Actionable Insights: Make informed decisions to enhance customer satisfaction and drive growth.
"""
)

st.subheader('Features', divider='blue')
st.markdown(
"""
- Easy Customer Data Entry \n
Admins can quickly log in and input customer information through a straightforward interface.
- Instant Predictions \n
Generate immediate predictions about customer behavior, risk of churn, and potential value.
- Personalized Insights \n
Receive tailored recommendations on how to best engage with each customer.
"""
)

st.subheader('How It Works', divider='green')
st.markdown(
"""
<b>1. Log In</b> \n
Access your secure admin dashboard with ease.\n
2. Add Customer Details\n
Enter customer information using our simple, intuitive form.\n
3. Generate Predictions \n
Click to generate instant, actionable insights about your customers.
""", unsafe_allow_html=False
)

st.write("# Get Started!")
data_customer = st.button("Dataset")
if data_customer:
    switch_page("Customer_Data")
churn_pred = st.button("Churn Prediction")
if churn_pred:
    switch_page("Churn_Prediction")
