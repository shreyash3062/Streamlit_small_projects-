import streamlit as st
import google.generativeai as genai
st.title("welcome to my streamlit app")
user_input = st.text_input("ask me amything")
genai.configure(api_key="AIzaSyD-CVthktVp9DRBxm8YR3Ak5Wa_Q0PgdAI")
model = genai.GenerativeModel("models/gemini-2.5-flash")
if user_input:
    response = model.generate_content(user_input)
    st.write("response",response.text)
