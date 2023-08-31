import json
import boto3
import urllib.request
from datetime import datetime


def lambda_handler(event, context):
    # Leer pagina web
    with urllib.request.urlopen('https://www.eltiempo.com') as response:
        html = response.read()
    # Guardar en bucket
    s3_client = boto3.client('s3')
    current_date = datetime.now().strftime("%Y-%m-%d")
    key = "news/raw/eltiempo-"+str(current_date)+".html"
    s3_client.put_object(Body=html,
                         Bucket='zappa-parcial1',
                         Key=key,
                         ContentType='text/html')
    # Leer pagina web
    with urllib.request.urlopen('https://www.elespectador.com') as response:
        html = response.read()
    # Guardar en bucket
    s3_client = boto3.client('s3')
    current_date = datetime.now().strftime("%Y-%m-%d")
    key = "news/raw/elespectador-"+str(current_date)+".html"
    s3_client.put_object(Body=html,
                         Bucket='zappa-parcial1',
                         Key=key,
                         ContentType='text/html')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
