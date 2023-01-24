import streamlit as st
import webbrowser

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

    url = "[Het Archief](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl" \
          "/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments" \
          "%2Fproject%20minor%20ICT%20voor%20niet%20ICT%27%20ers&ga=1)"
    # if st. button("Naar het archief", key='archief'):
    #    webbrowser.open(url)
    st.markdown(url, unsafe_allow_html=True)
