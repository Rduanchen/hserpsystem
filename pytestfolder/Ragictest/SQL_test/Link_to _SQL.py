from msilib.schema import tables
from venv import create
import pymysql
conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='hsdeveloper',charset='utf8',db='python_test')
print("link sucessfully")
create_table="""
CREATE TABLE IF NOT exists `pytrain` (
	`ID` INT PRIMARY KEY,
	`name` VARCHAR(20),
	`score` int(3)
);
"""

show_database='show databases;'
with conn.cursor() as cusor:
    cusor.execute('use `python_test`;')
    cusor.execute('create database `emma`;')
    cusor.execute(show_database)
    # data=cusor.fetchall()
    # print(data)
    # conn.commit()
conn.close()
print("loss connect")
