from fastapi import FastAPI
import psycopg2 as psycopg
from dotenv import dotenv_values


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
    return "Processing successful"


# 1. Получение всех данных таблицы
@app.get("/get-projects")
def get_all_projects():
    try:
        cursor.execute("SELECT * FROM project")
        result = cursor.fetchall()
        responce = []
        for i in result:
            responce.append({"id": i[0], "name": i[1], "lead_name": i[2], "count_user": i[3], "is_finish": i[4]})
        return responce
    except Exception as e:
        print(e)
        return e

# 2. Чтение записи по ID
@app.get("/get-project/{id}")
def get_project(id: int):
    try:
        cursor.execute(f"SELECT * FROM project WHERE id = {id}")

        result = cursor.fetchone()
        return {"name": result[1], "lead_name": result[2], "count_user": result[3], "is_finish": result[4]}

    except Exception as e:
        print(e)
        return e

# 3. Добавление записи
