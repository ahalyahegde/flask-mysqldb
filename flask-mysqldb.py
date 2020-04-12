from flask import Flask
from flask_mysqldb import MySQL

db = Flask(__name__)
mysql = MySQL(db)

class dbschema:
  db.config['MYSQL_HOST']     = 'localhost'
  db.config['MYSQL_USER']     = 'root'
  db.config['MYSQL_PASSWORD'] = 'root'
  
  def createdb(self):
    try:
      with db.app_context():
        cursor  = mysql.connection.cursor()
        cursor.execute("create database if not exists mydb")
        mysql.connection.commit()
        cursor.close()
    except Exception as e:
      print(e)
  
  def createtable(self, dbname, tablename):
    try:
      with db.app_context():
        cursor  = mysql.connection.cursor()
        cursor.execute(f"use {dbname}")
        cursor.execute(f"create table if not exists {tablename} (testid varchar(10))")
        mysql.connection.commit()
        cursor.close()
    except Exception as e:
      print(e)

  def selecttable(self, dbname, tablename):
    try:
      with db.app_context():
        cursor  = mysql.connection.cursor()
        cursor.execute(f"use {dbname}")
        cursor.execute(f"select * from {tablename}")
        val = cursor.fetchall()
        mysql.connection.commit()
        cursor.close()
        return val
    except Exception as e:
      print(e)
