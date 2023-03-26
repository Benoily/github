import streamlit as st
import requests


# Ajout d'un titre 
st.title('My Content - Recommandation d\'articles')

# Ajout d'un logo
st.image('logo.png', width=200)

# Ajout d'un texte de présentation 
st.markdown("Bienvenue sur My Content ! Veuillez renseigner ci-dessous pour voir les articles que nous vous recommandons.")


#if api_url == '':
#api_url = 'https://recmt.azurewebsites.net/api/HttpTrigger1?'

# Récupération de l'id 
type = st.text_input('Entrez votre type (Mettez **cb** ou **cf**) : ')

# Récupération de l'id 
id = st.text_input('Entrez votre id : ')

if st.button("Soumettre"):
    with st.spinner("Recommandation d'articles en cours..."):
        if id:
            params = {"id": int(id), "type": type }
    
            r = requests.get('https://recmt.azurewebsites.net/api/HttpTrigger1?', json=params, verify=True)
            content = r.content.decode("utf-8")
    
            remove ='[ ]'
            for charac in remove:
                content = content.replace(charac, '')

            content = content.split(',')

            try:
                response = content
    #try:
    #    response = requests.get('https://recomt.azurewebsites.net/api/HttpTrigger1?', json=params)
            except Exception as e:
                 st.error(e)
            st.info("Les résultats sont classés par ordre de pertinence.")
            st.write('Voici les articles recommandés pour l\'utilisateur ' + str(id) + ' :')
            st.write(response)
st.markdown("made by **FOLY BENOIT KUEVIAKOE**")
