import streamlit as st
from resize import resize

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    image = resize('images/welcome.png')
    st.image(image, use_column_width='auto')
with col2:
    st.subheader("Dit is de website van Team MYLDD")
    st.info('''
    Op deze site zul je verschillende dingen terug kunnen vinden wat betreft 
    de minor ICT voor niet ICT-ers
    ''')

col3, col4 = st.columns(2)

with col3:
    st.header('Het project')
    st.subheader("Ons project bestaat uit twee delen:")
    st.write('''
Een verkenning van de rol van ICT in het beroepenveld : Er wordt onderzoek 
gedaan wat voor invloed ICT binnen het beroepenveld heeft. Zo wordt er gekeken 
naar de huidige situatie (Ist) en naar de gewenste situatie (Soll). Tot slot 
komen wij tot een conclusie wat er verbeterd kan worden om tot de die 
gewenste situatie te komen.

Pitch je innovatie: Hierbij wordt er een Mock-up (prototype) ontwikkeld van de 
innovatie die wij zouden willen doorvoeren binnen een beroepsomgeving. Dit 
prototype zal ook worden gepresenteerd.
    ''')

with col4:
    image = resize('images/projectmanage.png')
    st.image(image, use_column_width='auto')

col5, col6 = st.columns(2)

with col5:
    image = resize('images/team.png')
    st.image(image, use_column_width='auto')

with col6:
    st.title('Ons team')
    st.write('''
Wij zijn met het team een groep die graag een goed eindresultaat wilt behalen, 
waar wij gezamenlijk moeite in hebben gestoken en trots op kunnen zijn. Wij 
kunnen elkaar goed aanvullen en staan allemaal open voor feedback van andere 
groepsleden. Hierdoor hebben wij vertrouwen in een goede samenwerking en een mooi eindresultaat. 
    ''')
    st.markdown("[Dit is ons team!](Team)")