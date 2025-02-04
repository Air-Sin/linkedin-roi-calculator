import streamlit as st
import os

# Branding: Seitenkonfiguration
st.set_page_config(page_title="LinkedIn ROI-Rechner | Talify", page_icon="📊", layout="centered")

# Branding: Logo & Header
logo_path = "Asset 4@2x-8 (5).png"
text_path = "Kein Titel (389 x 129 px) (389 x 129 px) (3).png"

if os.path.exists(logo_path):
    st.image(logo_path, width=200)
else:
    st.warning("⚠️ Talify-Logo nicht gefunden!")

if os.path.exists(text_path):
    st.image(text_path, width=300)
else:
    st.warning("⚠️ Talify-Schriftzug nicht gefunden!")

st.title("🚀 LinkedIn ROI-Rechner")
st.write("Berechne schnell und einfach deine LinkedIn-Marketing-Rentabilität – bereitgestellt von Talify.")

# Eingabefelder mit verbessertem Design
st.markdown("### 📌 Gib deine Werte ein:")
spent = st.number_input("💰 Geld ausgegeben auf LinkedIn ($)", min_value=0.0, format="%.2f")
earned = st.number_input("💵 Geld verdient durch LinkedIn ($)", min_value=0.0, format="%.2f")

# ROI Berechnung
def calculate_linkedin_roi(spent, earned):
    if spent == 0:
        return "❌ Kein Investment getätigt. ROI kann nicht berechnet werden."
    roi = ((earned - spent) / spent) * 100
    return f"💡 Ihr LinkedIn-ROI beträgt {roi:.2f}%. {'✅ Rentabel' if roi > 0 else '❌ Nicht rentabel'}"

# Button für Berechnung
if st.button("📊 ROI berechnen"):
    result = calculate_linkedin_roi(spent, earned)
    st.success(result)

# Footer mit Branding und funktionierenden Links
st.markdown("---")
st.markdown(
    "💡 Entwickelt von **Talify** | 🔗 <a href='https://www.talify.de/' target='_blank'>Mehr erfahren</a>",
    unsafe_allow_html=True
)
