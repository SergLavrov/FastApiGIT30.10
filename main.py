from fastapi import FastAPI
import psycopg2 as psycopg
from dotenv import dotenv_values


config = dotenv_values(".env")

config = dotenv_values(".env")

connect = psycopg.connect(
    host=config['HOST'],
    port=config['PORT'],
    user=config['USERID'],
    password=config['USERPW'],
    database=config['DBNAME'],
)

cursor = connect.cursor()

app = FastAPI

