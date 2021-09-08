import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Aec Tax Estimator")

st.title("AEC Tax Estimator")
st.text_input("Business Name", key="name")
Business_Registration = st.selectbox('Select Registration Status:',('Yes', 'No','In Progress'))
Business_Registration_Structure = st.selectbox('Select Registration Status:',('Sole-Proprietor', 'Partnership','Private Company'))
st.header("**Taxes**")
st.subheader("Sales Tax")
colAnnualSal, colTax = st.columns(2)



with colAnnualSal:
    salary = st.number_input("Enter your annual Sales(Ksh): ", min_value=0.0, format='%f')
with colTax:
    tax_rate = st.number_input("Enter your tax rate(%): ", min_value=0.0, format='%f')

tax_rate = tax_rate / 100.0
salary_after_taxes = salary * (1 - tax_rate)
monthly_takehome_salary = round(salary_after_taxes / 12.0, 2)

st.header("**Monthly Expenses**")
colExpenses1, colExpenses2 = st.columns(2)

with colExpenses1:
    st.subheader("Monthly Rental Income Tax")
    monthly_rental = st.number_input("Enter your monthly rental(Ksh): ", min_value=0.0, format='%f')

    st.subheader("Company ITC Tax")
    daily_food = st.number_input("Enter your ITC Amount (Ksh): ", min_value=0.0, format='%f')
    monthly_food = daily_food * 30

    st.subheader("PAYE")
    monthly_unforeseen = st.number_input("Enter your monthly unforeseen expenses (Ksh): ", min_value=0.0, format='%f')

with colExpenses2:
    st.subheader(" MRI Rate")
    monthly_transport = st.number_input("Enter your monthly tax rate (Ksh): ", min_value=0.0, format='%f')

    st.subheader("Monthly WHT Tax ")
    monthly_utilities = st.number_input("Enter your monthly WHT tax (Ksh): ", min_value=0.0, format='%f')

    st.subheader(" TOT Tax")
    monthly_entertainment = st.number_input("Enter your TOT Tax (Ksh): ", min_value=0.0, format='%f')

monthly_expenses = monthly_rental + monthly_food + monthly_transport + monthly_entertainment + monthly_utilities + monthly_unforeseen
monthly_savings = monthly_takehome_salary - monthly_expenses

st.header("**Tax Estimated**")
st.subheader("Monthly Tax: Ksh" + str(round(monthly_takehome_salary,2)))
st.subheader("Monthly Expenses: Ksh" + str(round(monthly_expenses, 2)))
st.subheader("Monthly Savings: Ksh" + str(round(monthly_savings, 2)))