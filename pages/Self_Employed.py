import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Credit Worthiness Of the Applicant", page_icon="📈")

st.markdown("# Self Employed Analysis")
st.sidebar.header("Self Employed")

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

st.header("Analysis of Self-Employed")
st.write("Assumption-Self-employed individuals may face different considerations during loan approval, as their income stability might vary compared to salaried applicants. So self_employed individual are people who may require bigger loans as well.")

st.write(px.histogram(df_1, x="Self_Employed",color='Loan_Status',text_auto=True))
st.write(px.histogram(df_1, x="Self_Employed",color='Loan_Status',text_auto=True,barnorm="percent"))
st.subheader("Inference :- Self-Employed status has no impact on Loan Approval.")
st.markdown("""---""")

st.subheader("Statistical Analysis of Self Employed with other features")
from scipy.stats import chi2_contingency

# Create a cross-tabulation of self_employed and each categorical feature
categorical_features = ['Property_Area','Credit_History']
for feature in categorical_features:
    contingency_table = pd.crosstab(df_1['Self_Employed'], df_1[feature])
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Print the results
    st.write(f"Chi-square test for {feature}:")
    st.write(f"Chi-square statistic: {chi2}")
    st.write(f"P-value: {p}")
    if p < 0.05:
        st.write("There is a significant association between self_employed and the ",feature)
    else:
        st.write("There is no significant association between self_employed and the ",feature)
    st.text("")
st.markdown("""---""")

st.subheader("Statistical Analysis of Self Employed with Applicant Income")
from scipy.stats import ttest_ind

self = df[df_1['Self_Employed'] == 'Yes']['ApplicantIncome']
self_no = df[df_1['Self_Employed'] == 'No']['ApplicantIncome']
t_stat, p_value = ttest_ind(self,self_no)
st.write("T-test for ApplicantIncome:")
st.write(f"T-statistic: {t_stat}")
st.write(f"P-value: {p_value}")
if p_value < 0.05:
    st.write("There is a significant difference in ApplicantIncome between person who is self-employed and one who is not.")
else:
    st.write("There is no significant difference in ApplicantIncome between person who is self-employed and one who is not.")

st.markdown("""---""")

st.subheader("Statistical Analysis of Self Employed with Loan Amount")
self = df[df_1['Self_Employed'] == 'Yes']['LoanAmount']
self_no = df[df_1['Self_Employed'] == 'No']['LoanAmount']
t_stat, p_value = ttest_ind(self,self_no)
st.write("T-test for ApplicantIncome:")
st.write(f"T-statistic: {t_stat}")
st.write(f"P-value: {p_value}")
if p_value < 0.05:
    st.write("There is a significant difference in LoanAmount between person who is self-employed and one who is not.")
else:
    st.write("There is no significant difference in LoanAmount between person who is self-employed and one who is not.")

se=pd.DataFrame(df_1.groupby(by=['Education','Self_Employed','Loan_Status'])['Loan_ID'].count()).reset_index()
se['percentage'] = se.groupby(['Education','Self_Employed','Loan_Status']).sum('Loan_ID').groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
st.markdown("""---""")

st.subheader("Analysis of Self Employed with Education")
st.write(px.bar(se, x="Education", y="percentage", color="Loan_Status", pattern_shape="Self_Employed",text_auto=True))