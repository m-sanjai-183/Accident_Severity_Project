# AI-Powered Road Accident Severity Prediction

## Project Description

Road accidents are a major cause of injuries and fatalities worldwide. This project uses Artificial Intelligence (AI) and Machine Learning (ML) techniques to predict the severity of road accidents based on factors such as vehicle speed, weather conditions, traffic density, road conditions, and time of accident.

The system classifies accident severity into:
- Low Severity
- Medium Severity
- High Severity

## Problem Statement

Road accident severity prediction is important for improving road safety and emergency response. Traditional methods rely on manual analysis, which can be time-consuming. This project aims to develop an intelligent system that predicts accident severity using machine learning algorithms and historical accident data.

## Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Flask (Python)

### Database
- MySQL

### AI/ML Technologies
- TensorFlow
- Scikit-learn
- Pandas
- NumPy
- Matplotlib

## Modules

### 1. User Management
- User Registration
- User Login
- Authentication

### 2. Accident Data Collection
- Accident Data Entry
- Data Validation
- Data Storage

### 3. Data Preprocessing
- Data Cleaning
- Missing Value Handling
- Feature Engineering

### 4. Machine Learning Model
- Model Training
- Model Testing
- Model Evaluation

### 5. Severity Prediction
- Predict Accident Severity
- Display Prediction Results

### 6. Reports and Visualization
- Statistical Reports
- Graphical Analysis
- Model Performance Metrics

## ER Diagram

```text
+----------------+
|      USER      |
+----------------+
| User_ID (PK)   |
| Name           |
| Email          |
| Password       |
+----------------+
         |
         | 1
         |
         | M
+----------------------+
|   ACCIDENT_DATA      |
+----------------------+
| Accident_ID (PK)     |
| User_ID (FK)         |
| Speed                |
| Weather              |
| Traffic_Density      |
| Road_Condition       |
| Time_Of_Accident     |
+----------------------+
         |
         | 1
         |
         | 1
+-----------------------+
|  PREDICTION_RESULT    |
+-----------------------+
| Prediction_ID (PK)    |
| Accident_ID (FK)      |
| Severity_Level        |
| Prediction_Date       |
+-----------------------+

+-----------------------+
|  MODEL_PERFORMANCE    |
+-----------------------+
| Model_ID (PK)         |
| Accuracy              |
| Precision             |
| Recall                |
+-----------------------+
```
