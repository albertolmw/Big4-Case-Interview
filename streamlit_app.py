import streamlit as st
import pandas as pd
st.title('First App')
st.write('Hello World')
path="https://github.com/albertolmw/DataScientist-Case-Interview/blob/main/Data.xlsx"
df1 = pd.read_excel(path, sheet_name='Charges')
df2 = pd.read_excel(path, sheet_name='Other data')
df3 = pd.read_excel(path, sheet_name='Churn')
df1
