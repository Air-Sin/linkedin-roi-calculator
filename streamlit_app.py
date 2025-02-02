import streamlit as st

def calculate_linkedin_roi(spent, earned):
    if spent == 0:
        return "Kein Investment getätigt. ROI kann nicht berechnet werden."
    roi = ((earned - spent) / spent) * 100
    return f"Ihr LinkedIn-ROI beträgt {roi:.2f}%. {'Rentabel' if roi > 0 else 'Nicht rentabel'}"

st.title("📊 LinkedIn ROI-Rechner")

# Eingaben vom Nutzer
spent = st.number_input("💰 Geld ausgegeben auf LinkedIn ($)", min_value=0.0, format="%.2f")
earned = st.number_input("💵 Geld verdient durch LinkedIn ($)", min_value=0.0, format="%.2f")

if st.button("ROI berechnen"):
    result = calculate_linkedin_roi(spent, earned)
    st.success(result)
