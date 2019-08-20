# ecom-util-app
Utility app for ecommerce

This app is built to consume utility rest services of ecommerce application.

Works on python 3.7 + versions

Steps to deploy app in local:

1. Pull the code to your local
2. Create pyhton virutal environment with python version 3.7 or above.
3. Install dependecies mentioned in requirements.txt
4. RUN python run.py in terminal


Steps to build and deploy app in docker:

1. Install docker in your local system
2. Download the base image from below link:
   https://drive.google.com/file/d/1Aqctw2yUVh_3lue1SlPwAeO0nFfEiRJC/view?usp=sharing
3. cd into the downloaded location
4. Run the command
   docker import ubuntu_read.tar ubuntu-ready:version4
5. cd into the app folder, make sure the Dockerfile is in the folder and run the below command
   docker build --tag=util-app .
6. Run the docker image with below command
   docker run -p 8000:8000 util-app      
