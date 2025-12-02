import streamlit as st
import pickle
import numpy as np

# Load model from pickle file
with open("D:\Python_Course\Projects\simple linear regression\simple_linear_regression_project\linear_regression_house_prediction_model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit UI
st.title("🏡 House Price Prediction")

size = st.text_input("Enter the size of the house (in sq ft):")

if st.button("Predict"):
    if size.strip() == "":
        st.error("Please enter a valid number!")
    else:
        try:
            size_value = float(size)
            input_data = np.array([[size_value]])
            prediction = model.predict(input_data)
            st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")
        except:
            st.error("Please enter a valid numeric value!")
 
 # To run the app, use the command:
 # streamlit run main.py