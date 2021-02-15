import time
from botocore.vendored import requests

def load_time(link):
    get_time = requests.get(link).elapsed.total_seconds()
    return get_time
    
def lambda_handler(event, context):

    result = {}
    links = event['links']
    for link in links:
        time = load_time(link)
        time = str(time) + 's'
        result.update({link:time})

    return{
         "statusCode": 200,
         "result": result
    }
