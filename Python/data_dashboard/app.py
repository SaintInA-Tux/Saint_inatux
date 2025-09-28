"""Streamlit dashboard: upload CSV and show simple charts."""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title='Data Dashboard')
st.title('Data Dashboard — Upload CSV')


uploaded = st.file_uploader('Upload CSV', type=['csv'])
if uploaded is not None:
df = pd.read_csv(uploaded)
st.write('Data preview', df.head())
numeric = df.select_dtypes(include='number')
if not numeric.empty:
col = st.selectbox('Choose numeric column to plot', numeric.columns)
fig, ax = plt.subplots()
df[col].plot(kind='hist', ax=ax)
ax.set_xlabel(col)
st.pyplot(fig)
else:
st.info('No numeric columns found in uploaded CSV')
