import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Johnleo1152003."
    # database = "nameofdatabase" # Can only use this if there is a DB created
)

mycursor = db.cursor()

# mycursor.execute("CREATE DATABASE nameofdatabase")
