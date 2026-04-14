import streamlit as st

# Configuration de la page pour qu'elle soit responsive
st.set_page_config(page_title="Lexiguard - Assistant Juridique", layout="wide")

# Style CSS pour coller au design (responsive et couleurs)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stButton>button { width: 100%; border-radius: 10px; background-color: #0056b3; color: white; }
    .status-box { padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 5px solid; }
    .danger { background-color: #ffe5e5; border-color: #ff4d4d; }
    .warning { background-color: #fff4e5; border-color: #ffa64d; }
    .safe { background-color: #e5f9e5; border-color: #4dff4d; }
    </style>
    """, unsafe_allow_html=True)

# Header avec Logo et Titre
st.title("🛡️ Lexiguard")
st.caption("Votre assistant juridique sécurisé - Analyse par IA")

# Organisation en colonnes (se transforme en pile sur mobile automatiquement)
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Analyse du contrat")
    contrat_text = st.text_area("Collez votre texte ici ou glissez un fichier...", height=300)
    if st.button("Analyser mon contrat"):
        if contrat_text:
            st.session_state['analyse_faite'] = True
        else:
            st.error("Veuillez coller un texte à analyser.")

with col2:
    st.subheader("Résultats")
    if st.session_state.get('analyse_faite'):
        # Simulation des résultats pour la démo BGE
        st.markdown('<div class="status-box danger">⚠️ **ALERTE :** Préavis de 4 mois requis. Clause très contraignante.</div>', unsafe_allow_html=True)
        st.markdown('<div class="status-box warning">🟡 **ATTENTION :** Reconduction automatique annuelle détectée.</div>', unsafe_allow_html=True)
        st.markdown('<div class="status-box safe">✅ **CONFORME :** Droit de rétractation de 14 jours respecté.</div>', unsafe_allow_html=True)
        
        st.info("💡 Cette analyse est une démonstration. La version complète à 2,99€ débloque les conseils de négociation.")
    else:
        st.write("Les résultats apparaîtront ici après l'analyse.")

# Footer de protection
st.markdown("---")
st.caption("🔒 Protection API : Vos données sont chiffrées et ne sont jamais stockées pour l'entraînement.")
