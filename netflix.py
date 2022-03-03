import pandas as pd
import numpy as np
import streamlit as st
import codecs
import re
st.subheder('Integrantes: Pedro de Jesus Hernandez Rojas \nCristian Terán Juárez ')
st.title('Peliculas de Netflix')


DATA_URL = ('https://raw.githubusercontent.com/Pedrohero13/netflix/main/movies.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, encoding_errors='ignore')
    return data

#Cargar datos si se selecciona en el checkbox
agree = st.sidebar.checkbox("¿Quieres mostrar todos los datos? ")
if agree:
  data_load_state = st.text('Cargando...')
  data = load_data(2000)
  data_load_state.text("Cargado! (using st.cache)")
  st.dataframe(data)



#filtlar por el nombre de la pelicula
@st.cache
def load_data_byname(name):
  datafiltered = load_data(2000)
  filtered_data_byname = datafiltered[datafiltered['name'].str.contains(name, flags=re.IGNORECASE)]
  
  return filtered_data_byname

titulo = st.sidebar.text_input('Titulo de la pelicula: ')
btnFilteredMovie = st.sidebar.button('Buscar Pelicula')

if (btnFilteredMovie):
  st.write ("Titulo buscado: "+ titulo)
  filterbyname = load_data_byname(titulo)
  count_row = filterbyname.shape[0]
  st.write(f'Total de peliculas: {count_row}')

  st.dataframe(filterbyname)


#filtrar por el nombre del direcctor 
@st.cache
def load_data_bydire(director):
  data = load_data(2000)
  filtered_data_bydire = data[data['director'] == director]
  return filtered_data_bydire

data = load_data(2000)
selected = st.sidebar.selectbox("Selecciona el director", data['director'].unique())
btnFilterBydire = st.sidebar.button('Filtrar por Director')

if (btnFilterBydire): 
  st.write("Peliculas dirigidas por "+selected)
  filterbydire = load_data_bydire(selected)
  count_row = filterbydire.shape[0]
  st.write(f'Total Peliculas: {count_row}')

  st.dataframe(filterbydire)