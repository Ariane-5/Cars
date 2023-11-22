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

st.title('Analyse en fonction de la région :')

df = pd.read_csv('https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv')

options = list(df['continent'].unique())
choix_region = st.selectbox('Choisissez la région :', options)
df_region = df[(df['continent'] == choix_region)]
df_region

#var = ['mpg', 'cylinders', 'cubicinches', 'hp', 'weightlbs', 'time-to-60', 'year']

#for i in var :  
#  sns.boxplot(x='continent', y = i, data = df_region).figure
#  plt.close()

st.title('Quelques statistiques globales de nos données :')

nb = len(df_region)
f"La région {choix_region} comprend {nb} entrées, ce qui représente environ {round(nb / len(df) *100)} % de l'ensemble de nos données."

stats = pd.DataFrame(df_region.describe())
stats = stats.drop(['count'], axis = 0).round().astype('int')
stats

st.title('Visualisation :')

col1, col2, col3 = st.columns(3)

with col1 :
  sns.boxplot(x='continent', y = 'mpg', data = df_region).figure
  plt.close()

  sns.boxplot(x='continent', y = 'cylinders', data = df_region).figure
  plt.close()

  "Évolution de la consommation des véhicules au fil des années :"
  sns.regplot(x='year', y='mpg', data=df_region).figure
  plt.close()

with col2 :
  sns.boxplot(x='continent', y = 'cubicinches', data = df_region).figure
  plt.close()

  sns.boxplot(x='continent', y = 'hp', data = df_region).figure
  plt.close()

with col3 :
  sns.boxplot(x='continent', y = 'time-to-60', data = df_region).figure
  plt.close()

  sns.boxplot(x='continent', y = 'year', data = df_region).figure
  plt.close()
