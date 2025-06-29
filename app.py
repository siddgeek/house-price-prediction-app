import streamlit as st
import pandas as pd
import numpy as np
import joblib 

# Load trained model
model = joblib.load("model.pkl")

st.set_page_config(page_title="House Price Predictor", page_icon="🏡")
st.title("🏘️ End-to-End House Price Prediction App (19 Features, ML + Streamlit)")

st.markdown("Fill in the details below:")

# Input fields with corrected types
bedrooms = st.slider("Bedrooms", 0, 10, 3)
bathrooms = st.slider("Bathrooms", 0, 10, 2)
sqft_living = st.number_input("Living Area (sqft)", min_value=100, max_value=10000, step=50, value=1500)
sqft_lot = st.number_input("Lot Area (sqft)", min_value=100, max_value=100000, step=100, value=5000)
floors = st.slider("Floors", 1, 4, 1)
waterfront = st.selectbox("Waterfront", [0, 1])
view = st.slider("View Rating", 0, 4, 0)
condition = st.slider("Condition (1–5)", 1, 5, 3)
grade = st.slider("Grade (1–13)", 1, 13, 7)
sqft_above = st.number_input("Sqft Above Ground", min_value=100, max_value=10000, step=50, value=1200)
sqft_basement = st.number_input("Sqft Basement", min_value=0, max_value=5000, step=50, value=300)
yr_built = st.number_input("Year Built", min_value=1900, max_value=2025, step=1, value=2005)
yr_renovated = st.number_input("Year Renovated (0 if never)", min_value=0, max_value=2025, step=1, value=0)
zipcode = st.number_input("Zipcode", min_value=98001, max_value=98299, step=1, value=98178)
lat = st.number_input("Latitude", min_value=47.0, max_value=47.9, format="%.6f", value=47.511234)
long = st.number_input("Longitude", min_value=-122.9, max_value=-121.0, format="%.6f", value=-122.257)
sqft_living15 = st.number_input("Sqft Living (15 Neighbors)", min_value=100, max_value=10000, step=50, value=1500)
sqft_lot15 = st.number_input("Sqft Lot (15 Neighbors)", min_value=100, max_value=100000, step=100, value=5000)
date = st.selectbox("Sold after 2014?", [0, 1])

# Prediction
if st.button("Predict Price"):
    input_data = np.array([[
        bedrooms, bathrooms, sqft_living, sqft_lot, floors,
        waterfront, view, condition, grade, sqft_above,
        sqft_basement, yr_built, yr_renovated, zipcode,
        lat, long, sqft_living15, sqft_lot15, date
    ]])
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted House Price: ${prediction:,.2f}")
