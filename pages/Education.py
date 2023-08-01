import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Credit Worthiness Of the Applicant", page_icon="📈")

st.markdown("# Education Analysis")
st.sidebar.header("Education")

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

st.header("Analysis Of Education")
st.caption("Assumption-Education level may also influence loan approval decisions. Higher education might be associated with better job opportunities and higher income. The two assumptions can be that educated people might need loan less and if they need it will be approved easily considering the income.")

st.write(px.histogram(df_1, x="Education",color='Loan_Status',text_auto=True))
st.write(px.histogram(df_1, x="Education",color='Loan_Status',text_auto=True,barnorm="percent"))
st.subheader("Inference:- If you are graduate you have high chances of getting approval of loan.")
st.markdown("""---""")
st.subheader(" Statistical Analysis of Education with other features")
from scipy.stats import chi2_contingency

# Create a cross-tabulation of Married and each categorical feature
categorical_features = ['Dependents', 'Self_Employed', 'Property_Area','Credit_History']
for feature in categorical_features:
    contingency_table = pd.crosstab(df_1['Education'], df_1[feature])
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Print the results
    st.text(f"Chi-square test for {feature}:")
    st.text(f"Chi-square statistic: {chi2}")
    st.text(f"P-value: {p}")
    if p < 0.05:
        st.write("There is a significant association between education and the ",feature)
    else:
        st.write("There is no significant association between education and the ",feature)
    st.write("")
st.markdown("""---""")
st.subheader(" Statistical Analysis of Education with Applicant Income")
from scipy.stats import ttest_ind

grad = df[df_1['Education'] == 'Graduate']['ApplicantIncome']
not_grad = df[df_1['Education'] == 'Not Graduate']['ApplicantIncome']
t_stat, p_value = ttest_ind(grad,not_grad)
st.write("T-test for ApplicantIncome:")
st.write(f"T-statistic: {t_stat}")
st.write(f"P-value: {p_value}")
if p_value < 0.05:
    st.write("There is a significant difference in ApplicantIncome of graduate and not graduate.")
else:
    st.write("There is no significant difference in ApplicantIncome of graduate and not graduate.")

st.markdown("""---""")
st.subheader(" Statistical Analysis of Education with Loan Amount")   
from scipy.stats import ttest_ind

grad= df[df_1['Education'] == 'Graduate']['LoanAmount']
not_grad = df[df_1['Education'] == 'Not Graduate']['LoanAmount']
t_stat, p_value = ttest_ind(grad,not_grad)
st.write("T-test for ApplicantIncome:")
st.write(f"T-statistic: {t_stat}")
st.write(f"P-value: {p_value}")
if p_value < 0.05:
    st.write("There is a significant difference in Loan Amount of graduate and not graduate.")
else:
    st.write("There is no significant difference in Loan Amount of graduate and not graduate.")

st.markdown("""---""")
st.subheader(" Analysing the Education and Credit_History")   
# Further Analysis
edu=pd.DataFrame(df_1.groupby(by=['Education','Credit_History','Loan_Status'])['Loan_ID'].count()).reset_index()
edu['percentage'] = edu.groupby(['Education','Credit_History','Loan_Status']).sum('Loan_ID').groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values

st.write(px.bar(edu, x="Education", y="percentage", color="Loan_Status", pattern_shape="Credit_History",text_auto=True))
st.subheader("Inference :- You have 70% chance of loan approval if you are graduated and have credit history")