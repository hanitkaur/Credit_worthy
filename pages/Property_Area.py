import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Credit Worthiness Of the Applicant", page_icon="📈")

st.markdown("# Property Area Analysis")
st.sidebar.header("Property Area")

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

st.header("Analysis of Property Area")
st.write(" Assumption:--The applicant's property location (rural or urban) could be a factor in the loan approval decision, as it may relate to property values and potential for property appreciation.")

st.write(px.histogram(df_1, x="Property_Area",color='Loan_Status',text_auto=True))
st.write(px.histogram(df_1, x="Property_Area",color='Loan_Status',text_auto=True,barnorm="percent"))
st.subheader("Inference: If you have property in Semi-Urban you might get loan. Since this sector is getting developed at high speed.")
st.markdown("""---""")
st.subheader(" Statistical Analysis on Property Area with Credit History")
from scipy.stats import chi2_contingency
contingency_table = pd.crosstab(df_1['Property_Area'], df_1['Credit_History'])
chi2, p, dof, expected = chi2_contingency(contingency_table)

st.write(f"Chi-square test for Credit history:")
st.write(f"Chi-square statistic: {chi2}")
st.write(f"P-value: {p}")
if p < 0.05:
        st.write("There is a significant association between property area and credit history")
else:
        st.write("There is no significant association between property area and credit history")
st.write("")