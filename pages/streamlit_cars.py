import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

title1, title2 = st.columns(2)

with title1 :
  st.title('Julie D - Streamlit : build and share data apps')
with title2 :
  st.image('logo_WCS.png')

st.title("Analyse de l'ensemble des données :")

colA, colB = st.columns(2)

with colA :
  df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')
  df

with colB :
  'Corrélation entre les variables :'
  sns.heatmap(df.corr(), cmap = 'Spectral_r', center = 0, annot = True).figure
  plt.close()

st.title('Quelques statistiques globales de nos données :')

f"Nombre d'entrées : {len(df)}."

stats = pd.DataFrame(df.describe())
stats = stats.drop(['count'], axis = 0).round().astype('int')
stats


st.title('Visualisation :')

col1, col2, col3 = st.columns(3)

with col1 :
  sns.boxplot(x='continent', y = 'mpg', data = df).figure
  plt.close()

  sns.boxplot(x='continent', y = 'cylinders', data = df).figure
  plt.close()
  
  sns.scatterplot(x='year', y='mpg', data=df, hue = 'continent').figure
  plt.close()

with col2 :
  sns.boxplot(x='continent', y = 'cubicinches', data = df).figure
  plt.close()

  sns.boxplot(x='continent', y = 'hp', data = df).figure
  plt.close()

with col3 :
  sns.boxplot(x='continent', y = 'time-to-60', data = df).figure
  plt.close()

  sns.boxplot(x='continent', y = 'year', data = df).figure
  plt.close()
