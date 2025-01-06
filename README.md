# Streamlit App: Sleep Health and Lifestyle Analysis

## Overview
This repository contains a Streamlit web application designed to analyze and visualize sleep health and lifestyle data. The app allows users to explore relationships between various factors such as sleep duration, quality of sleep, physical activity, stress levels, and more. The dataset used in this project includes information about individuals' sleep patterns, occupation, BMI, and whether they have sleep disorders.

## Features
- **Interactive Data Exploration**: Users can interact with the dataset through visualizations and filters.
- **Data Visualization**: The app includes various charts and graphs to help users understand trends and correlations in the data.
- **Predictive Insights**: The app provides insights into potential sleep disorders based on lifestyle and health metrics.
- **User-Friendly Interface**: Built with Streamlit, the app is easy to navigate and use.

## Dataset
The dataset used in this project is titled "Sleep_health_and_lifestyle_dataset.csv" and contains the following columns:
- **Person ID**: Unique identifier for each individual.
- **Gender**: Gender of the individual (Male or Female).
- **Age**: Age of the individual.
- **Occupation**: Occupation of the individual.
- **Sleep Duration**: Average hours of sleep per day.
- **Quality of Sleep**: Subjective rating of sleep quality.
- **Physical Activity Level**: Minutes of physical activity per day.
- **Stress Level**: Subjective stress level.
- **BMI Category**: Body Mass Index category (e.g., Normal, Overweight, Obese).
- **Blood Pressure**: Blood pressure measurement (systolic/diastolic).
- **Heart Rate**: Resting heart rate (beats per minute).
- **Daily Steps**: Number of steps taken per day.
- **Sleep Disorder**: Indicates if the individual has a sleep disorder (e.g., None, Sleep Apnea, Insomnia).

## Installation
To run this Streamlit app locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hemalikaa/Streamlit-App.git
   cd Streamlit-App

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py

4. **Open your browser and navigate to http://localhost:8501 to view the app.**:
   
## Usage
This Streamlit app provides an interactive dashboard for exploring sleep health and lifestyle data. Here's how to use it:

### 1. **Filters**
   - **Select Gender**: Filter data by gender (Male or Female).
   - **Select Age Range**: Adjust the slider to filter by age (27 to 59 years).

### 2. **Visualizations**
   - **Occupation Distribution**: Pie chart showing the distribution of occupations.
   - **Sleep Disorder Distribution**: Bar chart showing sleep disorders (Insomnia, Sleep Apnea) by occupation.
   - **Sleep Duration vs Physical Activity**: A scatter plot showing the relationship between sleep duration and physical activity.
   - **Sleep Quality by Occupation**: The bar chart shows average sleep quality scores by occupation.

### 3. **Correlation Matrix**
   - View relationships between variables like Age, Sleep Duration, Stress Level, Heart Rate, and Daily Steps.

### 4. **Interactivity**
   - Use filters to update charts dynamically.
   - Hover over visualizations for detailed insights.

### Example Workflow
1. Filter by gender and age.
2. Explore occupation distribution.
3. Analyze sleep disorders and sleep quality.
4. Study correlations between variables.
