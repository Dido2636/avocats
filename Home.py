import time, json
import streamlit as st
from function import scraping_acovat
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# Title 
st.title('Bonjour')
st.markdown('Bienvenue sur notre annuaire d avocats')

# input_value = st.text_input('Choisissez un numero de page :')
# st.write(f'{input_value}')

page_slider = st.slider('Vous voulez voir les avocats jusqu a quel page ?', 0, 104, 5)
st.write('Nous allons scrapper jusqu a la:', page_slider,)

st.write('Que recherchez-vous comme informations ?')
image = st.checkbox("Image")
nom = st.checkbox("Nom")
adresse = st.checkbox("Adresse")
email = st.checkbox("Email")


if st.button('Recherchez', key="recherche_button"):
    time.sleep(3)

    avocat_page = scraping_acovat(n_page= page_slider)

    for page_number in range(1, page_slider + 1):
        avocat_page = scraping_acovat(n_page=str(page_number))



    for key in avocat_page:
        col1, col2 = st.columns(2)

        with col1:
            st.write(key)
            if image:
                st.image(avocat_page[key]['image'])

        with col2:
            if nom:
                st.write(avocat_page[key]['nom'])
        
            if adresse:
                st.write(avocat_page[key]['adresse'])
        
            if email:
                st.write(avocat_page[key]['email'])
           
        