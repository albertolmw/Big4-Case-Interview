import streamlit as st
import pandas as pd
import requests as rq
st.title('First App')
st.write('Hello World')
path='Data.xlsx'
datos=rq.get(path)
df1 = pd.read_excel(datos.content,sheet_name='Other data')
#df2 = pd.read_excel(path, sheet_name='Other data')
#df3 = pd.read_excel(path, sheet_name='Churn')
df1

