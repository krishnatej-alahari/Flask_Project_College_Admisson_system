import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="krishnatej",database="sample1")

mycursor = mydb.cursor()

mycursor.execute("select * from s1")

for i in mycursor:
    print(i)