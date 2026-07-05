import streamlit as st
from PyPDF2 import PdfReader
from langchain.splitter import CharacterTextSplitter

def main():
    print("Hallo")
    
    # Was ist unseres Ziel ?
    # Users zu erlauben mit ihrer PDF-Doku zu chatten
    # Als Erstes brauchen wir ein Interface, ueber das Users ihre PDF hochladen koennen
    # dafuer brauchen wir streamlit
    
    # wir richten erstmal die streamlit configuration ein
    st.set_page_config(page_title="Ask your PDF", page_icon=":books")
    st.header("Ask your PDF")
    
    pdf = st.file_uploader("Upload PDF")
    
    # wie brauchen ein Guard check here falls der User kein PDF hochlädt
    if pdf is not None:
        #danach wir mussen text extrahieren, dafür benötigen wir ein PdfReader Objekt
        text = ""
        for page in PdfReader(pdf).pages:
            text += page.extract_text()

        st.write(text)
        

if __name__ == "__main__":
    main()