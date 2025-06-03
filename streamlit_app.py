import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
pipeline = joblib.load("pipeline.pkl")

st.title("HDB Flat Resale Price Predictor")

# User inputs
year = st.slider("Year of Resale Transaction", 2025, 2030, 2025)
town = st.selectbox("Town", ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH', 'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST', 'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL', 'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN'])
flat_type = st.selectbox("Flat Type", ['1 ROOM', '2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE', 'MULTI-GENERATION'])
flat_model = st.selectbox("Flat Model", ['2-room', 'Adjoined flat', 'Apartment', 'DBSS', 'Improved', 'Improved-Maisonette', 'Maisonette', 'Model A', 'Model A-Maisonette', 'Model A2', 'Multi Generation', 'New Generation', 'Premium Apartment', 'Premium Apartment Loft', 'Premium Maisonette', 'Simplified', 'Standard', 'Terrace', 'Type S1', 'Type S2'])
floor_area_sqm = st.number_input("Floor Area (square meters)", 0)
storey_range_mean = st.slider("Storey", 1, 50, 1)
remaining_lease_years = st.slider("Remaining Lease (years)", 1, 99, 1)

# Build input DataFrame
input_df = pd.DataFrame([{
    "floor_area_sqm": floor_area_sqm,
    "storey_range_mean": storey_range_mean,
    "remaining_lease_years": remaining_lease_years,
    "year": year,
    "town": town,
    "flat_type": flat_type,
    "flat_model": flat_model
}])

if st.button("Predict HDB Flat Resale Price"):
    prediction = pipeline.predict(input_df)
    st.success(f"Estimated HDB Flat Resale Price: ${prediction[0]:,.2f}")