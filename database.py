import mysql.connector as mysql

mydb = mysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'nimda321',
    port = '3306',
    database = 'tcsai'
)

mycursor = mydb.cursor()