import streamlit as st
import plotly.express as px
import pandas as pd

st.title("Comparing Happiness")

#X axis search data
xoption = st.selectbox("Select the Data For the X axis",("GDP", "Happiness", "Generosity"))

#Y axis search data
yoption = st.selectbox("Select the Data For the Y axis",("GDP", "Happiness", "Generosity"))

df = pd.read_csv("happy.csv")

#match cases to arrange charts
x_array = None
match xoption:
    case "Happiness":
        x_array = df["happiness"]
    case "GDP":
        x_array = df["gdp"]
    case "Generosity":
        x_array = df["generosity"]

y_array = None
match yoption:
    case "Happiness":
        y_array = df["happiness"]
    case "GDP":
        y_array = df["gdp"]
    case "Generosity":
        y_array = df["generosity"]

#dynamic subheader
st.subheader(f"{xoption} and {yoption}")

figure1 = px.scatter(x=x_array, y=y_array, labels={"x": xoption, "y": yoption})
st.plotly_chart(figure1)
