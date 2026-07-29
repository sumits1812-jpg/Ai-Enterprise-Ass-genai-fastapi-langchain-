import streamlit as st
import requests
import pandas as pd
import fitz

title = st.header("Ai SQL platform")
mode = st.sidebar.selectbox("chose your file first", options=["pdf", "csv","sql" ])

if mode=="pdf":
    pdf = st.file_uploader("upload file here",type=["pdf"])
    if pdf is not None:
          docs =fitz.open(stream=pdf.read(), filetype="pdf")
          for page in docs:
           st.write(page.get_text())      
elif mode=="csv":
    csv = st.file_uploader("upload file here",type=["csv"])
    if csv is not None:
          df = pd.read_csv(csv)
          st.write(df)

else:
    st.info("connected with sql database")  

question = st.text_input("Ask your question")    

if question and st.button(("Ask AI")):
    with st.chat_message("user"):
         st.write(question)

    try:
        response = requests.post("http://127.0.0.1:8000/sql_query",json={"mode" :mode, "question" :question })
        if response.status_code ==200:
            answer = response.json()["response"]
        else:
            answer = "server error"
    except:
        answer= "fastapi error"
    with st.chat_message("Assistant"):
         st.write(answer)

            


        
