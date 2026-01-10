import streamlit as st
import requests

# Page setup
st.set_page_config(page_title="AI Fashion Studio", layout="wide")

st.title("👗 Mera AI Fashion Studio")
st.write("Apne kisi bhi kapde ko model par pehna kar dekhein.")

# Sidebar for API Key
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Fal.ai API Key", type="password", help="Fal.ai se apni key yahan dalein")

# UI Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Kapde ki Photo")
    garment_file = st.file_uploader("Upload Garment", type=['jpg', 'jpeg', 'png'])

with col2:
    st.subheader("2. Model ki Photo")
    person_file = st.file_uploader("Upload Person", type=['jpg', 'jpeg', 'png'])

# Generate Button
if st.button("Magic Generate ✨"):
    if not api_key:
        st.error("Pehle Sidebar mein API Key dalein!")
    elif garment_file and person_file:
        st.info("AI kaam kar raha hai... Kripya 30 seconds intezar karein.")
        # Yahan AI API ka logic chalega
        st.warning("Note: Abhi humne sirf front-end banaya hai. API connect karne ke liye agla step follow karein.")
    else:
        st.warning("Kripya dono photos upload karein.")

st.markdown("---")
st.caption("Powered by Fal.ai & Streamlit")
