import streamlit as st
import webbrowser
import base64

st.set_page_config(
    page_title="Auto_Price_Prediction")

hide_st_style = """
           <style>
            MainMenu {visibility: hidden;}
            footer {visibility: visible;}
            footer:before{
                content: "It is Machine Learning Model with an accuracy of 92%"; 
                display: block;
                position: relative;
                color: black;
                }
            footer:after{
                content: "Built by Pragya."; 
                display: block;
                position: relative;
                color: black;
                }
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



st.title("Auto Price Prediction (APP)")


st.write("""### Want to sell or buy a used Car or Bike?
You can use this resale value prediction for cars and bikes.""")



st.write("Check out [Github](https://github.com/pragya-vats/auto_price_prediction) for more information about this Project")


