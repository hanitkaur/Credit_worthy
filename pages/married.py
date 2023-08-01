import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Credit Worthiness Of the Applicant", page_icon="📈")

st.markdown("# Married Analysis")
st.sidebar.header("Married")

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

st.header("Analysis Of Married Feature")
st.write("(Assumption:- Marital status can play a role in loan approval as married individuals might be perceived as more financially stable and responsible compared to unmarried. However, this needs to be analysed carefully to avoid any biased decision-making.)")

st.write(px.histogram(df_1, x="Married",color='Loan_Status',text_auto=True))
st.write(px.histogram(df_1, x="Married",color='Loan_Status',text_auto=True,barnorm="percent"))
st.subheader("It is inferred that there is no distinctional difference that infer that married people are preferred more that unmarried.")
st.markdown("""---""")

st.subheader("Statistical Analysis of Married with other features")

# comparing the Married with other features
from scipy.stats import chi2_contingency

# Create a cross-tabulation of Married and each categorical feature
categorical_features = ['Dependents','Education', 'Self_Employed', 'Property_Area','Credit_History']
for feature in categorical_features:
    contingency_table = pd.crosstab(df_1['Married'], df_1[feature])
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Print the results
    st.write(f"Chi-square test for {feature}:")
    st.write(f"Chi-square statistic: {chi2}")
    st.write(f"P-value: {p}")
    if p < 0.05:
        st.write("There is a significant association between married and the ",feature)
    else:
        st.write("There is no significant association between married and the ",feature)
    st.write("")
st.markdown("""---""")
st.subheader("Statistical Analysis of Married with Applicant Income")
from scipy.stats import ttest_ind

married_income = df[df_1['Married'] == 'Yes']['ApplicantIncome']
unmarried_income = df[df_1['Married'] == 'No']['ApplicantIncome']
t_stat, p_value = ttest_ind(married_income, unmarried_income)
st.write("T-test for ApplicantIncome:")
st.write(f"T-statistic: {t_stat}")
st.write(f"P-value: {p_value}")
if p_value < 0.05:
    st.write("There is a significant difference in ApplicantIncome between married and unmarried applicants.")
else:
    st.write("There is no significant difference in ApplicantIncome between married and unmarried applicants.")

st.markdown("""---""")
st.subheader("Statistical Analysis of Married with Loan Amount")
married_income = df[df_1['Married'] == 'Yes']['LoanAmount']
unmarried_income = df[df_1['Married'] == 'No']['LoanAmount']
t_stat, p_value = ttest_ind(married_income, unmarried_income)
st.write("T-test for ApplicantIncome:")
st.write(f"T-statistic: {t_stat}")
st.write(f"P-value: {p_value}")
if p_value < 0.05:
    st.write("There is a significant difference in LoanAmount between married and unmarried applicants.")
else:
    st.write("There is no significant difference in LoanAmount between married and unmarried applicants.")


# doing further analysis
married=pd.DataFrame(df_1.groupby(by=['Married','Dependents','Loan_Status'])['Loan_ID'].count()).reset_index()
married['percentage'] = married.groupby(['Married','Dependents','Loan_Status']).sum('Loan_ID').groupby(level=0).apply(lambda x: 100 * x / float(x.sum())).values
st.markdown("""---""")
st.subheader("Analysing Married and Dependents")

st.write(px.bar(married, x="Married", y="percentage", color="Loan_Status", pattern_shape="Dependents",text_auto=True))
st.write("If you are unmarried and no dependents you have chance of getting approval keeping other things into consideration")