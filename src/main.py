from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os
from time import sleep
from sqlalchemy import create_engine
import psycopg2
import logging
from dotenv import load_dotenv
load_dotenv()


logging.basicConfig(filename='logs.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s - %(name)s')

DATABASE_PATH = os.getenv("DATABASE_PATH")
API_KEY = os.getenv('API_KEY')

engine = create_engine(DATABASE_PATH)

def api_collector():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

    parameters = {
      'start':'1',
      'limit':'100',
      'convert':'USD'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': API_KEY,
    }
    session = Session()
    session.headers.update(headers)
    
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      # print(data)
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        logging.error(e)


    df_dict = pd.json_normalize(data['data'])
    df = pd.DataFrame(df_dict)
    df['timestamp'] = pd.to_datetime('now')
    df['coin_id'] = df['id'].astype(str) + '_' + df['timestamp'].dt.strftime('%Y%M%S')
    df

    df.to_sql('crypto_currency', engine, if_exists='append', index=False)
    logging.info(f'{len(df)} rows loaded succesfully')

for i in range(5):
    api_collector()
    logging.info('Collecting API data.......')
    print('API runner completed succesfully')
    sleep(60)
exit()