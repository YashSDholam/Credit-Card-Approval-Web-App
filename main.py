import streamlit as st
import pickle
import numpy as np


model = pickle.load(open('model.sav', 'rb'))

def run():

    st.title("Credit Card Approval using Machine Learning")

    ## Num_family
    Num_family = float(st.selectbox('Select your family member count', [1,2,3,4,5,6]))

    ## Total_income
    st.write("""
    ## Income
    """)
    Total_income = int(st.text_input('Enter your income (in USD)', 0))

    ## Age
    st.write("""
    ## Age
    """)
    input_age = np.negative(st.slider('Select your age', value=42, min_value=18, max_value=70, step=1) * 365.25)

    ## Years_employed
    Years_employed = st.number_input("Applicant's Years_employed", value=0)

    ## Income_type
    input_Income_type = st.radio('Income_type', ['Working', 'Commercial associate', 'Pensioner', 'State servant', 'Student'], index=0)
    Income_type_dict = {'Working': 4, 'Commercial associate': 0, 'Pensioner': 1, 'State servant': 2, 'Student': 3}
    Income_type_val = Income_type_dict.get(input_Income_type)

    ## Education_type
    input_Education_type = st.radio('Education_type',
                                    ['Secondary school', 'Academic degree', 'Higher education', 'Incomplete higher', 'Lower secondary'],
                                    index=0)
    Education_type_dict = {'Secondary school': 4, 'Academic degree': 0, 'Higher education': 1, 'Incomplete higher': 2, 'Lower secondary': 3}
    Education_type_val = Education_type_dict.get(input_Education_type)

    ## Gender
    st.write("""
    ## Gender
    """)
    input_gender = st.radio('Select you gender', ['Male', 'Female'], index=0)

    ## Marital_status
    input_Marital_status = st.radio('Marital_status',
                                    ['Widow', 'Civil marriage', 'Married', 'Separated',
                                     'Single'],
                                    index=0)
    Marital_status_dict = {'Widow': 4, 'Civil marriage': 0, 'Married': 1, 'Separated': 2,
                           'Single': 3}
    Marital_status_val = Marital_status_dict.get(input_Marital_status)

    ## Housing_type
    input_Housing_type = st.radio('Housing_type',
                                    ['Rented apartment', 'Co-op apartment', 'House', 'Municipal apartment',
                                     'Office apartment','With parents'],
                                    index=0)
    Housing_type_dict = {'Rented apartment': 4, 'Co-op apartment': 0, 'House': 1, 'Municipal apartment': 2,
                           'Office apartment': 3,'With parents': 5}
    Housing_type_val = Housing_type_dict.get(input_Housing_type)

    ## Own_car
    st.write("""
    ## Car ownership
    """)
    input_Own_car = st.radio('Do you own a car?', ['Yes', 'No'], index=0)

    ## Own_property
    st.write("""
    ## Property ownership
    """)
    input_Own_property = st.radio('Do you own a property?', ['Yes', 'No'], index=0)

    ## Email
    st.write("""
    ## Email
    """)
    input_Email = st.radio('Do you have an email?', ['Yes', 'No'], index=0)
    Email_dict = {'Yes': 1, 'No': 0}
    Email_val = Email_dict.get(input_Email)

    ## Unemployed
    st.write("""
        ## Unemployed
        """)
    input_Unemployed = st.radio('Are you Unemployed?', ['Yes', 'No'], index=0)
    Unemployed_dict = {'Yes': 1, 'No': 0}
    Unemployed_val = Unemployed_dict.get(input_Unemployed)

    if st.button("Submit"):
            features = [[Num_family, Total_income, input_age, Years_employed, input_Income_type, input_Education_type, input_gender, input_Marital_status, input_Housing_type, input_Own_car, input_Own_property,input_Email,input_Unemployed]]
            print(features)
            prediction = model.predict(features)
            lc = [str(i) for i in prediction]
            ans = int("".join(lc))
            if ans == 0:
                st.error(
                    'Your Credit Card Application has been Approved'
                )
            else:
                st.success(
                    'Your Credit Card Application has been Declined'
                )
run()