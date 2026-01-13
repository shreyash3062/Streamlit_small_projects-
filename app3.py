import streamlit as st

st.title("simple calculator app")

num1 = st.number_input("enter first number")
num2 = st.number_input("enter second number")

operation = st.selectbox("choose operation", ["addition", "subtraction", "multiplication", "division"])

if st.button("result"):
    if operation == "addition":
        st.success(f"Result: {num1 + num2}")
    elif operation == "subtraction":
        st.success(f"Result: {num1 - num2}")
    elif operation == "multiplication":
        st.success(f"Result: {num1 * num2}")
    elif operation == "division":
        if num2 != 0:
            st.success(f"Result: {num1 / num2}")
        else:
            st.error("Division by zero not allowed!")

        