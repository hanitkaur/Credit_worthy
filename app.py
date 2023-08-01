import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Page 1----------------------------------------------------------------------------
st.set_page_config(page_title="Credit Worthiness Of the Applicant", page_icon="📈")

st.markdown("# DataSet Summary")
st.sidebar.header("Summary")
col1,col2=st.columns(2)

# reading the data
df=pd.read_excel('train.xlsx')
df['Dependents']=df['Dependents'].astype(str)
with col1:
    st.header("""Overlook of the dataset:-""")
    st.write(df.head(10))

# creating the summary of the data
def get_summary(df):
    st.write("The shape of data is : ",df.shape)
    summary=pd.DataFrame(df.dtypes,columns=['Data_Type'])
    summary=summary.reset_index()
    summary['Name']=summary['index']
    summary=summary[['Name','Data_Type']]
    summary['Missing']=df.isnull().sum().values
    summary['unique']=df.nunique().values
    summary['per_missing']=(df.isnull().sum().values/df.shape[0])*100
    return summary.astype(str)

with col2:
    st.header("""Summary of the dataset is:-""")
    st.write(get_summary(df))

#Now checking all the unique values
def get_unique(df):
    for x in df.columns:
        if df[x].dtype=='object':
            st.write("------------------------------------")
            st.write("Unique Values of ",x," is:-")
            st.write(df[x].value_counts())
            st.write("------------------------------------")
            st.write("\n")
st.header(" Getting the unique values of categorical features:-")
st.write(get_unique(df))

st.header("Some important pointer:-")
st.write("Percentage of loss of rows after removing the null values :",((df.shape[0]-df.dropna().shape[0])/df.shape[0]) *100)
st.write("Loosing 19% rows is much as we have less of data so, we will treat the null values")



st.button("Re-run")

















