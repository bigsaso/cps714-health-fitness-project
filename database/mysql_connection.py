import mysql.connector
from mysql.connector import errorcode
import json

with open("config.json", "r") as jsonfile:
    config = json.load(jsonfile)

try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

cursor = cnx.cursor() 

while True:
  query = input("Enter Query (type q to leave):\n")
  if query.lower() == 'q': break
  cursor.execute(query)
  for results in cursor.fetchall():
    print(results)

cnx.close() 