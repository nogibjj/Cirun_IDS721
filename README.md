# ids721-projects
[![Python application test with Github Actions](https://github.com/nogibjj/Cirun_IDS721/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/nogibjj/Cirun_IDS721/actions/workflows/main.yml)

# Project 1 Summary:
Repo: https://github.com/zhangcirun/ids721-project
* Create a new github repository
* Setup github action
* Setup makefile
* Write a API with Flask to solve the N-Queens Problem
* Setup AWS Elastic Beanstalk to deploy the API
* Setup AWS Code Pipeline for CI/CD

To run the N-Queens API, please visit:
http://flaskapiproj1-env.eba-sx2q5cpp.us-east-2.elasticbeanstalk.com/nqueens/4

Change the number in url to modify the number of queens

# Project 2 Summary:
In this project, I built a simple calculator API service with flask and docker. And pushed the image to AWS ECR and deployed to AWS ECS fargate cluster.
try this: http://18.222.52.183:3000/cal/1+2*12-9

### Tutorial
* Tutorial: https://towardsdatascience.com/deploying-a-docker-container-with-ecs-and-fargate-7b0cbc9cd608
* AWS ECR: https://us-east-2.console.aws.amazon.com/ecr/repositories?region=us-east-2
* AWS ECS: https://us-east-2.console.aws.amazon.com/ecs/v2/getStarted?region=us-east-2
* install aws cli: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

### docker run:
* docker run: docker container run -d -p 3000:3000 public.ecr.aws/s5p1t7g5/ids721-cirun:latest

### docker hub:
* docker build: docker build -t cirunzhang/ids721-python-flask:0.0.1.RELEASE ./
* docker list images: docker images
* docker list containers: docker container ls
* dockerhub login: docker login -u "myusername" -p "mypassword" docker.io

### ECR:
* docker build -t ids721-cirun .
* docker tag ids721-cirun:latest public.ecr.aws/s5p1t7g5/ids721-cirun:latest
* docker push public.ecr.aws/s5p1t7g5/ids721-cirun:latest



# Project 3 Summary:

A salary data query CLI tool.

This project used Azure Databricks and Click to creates a CLI tool for getting the salary data. The data was imported from kaggle open-souce datasets and imported to a single-cluster databricks server.

How to use this CLI:
```python
get-average-salary  Get average salary
get-max-salary      Get the highest salary
get-min-salary      Get the lowest salary
get-salary          Get salary
```

Example:
```bash
@zhangcirun ➜ /workspaces/Cirun_IDS721/project3 (main) $ ./main.py get-salary --year=2021
Getting salary data for year:  2021
99853.79262672811 USD/Year
```


# Project 4 Summary:
A severless image recognition service using AWS Lambda, Rekognition, SNS, S3, and Python.

Basically when the user uploads a image to the S3 bucket, the lamba function will be trigged and process the image with AWS rekognition, and send back the result by SNS.

