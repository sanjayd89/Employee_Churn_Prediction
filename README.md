# Employee Churn Prediction | An End-to-End Project

## Link to StreamLit Web App
The link to web app developed and deployed on Streamlit cloud for Employee Churn prediction can be found [here](https://sanjayd89-employee-churn-prediction-app-74euga.streamlitapp.com/).

## Table of Contents

[1. Problem Statement](#section1)<br>
[2. Approach towards problem](#section2)<br>
[3. Libraries used](#section3)<br>
[4. Pre-Processing of Data](#section4)<br>
[5. Exploratory Data Analysis](#section5)<br>
[6. Model Preparation & Building](#section6)<br>
[7. Model Deployment](#section7)<br>

<a id=section1></a>
### 1. Problem Statement

The aim of this project is to predict whether an employee will leave an organization. Consequently a web app is developed where based on trained parameters, a prediction can be made.
![](https://github.com/sanjayd89/Employee_Churn_Prediction/blob/main/images/employee%20churn.png)

<a id=section2></a>
### 2. Approach towards problem
- The date needs to be fetched and merged from SQL databases.
- After performing data cleaning and exploratory data analysis, consideration needs to be given on using correct performance metrics as the given dataset is an **imbalanced dataset**
- Since, we want to take appropriate and timely action on employees who are bound to leave, the aim of the model should be to have minimum **False Negatives** i.e. employees who are bound to leave but predicted as they will stay.
- For deployment purposes, a streamlit API shall be used and deployed on streamlit cloud.

<a id=section3></a>
### 3. Libraries used

In addition to frequently used python libraries like pandas, numpy, matplotlib, the project involves use of following libraries:

|  Scikit Learn | MySQL  | Streamlit  | 
| :------------: | :------------: | :------------: |
| ![](https://th.bing.com/th/id/OIP.YGUYNJgwK9FNokDLlS6shQHaD_?w=323&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7) | ![](https://th.bing.com/th/id/OIP.LoZmnOuFptQr8wNvhp3g4wHaE8?w=241&h=180&c=7&r=0&o=5&dpr=1.3&pid=1.7) | ![](https://th.bing.com/th/id/OIP.M6ZtP4BNUvzjUtw651U7ygAAAA?w=195&h=124&c=7&r=0&o=5&dpr=1.3&pid=1.7) |

<a id=section4></a>
### 4. Pre-Processing of Data

- The data is stored in **three SQL databases** which is fetched and merged in python using *mysql.connector* python library.
- Some of the columns had missing data which were handled as below:
	-  recently_promoted : Null values indicate that employee was not promoted and hence, the null values were replaced with "0". Similarly null values in 'filed_complaint' were replaced with "0".
	- last_evaluation, satisfaction, tenure, age, gender, marital_status: The missing values were replaced with median for continuous variables and Mode for categorical ones.
	- dept_id, dept_name and dept_head have 707 each missing value, which is nearly 5% of the dataset and if we fill it with Mode, it may create imbalance in the data. So, to replace missing value creating one missing_dept with dept_id: D00-XX and dept_head: missing_head.

<a id=section5></a>
### 5. Exploratory Data Analysis

Following were the insights gained from **EDA** performed after data cleaning operation:
- Analysis of 'AGE' indicates that only in the Age-Group of 22-25 years attrition is very high at 30.4% as most of them are freshers so they change jobs very frequently. From Age-Group 26-29 to 50-53 years, attrition is between 17% to 20.5%. In Age-Group 54-57 years, attrition is low.
- Gender Analysis indicates that Female has much higher attrition level at 30.9% as against Male at 20.1%
- Marital Status of Employee shows that attrition is quite high in Unmarried at 27% against 20.4% in Married
- Salary of Employee plays a vital role on attrition as Low Salaried have 29.6% attrition rate compared to Higher salaried that have 6.7% attrition rate.
- Analysis of Average Monthly Hour shows that employees worked over 250 Hours in a month have significantly higher attrition rate. On the other hand, low values of  avg_monthly hour between 100-150 hours also has high attrition level which could be because they have more time for JOB SEARCH.
- Analysis of Number of Projects also give similar indication what Monthly Hours gave that over 6 Project, attrition level is very high and employees having 2 projects also have very high attrition.
- If we look at the Tenure of the Employee, we can see that once the employee completed 2 years, they have the tendency to leave the organization and after 6 years, hardly any employee changes jobs.
- Employee who recently got promoted have significantly lower attrition rate.

<a id=section6></a>
### 6. Model Preparation & Building
- The correlation matrix indicates dept_id, dept_name and dept_head high correlation values which makes sense and hence, dropping dept_name and dept_head columns.
- Converting the categorical columns like gender, marital_status, salary, dept_id as well as the target variable "status" into labels using Label Encoder.
- As model focus is to reduce *False Negatives*, along with **Accuracy, Recall** will also be used to evaluate which model is performing the best.
- Following machine learning algorithms were trained and tested:
	- **Logistic Regression**
	- **Decision Tree**
	- **Random Forest**
	- **Stacking**
	- **Voting**
	- **Bagging**
	- **AdaBoost**
	- **Gradient Boosting**
	- **K-Nearest Neighbours**
	- **Naive Bayes**
	- **Support Vector Machine**
	- **XGBoost**

- The best model was obtained by using Stacking model and following are results:

|  Accuracy train | Accuracy test  | Recall score train | Recall score test | 
| :------------: | :------------: | :------------: | :------------: |
| 0.998849 | 0.972035 | 1.000000 | 0.921212 |

<a id=section7></a>
### 7. Model Deployment
- **Streamlit API** was developed in order to deploy the model
- Below is a sample screenshot of the same:
![](https://github.com/sanjayd89/Employee_Churn_Prediction/blob/main/images/web_app1.JPG)
![](https://github.com/sanjayd89/Employee_Churn_Prediction/blob/main/images/web_app2.JPG)
