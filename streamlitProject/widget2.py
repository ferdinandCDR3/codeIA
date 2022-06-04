# Importer les packages
import streamlit as st
import pandas as pd
import numpy as np
from vega_datasets import data as vds
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import altair as alt
import datetime

# Titre
st.title("Streamlit Application")
st.text("Text")

# Dataframe
st.title("Dataframe")
cars = vds.cars()
st.write(cars.head())
st.dataframe(cars)

# Table
st.title("Table")
st.table(cars.head())

# Courbe 1
st.title("Line Chart")
line_chart_data = pd.DataFrame({'A': [2,1,3,4,2], 'B':[4,3,2,5,3]})
st.line_chart(line_chart_data)

# Courbe 2
st.title("Line Chart 2")
plt.plot([3,4,3,5,4])
st.pyplot()

# Histogramme
st.title("Bar Chart")
fig, ax = plt.subplots()
ax.bar([1,2,3,4,5],[2,1,3,4,1])
ax.set_xticks([1,2,3,4,5])
ax.set_xticklabels(list('ABDCE'))
st.write(fig)

# Nuage de point avec altair
cars = vds.cars()
st.write(cars.head())
scatter = alt.Chart(cars).mark_circle().encode(x='Weight_in_lbs', y='Miles_per_Gallon').interactive()
st.altair_chart(scatter)

# Carte
st.title("Map")
airports = vds.airports()[['latitude', 'longitude']][0:100]
st.map(airports)

# Slider
st.title("Slider")
slider = st.slider(label='slider', min_value=0, max_value=10, value=5)
st.write(slider, 'squared is', slider * slider)

# Case à coucher
st.title("Chackbox")
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_global()
if st.checkbox('land'): ax.add_feature(cfeature.LAND)
if st.checkbox('ocean'): ax.add_feature(cfeature.OCEAN)
if st.checkbox('coastline'): ax.add_feature(cfeature.COASTLINE)
if st.checkbox('borders'): ax.add_feature(cfeature.BORDERS, linestyle=':')
if st.checkbox('lakes'): ax.add_feature(cfeature.LAKES, alpha=0.5)
if st.checkbox('rivers'): ax.add_feature(cfeature.RIVERS)
st.write(fig)

# Liste déroulante
st.title("Selectbox")
st.subheader("See Slidebar for selectbox Widget")
option = st.sidebar.selectbox('Choose',['a','b','c','d','e'])
st.write('You selected: ', option)

# zone de saisie et boutton
st.title("Text Input and Button")
text = st.text_input('Enter Name')
if st.button('Click button'):
    st.write(f'Hello {text}') 

# Radio bouton
st.title("Radio Buttons")
radio_button_options = st.radio('Options:', ('A', 'B', 'C'))
if radio_button_options == 'A':
    st.write('option A chosen')
elif radio_button_options == 'B':
    st.write('option B chosen')    
elif radio_button_options == 'C':
    st.write('option C chosen')

# Multiselect
st.title("Multiselect") 
options = st.multiselect('What are your favorite colors', ['green', 'orange', 'red', 'blue', 'purple'])  
st.write('You selected:')
for i in options:
    st.write(i) 

# Dates
st.title("Select Dates")
d = st.date_input('select date:', datetime.date(2022, 6, 3))
st.write(d)


