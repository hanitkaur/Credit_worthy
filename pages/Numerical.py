import streamlit as st

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Credit Worthiness Of the Applicant", page_icon="📈")

st.markdown("# Numerical Analysis")
st.sidebar.header("Numerical Analysis")

# reading the data
df=pd.read_excel('train.xlsx')


df_1=df
df_1['Gender'] = df_1['Gender'].fillna(df_1['Gender'].mode()[0])
df_1['Loan_Amount_Term'] = df_1['Loan_Amount_Term'].fillna(df_1['Loan_Amount_Term'].mode()[0])
df_1['Married'] = df_1['Married'].fillna(df_1['Married'].mode()[0])
df_1['Dependents'] = df_1['Dependents'].fillna(df_1['Dependents'].mode()[0])
df_1['Self_Employed'] = df_1['Self_Employed'].fillna(df_1['Self_Employed'].mode()[0])
df_1['Credit_History'] = df_1['Credit_History'].fillna(df_1['Credit_History'].mode()[0])

st.header("Analysis of Applicant Income, CoapplicantIncome, Loan Amount, Loan Term")
# Box plot
st.subheader("Checking for outliers for Applicant Income")
st.write(px.box(df_1, x="Loan_Status", y="ApplicantIncome",color="Gender"))
st.markdown("""---""")

st.subheader("Check for outliers for Loan Amount")
st.write(px.box(df_1, x="Loan_Status", y="LoanAmount",color="Gender"))
st.markdown("""---""")

st.subheader("Analysing the Loan Amount and Applicant Income on basis of Married")
st.write(px.scatter(df_1,x='LoanAmount',y='ApplicantIncome',color="Loan_Status",symbol='Married'))
st.markdown("""---""")

st.subheader("Analysing the Loan Amount and Applicant Income on basis of Gender")
st.write(px.scatter(df_1,y="ApplicantIncome",x="LoanAmount",color='Loan_Status',symbol='Gender'))
st.markdown("""---""")

st.subheader("Analysing the Loan Amount and Applicant Income on basis of Education and Gender ")
st.write(px.scatter(df_1,x="LoanAmount",y="Loan_Status",symbol="Education",color='Gender'))
st.markdown("""---""")

st.subheader("Analysing the Correlation")
fig = plt.figure(figsize=(10, 4))
sns.heatmap(df_1.corr())
st.pyplot(fig)

st.markdown("""---""")
st.subheader("These are the inferences drawn from the above charts:-")

st.write("1. Applicant Income has potential outliers and could not be treated as there is no limit to income.")
st.write("2. On seperating Applicant Income on the basis of Gender, maximum outliers belomg to the Male class.")
st.write("3. Loan Amount has significant impact on Education, gender, and Married.")
st.write("4. Highest Loan Amount has been given to male as compared to female.")
st.write("5. Aplicant Income and Loan Amount is showing Linear relationship.")
st.write("6. Loan Approval is dependent if you are Male and Graduated.")
st.write("7. This further has also lead to creating of new features like Total_Income and ratio of LoanAmount to ApplicantIncome.")