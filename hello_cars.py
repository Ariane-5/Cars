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

st.title('Challenge :')

st.write('''
         A partir du dataset des voitures, tu afficheras : 
         une analyse de corrélation et de distribution grâce à différents graphiques et des commentaires. \n des boutons doivent être présents pour pouvoir filtrer les résultats par région (US / Europe / Japon). \n l'application doit être disponible sur la plateforme de partage. \n Publie ensuite ici le lien de ton application. Le lien doit ressembler à https://share.streamlit.io/wilder/streamlit_app/my_streamlit_app.py.
         ''')
