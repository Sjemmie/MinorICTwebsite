import streamlit as st
from resizemain import resize_team
from streamlit_extras.switch_page_button import switch_page
import webbrowser

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

# center title of the page
fill_space1, title, fill_space2 = st.columns(3)

with title:
    st.header("Welkom op onze Team pagina!")

col1, col2, col3 = st.columns(3)

# create columns to line up 'belbin rapport' button
rapport1, rapport2, rapport3 = st.columns(3)


# create team member
with col1:
    image = resize_team('images/david.png')
    st.image(image, use_column_width=True)
    st.subheader("David Schimmel")
    st.write('''
    Accountancy\n
    Specialist\n
    Studentnummer:  1778480
    ''')
    st.write('''
    Een specialist komt aardig overeen bij mijn persoonlijkheid. Ik werk graag 
    alleen zodat ik zelf kan bepalen wat ik wanneer ga doen. Ook ben ik een 
    bedrijfsman. Ik ben zeer gedisciplineerd en werk graag op volgorde aan 
    een opdracht
    ''')

with rapport1:
    url = '[Belbin Rapport](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl' \
          '/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%' \
          '20minor%20ICT%20voor%20niet%20ICT%27%20ers%2F1%2E%20Belbin%20testen%2FPDF%2FBelbin%20David%2Epdf&' \
          'parent=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%20ICT%20voor%20niet%' \
          '20ICT%27%20ers%2F1%2E%20Belbin%20testen%2FPDF)'
    # if st.button("Belbin Rapport", key='belbindavid'):
    st.markdown(url, unsafe_allow_html=True)


# create team member
with col2:
    image = resize_team('images/youri.png')
    st.image(image, use_column_width=True)
    st.subheader("Youri Dibbet")
    st.write('''
    Built Environment\n
    Brononderzoeker\n
    Studentnummer: 1748563
    ''')
    st.write('''
    Als brononderzoeker en voorzitter ben ik breed geïnteresseerd, 
    positief en gericht op vernieuwing en ontwikkeling.  
    ''')

# add belbin rapport
with rapport2:
    url = '[Belbin Rapport](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl/_' \
          'layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20' \
          'minor%20ICT%20voor%20niet%20ICT%27%20ers%2F1%2E%20Belbin%20testen%2FPDF%2FTICT-MICT%20-%20Belbin%20' \
          'analyse%20-%20Youri%20Dibbet%2Epdf&parent=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%' \
          '2Fproject%20minor%20ICT%20voor%20niet%20ICT%27%20ers%2F1%2E%20Belbin%20testen%2FPDF)'
    # if st.button("Belbin Rapport", key='belbinyouri'):
    st.markdown(url, unsafe_allow_html=True)

# create team member
with col3:
    image = resize_team('images/menno.png')
    st.image(image, use_column_width=True)
    st.subheader("Menno Zandvliet")
    st.write('''
    Gezonheidszorgtechnologie\n
    Vormer\n
    Studentnummer: 1841754
    ''')
    st.write('''
    Menno moet z'n tekst nog maken 
    ''')

# add belbin rapport
with rapport3:
    url = "[Belbin Rapport](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl/_" \
          "layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%" \
          "20minor%20ICT%20voor%20niet%20ICT%27%20ers%2F1%2E%20Belbin%20testen%2FPDF%2FBelbin%20analyse%20mz%2" \
          "Epdf&parent=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%20ICT%20voor%20" \
          "niet%20ICT%27%20ers%2F1%2E%20Belbin%20testen%2FPDF)"
    # if st.button("Belbin Rapport", key='belbinmenno'):
    #    webbrowser.open(url)
    st.markdown(url, unsafe_allow_html=True)

# add whitespace
st.markdown('##')
st.markdown('##')
st.markdown('##')

# create columns for team members
col4, col5, col6 = st.columns(3)
# create columns to line up 'belbin rapport' button
rapport4, rapport5, rapport6 = st.columns(3)

# create team member
with col4:
    image = resize_team('images/daan.png')
    st.image(image, use_column_width=True)
    st.subheader("Daan Lieftink")
    st.write('''
    Voedingsmiddelentechnologie\n
    Bedrijfsman\n
    Studentnummer: 1840275
    ''')
    st.write('''
    Het blijkt dat ik een bedrijfsman en specialist ben. 
    Dit komt omdat ik het erg fijn vind om een probleem 
    of opdracht in taken op te delen en er gelijk mee aan 
    de slag te gaan. Ook wil ik graag mijn kennis over 
    specifieke onderwerpen delen met de groep en ze m.b.t 
    dit onderwerp steunen. 
    ''')

with rapport4:
    url = "[Belbin Rapport](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl" \
          "/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject" \
          "%20minor%20ICT%20voor%20niet%20ICT%27%20ers%2F1%2E%20Belbin%20testen%2FPDF%2FBelbin%20verslag%20Daan" \
          "%20Lieftink%2Epdf&parent=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%" \
          "20ICT%20voor%20niet%20ICT%27%20ers%2F1%2E%20Belbin%20testen%2FPDF)"
    # if st.button("Belbin Rapport", key='belbindaan'):
    #    webbrowser.open(url)
    st.markdown(url, unsafe_allow_html=True)

# create team member
with col5:
    image = resize_team('images/luuk.png')
    st.image(image, use_column_width=True)
    st.subheader("Luuk Rutten")
    st.write('''
    Optometrie\n
    Voorzitter\n
    Studentnummer: 1735674
    ''')
    st.write('''
    Uit de Belbin test kwam voorzitter en brononderzoeker 
    uit. De eigenschappen van deze rollen zijn kalm, nuchter, 
    realistisch en goed kunnen luisteren/reflecteren. Ik kan 
    mij goed vinden in deze eigenschappen. 
    ''')

with rapport5:
    url = "[Belbin Rapport](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl/_" \
          "layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%" \
          "20minor%20ICT%20voor%20niet%20ICT%27%20ers%2F1%2E%20Belbin%20testen%2FPDF%2Fbelbin%20groepsindeling%" \
          "20Luuk%2Epdf&parent=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%20ICT%" \
          "20voor%20niet%20ICT%27%20ers%2F1%2E%20Belbin%20testen%2FPDF)"
    # if st.button("Belbin Rapport", key='belbinluuk'):
    #    webbrowser.open(url)
    st.markdown(url, unsafe_allow_html=True)

# create whitespace
st.markdown("##")
st.markdown("##")

# next and previous page buttons
colp, coln = st.columns([1, 0.15])

with colp:
    if st.button("Vorige Pagina"):
        switch_page("Home")

with coln:
    if st.button("Volgende Pagina"):
        switch_page("Projecten")