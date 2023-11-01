from fastapi import FastAPI
import psycopg2 as psycopg
from dotenv import dotenv_values
from pydantic import BaseModel


class Adding_to_project(BaseModel):
    id: int
    name: str
    lead_name: str
    count_user: int
    is_finish: bool


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

# ВАРИАНТ 1
# @app.post("/add-project")
# def add_project():
#     try:
#         cursor.execute(f"""
#             INSERT INTO project (id, name, lead_name, count_user, is_finish)
#             VALUES (5, 'Project5', 'Nazar', 3, TRUE)
#         """)
#
#         connect.commit()
#         return {"message": "Processing successful"}
#
#     except Exception as e:
#         print(e)
#         return e


# ВАРИАНТ 2 (через pydantic (BaseModel))
@app.post("/add-project")
def add_project(proj: Adding_to_project):
    try:
        cursor.execute(f"""
            INSERT INTO project (id, name, lead_name, count_user, is_finish)
            VALUES ({proj.id}, '{proj.name}', '{proj.lead_name}', {proj.count_user}, {proj.is_finish})
        """)

        connect.commit()
        return {"message": "Processing successful"}

    except Exception as e:
        print(e)
        return e


# 3. Удаление записи по ID
@app.delete("/delete-entry/{id}")
def delete_table_entry(id: int):
    try:
        cursor.execute(f"DELETE FROM project WHERE id = {id}")

        connect.commit()
        return {"message": "Processing successful"}

    except Exception as e:
        print(e)
        return e

