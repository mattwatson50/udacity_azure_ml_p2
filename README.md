### Udacity Azure Machine Learning Engineer - Project 2

# Project Overview
This project focuses on creating and deploying machine learning models. Then creating endpoints for those models and accessing them via rest API's. This is achieved manually via the the azure machine learning studio (AMLS) interface as well as through an automated pipeline that generates all required steps through a jupyter notebook.

## Creating the Model and Endpoints via Azure Machine Learning Studio
For this section I'll go over what was done to create the model via azure machine learning studio GUI.

*I completed this project within the Udacity provided lab so I will be skipping the authentication step.*

First we needed to upload a dataset for our automated machine learning experiment. We are using a bank marketing csv file that contains information about successful marketing campaigns for individual bank customers. We uploaded that data via the *Data* section within AMLS.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/bank_marketing_created.png)

Once the data was uploaded then we can run our experiment. We setup a classification automated machine learning experiment against our uploaded bank data via the *Automated ML* section of AMLS.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/completed_automl_run.png)

We then found the best model according to the automl run and deployed it with authentication enabled to an azure container instance so that we may access it and run different data against it later. This would be done in a work setting to allow others to access your model.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/best_model.png)

Once it was deployed we then needed to enable application insights and retrieve the logs with python.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/app_insights_enabled.png)

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/logs_running_terminal.png)

With our endpoint deployed we need a way to communicate what can be done with it. That's where Swagger comes in, we created a swagger docker container to host our swagger documentation .json file about our enpoint. It creates great documentation about what commands can be used with the endpoint.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/swagger_running.png)

We can now consume our endpoint since we know what commands can be used against it. I then ran endpoint.py with some sample data included in order to ensure the model was working.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/endpoint_success.png)

