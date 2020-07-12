import mysql.connector
mydb=mysql.connector.connect(
host='localhost',
user="root",
password="12345",
database='bank'
)

mycursor=mydb.cursor()
#mycursor.execute("alter table customer add column id int auto_increment PRIMARY KEY")
mycursor.execute("show tables")
for x in mycursor:
    print(x)


class bank:
    def __init__(self):
        self.balance = 0

    def customer(self,deposit_name):

        mycursor = mydb.cursor()
        result = "insert into customer (name,balance) values(%s,%s)"
        data = (deposit_name, 0)
        mycursor.execute(result, data)
        mydb.commit()
    def deposit(self,deposit_name):
        print("hello ",deposit_name)
        deposit = int(input("enter the amount u want to deposite"))
        mycursor = mydb.cursor()
        mycursor.execute("SELECT balance FROM Customer where name=%s", (deposit_name,))
        #mycursor.execute(data, (deposit_name,))
        bal = mycursor.fetchall()
        amount=bal[0][0]+deposit
        print(amount)
        mycursor = mydb.cursor()
        result = "insert into customer (name,balance) values(%s,%s)"
        data = (deposit_name, amount)
        mycursor.execute(result, data)
        mydb.commit()
        mycursor.execute ("SELECT * FROM Customer where name=%s",(deposit_name,))
        #mycursor.execute(data, (deposit_name,))
        #mycursor.execute("select * from customer")
        details= mycursor.fetchall()
        for bal in details:
            print(bal)

    def withdraw(self):
        withdraw = int(input("enter the amount u want to withdraw"))
        if self.balance >= withdraw:
            self.balance -= withdraw
            print("you withdrawed the amound of :", withdraw)
        else:
            print("you dnt have enough money")

    def balanc(self):
        print("current amount in your account is:", self.balance)

deposit_name = str(input("enter your name"))
customer = bank()
customer.customer(deposit_name)
customer.deposit(deposit_name)