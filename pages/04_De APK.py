import streamlit as st

st.set_page_config(layout='wide')

# center title of the page
fill_space1, title, fill_space2 = st.columns(3)

with title:
    st.header("De menselijke APK")
    st.write("""
    De uiteindelijke keuze is gevallen op de gezonheidszorg sector. We hebben dankzij de Design Thinking methode het
    idee wat aangepast zodat het 'beter' was dan het idee dat we in eerste instantie hadden bedacht. 
    """)
# create whitespace
st.markdown("##")
st.markdown("##")