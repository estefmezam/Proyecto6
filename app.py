import pandas as pd
import plotly.express as px
import streamlit as st

#Leer los fatos
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

#Titulo de la aplicacion
st.header('Analisis Exploratorio de Anuncios de Ventas de Coches')

hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')      
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")  
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    
scatt_button = st.button('Construir un gráfico de dispersión')

if scatt_button: #al hacer clic en el boton
    #Escribe el mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    #Crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
    #Mostrar un grafico Plotly 
    st.plotly_chart(fig,use_container_width=True) # crear gráfico de dispersión