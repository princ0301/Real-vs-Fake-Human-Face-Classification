# Real vs Fake Face Classification

This repository contains a Streamlit web application that classifies faces as either "Real" or "Fake" (AI-generated) using a pre-trained VGG16 model.

## Overview

This project aims to create a user-friendly interface for classifying human faces into two categories: real or AI-generated. The app leverages the convolutional neural network architecture for image classification. The app also provides a confidence score for the prediction.

### Features

- **Upload Images**: Users can upload in JPG, JPEG, or PNG formats.
- **Classification**: The model predict whether the uploaded image is real or AI-generated.
- **Confidence Score**: The app provides a confidence score for the classification.

## Usage

### 1. Clone the repository:
```bash
https://github.com/princ0301/Real-vs-Fake-Human-Face-Classification
cd Real-vs-Fake-Classification
```

## 2. Installation
```bash
pip install -r requirements.txt
```

## 3. Run the Streamlit app:
```gd
streamlit run application.py
```
## 4. Upload an image:
Upload an image to the interface to classify it as "Real" or "Fake" with a confidence score.
