import configparser
import hashlib

from peewee import *
import psycopg2
import os

# Инициализация БД
conn = psycopg2.connect(dbname=os.getenv("POSTGRES_USER"), user=os.getenv("POSTGRES_USER"), password=os.getenv("POSTGRES_PASSWORD"), host=os.getenv("POSTGRES_HOST"))
cursor = conn.cursor()

conn.autocommit = True
# команда для создания базы данных metanit
sql = os.getenv("POSTGRES_DB")

try:
    cursor.execute('CREATE DATABASE ' + sql)

except psycopg2.ProgrammingError as e:
    print("Already exists")
cursor.close()
conn.close()
conn = psycopg2.connect(dbname=os.getenv("POSTGRES_DB"), user=os.getenv("POSTGRES_USER"), password=os.getenv("POSTGRES_PASSWORD"), host=os.getenv("POSTGRES_HOST"))
cursor = conn.cursor()

conn.autocommit = True
try:
    cursor.execute("CREATE TABLE "+ "speciality(id SERIAL PRIMARY KEY, specialit VARCHAR(1000));")
    cursor.execute(
        "CREATE TABLE "+ "doctor(id INT PRIMARY KEY,name VARCHAR(1000) NOT NULL,surname VARCHAR(1000) NOT NULL,patronimic  VARCHAR(1000) NULL,phone VARCHAR(11)  NOT NULL,parol VARCHAR(100)  NOT NULL,adress VARCHAR(1000)  NOT NULL,speciality_id INT NOT NULL REFERENCES speciality ON DELETE CASCADE);")
    cursor.execute(
        "CREATE TABLE " + "patient(id INT PRIMARY KEY,name VARCHAR(1000) NOT NULL,surname VARCHAR(1000) NOT NULL,patronimic  VARCHAR(1000) NULL,phone VARCHAR(11)  NOT NULL,parol VARCHAR(100)  NOT NULL,adress VARCHAR(1000)  NOT NULL);")
    cursor.execute(
        "CREATE TABLE " + "registrator(id INT PRIMARY KEY,name VARCHAR(1000) NOT NULL,surname VARCHAR(1000) NOT NULL,patronimic  VARCHAR(1000) NULL,phone VARCHAR(11)  NOT NULL,parol VARCHAR(100)  NOT NULL,adress VARCHAR(1000)  NOT NULL);")
    cursor.execute(
        "CREATE TABLE " + "schedule(id SERIAL PRIMARY KEY,doctor_id INT REFERENCES doctor ON DELETE CASCADE,days VARCHAR(1000) NOT NULL,times_s TIME NOT NULL,times_f TIME NOT NULL,cabinet INT NOT NULL );")
    cursor.execute(
        "CREATE TABLE " + "talon(id SERIAL PRIMARY KEY,patient_id INT NOT NULL REFERENCES patient ON DELETE CASCADE,day DATE NOT NULL,times TIME NOT NULL,cabinet INT NOT NULL,doctor_id INT REFERENCES doctor ON DELETE CASCADE);")
    cursor.execute(
        "CREATE TABLE " + "receipt(id SERIAL PRIMARY KEY,recomendation VARCHAR(10000),day DATE NOT NULL,doctor_id INT REFERENCES doctor ON DELETE CASCADE,patient_id INT NOT NULL REFERENCES patient ON DELETE CASCADE);")
    cursor.execute(
        "CREATE TABLE " + "seek_history(id SERIAL PRIMARY KEY,day DATE NOT NULL,patient_id INT NOT NULL REFERENCES patient ON DELETE CASCADE,diagnos VARCHAR(1000) NOT NULL,doctor_id INT NOT NULL REFERENCES doctor ON DELETE CASCADE,conclusion VARCHAR(1000) NOT NULL);")
    cursor.execute(
        "CREATE TABLE " + "patient_card(id SERIAL PRIMARY KEY,patient_id INT NOT NULL REFERENCES patient ON DELETE CASCADE);")
    cursor.execute(
        "CREATE TABLE " + "admin(id INT PRIMARY KEY,parol VARCHAR(100)  NOT NULL);")
    pos_in = "INSERT INTO" + " admin (id, parol) VALUES (%s, %s)"
    l = input('Введите логин:')
    p = input('Введите пароль:')
    parol = str(hashlib.md5(p.encode()).hexdigest())
    val = [l, parol]
    print(val)
    cursor.execute(pos_in, val)
except psycopg2.ProgrammingError as e:
    print("Already exists")
cursor.close()
conn.close()


db = PostgresqlDatabase(
    database=os.getenv("POSTGRES_DB"),
    host=os.getenv("POSTGRES_HOST"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)


class BaseModel(Model):
    class Meta:
        database = db