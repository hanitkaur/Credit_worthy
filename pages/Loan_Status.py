import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Credit Worthiness Of the Applicant", page_icon="📈")

st.markdown("# Loan Status Analysis")
st.sidebar.header("Loan status")

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

st.write(px.histogram(df_1, x="Loan_Status",color='Loan_Status',text_auto=True))
st.subheader("Inference:- We can say data is imbalance as we have 68% of data of acceptance and only 32% of rejection of Loan.")

st.markdown("""---""")
st.subheader("Statistical Analysis of Loan status with other features")
from scipy.stats import chi2_contingency

# Create a cross-tabulation of gender and each categorical feature
categorical_features = ['Gender','Married','Dependents','Education', 'Self_Employed', 'Property_Area','Credit_History']
for feature in categorical_features:
    contingency_table = pd.crosstab(df_1['Loan_Status'], df_1[feature])
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Print the results
    st.write(f"Chi-square test for {feature}:")
    st.write(f"Chi-square statistic: {chi2}")
    st.write(f"P-value: {p}")
    if p < 0.05:
        st.write("There is a significant association between Loan_Status and the ",feature)
    else:
        st.write("There is no significant association between Loan_Status and the ",feature)
    st.write("")
    
st.markdown("""---""")   
st.subheader(" Statistical Analysis of Loan Status with Applicant Income")
# t-test
from scipy.stats import ttest_ind
yes = df[df_1['Loan_Status'] == 'Y']['ApplicantIncome']
no = df[df_1['Loan_Status'] == 'N']['ApplicantIncome']
t_stat, p_value = ttest_ind(yes,no)
st.write("T-test for ApplicantIncome:")
st.write(f"T-statistic: {t_stat}")
st.write(f"P-value: {p_value}")
if p_value < 0.05:
    st.write("There is a significant difference in ApplicantIncome of approved and rejected applicants.")
else:
    st.write("There is no significant difference in ApplicantIncome of approved and rejected applicants.")
 

st.markdown("""---""")
st.subheader(" Statistical Analysis of Loan Status with Loan Amount")
from scipy.stats import ttest_ind
yes = df[df_1['Loan_Status'] == 'Y']['LoanAmount']
no = df[df_1['Loan_Status'] == 'N']['LoanAmount']
t_stat, p_value = ttest_ind(yes,no)
st.write("T-test for LoanAmount:")
st.write(f"T-statistic: {t_stat}")
st.write(f"P-value: {p_value}")

if p_value < 0.05:
    st.write("There is a significant difference in loan amount of approved and rejected applicants.")
else:
    st.write("There is no significant difference in loan amount of approved and rejected applicants..")
    
    
