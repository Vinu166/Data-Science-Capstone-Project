import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model_path = 'car_price_model.pkl'  # Updated model file name
model = joblib.load(model_path)

# Streamlit App Title
st.title("Car Price Prediction App")

# Sidebar for User Input
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

# Create a DataFrame for user input
input_data = pd.DataFrame({
    'km_driven': [km_driven],
    'car_age': [car_age],
    'fuel': [fuel],
    'seller_type': [seller_type],
    'transmission': [transmission],
    'owner': [owner]
})

# One-Hot Encoding to match training data structure
input_data_encoded = pd.get_dummies(input_data)

# Align columns with the training data
# Ensure all expected columns are present, setting missing ones to 0
expected_columns = model.feature_names_in_
input_data_encoded = input_data_encoded.reindex(columns=expected_columns, fill_value=0)

# Prediction
if st.button("Predict Selling Price"):
    try:
        prediction = model.predict(input_data_encoded)
        st.success(f"Estimated Selling Price: ₹{prediction[0]:,.2f}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
