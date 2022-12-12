import streamlit as st
import pickle
import pandas as pd
import numpy as np
import base64

hide_st_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# BACKGROUND IMAGE
def add_bg_from_local(photo):
    with open(photo, "rb") as photo:
        encoded_string = base64.b64encode(photo.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('photo.jpg')

st.title("Bike Price Prediction")

bike_data = pickle.load(open("Bike_data.pkl","rb"))
model=pickle.load(open('RegressionModel_bike.pkl','rb'))

Brand=sorted(bike_data['Brand'].unique())
year = sorted(bike_data['Year'].unique())

st.markdown("""
<style>
div[data-baseweb="select"] > div {
    background-color: #A4DCC5;
    width: 600px;
}
</style>""", unsafe_allow_html=True)

Selected_Brand = st.selectbox("Brand",Brand)

bike_model = bike_data.loc[bike_data['Brand'] == Selected_Brand]
Model=sorted(bike_model['Model'].unique())
Selected_Model = st.selectbox("Model",Model)
Selected_Year = st.selectbox("Year of Purchase",year)

Selected_Kms_driven = st.number_input("Distance Travelled", min_value=1)


Kms_driven = np.sqrt(Selected_Kms_driven)
Year = 2022-Selected_Year



_, _, _, col, _, _, _ = st.columns([1]*6+[1.18])

st.markdown("""
<style>
div.stButton > button:first-child {
    background-color:#e7e7e7;
    color:black;
}
div.stButton > button:hover {   
    background-color: #53CFBE;
    color:##ff99ff;
    }
</style>""", unsafe_allow_html=True)

if col.button('Predict'):
    pred=np.exp(model.predict(pd.DataFrame(columns=['Model', 'Brand', 'Years_used', 'Kms_driven_treated'],
                              data=np.array([Selected_Model,Selected_Brand,Year,Kms_driven]).reshape(1, 4))))

    prediction = str(int(np.round(pred[0],2)))
    st.write("### Predicted Price is : ₹",prediction)
    

st.markdown("""
<style>
div[class="stNumberInput"] > div {
    background-color: #A4DCC5;
    width: 600px;
}
</style>""", unsafe_allow_html=True)
st.markdown("""
<style>
div[data-baseweb="input"] > div {
    background-color: #A4DCC5;
}
</style>""", unsafe_allow_html=True)