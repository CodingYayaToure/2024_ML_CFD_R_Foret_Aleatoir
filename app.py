import streamlit as st
import joblib
import pandas as pd

# Charger le meilleur modèle avec gestion d'erreur
try:
    best_rf = joblib.load('meilleur_modele_rf.pkl')
except Exception as e:
    st.error(f"Erreur lors du chargement du modèle : {e}")
    st.stop()  # Arrête l'exécution si le modèle ne peut pas être chargé

# Informations personnelles
photo_url = "CFD_2024.png"  # Assurez-vous que cette image est dans le même répertoire que votre script
prenom = "Yaya"
nom = "Toure"
email = "yaya.toure@unchk.edu.sn"
whatsapps_url = "https://wa.me/message/GW7RWRW3GR4WN1"
linkedin_url = "https://www.linkedin.com/in/yaya-toure-8251a4280/"
github_url = "https://github.com/CodingYayaToure"
universite = "UNCHK"
formation = "Licence Analyse Numerique et Modelisation | Master Calcul scientifique et Modelisation"
certification = "Collecte et Fouille de Donnees (UADB-CNAM Paris)"
responsable_cours = "Professeur Abdoulaye Barro"
email_responsable = "abdoulayebarro9@gmail.com"

# Interface Streamlit
st.sidebar.title("Informations personnelles")
st.sidebar.image(photo_url, caption=f"{prenom} {nom}", width=450)
st.sidebar.write(f"Nom: {prenom} {nom}")
st.sidebar.write(f"Email: {email}")
st.sidebar.markdown(f"[Whatsapps]({whatsapps_url})")
st.sidebar.markdown(f"[LinkedIn]({linkedin_url})")
st.sidebar.markdown(f"[GitHub]({github_url})")
st.sidebar.write(f"Université: {universite}")
st.sidebar.write(f"**Formations:** {formation}")
st.sidebar.write(f"**Certification:** {certification}")

# Description du projet
st.title("Prédiction de Prix de Produit")

st.write("""
Ce projet utilise des techniques d'apprentissage supervisé pour prédire le prix de produits en fonction de leurs spécifications techniques. Les variables d'entrée utilisées pour la prédiction incluent la RAM, le stockage et la taille de l'écran. 

### Objectif du Projet

L'objectif principal est d'obtenir la certification en collecte et fouille de données de l'UADB-CNAM de Paris. Le responsable du cours est le professeur Abdoulaye Barro, que vous pouvez contacter à l'adresse suivante : [abdoulayebarro9@gmail.com](mailto:abdoulayebarro9@gmail.com) ou par téléphone : +221 77 262 80 20.

### Méthodologie

Nous avons développé un modèle de régression basé sur des données historiques de prix et des caractéristiques de produits. L'application permet aux utilisateurs de saisir les spécifications d'un produit et d'obtenir une estimation de son prix, facilitant ainsi la prise de décision lors de l'achat.

### Variables d'Entrée

Les variables d'entrée pour la prédiction sont :
- **RAM (GB)** : La mémoire vive du produit.
- **Storage (GB)** : La capacité de stockage du produit.
- **Screen Size (inches)** : La taille de l'écran du produit.

Cette approche permet d'utiliser efficacement les données pour générer des prédictions précises et utiles.
""")

# Entrées utilisateur pour la prédiction
ram = st.number_input("RAM (GB)", min_value=0, step=1)
storage = st.number_input("Stockage (GB)", min_value=0, step=1)
screen_size = st.number_input("Taille d'écran (pouces)", min_value=0.0, step=0.1)

# Bouton pour faire la prédiction
if st.button("Prédire le Prix"):
    # Validation des entrées
    if ram < 0 or storage < 0 or screen_size < 0:
        st.error("Veuillez entrer des valeurs valides pour RAM, stockage et taille d'écran.")
    else:
        new_data = pd.DataFrame({
            'RAM (GB)': [ram],
            'Storage (GB)': [storage],
            'Screen Size (inches)': [screen_size]
        })
        prediction = best_rf.predict(new_data)
        st.write(f'Prix prédit: ${prediction[0]:.2f}')
