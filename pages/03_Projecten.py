import streamlit as st
from resizemain import resize_projecten
import webbrowser

st.set_page_config(layout='wide')

# center title of the page
fill_space1, title, fill_space2 = st.columns(3)

with title:
    st.header("Projecten")
    st.write("Wij hebben een onderzoek verricht binnen ons werkgebied "
                 "(hoofdvraag) en daarover een rapport geschreven. Hieronder "
                 "ziet u de samenvattingen van onze onderzoeken.")
# create whitespace
st.markdown("##")
st.markdown("##")

col1, col2 = st.columns(2)

with col1:
    image = resize_projecten('images/accountancy.png')
    st.image(image, use_column_width='auto')
with col2:
    st.subheader("Accountantscontrole efficiënter door boekhoudbot")
    st.write('''
    De problemen die een accountant tegenkomt bij zijn controlerende werkzaamheden, 
    zijn fouten die gemaakt worden bij het inboeken van facturen. Wanneer de invoer 
    automatisch zou verlopen, worden er geen fouten meer gemaakt en verloopt de 
    controle ook efficiënter. Als een onderneming ook nog gebruik gaat maken van
     een boekhoudbot, zou de boekhouding zelfs voor 100% geautomatiseerd kunnen worden. 
     De boekhoudbot verwerkt alle regels van de belastingdienst in de boekhouding. 
     Hierdoor maakt de ondernemer ook nog eens optimaal gebruik van de belastingvoordelen. 
    ''')
    url = "[Onderzoeksrapport](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl" \
          "/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments" \
          "%2Fproject%20minor%20ICT%20voor%20niet%20ICT%27%20ers%2FBeroepenveld%20analyse%2FPDF" \
          "%20formaat%2FDe%20toekomst%20binnen%20accountancy%2Epdf&parent=%2Fpersonal%2Fmenno_" \
          "zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%20ICT%20voor%20niet%20ICT%27%" \
          "20ers%2FBeroepenveld%20analyse%2FPDF%20formaat&ga=1)"
    # if st.button("Onderzoeksrapport", key='onderzoek_david'):
    #    webbrowser.open(url)
    st.markdown(url, unsafe_allow_html=True)

# create whitespace
st.markdown("##")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Een nieuw planningssysteem voor op het laboratorium")
    st.write('''
    Op dit moment wordt er een planningssysteem gebruikt wat niet aan de 
    wensen van de gebruikers voldoet. Het programma kiest samples verkeerd 
    uit, medewerkers worden under en overplanned en er wordt niet naar de 
    huidige prioriteiten gekeken. Er moet een nieuw systeem komen om deze 
    problemen op te lossen.
    ''')

    url = "[Onderzoeksrapport](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl" \
          "/_layouts/15/onedrive.aspx?ct=1665743172799&or=OWA-NT&cid=826f4617-ab11-c1b1-4649-" \
          "674b7428668b&ga=1&id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2F" \
          "project%20minor%20ICT%20voor%20niet%20ICT%27%20ers%2FBeroepenveld%20analyse%2FPDF%" \
          "20formaat%2FVerkenning%20beroepsveld%20Daan%20Lieftink%2Epdf&parent=%2Fpersonal%2F" \
          "menno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%20ICT%20voor%20niet%20" \
          "ICT%27%20ers%2FBeroepenveld%20analyse%2FPDF%20formaat)"
    # if st.button('Onderzoeksrapport', key='onderzoek_daan'):
    #    webbrowser.open(url)
    st.markdown(url, unsafe_allow_html=True)

with col4:
    image = resize_projecten('images/lab.png')
    st.image(image, use_column_width='auto')

# create whitespace
st.markdown("##")

col5, col6 = st.columns(2)

with col5:
    image = resize_projecten('images/parametrischontwerpen.png')
    st.image(image, use_column_width='auto')

with col6:
    st.subheader("Parametrisch Ontwerpen")
    st.write('''
    Het automatisch genereren van modellen op basis van data en relaties 
    oftewel parametrisch ontwerpen. Het bedrijf waar ik stage heb gelopen 
    ziet hier kansen liggen en wil deze graag aanpakken. Ze willen met input 
    van de opdrachtgever een model kunnen genereren zonder dat hier een 
    tekenaar aan te pas komt. Als uitgangspunt kan een uitbouw gebruikt worden. 
    De opdrachtgever geeft aan hoe diep, breed en hoog de uitbouw wordt en 
    met behulp van een script zal hier een eerste opzet voor gegenereerd 
    worden door de computer en de input van de opdrachtgever. Zo worden er 
    minder fouten gemaakt en kan er tijd bespaart worden.
    ''')

    url = "[Onderzoeksrapport](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_" \
          "zandvliet_student_hu_nl/_layouts/15/onedrive.aspx?ga=1&id=%2Fpersonal%2F" \
          "menno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%20ICT%20voor" \
          "%20niet%20ICT%27%20ers%2FBeroepenveld%20analyse%2FPDF%20formaat%2FTICT-MICT%" \
          "20-%20Beroepenveldanalyse%20-%20Youri%20Dibbet%2Epdf&parent=%2Fpersonal%2F" \
          "menno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%20ICT%20voor%20" \
          "niet%20ICT%27%20ers%2FBeroepenveld%20analyse%2FPDF%20formaat)"
    # if st.button('Onderzoeksrapport', key='onderzoek_youri'):
    #    webbrowser.open(url)
    st.markdown(url, unsafe_allow_html=True)

