from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from openai import OpenAI
import streamlit as st
import os

def main():
    load_dotenv(override=True)

    # Was ist unseres Ziel ?
    # Users zu erlauben mit ihrer PDF-Doku zu chatten
    # Als Erstes brauchen wir ein Interface, ueber das Users ihre PDF hochladen koennen
    # dafuer brauchen wir streamlit
    
    # wir richten erstmal die streamlit configuration ein
    st.set_page_config(page_title="Ask your PDF", page_icon=":books")
    st.header("Ask your PDF")
    
    pdf = st.file_uploader("Upload PDF", type="pdf")
    
    # wie brauchen ein Guard check here falls der User kein PDF hochlädt
    if pdf is not None:
        #danach wir mussen text extrahieren, dafür benötigen wir ein PdfReader Objekt
        text = ""
        for page in PdfReader(pdf).pages:
            text += page.extract_text()
            
        #wir splitten den Text in kleine Chunks, dafuer benoetigen wir ein Textsplitter
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        
        #create chunks
        chunks = text_splitter.split_text(text)
        
        #Chunks zum Embeddings wandel, dafuer benoetigen wir ein Encoder
        #wir koennen als bsp das Embeddiungmodel von Openai verwenden
        encoder = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, encoder)
        
        #Retrieval 
        #wir nehmen zuerst Input von dem Benutzer
        user_question = st.text_input("Ask a question")
        if user_question:
            
            #Jetzt tun wir ein Cosine-Similarity Search
            docs = knowledge_base.similarity_search(user_question)
            
            #anschliessend geben wir das Ergebnis als Context zu unserem LLM ein
            client = OpenAI()
            
            prompt = f"""
            Beantworte die Frage basierend auf den folgenden Kontext:
            
            Kontext:
            {docs}
            
            Frage:
            {user_question}
            """
            
            response = client.responses.create(
                model="gpt-5-nano",
                input=prompt
            )
            
            st.write(response.output_text)
    
if __name__ == "__main__":
    main()