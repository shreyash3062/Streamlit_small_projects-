import streamlit as st
st.title("some basic commands like slider button etc")
age = st.slider("enter your age",1,100)
city = st.selectbox("choose your city",["pune","kolhapur","mumbai"])
if st.button("show details"):
    st.write("age is",age)
    st.write("city name is",city)