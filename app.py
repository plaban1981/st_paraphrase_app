import streamlit as st
from PIL import Image
import requests
import pandas as pd
import os
import json
#
image_path = "image.png"
image = Image.open(image_path)

st.set_page_config(page_title="Paraphrase Generation App", layout="centered")
st.image(image, caption='Paraphrase Generation')
#
# page header
st.title(f"Paraphrase Generation App")
with st.form("Generate"):
   text = st.text_input("Enter text here")
   submit = st.form_submit_button("Paraphrase")
   #
   if submit:    
        print(text)
        #
        with open("input.txt", "wb") as f:
            f.write(text.encode("utf-8"))
        os.chmod("input.txt", 0o777)
        # Paraphrase Generation API
        url = "https://app.aimarketplace.co/api/marketplace/models/paraphrase-text-36df92e2/predict/"
        payload={'data': open('input.txt','rb')}
        headers = {'Authorization': 'Api-Key GfDUn4cF.Zza6moVCDEbdMbGhSozDBWG4w6EgNYso'}

        response = requests.request("POST", url, headers=headers, files=payload)

        #print(type(response))
        #print(response.json()['output'])
        #print(response.text)
        #print(response.text.split("Predictions: [")[1].split("]")[0])
        #print(response.json()["output"])
        # output header
        st.header("Paraphrased Text")
        # output results
        st.success(response.text)   
