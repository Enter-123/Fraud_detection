import streamlit as st
import pandas as pd
import joblib
import imblearn


# Load model
model = joblib.load("fraud_detection_pipeline.pkl")

st.title("💳 Fraud Transaction Detection")

# Inputs
step = st.number_input("Step", min_value=0, value=1)
type_ = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
nameOrig = st.text_input("Sender Account", value="C123456789")
oldbalanceOrg = st.number_input("Old Balance Origin", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance Origin", min_value=0.0, value=9000.0)
nameDest = st.text_input("Receiver Account", value="C987654321")
oldbalanceDest = st.number_input("Old Balance Destination", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance Destination", min_value=0.0, value=0.0)
isFlaggedFraud = st.selectbox("Is Flagged Fraud?", [0, 1])

# Create input DataFrame
input_df = pd.DataFrame([{
    "step": step,
    "type": type_,
    "amount": amount,
    "nameOrig": nameOrig,
    "oldbalanceOrg": oldbalanceOrg,
    "newbalanceOrig": newbalanceOrig,
    "nameDest": nameDest,
    "oldbalanceDest": oldbalanceDest,
    "newbalanceDest": newbalanceDest,
    "isFlaggedFraud": isFlaggedFraud
}])

# Prediction
if st.button("Predict Fraud"):
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("⚠️ This transaction is FRAUDULENT")
    else:
        st.success("✅ This transaction is NOT fraudulent")
