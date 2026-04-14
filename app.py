import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Lexiguard", layout="wide")

# --- CSS PERSONNALISÉ POUR COLLER AU DESIGN ---
st.markdown("""
    <style>
    /* Fond gris très clair comme sur l'image */
    .stApp {
        background-color: #F8FAFC;
    }
    
    /* Style du Header */
    .header-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
    }
    
    /* Simulation des onglets Particulier/Professionnel */
    .tabs-container {
        display: flex;
        background-color: #E2E8F0;
        border-radius: 50px;
        padding: 5px;
        width: fit-content;
        margin-bottom: 30px;
    }
    .tab {
        padding: 8px 25px;
        border-radius: 40px;
        font-weight: bold;
        font-size: 14px;
    }
    .tab-active {
        background-color: #BFDBFE;
        color: #1E40AF;
    }
    
    /* Boîtes de texte et résultats */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        height: 100%;
    }
    
    /* Alertes colorées à droite */
    .alert {
        padding: 12px;
        border-radius: 8px;
        margin-bottom: 10px;
        font-size: 13px;
        display: flex;
        align-items: center;
        border: 1px solid transparent;
    }
    .alert-red { background-color: #FEE2E2; border-color: #FCA5A5; color: #991B1B; }
    .alert-orange { background-color: #FFEDD5; border-color: #FDBA74; color: #9A3412; }
    .alert-green { background-color: #DCFCE7; border-color: #86EFAC; color: #166534; }
    .alert-blue { background-color: #DBEAFE; border-color: #BFDBFE; color: #1E40AF; }
    
    /* Zone centrale de drop */
    .drop-zone {
        border: 2px dashed #94A3B8;
        border-radius: 10px;
        padding: 40px;
        text-align: center;
        color: #64748B;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENU DE L'INTERFACE ---

# 1. LOGO ET ONGLETS
st.markdown("""
    <div class="header-container">
        <h1 style='color: #1E3A8A; margin-bottom: 10px;'>🛡️ Lexiguard</h1>
        <div class="tabs-container">
            <div class="tab tab-active">Particulier</div>
            <div class="tab">Professionnel <span style='font-size: 10px; color: #6366F1;'>OFFRE PRO</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# 2. COLONNES (3 colonnes pour imiter le design)
col_left, col_mid, col_right = st.columns([1.2, 1, 1.2])

with col_left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Conditions de Résiliation")
    st.write("Contrat fit du gym est simulant un membre...")
    # Texte surligné comme sur l'image
    st.markdown("""
    <p style='font-size: 13px;'>
    <span style='background-color: #FCA5A5;'>un claushe contrat loection et Préavis requis</span>. 
    Il s'as samementer acomittrote <span style='background-color: #FCA5A5;'>Préavis clause de 4 mois</span>.
    <br><br>
    Le <span style='background-color: #FDBA74;'>attention : reconduction automatique annuelle</span>, pensez à résiliite anniversaire.
    <br><br>
    <span style='background-color: #86EFAC;'>Conditions : Droit de rétractation et 14 jours</span>, annuellement es généfits...
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_mid:
    st.markdown('<div class="drop-zone">📤<br>Glissez votre contrat ici<br>ou collez le texte</div>', unsafe_allow_html=True)
    if st.button("Analyser mon contrat", use_container_width=True):
        st.balloons()

with col_right:
    st.markdown("""
    <div class="alert alert-red">🔴 <b>ALERTE :</b> Préavis de 4 mois requis. Clause très contraignante, risque élevé.</div>
    <div class="alert alert-orange">🟡 <b>ATTENTION :</b> Reconduction automatique annuelle. Pensez à résilier avant la date anniversaire.</div>
    <div class="alert alert-green">🟢 <b>Conforme :</b> Droit de rétractation de 14 jours. Délai légal respecté.</div>
    <div class="alert alert-blue">🔒 <b>Protection API :</b> Analyse chiffrée, vos données sont éphémères et ne sont jamais stockées.</div>
    """, unsafe_allow_html=True)
    
    st.checkbox("Anonymiser automatiquement mes données", value=True)
