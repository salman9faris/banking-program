import mysql.connector
mydb=mysql.connector.connect(
host='localhost',
user="root",
password="12345",
database='bank'
)

mycursor=mydb.cursor()
#mycursor.execute("show tables")
data="insert into customer(name,balance) values(%s,%s)"
name=("salman","10")
mycursor.execute(data,name)
mycursor.comit()
for x in mycursor:
    print(x)

