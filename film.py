import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from omdb import OMDBClient
import os
from dotenv import load_dotenv
import requests
from PIL import Image
load_dotenv('keys_api.env')
client = OMDBClient(apikey=os.getenv('OMDB_HOTMAIL_KEY'))


st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://raw.githubusercontent.com/Viniciusneri1/projeto-recomenda-es-de-filmes/main/image.jpg")
    }
   .sidebar .sidebar-content {
        background: url("https://raw.githubusercontent.com/Viniciusneri1/projeto-recomenda-es-de-filmes/main/image.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("""
<style>
.big-font {
    font-size:70px !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown(f"<p class=big-font><font color='red'> Recomendações de Filmes</font>", unsafe_allow_html=True )

data = pd.read_csv('/Users/vanessa/Desktop/Projeto_rec/data_cs.csv')
data = data.set_index('Title')
select = st.selectbox('Selecione seu filme', data.columns)

try:
    scores = data[[select]].reset_index().to_numpy()
    sorted_scores = sorted(scores, key=lambda x:x[1], reverse = True)
    sorted_scores = sorted_scores[1:]

    
    i = 0
    st.markdown(f"<font color='red'>As recomendações de {select} são:\n</font>", unsafe_allow_html=True )
    for item in sorted_scores:
        movie_title = item[0]
        url = client.get(title = movie_title)['poster']
        st.image(url)
        st.markdown(f"<font color='red'> {i+1} {movie_title} </font>" , unsafe_allow_html=True)
        i = i+1
        if i>5:
            break
except:
    pass


