import streamlit as st

# Branding: Seitenkonfiguration
st.set_page_config(page_title="LinkedIn ROI-Rechner | Talify", page_icon="📊", layout="centered")

# Branding: Logo & Header
st.image("Asset 4@2x-8 (5).png", width=200)  # Talify-Logo
st.image("Kein Titel (389 x 129 px) (389 x 129 px) (3).png", width=300)  # Talify-Schriftzug
st.title("🚀 LinkedIn ROI-Rechner")
st.write("Berechne schnell und einfach deine LinkedIn-Marketing-Rentabilität – bereitgestellt von Talify.")

# Eingabefelder mit verbessertem Design
st.markdown("### 📌 Gib deine Werte ein:")
spent = st.number_input("💰 Geld ausgegeben auf LinkedIn ($)", min_value=0.0, format="%.2f")
earned = st.number_input("💵 Geld verdient durch LinkedIn ($)", min_value=0.0, format="%.2f")

# ROI Berechnung
def calculate_linkedin_roi(spent, earned):
    if spent == 0:
        return "Kein Investment getätigt. ROI kann nicht berechnet werden."
    roi = ((earned - spent) / spent) * 100
    return f"Ihr LinkedIn-ROI beträgt {roi:.2f}%. {'✅ Rentabel' if roi > 0 else '❌ Nicht rentabel'}"

# Button für Berechnung
if st.button("📊 ROI berechnen"):
    result = calculate_linkedin_roi(spent, earned)
    st.success(result)

# Footer mit Branding und funktionierenden Links
st.markdown("---")
st.markdown("💡 Entwickelt von <strong>Talify</strong> | 🔗 <a href='https://www.talify.de/' target='_blank'>Mehr erfahren</a>", unsafe_allow_html=True)
