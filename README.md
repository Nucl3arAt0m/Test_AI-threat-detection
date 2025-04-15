# Test_AI-threat-detection
## Overview
Test_AI-threat-detection is a proof-of-concept project developed to explore AI-driven threat detection in network security. This project implements a basic machine learning model to identify potential network intrusions, focusing on Denial-of-Service (DoS) attacks, using a simplified dataset and Python-based tools. It serves as a learning exercise to demonstrate data preprocessing, model training, and evaluation for cybersecurity applications.
## Features

• Data Preprocessing: Cleans and prepares network traffic data for analysis.
• Machine Learning Model: Utilizes a Random Forest classifier to detect anomalies indicative of DoS attacks.
• Evaluation Metrics: Provides accuracy, precision, recall, and F1-score to assess model performance.
• Modular Codebase: Organized scripts for data handling, model training, and prediction.

## Requirements

Python 3.8+
Libraries:

pandas
scikit-learn
numpy


Dataset: NSL-KDD (or similar network traffic dataset, not included in the repository)

## Dataset
This project was tested with the NSL-KDD dataset, filtered for DoS and normal traffic. You can download it from NSL-KDD or use a similar network traffic dataset. Ensure the dataset is in CSV format or modify preprocess_data.py to handle other formats.

## Acknowledgments
• Inspired by open-source cybersecurity projects and the NSL-KDD dataset.
• Built as a learning project to explore AI in threat detection.
This project is licensed under the MIT License. See the LICENSE file for details.
Acknowledgments

Inspired by open-source cybersecurity projects and the NSL-KDD dataset.
Built as a learning project to explore AI in threat detection.

