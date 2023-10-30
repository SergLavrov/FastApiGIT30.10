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

app = FastAPI()

@app.get("/")
def root():
    try:
        cursor.execute("SELECT * FROM project")
        result = cursor.fetchall()
        responce = []
        for i in result:
            responce.append({"id": i[0], "name": i[1], "lead_name": i[2], "count_user": [3], "is_finish": [4]})
        return responce
    except Exception as e:
        print(e)
        return e

