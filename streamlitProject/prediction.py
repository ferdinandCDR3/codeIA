import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from vega_datasets import data as vds

# Dataframe
st.title("Cars Dataframe")
cars = vds.cars().dropna()
st.write(cars)

measures = ['Miles_per_Gallon', 'Cylinders', 'Displacement', 'Horsepower', 'Weight_in_lbs', 'Acceleration']

# Liste deroulante et courbe
st.title("Scatter Plot")
scatter_x = st.selectbox('x', measures)
scatter_y = st.selectbox('y', measures)
sns.regplot(x=scatter_x, y=scatter_y, data=cars)
st.pyplot()

# model de prédiction
st.title("Predict MPG")
weight = st.number_input('enter vehicule weight', min_value=1500, max_value=6000)
x = np.array(cars.Weight_in_lbs).reshape(-1,1)
y = np.array(cars.Miles_per_Gallon)
lr = LinearRegression().fit(x, y)
prediction = lr.predict(np.array([[weight]]))
st.text('predicted mpg')
st.text(f'{prediction[0]:2f}')

# courbe avec radio boutton
st.title("Radio Buttons")
radio_button_options = st.radio('Choose measure for boxplot:', measures)

# Function qui affiche les nuages de point et le courbe
def create_boxplot(measure):
    swarmplot = st.checkbox('Overlay swarmplot')
    if swarmplot and radio_button_options == measure:
        sns.boxplot(data=cars[measure])
        sns.stripplot(data=cars[measure], color='lightgrey')
        st.pyplot()
    else:
        sns.boxplot(data=cars[measure])
        st.pyplot()

# Appel de la fonction create_boxplot créée
create_boxplot(radio_button_options)