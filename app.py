import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('Sleep_health_and_lifestyle_dataset.csv')
    return data
data = load_data()

# Load custom CSS using inline CSS
st.markdown(
    """
    <style>
    /* Apply font to all elements */
    * {
        font-family: 'monospace', sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app
st.title("Sleep Health and Lifestyle Dashboard")

# Filters
st.sidebar.header("Filters")
gender_options = data['Gender'].unique()
selected_gender = st.sidebar.multiselect('Select Gender', gender_options, default=gender_options)

age_range = st.sidebar.slider('Select Age Range', int(data['Age'].min()), int(data['Age'].max()), (int(data['Age'].min()), int(data['Age'].max())))

# Apply filters
filtered_data = data[(data['Gender'].isin(selected_gender)) & (data['Age'] >= age_range[0]) & (data['Age'] <= age_range[1])]

# Visualization 1: Pie Chart for Occupation Distribution
st.subheader("Occupation Distribution")
occupation_counts = filtered_data['Occupation'].value_counts().reset_index()
occupation_counts.columns = ['Occupation', 'Count']
fig1 = px.pie(occupation_counts, names='Occupation', values='Count', title='Occupation Distribution')
st.plotly_chart(fig1)

# Visualization 2: Stacked Bar Chart for Sleep Disorder Distribution by Occupation
st.subheader("Sleep Disorder Distribution by Occupation")
sleep_disorder_counts = filtered_data.groupby(['Occupation', 'Sleep Disorder']).size().unstack().fillna(0)
fig2 = px.bar(sleep_disorder_counts, x=sleep_disorder_counts.index, y=sleep_disorder_counts.columns,
              title='Sleep Disorder Distribution by Occupation', barmode='stack')
st.plotly_chart(fig2)

# Visualization 3: Scatter Plot 
st.subheader("Relationship Between Sleep Duration and Physical Activity Level")
fig3 = px.scatter(filtered_data, x='Sleep Duration', y='Physical Activity Level', color='Occupation',
                  title='Sleep Duration vs Physical Activity Level by Occupation', color_discrete_sequence=px.colors.qualitative.Plotly)
st.plotly_chart(fig3)

# Visualization 4: Box Plot for Sleep Quality by Occupation
occupations = filtered_data['Occupation'].unique()
color_map = {occ: px.colors.qualitative.Plotly[i % len(px.colors.qualitative.Plotly)] for i, occ in enumerate(occupations)}
st.subheader("Sleep Quality Distribution by Occupation")
fig4 = px.box(filtered_data, x='Occupation', y='Quality of Sleep', title='Sleep Quality by Occupation',
              color='Occupation', color_discrete_map=color_map)
st.plotly_chart(fig4)

# Visualization 5: Heatmap for Correlation Matrix
st.subheader("Correlation Matrix Heatmap")
numeric_columns = filtered_data.select_dtypes(include=['number'])
if not numeric_columns.empty:
    corr_matrix = numeric_columns.corr()
    fig5, ax4 = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', ax=ax4)
    st.pyplot(fig5)
else:
    st.write("No numeric columns available for correlation matrix.")

