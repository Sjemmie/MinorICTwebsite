import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import webbrowser

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

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

# create whitespace
st.markdown("##")
st.markdown("##")

# next and previous page buttons
colp, coln = st.columns([1, 0.15])

with colp:
    if st.button("Vorige Pagina"):
        switch_page("De APK")

with coln:
    if st.button("Volgende Pagina"):
        switch_page("Contact Us")
