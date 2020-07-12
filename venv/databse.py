import mysql.connector
mydb=mysql.connector.connect(
host='localhost',
user="root",
password="12345",
database='bank'
)

mycursor=mydb.cursor()
#sq="delete from customer"
#mycursor.execute("alter table customer add column id int auto_increment PRIMARY KEY")
#mycursor.execute(sq)

mycursor.execute("select * from customer")
result=mycursor.fetchall()
print("hellllllllo")
for x in result:
    print("hello")
    print(x)

