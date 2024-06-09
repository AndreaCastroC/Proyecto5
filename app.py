import pandas as pd
import streamlit as st
import plotly_express as px
car_data = pd.read_csv('/Users/andreacastrocaparo/Desktop/Importante/Bootcamp/Proyecto5/vehicles_us.csv') # leer los datos
st.header('Automóviles')

hist_button = st.button('Histograma')
if hist_button:
    st.write('Precio de los automóviles')
    fig = px.histogram(car_data, x="price")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Gráfico de dispersión')
if scatter_button:
    st.write('Kilometraje y precio de los automóviles según año del automóvil')
    fig = px.scatter(car_data, x="odometer", y="price", color="model_year")
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram:
    st.write('Histograma del precio de los automóviles')
    fig = px.histogram(car_data, x="price")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Gráfico de dispersión del kilometraje yl el precio de los automóviles según el año del automóvil')
    fig = px.scatter(car_data, x="odometer", y="price", color="model_year")
    st.plotly_chart(fig, use_container_width=True)
    
