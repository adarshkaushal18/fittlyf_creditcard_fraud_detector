import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA

# Function to detect anomalies
def detect_anomalies(data, contamination=0.0017):
    # Initialize the Isolation Forest model
    model = IsolationForest(contamination=contamination, random_state=42)

    # Select only numeric features
    numeric_features = data.select_dtypes(include=[np.number])

    # Fit the model and predict anomalies
    model.fit(numeric_features)
    predictions = model.predict(numeric_features)

    # Convert predictions to binary labels (1 for anomaly, 0 for normal)
    data['predictions'] = np.where(predictions == -1, 1, 0)

    return data, model

# Upload file
st.title("Credit Card Fraud Detection")
uploaded_file = st.file_uploader("Upload your Excel file with credit card transactions", type=["xlsx"])

if uploaded_file:
    # Load the Excel file
    sheet_name = 'creditcard_test'
    transactions = pd.read_excel(uploaded_file, sheet_name=sheet_name)

    st.write("Data Preview")
    st.write(transactions.head())

    # Detect anomalies
    transactions, model = detect_anomalies(transactions)

    # Display results
    st.write("Anomaly Detection Results")
    st.write(transactions[['Time', 'Amount', 'predictions']].head())

    # Visualize the anomalies
    st.write("Visualizing Anomalies using PCA")
    pca = PCA(n_components=2)
    transactions['PC1'], transactions['PC2'] = pca.fit_transform(transactions.select_dtypes(include=[np.number])).T

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='PC1', y='PC2', hue='predictions', data=transactions, palette='viridis')
    plt.title('Anomaly Detection Results')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    st.pyplot(plt)
else:
    st.info("Please upload a file to start the anomaly detection.")
