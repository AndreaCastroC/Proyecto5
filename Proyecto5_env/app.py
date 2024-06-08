import pandas as pd
import streamlit as st
import plotly_express as px
car_data = pd.read_csv('/Users/andreacastrocaparo/Desktop/Importante/Bootcamp/Proyecto5/Proyecto5_env/vehicles_us.csv') # leer los datos
st.header('Análisis de Vehículos Usados')

hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:
    st.write('Creación de un gráfico de dispersión para el precio y el kilometraje de los coches')
    fig = px.scatter(car_data, x="odometer", y="price", color="year")
    st.plotly_chart(fig, use_container_width=True)

build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_histogram:
    st.write('Construcción de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter:
    st.write('Creación de un gráfico de dispersión para el precio y el kilometraje de los coches')
    fig = px.scatter(car_data, x="odometer", y="price", color="year")
    st.plotly_chart(fig, use_container_width=True)