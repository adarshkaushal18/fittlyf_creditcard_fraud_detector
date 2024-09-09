# Credit Card Fraud Detection with Isolation Forest

This project focuses on detecting fraudulent credit card transactions using the Isolation Forest machine learning algorithm. The application is built using Streamlit, providing an interactive web-based interface for users to upload transaction data, detect anomalies, and visualize results.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Data Requirements](#data-requirements)
- [Model Explanation](#model-explanation)
- [Results Visualization](#results-visualization)
- [Contributing](#contributing)

## Overview

Credit card fraud is a major concern in the financial industry, resulting in billions of dollars in losses annually. This project addresses the challenge of fraud detection by leveraging machine learning techniques to identify potential fraudulent transactions. The solution utilizes the Isolation Forest algorithm, which is well-suited for anomaly detection in high-dimensional datasets.

## Features

- **Anomaly Detection:** Uses the Isolation Forest algorithm to detect outliers that may indicate fraudulent transactions.
- **Interactive Dashboard:** Built with Streamlit to allow users to upload datasets, view data previews, and explore anomaly detection results.
- **Data Visualization:** Visualizes detected anomalies using PCA (Principal Component Analysis) to reduce dimensionality and display results on a 2D scatter plot.
- **Customizable Contamination Rate:** Allows users to adjust the contamination rate to fine-tune the sensitivity of the fraud detection model.

## Installation

To run this project locally, you need to have Python installed along with some essential libraries.

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/credit-card-fraud-detection.git
    cd credit-card-fraud-detection
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

   Ensure you have the following libraries in your `requirements.txt` file:
   ```text
   streamlit
   pandas
   numpy
   matplotlib
   seaborn
   scikit-learn
   ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

## Usage

1. **Upload Data:** Upload an Excel file containing credit card transaction data using the provided file uploader.
2. **Preview Data:** View a preview of the uploaded data.
3. **Anomaly Detection:** The app will automatically apply the Isolation Forest model to detect anomalies in the data.
4. **View Results:** Explore the results, including the anomaly detection labels, and visualize them using PCA-based scatter plots.

## Data Requirements

The application expects an Excel file containing credit card transaction data. The data should have numeric columns like `'Time'` and `'Amount'`. The model will only operate on numeric data and will ignore non-numeric columns. Ensure the dataset is clean and properly formatted for best results.

### Example File Format

| Time | Amount | ... |
|------|--------|-----|
| 1    | 20.50  | ... |
| 2    | 15.00  | ... |

## Model Explanation

The **Isolation Forest** algorithm is an unsupervised learning method designed specifically for anomaly detection. It isolates observations by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of the selected feature. The algorithm isolates anomalies closer to the root of the trees, making them easier to identify compared to normal data points.

## Results Visualization

The application provides a visual representation of the detected anomalies using **PCA (Principal Component Analysis)** to reduce the dimensionality of the dataset to two principal components. This allows for a clearer visualization of how anomalies differ from normal transactions in a scatter plot.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please feel free to submit a pull request or open an issue.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.
