import streamlit as st
import pandas as pd
import numpy as np
from config import *

st.title("Data Explainability")

data = pd.read_csv(config["data_path"])

text = st.text_input("Enter your term", "")
text_list = text.split(",")
text_list = [txt.strip() for txt in text_list]

if st.button("Search"):
    st.write("Searching for", text)
    data['match'] = data[config['search_col']].apply(lambda x: 1 if 
                                                 any([text.lower() in str(x).lower() for text in text_list]) else 0)
    st.dataframe(data[data.match == 1][[config['search_col'], config['result_col']]])

