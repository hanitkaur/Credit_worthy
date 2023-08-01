import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Credit Worthiness Of the Applicant", page_icon="📈")

st.markdown("# Credit History Analysis")
st.sidebar.header("Credit History")

# reading the data
df=pd.read_excel('train.xlsx')
df['Dependents']=df['Dependents'].astype(str)

df_1=df
df_1['Gender'] = df_1['Gender'].fillna(df_1['Gender'].mode()[0])
df_1['Loan_Amount_Term'] = df_1['Loan_Amount_Term'].fillna(df_1['Loan_Amount_Term'].mode()[0])
df_1['Married'] = df_1['Married'].fillna(df_1['Married'].mode()[0])
df_1['Dependents'] = df_1['Dependents'].fillna(df_1['Dependents'].mode()[0])
df_1['Self_Employed'] = df_1['Self_Employed'].fillna(df_1['Self_Employed'].mode()[0])
df_1['Credit_History'] = df_1['Credit_History'].fillna(df_1['Credit_History'].mode()[0])

st.header("Analysis of Credit_History")
st.caption("ASSUMPTION:- Credit history is a strong indicator of an applicant's creditworthiness. A positive credit history significantly increases the chances of loan approval.")

df_1['Credit_History']=df_1['Credit_History'].astype(str)
st.subheader("Analysing the Credit History")
st.write(px.histogram(df_1, x="Credit_History",color='Loan_Status',text_auto=True))
st.write(px.histogram(df_1, x="Credit_History",color='Loan_Status',text_auto=True,barnorm="percent"))
st.subheader("Inference: If you have credit history you have good chances of loan approval.")
st.markdown("""---""")
from scipy.stats import ttest_ind
st.subheader("Statistical Analysis of Credit History and Applicant Income")
yes = df[df_1['Credit_History'] == '1.0']['ApplicantIncome']
no = df[df_1['Credit_History'] == '0.0']['ApplicantIncome']
t_stat, p_value = ttest_ind(yes,no)
st.write("T-test for ApplicantIncome:")
st.write(f"T-statistic: {t_stat}")
st.write(f"P-value: {p_value}")
if p_value < 0.05:
    st.write("There is a significant difference in ApplicantIncome between people having credit history and one not having.")
else:
    st.write("There is no significant difference in ApplicantIncome between people having credit history and one not having.")

st.markdown("""---""")
st.subheader("Statistical Analysis of Credit History and Loan Amount")
yes = df[df_1['Credit_History'] == '1.0']['LoanAmount']
no = df[df_1['Credit_History'] == '0.0']['LoanAmount']
t_stat, p_value = ttest_ind(yes,no)
st.write("T-test for ApplicantIncome:")
st.write(f"T-statistic: {t_stat}")
st.write(f"P-value: {p_value}")
if p_value < 0.05:
    st.write("There is a significant difference in Loan Amount between people having credit history and one not having.")
else:
    st.write("There is no significant difference in Loan Amount between people having credit history and one not having.")

st.markdown("""---""")