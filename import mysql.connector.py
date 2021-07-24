import mysql.connector
from mysql.connector import Error
import sys

def sql_connector():
     try:
         connection-mysql.connector.connect(host='localhost',user='root',password='test')
         return connection
        except Error:
            print("Error") 

def sql_insert(connection,intA,intB,intC,intD,intE,intF,totalmarks,avg,grade):
      try:
          cursor_connection.cursor()
          sql="INSERT INTO TEST.students_mark(Name,m1,m2,m3,m4,m5)"            
    data=[intA,intB,intC,intD,intE,intF,intG,totalmarks,avg,grade]
    cursor.execute(sql,data)
    connection.commit()
    connection.close()
    except Error as a:
        connection.rollback()
        print("Its an error",a)

def grade(average):
    if (average>=95):
        return "A+"
    elif (average>=75):
        return "A"
    elif (average>=50):
        return "B"
    else :
         print("fail")    

         print("Please enter the value to would like you do 1.Add student \n 2.Delete student\n 3.Insert student ") 
         intA=input("Enter your name? ")
         intB=input("Enter you mark1?")
         intC=input("Enter your mark2?")
         intD=input("Enter your marks3?")
         intE=input("Enter your marks4?")
         intF=input("Enter your marks5")

        total=(intB+intC+intD+intD+intE+intF)
        avg=(total/5)
        grade=grade(average)

        connection=sql_connection()
        sql_insert(intA,intB,intC,intD,intE,intF,intG,totalmarks,avg,grade)
        
        else:
            print("exit")

