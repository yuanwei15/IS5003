import json
import sqlite3
import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy

def lambda_handler(event, context):    
    url = 'https://raw.githubusercontent.com/plotly/datasets/master/1962_2006_walmart_store_openings.csv'
    df = pd.read_csv(url)
    engine = create_engine('sqlite://', echo=False)
    df.to_sql('Walmart_Store_Openings', engine, index=False)
    is_correct = False
    textResults = "\nYour SQL statement is not correct.  \n"
    def test_query(query, expected_query):
        try:
            user_result = engine.execute(query).fetchall()
            expected_result = engine.execute(expected_query).fetchall()

        except Exception as e:
            return False
        return user_result == expected_result
    
    method = event.get('httpMethod',{}) 
    
    with open('index.html', 'r') as f:
        indexPage = f.read()
    
    if method == 'GET':
        return {
            "statusCode": 200,
            "headers": {
            'Content-Type': 'text/html',
            },
            "body": indexPage
        }
    if method == 'POST':
        postReq = json.loads(event.get('body', {}))
        
        try:
            editable = postReq["editable"]["0"].strip()
            userToken = postReq["userToken"].strip()
            hidden = postReq["hidden"]["0"].strip()
            shown = postReq["shown"]["0"].strip()
            is_correct = test_query(editable, hidden)
            if is_correct:
                textResults = "\nGood Job! You provided the correct SQL statement.\n"
        except:
            editable = 'EMPTY'
            
        return {
            'statusCode': 200,
            'body': json.dumps(
                {
                    "isComplete": is_correct,
                    "jsonFeedback": json.dumps(textResults),
                    "htmlFeedback": "<div>" + textResults + "</div>",
                    "textFeedback": textResults,
                }
            )
        }   
    """   
    if method == 'POST':
        postReq = json.loads(event.get('body', {}))
        try:
            editable = postReq["editable"]["0"].strip()
            userToken = postReq["userToken"].strip()
            hidden = postReq["hidden"]["0"].strip()
            shown = postReq["shown"]["0"].strip()
            is_correct = test_query(editable, hidden)
        except:
            editable = 'EMPTY'
        
    return {
        'statusCode': 200,
        'body': json.dumps(
            {
                "isComplete": is_correct,
                "jsonFeedback": { "test": is_correct },
                "htmlFeedback": "<div>Test: " + str(is_correct) + "</div><div>" + str(editable) + "</div>",
                "textFeedback": "Test result: " + str(is_correct) + "\n" + str(editable),
            }
        )
    }
"""
