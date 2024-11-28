import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('car_price_model.pkl')

# Streamlit App Title
st.title("Car Price Prediction App")

# Sidebar Information
st.sidebar.header("Input Car Details")
st.sidebar.markdown("""
Use the sidebar to enter details about the car for price prediction.
""")

# Input Features
km_driven = st.sidebar.number_input("Kilometers Driven", min_value=0, value=50000, step=1000)
car_age = st.sidebar.number_input("Car Age (Years)", min_value=0, value=5, step=1)
fuel = st.sidebar.selectbox("Fuel Type", options=['Diesel', 'Petrol', 'CNG', 'LPG', 'Electric'])
seller_type = st.sidebar.selectbox("Seller Type", options=['Dealer', 'Individual', 'Trustmark Dealer'])
transmission = st.sidebar.selectbox("Transmission Type", options=['Manual', 'Automatic'])
owner = st.sidebar.selectbox("Owner Type", options=['First Owner', 'Second Owner', 'Third Owner', 
                                                    'Fourth & Above Owner', 'Test Drive Car'])

# Feature Encoding
feature_mapping = {
    'fuel': {'Diesel': 0, 'Petrol': 1, 'CNG': 2, 'LPG': 3, 'Electric': 4},
    'seller_type': {'Dealer': 0, 'Individual': 1, 'Trustmark Dealer': 2},
    'transmission': {'Manual': 0, 'Automatic': 1},
    'owner': {'First Owner': 0, 'Second Owner': 1, 'Third Owner': 2, 
              'Fourth & Above Owner': 3, 'Test Drive Car': 4}
}

# Encode user inputs
encoded_features = {
    'km_driven': km_driven,
    'car_age': car_age,
    'fuel': feature_mapping['fuel'][fuel],
    'seller_type': feature_mapping['seller_type'][seller_type],
    'transmission': feature_mapping['transmission'][transmission],
    'owner': feature_mapping['owner'][owner]
}

# Prediction
if st.button("Predict Selling Price"):
    input_df = pd.DataFrame([encoded_features])
    prediction = model.predict(input_df)
    st.success(f"Estimated Selling Price: ₹{prediction[0]:,.2f}")
