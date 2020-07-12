import mysql.connector
mydb=mysql.connector.connect(
host='localhost',
user="root",
password="12345",
database='bank'
)

mycursor=mydb.cursor()
#mycursor.execute("create databse bank") #creating database bank
#mycursor=mydb.cursor()
#mycursor.execute("create table customers (name varchar(50), balance varchar(50),id int auto_increment primary key)")
#creating table which contain customer name ,balance and id


class bank:
    def __init__(self):
        self.balance = 0

    def customer(self,deposit_name):
        mycursor.execute("select name from customer where name=%s",(deposit_name,))
        name=mycursor.fetchall()
        if len(name)==0: #checking the customer already exist or not
            print("you are a new customer")
            mycursor.execute("insert into customer (name,balance) values(%s,%s)",(deposit_name,self.balance))
            mydb.commit()
        else:
            pass

    def deposit(self,deposit_name):

        print("hello ",deposit_name)
        deposit = int(input("enter the amount you want to deposite"))
        mycursor = mydb.cursor()
        mycursor.execute("SELECT balance FROM Customer where name=%s", (deposit_name,))
        bal = mycursor.fetchall()
        amount=bal[0][0]+deposit #adding already existing amount of database with current deposited amount
        mycursor = mydb.cursor()
        mycursor.execute("update Customer set balance=%s  where name=%s", (amount,deposit_name))
        mydb.commit()
        mycursor.execute ("SELECT balance FROM Customer where name=%s",(deposit_name,))
        current_balance = mycursor.fetchall()
        print(deposit_name," your current balance:",current_balance[0][0])

    def withdraw(self,deposit_name):
        withdraw_amount = int(input("enter the amount you want to withdraw"))
        mycursor.execute("SELECT balance FROM Customer where name=%s", (deposit_name,))
        bal = mycursor.fetchall()
        amount = bal[0][0]
        if amount >= withdraw_amount:
            amount-=withdraw_amount
            mycursor.execute("update Customer set balance=%s  where name=%s", (amount, deposit_name))
            mydb.commit()
            print("you withdrawed the amound of :", withdraw_amount)
            mycursor.execute("SELECT balance FROM Customer where name=%s", (deposit_name,))
            remainig_balance = mycursor.fetchall()
            amount = remainig_balance[0][0]
            print("remaining balance in your account:", remainig_balance[0][0])
            print("thank you")
        else:
            print("you don't have enough money")
            print("thank you")

    def balanc(self):
        print("current amount in your account is:", self.balance)

deposit_name = str(input("enter your name"))
customer = bank()
customer.customer(deposit_name)
customer.deposit(deposit_name)

choice=input("did you want to withdraw from your account? y/n \n")
if choice=='y' or choice== 'Y':
    customer.withdraw(deposit_name)
elif choice=='n' or choice=='N':
    print("thank you")

else:
    print("wrong choice")
    print("please try again later")
