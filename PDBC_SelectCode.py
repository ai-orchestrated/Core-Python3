import csv
import datetime
import mysql.connector

try:
    query="select * from employees.salaries; "
    cnx = mysql.connector.connect(host="falcon", user="demo", password="p@ssw0rd", port="3306", database="employees")
    cursor=cnx.cursor(buffered=True)
    cursor.execute(query)
    a=cursor.fetchall()
    print(a)
    print(type(a))
    print("Record successfully printed")

except mysql.connector.errors as e:
    if cnx:
        cnx.rollback()
        print("There is a problem :",e)
finally:
    if cursor:
        cursor.close()
    if cnx:
        cnx.close()