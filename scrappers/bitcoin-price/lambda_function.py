import os
import time
import requests
import boto3
from dotenv import load_dotenv

load_dotenv()


def lambda_handler(event, context):
    response = requests.get(os.getenv('URL'))
    data = response.json()
    rate = str(data['bpi']['USD']['rate_float'])
    time_ms = str(int(round(time.time() * 1000)))
    print(f'Rate: {rate}')
    print(f'Time: {time_ms}')
    client = boto3.client('timestream-write')
    client.write_records(
        DatabaseName=os.getenv('DATABASE'),
        TableName=os.getenv('TABLE'),
        Records=[
            {
                'Dimensions': [{'Name': 'project', 'Value': 'coinjecture'}],
                'MeasureName': 'Bitcoin',
                'MeasureValueType': 'DOUBLE',
                'MeasureValue': rate,
                'Time': time_ms,
                'TimeUnit': 'MILLISECONDS'
            }
        ],
        CommonAttributes={}
    )
    client.close()
