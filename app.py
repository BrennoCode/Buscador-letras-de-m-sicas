import requests
import streamlit as st

def buscar_letra(banda, musica):
    endpoint = f'https://api.lyrics.ovh/v1/{banda}/{musica}'
    response = requests.get(endpoint)
    letra = response.json()['lyrics'] if response.status_code == 200 else ''
    return(letra)

st.image('https://i.pinimg.com/736x/ed/44/ce/ed44ce8d338c572c1a4f7d66ede9907d.jpg')
st.title('Pesquise sua letra!')

banda = st.text_input ('Digite o nome da banda', key = 'banda')
musica = st.text_input ('Digite o nome da Música ',key = 'musica')
pesquisar = st.button('Pesquisar')

if pesquisar:
    letra = buscar_letra(banda, musica)
    if letra:
        st.success('Encontramos a letra da sua música!')
        st.text(letra)
    else:
        st.error('Infelizmente não encontramos a letra')