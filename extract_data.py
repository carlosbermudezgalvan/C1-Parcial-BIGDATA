import boto3
from datetime import datetime
from bs4 import BeautifulSoup


def process_news(html_content):
    """
    Funcion para extraer la categoría, el titular y
    el enlace para cada noticia
    """
    html_parsed = BeautifulSoup(html_content, 'html.parser')
    articles = html_parsed.find_all('article')

    processed_data = []
    for article in articles:
        link_element = article.find('a', class_='title page-link')
        if link_element:
            link = link_element['href']
            name = article['data-name'].replace(",", "")
            category = article['data-seccion']
            processed_data.append(f'{category};{name};{link}')

    return '\n'.join(processed_data)


def lambda_handler_processing(event, context):
    """
    Funcion para guardar segun el formato solicitado.
    """
    current_date = datetime.today().strftime('%Y-%m-%d')
    s3 = boto3.resource('s3')
    bucket_name = 'zappa-parcial1'
    for newspaper in ['eltiempo', 'elespectador']:
        object_key = f'news/raw/{newspaper}-{current_date}.html'
        obj = s3.Object(bucket_name, object_key)
        body = obj.get()['Body'].read()
        processed_data = process_news(body)
        csv_key = f'headlines/final/periodico={newspaper}/year'\
            f'={current_date[:4]}'\
            f'/month={current_date[5:7]}/{current_date}.csv'
        s3_client = boto3.client('s3')
        s3_client.put_object(
            Body=processed_data, Bucket="zappa-parcial1", Key=csv_key
            )
        print(f'Data processed and saved for {newspaper}: {csv_key}')

    return {
        'statusCode': 200,
        'body': 'Data processing and saving completed successfully'
    }
