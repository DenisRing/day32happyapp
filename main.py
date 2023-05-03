import streamlit as st
import plotly.express as px

st.title("Comparing Happiness")

#X axis search data
xoption = st.selectbox("Select the Data For the X axis",("GDP", "Happiness", "Generosity"))

#Y axis search data
yoption = st.selectbox("Select the Data For the Y axis",("GDP", "Happiness", "Generosity"))

#dynamic subheader

st.subheader(f"{xoption} and {yoption}")

gdp = [20,60,80]
happiness = [1.0,3.0,6.0]
genero = [5, 7, 8]