# create whitespace
st.markdown("##")

col7, col8 = st.columns(2)


with col7:
    st.subheader("Gezondheidszorgtechnologie")
    st.write('''
    In een onderzoek dat ik (Menno) heb uitgevoerd naar het gebruik van elektronische 
    patiëntendossiers (EPD's), ben ik erachter gekomen dat er een grote spreiding is 
    per sector. In de ziekenhuissector is de marktleider overduidelijk Chipsoft. Chipsoft 
    is actief bezig met het versterken van haar machtspositie door communicatie met 
    andere EPD's te verhinderen en hun bizarre winstmarge (50% van de omzet) zo hoog 
    mogelijk te houden. Dit doet Chipsoft door een product te leveren wat geen automatische 
    terugkoppeling maakt tussen verschillende zorgmedewerkers. Omdat de rol van Chipsoft zo 
    groot is, is het haast onmogelijk om een goed vertaalsysteem tussen verschillende EPD's 
    te maken. Daarom heb ik een opzet gemaakt voor een systeem voor de gehele Nederlandse 
    zorg waarbij automatische terugkoppeling van toepassing is. Hier lees je meer over in 
    mijn onderzoeksverslag.
    ''')

    url = "[Onderzoeksrapport](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl" \
          "/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments" \
          "%2Fproject%20minor%20ICT%20voor%20niet%20ICT%27%20ers%2FBeroepenveld%20analyse%2FPDF" \
          "%20formaat%2FGZT%20en%20ICT%20%281%29%2Epdf&parent=%2Fpersonal%2Fmenno_zandvliet_" \
          "student_hu_nl%2FDocuments%2Fproject%20minor%20ICT%20voor%20niet%20ICT%27%20ers" \
          "%2FBeroepenveld%20analyse%2FPDF%20formaat&ga=1)"
    # if st.button("Onderzoeksrapport", key='onderzoek_menno'):
    #    webbrowser.open(url)
    st.markdown(url, unsafe_allow_html=True)

with col8:
    image = resize_projecten('images/gezondheid.png')
    st.image(image, use_column_width='auto')

# create whitespace
st.markdown("##")

col9, col10 = st.columns(2)

with col9:
    image = resize_projecten('images/oog.png')
    st.image(image, use_column_width='auto')

with col10:
    st.subheader("Optometrie Contactlenzen")
    st.write('''
    Een optometrist doet volledige oogonderzoeken en mag optische hulpmiddelen inschakelen. 
    Onder de optische hulpmiddelen vallen ook contactlenzen onder. Door ervaring ben ik 
    erachter gekomen dat lensdrager minder zorgvuldiger omgaan met contactlenzen dan dat 
    ik dacht. Dit kan serieuze gevolgen hebben voor de ogen. In mijn rapport wordt hier 
    verder naar gekeken. 
    ''')

    url = "[Onderzoeksrapport](https://hogeschoolutrecht-my.sharepoint.com/personal/menno_zandvliet_student_hu_nl" \
          "/_layouts/15/onedrive.aspx?ct=1667895179230&or=OWA-NT&cid=c3685b74-3801-aaa0-c3ca-" \
          "739dbdbd09bf&ga=1&id=%2Fpersonal%2Fmenno_zandvliet_student_hu_nl%2FDocuments%2F" \
          "project%20minor%20ICT%20voor%20niet%20ICT%27%20ers%2FBeroepenveld%20analyse%2FPDF%" \
          "20formaat%2FRapport%20Luuk%20Rutten%20Minor%20ICT%2Epdf&parent=%2Fpersonal%2F" \
          "menno_zandvliet_student_hu_nl%2FDocuments%2Fproject%20minor%20ICT%20voor%20niet%" \
          "20ICT%27%20ers%2FBeroepenveld%20analyse%2FPDF%20formaat)"
    # if st.button('Onderzoeksrapport', key='onderzoek_luuk'):
    #    webbrowser.open(url)
    st.markdown(url, unsafe_allow_html=True)

# create whitespace
st.markdown("##")