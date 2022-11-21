import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image('images/kluis.png')

with col2:
    st.header("Archief")
    st.write('''
    Voor de minor, hebben wij een archief aangemaakt. 
    Hierin staan onze uitwerkingen en rapportages beschreven.
    ''')
    st. button("Naar het archief", key='archief')