import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Credit Worthiness Of the Applicant", page_icon="📈")

st.markdown("# Analysis of Gender")
st.sidebar.header("Gender")

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

st.caption("(Assumption :- That gender won't be an important factor in determining the loan approval status)")
# checking the gender count
st.write(px.histogram(df_1, x="Gender",color='Loan_Status',text_auto=True))
st.write(px.histogram(df_1, x="Gender",color='Loan_Status',text_auto=True,barnorm="percent"))
st.subheader("**Inference:- We can say that loan approval is not biased on the basis of Gender, although we find that males contribute 82% of data compared to female.**")
st.markdown("""---""")
st.subheader("Statistical Analysis of Gender with other categorical features")
from scipy.stats import chi2_contingency

# Create a cross-tabulation of gender and each categorical feature
categorical_features = ['Married','Dependents','Education', 'Self_Employed', 'Property_Area','Credit_History']
for feature in categorical_features:
    contingency_table = pd.crosstab(df_1['Gender'], df_1[feature])
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Print the results
    st.write(f"Chi-square test for {feature}:")
    st.write(f"Chi-square statistic: {chi2}")
    st.write(f"P-value: {p}")
    if p < 0.05:
        st.write("There is a significant association between gender and the ",feature)
    else:
        st.write("There is no significant association between gender and the ",feature)
    st.write("")
    
st.markdown("""---""")
st.subheader("Statistical Analysis of Gender with Applicant Income")  
# t-test
from scipy.stats import ttest_ind
male_income = df[df_1['Gender'] == 'Male']['ApplicantIncome']
female_income = df[df_1['Gender'] == 'Female']['ApplicantIncome']
t_stat, p_value = ttest_ind(male_income, female_income)
st.write("T-test for ApplicantIncome:")
st.write(f"T-statistic: {t_stat}")
st.write(f"P-value: {p_value}")
if p_value < 0.05:
    st.write("There is a significant difference in ApplicantIncome between male and female applicants.")
else:
    st.write("There is no significant difference in ApplicantIncome between male and female applicants.")
st.markdown("""---""")
st.subheader("Statistical Analysis of Gender with Loan Amount")

from scipy.stats import ttest_ind
male_income = df[df_1['Gender'] == 'Male']['LoanAmount']
female_income = df[df_1['Gender'] == 'Female']['LoanAmount']
t_stat, p_value = ttest_ind(male_income, female_income)
st.write("T-test for LoanAmount:")
st.write(f"T-statistic: {t_stat}")
st.write(f"P-value: {p_value}")

if p_value < 0.05:
    st.write("There is a significant difference in loan amount between male and female applicants.")
else:
    st.write("There is no significant difference in loan amount between male and female applicants.")
   

st.markdown("""---""")    
st.subheader("Inference:- We found certain significant relationship between gender and following features :- Loan Amount,Married and Dependents")
st.markdown("""---""")

# Analysing the relationship further
gender=pd.DataFrame(df_1.groupby(by=['Gender','Married','Loan_Status'])['Loan_ID'].count()).reset_index()
gender['percentage'] = gender.groupby(['Gender', 'Married','Loan_Status']).sum('Loan_ID').groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values

st.header(" Analysing relationship between Gender and Married")
st.write(px.bar(gender, x="Gender", y="percentage", color="Loan_Status", pattern_shape="Married",text_auto=True))
st.write("This is the clear indication that if you are Married Male and you are unmarried Female you have high chances of getting the Loan approval.")

# now checking for Gender and dependents
dep=pd.DataFrame(df_1.groupby(by=['Gender','Dependents','Loan_Status'])['Loan_ID'].count()).reset_index()
dep['percentage'] = dep.groupby(['Gender', 'Dependents','Loan_Status']).sum('Loan_ID').groupby(level=0).apply(lambda x: 100 * x /float(x.sum())).values
st.header(" Analysing relationship between Gender and Dependents")
st.markdown("""---""")
st.write(px.bar(dep, x="Gender", y="percentage", color="Loan_Status", pattern_shape="Dependents",text_auto=True))
st.write("This is to be noted that if you dont have any dependent you have high chances of approval of loan")
