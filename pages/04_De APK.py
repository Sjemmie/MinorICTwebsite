import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(layout='wide', initial_sidebar_state='collapsed')

st.header("De menselijke APK")

col1, col2 = st.columns(2)
with col1:
    image = 'images/checklist.png'
    st.image(image, use_column_width=True)
with col2:
    st.write("""
    Het idee wat het meeste aanspraak had binnen ons groepje was het idee van Menno. De uiteindelijke keuze is dus ook 
    het idee van Menno. Met behulp van de Design Thinking methode hebben we verder onderzoek gedaan naar EPD's in de zorg. 
    Al vrij snel kwamen we erachter dat er al veel onderzoek is naar geweest. Ook zijn verschillende partijen er al mee 
    bezig geweest maar is geen van hen tot een oplossing gekomen. We kwamen er achter dat we eigenlijk het wiel opnieuw 
    aan het uitvinden waren en dus zijn we terug gegaan naar de tekentafel. Tijdens een brainstormsessie zijn we op het 
    idee van de menselijke APK gekomen. Het is een combinatie tussen de apk van je auto en een bevolkingsonderzoek. In 
    plaats van dat elke Nederlander zich op zijn 55e laat controleren, kan hij/zij dit bijvoorbeeld elk jaar doen. Het 
    idee erachter is dat mensen zich bewuster worden van hun gezondheid. Dit heeft als gevolg dat wij als samenleving 
    gezonder worden. Zo kan men langer genieten van zijn/haar pension. Ben je minder vaak ziek. Hoeft de verzekering 
    minder uit te keren. Is je baas blij, want je hebt minder verzuim dagen. Tijdens een APK kunnen mogelijk in een 
    vroegtijdig stadium ziektes worden opgespoord, voordat het te laat is. Zo kun je tijdig handelen. Als toevoeging 
    aan dit idee hebben we een eerste opzet gemaakt voor een mobiele app waarmee mensen hun APK kunnen inplannen, maar 
    ook gegevens en uitslagen kunnen inzien. 
    """)

# create whitespace
st.markdown("##")
st.markdown("##")

st.subheader("Een filmpje met uitleg over de app")

# add Youtube video
data = "https://www.youtube.com/watch?v=pJdenUXx-2E"
st.video(data, format="url", start_time=0)

# create whitespace
st.markdown("##")
st.markdown("##")

# next and previous page buttons
colp, coln = st.columns([1, 0.15])

with colp:
    if st.button("Vorige Pagina"):
        switch_page("Projecten")

with coln:
    if st.button("Volgende Pagina"):
        switch_page("Archief")