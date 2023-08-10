
import connections
import pandas as pd
from pandas import DataFrame
from abc import ABC, abstractmethod
from sqlalchemy import text



def select_all(table: str) -> DataFrame:
    print(f'Selecting all rows from {table} on host: {connections.source.url.host}')
    if(table):
        query = f"select * from {table}"
        return pd.read_sql(query, con=connections.source)
    else:
        raise ValueError('input for select-all action should have the table input')


def migrate(source: str, destinatin:str) -> bool:
    print(f'Migrating all rows from {source} on host: {connections.source.url.host} to {destinatin} on host {connections.destination.url.host}')
    df = select_all("LN_APP_USER")
    # truncate(destinatin)
    df.to_sql(name=destinatin, con=connections.destination, if_exists='replace', index=False)
    return True


def drop(table: str):
    with connections.defult_engine.connect() as connetion:
        connetion.execute(text(f'DROP TABLE {table}'))

def truncate(table: str):
    with connections.defult_engine.connect() as connection:
        connection.execute(text(f'TRUNCATE TABLE {table}'))
