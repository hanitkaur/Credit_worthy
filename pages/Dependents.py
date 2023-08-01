import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Credit Worthiness Of the Applicant", page_icon="📈")

st.markdown("# Dependent Analysis")
st.sidebar.header("Dependents")

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

st.header("Analysis of Dependents")
st.caption("Assumption-The number of dependents could affect loan approval as individuals with more dependents might have higher financial obligations due to the expenses that incur.")

st.write(px.histogram(df_1, x="Dependents",color='Loan_Status',text_auto=True))
st.write(px.histogram(df_1, x="Dependents",color='Loan_Status',text_auto=True,barnorm="percent"))
st.subheader("Inference:- Dependents only is not the major factor in deciding the Loan Approval.")
st.markdown("""---""")
st.subheader("Statistical Analysis of Dependents with other features")
from scipy.stats import chi2_contingency

# Create a cross-tabulation of Dependents and each categorical feature
categorical_features = [ 'Self_Employed', 'Property_Area','Credit_History']
for feature in categorical_features:
    contingency_table = pd.crosstab(df_1['Dependents'], df_1[feature])
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Print the results
    st.text(f"Chi-square test for {feature}:")
    st.text(f"Chi-square statistic: {chi2}")
    st.text(f"P-value: {p}")
    if p < 0.05:
        st.write("There is a significant association between dependents and the ",feature)
    else:
        st.write("There is no significant association between dependents and the ",feature)
    st.text("")
st.markdown("""---""")