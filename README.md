### Udacity Azure Machine Learning Engineer - Project 2

# Project Overview
This project focuses on creating and deploying a machine learning model. Then creating endpoints for those models and accessing them via rest API's. This is achieved manually via the the azure machine learning studio (AMLS) interface as well as through an automated pipeline that generates all required steps through a jupyter notebook.

## Architectural Diagram of ML Process
![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/amls_arch.drawio.png)

## Potential Improvements
In this project since we were focused on deploying the model, more time could be spent to ensure the model is in it's best form. That could be done via multiple automl runs with different parameters. Additional testing could be done as well against the endpoint to ensure it's benchmarks are good.

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

With our endpoint deployed we need a way to communicate what can be done with it. That's where Swagger comes in, we created a swagger docker container to host our swagger documentation json file about our enpoint. It creates great documentation about what commands can be used with the endpoint.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/swagger_running.png)

We can now consume our endpoint since we know what commands can be used against it. I then ran endpoint.py with some sample data included in order to ensure the model was working.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/endpoint_success.png)

## Creating a Pipeline of the Model for Automation
This process results in a similar outcome to the manual method however since everything is done via code it's reusable for future use cases and can be automated entirely. We largely follow the same methods as above but I'll focus on the differences here.

We first establish a connection to our workspace, create an experiment within that workspace, and then get the needed data.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/bank_mark_data_automl_python.png)

Then we can setup our AutoML step to be executed within the pipeline and create the pipeline itself.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/pipeline_created.png)

We then execute said pipeline and check on it's status.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/run_details_running.png)

After the pipeline completes the experiment we then retrieve the best results and prepare to deploy them to an endpoint for consumption.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/pipeline_endpoint.png)

Showing endpoint as active.

![alt text](https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_p2/main/screenshots/pipeline_endpoint_active.png)

## Link to Screencast
https://youtu.be/RbmDjXgmNSE
