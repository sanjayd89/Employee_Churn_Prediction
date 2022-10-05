
import numpy as np
import pickle
import pandas as pd
import streamlit as st 

st.title('Employee Churn Prediction')

#importing all the pkl:
with open(r'model.pkl', 'rb') as file:    
    model = pickle.load(file)

def predict(age, gender, marital_status, dept_name, avg_monthly_hrs, filed_complaint, last_evaluation, n_projects, recently_promoted, salary, satisfaction, tenure):

    dept_name_list = {'IT':0, 'Sales':1, 'Temp':2, 'Engineering':3, 
                        'Support':4, 'Finance':5, 'Procurement':6, 
                        'Admin':7, 'Management':8, 'Marketing':9, 'Product':10}
    dept_name = dept_name_list.get(dept_name)  #getting the category code # from dept name

    #converting the categorical values to numbers:
    if gender == "Male":
        gender = 1
    else:
        gender = 0

    if marital_status == "Married":
        marital_status = 0
    else:
        marital_status = 1

    if filed_complaint == "Yes":
        filed_complaint = 1.0
    else:
        filed_complaint = 0.0

    if recently_promoted == "Yes":
        recently_promoted = 1.0
    else:
        recently_promoted = 0.0

    if salary == "High":
        salary = 0
    elif salary == 'Medium':
        salary = 2
    else:
        salary = 1

    data = {
    'age': [age], 'gender': [gender] , 'marital_status' : [marital_status], 
    'dept_id' : [dept_name] , 'avg_monthly_hrs' : [avg_monthly_hrs], 'filed_complaint' : [filed_complaint], 
    'last_evaluation' : [last_evaluation], 'n_projects' : [n_projects], 'recently_promoted' : [recently_promoted],
    'salary' : [salary], 'satisfaction' : [satisfaction], 'tenure' : [tenure]
    }
    user_data = pd.DataFrame(data)
    prediction = model.predict(user_data)
    return prediction

def main():

    age = st.selectbox("Enter age", np.arange(22.0, 76.0)) 
    age = float(age)   
    gender = st.radio("Choose Employee Gender", ("Male", "Female")) 
    marital_status = st.radio("Choose Employee Gender", ("Married", "UnMarried"))
    dept_name = st.selectbox('Select Depart name of the Employee', 
    ['IT', 'Sales', 'Temp', 'Engineering', 'Support', 'Finance', 'Procurement', 'Admin', 'Management', 'Marketing', 'Product']
    )  
    avg_monthly_hrs = st.selectbox("Enter average monthly hours worked by the employee", np.arange(500.0))
    avg_monthly_hrs = float(avg_monthly_hrs)
    filed_complaint = st.radio("Has the employee filed a complaint in recent past", ("Yes", "No"))
    last_evaluation = st.slider("What was the score of the employee in last evaluation", 0.0, 1.0, 0.01)
    last_evaluation = float(last_evaluation)
    n_projects = st.selectbox("Enter number of projects the employee is currently working and responsible for", np.arange(50))
    recently_promoted = st.radio("Has the employee being promoted recently", ("Yes", "No"))
    salary = st.radio("Choose salary range of the employee", ("High", "Medium", "Low"))
    satisfaction = st.slider("What was the overall satisfaction level of the employee", 0.0, 1.0, 0.01)
    satisfaction = float(satisfaction)
    tenure = st.selectbox("Enter employee tenure at the organization", np.arange(60.0))    
    tenure = float(tenure)
    
    churn_prediction = ""
    if st.button("Predict"):
        churn_prediction = predict(age, gender, marital_status, dept_name, avg_monthly_hrs, filed_complaint, last_evaluation, n_projects, recently_promoted, salary, satisfaction, tenure)

    if churn_prediction == 0:
        st.success("The employee will stay")
    else:
        st.error("The employee will leave")

if __name__=='__main__':
    main()

