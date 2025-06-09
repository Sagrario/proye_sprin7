import streamlit as st
import pandas as pd
import plotly_express as px

st.header('Vehiculos')

st.write("""
    Para poder ver las gráficas de conteo contra el kilometraje da clic en el botón que desees  \n\n
    Escoge que tipo de grafica quieres ver seleccionando el botón con la etiqueta deseada:
""")


car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    # st.write(
    #   'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    Sobre la grafica se puede observar:
    - La mayoría de los coches tienen un kilometraje entre 0 y 200,000
    - El kilometraje aumenta y los coches disminuye
    """)


hist_button2 = st.button('Dispersion')  # crear un botón

if hist_button2:  # al hacer clic en el botón
    # escribir un mensaje
    # st.write(
    #   'Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig2 = px.scatter(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
    Sobre la grafica se puede observar:
    - La mayoría de los coches tienen un kilometraje por debajo de los 200,000
    - Hay valores atípicos, como autos con más de 800,000 o 1,000,000 km
    - La distribución es muy densa al inicio, lo que indica que la mayoría de los autos tiene poco uso o un uso medio.
    """)


# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig3 = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("""
    Sobre la grafica se puede observar:  \n\n
    - La mayoría de los coches tienen un kilometraje entre 0 y 200,000 \n\n
    - El kilometraje aumenta y los coches disminuye
    """)
