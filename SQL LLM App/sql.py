import sqlite3

## Connect to sqlite
connection  = sqlite3.connect("student.db")

## Create a cursor to insert record, create table, retrieve
cursor = connection.cursor();

## Create the table
table_info="""
Create table Student(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

## Insert some records
cursor.execute('''Insert into Student values('Mohneet','DS','A',90)''')
cursor.execute('''Insert into Student values('Srushti','MS','A',99)''')
cursor.execute('''Insert into Student values('Kushal','DS','B',80)''')
cursor.execute('''Insert into Student values('Karnaraj','DS','C',70)''')
cursor.execute('''Insert into Student values('Rabjot','DS','D',60)''')
cursor.execute('''Insert into Student values('Khushi','DS','E',50)''')
cursor.execute('''Insert into Student values('Vikas','DS','F',40)''')


## Display all the records
print("The inserted records are")

data = cursor.execute('''SELECT * FROM Student''')

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()