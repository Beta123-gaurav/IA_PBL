import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load data
df = pd.read_csv("EA.csv")

st.set_page_config(page_title="Chronic Disease Health Dashboard", layout="wide")

st.title("🩺 Chronic Disease Health & Lifestyle Dashboard")
st.markdown("""
This dashboard provides comprehensive health & lifestyle insights for the HR Director and stakeholders. 
Use filters to explore chronic disease risks and lifestyle patterns among individuals.
""")

# Sidebar filters
st.sidebar.header("Filter Data")
age_range = st.sidebar.slider("Age Range", int(df["Age"].min()), int(df["Age"].max()), (20,60))
gender = st.sidebar.multiselect("Select Gender", options=df["Gender"].unique(), default=list(df["Gender"].unique()))
smoking = st.sidebar.multiselect("Smoking Status", options=df["Smoking"].unique(), default=list(df["Smoking"].unique()))

# Apply filters
filtered_df = df[
    (df["Age"] >= age_range[0]) &
    (df["Age"] <= age_range[1]) &
    (df["Gender"].isin(gender)) &
    (df["Smoking"].isin(smoking))
]

st.subheader("Filtered Data Preview")
st.dataframe(filtered_df.head(20))

# 1. Chronic disease distribution
st.subheader("Chronic Disease Distribution")
st.markdown("This pie chart shows the proportion of individuals with chronic disease versus those without.")
chronic_counts = filtered_df["Chronic disease"].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(chronic_counts, labels=chronic_counts.index, autopct='%1.1f%%', startangle=90)
st.pyplot(fig1)

# 2. Age distribution
st.subheader("Age Distribution")
st.markdown("This histogram shows how ages are distributed in the filtered dataset.")
st.hist(filtered_df["Age"], bins=30)

# 3. Gender distribution
st.subheader("Gender Distribution")
st.markdown("Bar chart showing gender breakdown in filtered data.")
gender_counts = filtered_df["Gender"].value_counts()
st.bar_chart(gender_counts)

# 4. BMI vs Age by chronic disease
st.subheader("BMI vs Age by Chronic Disease")
st.markdown("This scatter plot shows BMI and age colored by chronic disease presence.")
fig2 = px.scatter(filtered_df, x="BMI", y="Age", color="Chronic disease")
st.plotly_chart(fig2)

# 5. Alcohol consumption by chronic disease
st.subheader("Alcohol Consumption vs Chronic Disease")
st.markdown("Boxplot comparing alcohol consumption for those with and without chronic disease.")
fig3 = px.box(filtered_df, x="Chronic disease", y="Alcohol Consumption")
st.plotly_chart(fig3)

# 6. Smoking status vs chronic disease
st.subheader("Smoking Status vs Chronic Disease")
st.markdown("Bar chart showing smoking categories split by chronic disease status.")
smoke_crosstab = pd.crosstab(filtered_df["Smoking"], filtered_df["Chronic disease"])
st.bar_chart(smoke_crosstab)

# 7. Physical activity distribution
st.subheader("Physical Activity Level")
st.markdown("Histogram of physical activity scores among individuals.")
st.hist(filtered_df["Physical Activity"], bins=30)

# 8. Sleep hours by chronic disease
st.subheader("Sleep Hours by Chronic Disease")
st.markdown("This boxplot shows average sleep hours for individuals with or without chronic disease.")
fig4 = px.box(filtered_df, x="Chronic disease", y="Sleep Hours")
st.plotly_chart(fig4)

# 9. Steps vs BMI
st.subheader("Steps per Day vs BMI")
st.markdown("Scatter plot of daily steps compared to BMI, colored by chronic disease status.")
fig5 = px.scatter(filtered_df, x="Steps per Day", y="BMI", color="Chronic disease")
st.plotly_chart(fig5)

# 10. Correlation heatmap
st.subheader("Correlation Heatmap")
st.markdown("Heatmap of correlations between numerical variables.")
fig6, ax6 = plt.subplots(figsize=(10,6))
sns.heatmap(filtered_df.corr(), annot=True, cmap="coolwarm", ax=ax6)
st.pyplot(fig6)

# 11. Average alcohol by gender
st.subheader("Average Alcohol Consumption by Gender")
st.markdown("Bar chart of average alcohol consumption by gender.")
avg_alcohol = filtered_df.groupby("Gender")["Alcohol Consumption"].mean()
st.bar_chart(avg_alcohol)

# 12. Steps distribution
st.subheader("Steps per Day Distribution")
st.markdown("Histogram of how many steps individuals take per day.")
st.hist(filtered_df["Steps per Day"], bins=30)

# 13. Average sleep by gender
st.subheader("Average Sleep Hours by Gender")
st.markdown("Bar chart of average sleep by gender.")
avg_sleep = filtered_df.groupby("Gender")["Sleep Hours"].mean()
st.bar_chart(avg_sleep)

# 14. Age vs Sleep
st.subheader("Age vs Sleep Hours")
st.markdown("Scatter showing how age relates to sleep hours.")
fig7 = px.scatter(filtered_df, x="Age", y="Sleep Hours", color="Gender")
st.plotly_chart(fig7)

# 15. BMI by gender
st.subheader("BMI by Gender")
st.markdown("Boxplot comparing BMI between genders.")
fig8 = px.box(filtered_df, x="Gender", y="BMI", color="Gender")
st.plotly_chart(fig8)

# 16. Alcohol consumption by age
st.subheader("Alcohol Consumption vs Age")
st.markdown("Scatter plot of alcohol consumption by age.")
fig9 = px.scatter(filtered_df, x="Age", y="Alcohol Consumption", color="Chronic disease")
st.plotly_chart(fig9)

# 17. Physical activity by chronic disease
st.subheader("Physical Activity vs Chronic Disease")
st.markdown("Boxplot comparing physical activity level for chronic disease presence.")
fig10 = px.box(filtered_df, x="Chronic disease", y="Physical Activity")
st.plotly_chart(fig10)

# 18. Smoking status distribution
st.subheader("Smoking Status Distribution")
st.markdown("Pie chart showing the proportion of smokers vs non-smokers.")
smoke_counts = filtered_df["Smoking"].value_counts()
fig11, ax11 = plt.subplots()
ax11.pie(smoke_counts, labels=smoke_counts.index, autopct='%1.1f%%')
st.pyplot(fig11)

# 19. Steps per day by chronic disease
st.subheader("Steps per Day by Chronic Disease")
st.markdown("Boxplot comparing daily steps with chronic disease status.")
fig12 = px.box(filtered_df, x="Chronic disease", y="Steps per Day")
st.plotly_chart(fig12)

# 20. Alcohol consumption vs smoking
st.subheader("Alcohol Consumption vs Smoking Status")
st.markdown("Boxplot comparing alcohol consumption by smoking status.")
fig13 = px.box(filtered_df, x="Smoking", y="Alcohol Consumption")
st.plotly_chart(fig13)

st.success("✅ Dashboard loaded successfully! Explore the filters and charts above to gain insights.")
