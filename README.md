## IS5003
#### Team Temporary

#### [Running AWS Lambda Function](https://24y9j7i6q5.execute-api.us-east-1.amazonaws.com/default/SQLwizard)

#### [Achievements Course](https://achievements-prod.firebaseapp.com/#/paths/-LqGUm8_gOs0BzTkffWy)

###  Instruction

1. Clone the repository: ```git clone https://github.com/yuanwei15/IS5003```
2. Run ```pip install pandas sqlalchemy --target .```
  * AWS requires Pandas and NumPy for Linux
  * For MacOS users, please download Linux versions of Pandas and NumPy libraries:
    * [Pandas](https://pypi.org/project/pandas/#files)
    * [NumPy](https://pypi.org/project/numpy/#files)
3. zip the directory
4. upload to AWS S3 bucket
5. create new AWS Lambda, selecting Python 3.6 or 3.7
6. Upload the zip file from S3 bucket to lambda
7. Add trigger for API Gateway
8. Go to the link on API Gateway menu
