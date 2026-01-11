import streamlit as st
import fal_client

# 1. Get the key from Secrets (or Sidebar as a backup)
api_key = st.secrets.get("FAL_KEY") or st.sidebar.text_input("Enter Fal.ai Key", type="password")

if st.button("Magic Generate ✨"):
    if not api_key:
        st.error("Pehle Sidebar mein API Key dalein!")
    else:
        # 2. This is the 'Brain' the front-end was missing
        with st.spinner("AI kaam kar raha hai..."):
            import os
            os.environ["FAL_KEY"] = api_key
            
            # Example for FLUX model
            handler = fal_client.submit(
                "fal-ai/flux/dev",
                arguments={"prompt": "Your image description here"}
            )
            result = handler.get()
            st.image(result['images'][0]['url'])
