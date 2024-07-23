import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="calistus",
  database="caltech"
  )

print(mydb.get_server_info())


mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM employees")
myresult = mycursor.fetchall()

for i in myresult:
    print(i)

sql = "INSERT INTO employees (EmployeeID, FirstName, LastName, Department, HireDate) VALUES (6, 'Lynda', 'Anyanwu', 'Accounts', '2020-07-05')"
mycursor.execute(sql)
mydb.commit()

mycursor.close()
mydb.close()

