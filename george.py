import streamlit as st
st.set_page_config(
    page_title="Aec Tax Estimator")

st.title("AEC Tax Estimator")
st.text_input("Business Name", key="name")
Business_Registration = st.selectbox('Select Registration Status:',('Yes', 'No','In Progress','_'))
Business_Registration_Structure = st.selectbox('Select Registration Status:',('Sole-Proprietor', 'Partnership','Private Company','_'))
Business_Registration = st.selectbox('Pin No:',('Yes', 'No','_'))

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:

# Or even better, call Streamlit functions inside a "with" block:
with left_column:
    chosen = st.radio(
        'Obligation-Tax-type',
        ("Income Tax Company (ITC)", "VAT-Tax", "WHT Tax", "PAYEE Tax","Monthly-MRI Tax",))
    st.write(f"You have chosen {chosen} !")
st.header("**Income**")
st.subheader("Sales Total")
colAnnualSal, colTax = st.columns(2)


with colAnnualSal:
    salary = st.number_input("Enter your annual Sales(Ksh): ", min_value=0.0, format='%f')
with colTax:
    tax_rate = st.number_input("Enter your tax rate(%): ", min_value=0.0, format='%f')

tax_rate = tax_rate / 100.0
salary_after_taxes = salary * (1 - tax_rate)
monthly_takehome_salary = round(salary_after_taxes / 12.0, 2)



st.header("**Tax Estimated**")
st.subheader("Monthly Tax: Ksh" + str(round(monthly_takehome_salary,2)))
