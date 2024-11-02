# Credit Card Fraud Detection App built with Streamlit, FastAPI

[![Language](https://img.shields.io/badge/Python-darkblue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![Framework](https://img.shields.io/badge/sklearn-darkorange.svg?style=flat&logo=scikit-learn&logoColor=white)](http://www.pytorch.org/news.html)
[![Framework](https://img.shields.io/badge/FastAPI-darkgreen.svg?style=flat&logo=fastapi&logoColor=white)](https://lung-cancer-api.herokuapp.com/docs)
[![Framework](https://img.shields.io/badge/Streamlit-red.svg?style=flat&logo=streamlit&logoColor=white)](https://share.streamlit.io/nneji123/lung-cancer-prediction/main)
![build](https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat)
![reposize](https://img.shields.io/github/repo-size/Nneji123/Credit-Card-Fraud-Detection)


## Problem Statement
Credit card fraud is an inclusive term for fraud committed using a payment card, such as a credit card or debit card. The purpose may be to obtain goods or services or to make payment to another account, which is controlled by a criminal.
 
**This Streamlit App utilizes a Machine Learning model served as an API with FastAPI framework in order to detect fraudulent credit card transactions  based on the following criteria: hours, type of transaction, amount, balance before and after transaction etc.**

The machine learning model used for this web application was deployed as an API using the FastAPI framework and then accessed through a frontend interface with Streamlit.

The App can be viewed [through this link](https://share.streamlit.io/nneji123/credit-card-fraud-detection/main)



## Data Preparation

Publicly accessible datasets on financial services are scarce, particularly in the newly growing field of mobile money transfers. Many scholars, like us who conduct research in the field of fraud detection, value financial datasets. Because financial transactions are inherently private, there are no publicly accessible datasets, which contributes to the problem. 

A synthetic dataset generated using the simulator called PaySim was used as the dataset for building the model used in this project. PaySim uses aggregated data from the private dataset to generate a synthetic dataset that resembles the normal operation of transactions and injects malicious behaviour to later evaluate the performance of fraud detection methods.

[Dataset Link](https://www.kaggle.com/datasets/ealaxi/paysim1v)

### Modelling
In this project 2 different classification algorithms were tested namely:

- Logistic Regression
- Random Forest

The final model used for the API was the **Random Forest Classifier** model which had an accuracy score of 0.99 and an F1 score of 0.86.




## Deployment
Streamlit App have both been deployed in Streamlit Cloud.


<details> 
  <summary><b>💻 Deploying the Streamlit App to Streamlit Cloud</b></summary>
 
The Streamlit App was deployed using the streamlit cloud and accesses the API deployed on Heroku. To deploy the app using streamlit cloud share do the following:
1. Fork this repository to your Github account.
2. Create a Streamlit Account and then navigate to https://streamlit.io/cloud
3. Create a new app and then choose the repository you cloned and the **"streamlit_app.py"** and then click deploy.

After the app has been built on the cloud you should then be able to view your app right away!
</details>
