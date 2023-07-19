## Introduction
This project is bascially on two different usecases 
    1. First Usecase is for Building the infra on AWS and Deploying some Rest API's using different tools and technology
    2. Second Usecase is to have the detailed overview or design document for setting up the Private Blockchain
## IAC
-  This is used for infrastructure automation on Cloud 
-  In ourcase we have the Cloudformation template or script available i.e `infra.yml`  

## Steps to be followed if you want to deploy the usecase - 1 
- Download the code or clone from github by executing the below command
        git clone https://github.com/vija-sketch/assignment.git
- validate the infra template
     ```aws cloudformation validate-template --template-body <filepath>```
     ```In our-case our path will be `assignment/usecase1/infra.yml` ```
- After successful template verification lets create stack using our template
        ```aws cloudformation create-stack --stack-name assignment-usecae1 --template-body assignment/usecase1/infra.yml```
- Check if the stack we created via template is completed successfully
        ```aws cloudformation list-stack-resources --stack-name assignment-usecae1```
- Describe stack and its resources to view its properties
       ``` aws cloudformation describe-stacks --stack-name assignment-usecae1```
       ``` aws cloudformation describe-stack-resources --stack-name assignment-usecae1``` 
- Check events for stack formation
        ```aws cloudformation describe-stack-events --stack-name assignment-usecae1```




 