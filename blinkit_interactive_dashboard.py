
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.set_page_config(layout="wide", page_title="Blinkit Survey Dashboard")

# Load data
df = pd.read_excel("Blinkit_Dashboard_Data.xlsx")

st.title("📊 Blinkit Survey Dashboard")

# Sidebar filters
st.sidebar.header("Filter Data")
age_filter = st.sidebar.multiselect("Select Age Group", options=df['What is your age?'].unique(), default=df['What is your age?'].unique())
gender_filter = st.sidebar.multiselect("Select Gender", options=df['What is your gender?'].unique(), default=df['What is your gender?'].unique())

# Apply filters
df_filtered = df[df['What is your age?'].isin(age_filter) & df['What is your gender?'].isin(gender_filter)]

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Age Distribution")
    age_counts = df_filtered['What is your age?'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=age_counts.index, y=age_counts.values, palette="Set2", ax=ax)
    ax.set_title("Age Distribution")
    ax.set_xlabel("Age Group")
    ax.set_ylabel("Count")
    st.pyplot(fig)

with col2:
    st.subheader("Gender Distribution")
    gender_counts = df_filtered['What is your gender?'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=gender_counts.index, y=gender_counts.values, palette="Set2", ax=ax)
    ax.set_title("Gender Distribution")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Count")
    st.pyplot(fig)

col3, col4 = st.columns(2)

with col3:
    st.subheader("How Users Learned About Blinkit")
    source_counts = df_filtered['How did you first learn about Blinkit?'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(y=source_counts.index, x=source_counts.values, palette="Set2", ax=ax)
    ax.set_xlabel("Count")
    ax.set_ylabel("Source")
    st.pyplot(fig)

with col4:
    st.subheader("Usage Frequency")
    usage_counts = df_filtered['How often do you use Blinkit?'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(y=usage_counts.index, x=usage_counts.values, palette="Set2", ax=ax)
    ax.set_xlabel("Count")
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

st.subheader("Customer Care Service Rating")
cust_rating = df_filtered['How much would you rate customer care service of Blinkit ?'].astype(str).value_counts()
fig, ax = plt.subplots()
sns.barplot(x=cust_rating.index, y=cust_rating.values, palette="Set2", ax=ax)
ax.set_xlabel("Rating")
ax.set_ylabel("Count")
st.pyplot(fig)

st.subheader("Suggestions Word Cloud")
suggestions = df_filtered['Any Suggestions you would recommend'].dropna().astype(str).str.cat(sep=' ')
wordcloud = WordCloud(width=1000, height=400, background_color='black', colormap='Set2').generate(suggestions)
fig, ax = plt.subplots(figsize=(15, 6))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)
