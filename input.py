import psycopg2
import pandas as pd
import os
import sql_query
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

dbname = os.getenv("dbname")
user = os.getenv("user")
password = os.getenv("password")
host = os.getenv("host")

with psycopg2.connect(dbname=dbname, user=user, password=password, host=host) as conn:
    sql = sql_query.select_actors_director_note_by_film
    df = pd.read_sql_query(sql,conn)

print(df.head(10))

