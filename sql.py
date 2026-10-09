import pymysql  #pymysql is a python module which is used to connect python with mysql database
#conn is a variable which is used to connect python with mysql databases
conn=pymysql.connect(
    host="localhost",
    user="root",
    password="Jyotsna@27",
    database="aug2026",
)
cursor=conn.cursor()
#sql="insert into employee values(1,'Arun',25000,'dev')"
#sql="insert into employee values(2,'Arjun',30000,'dev')"
#sql="insert into employee values(3,'Aravind',35000,'HR')"
#sql="insert into employee values(4,'Arun',40000,'HR')"
#sql="insert into employee values(5,'Arun',45000,'Finance')"
#sql="insert into employee values(6,'Arjun',50000,'it')"
#sql="create table employee(id int primary key ,name varchar(20),salary int,dept varchar(20))"

sql="select * from employee"
cursor.execute(sql)

#row=cursor.fetchall() i
#print(row)  #in this line of code it will print in nested loop format
#row=cursor.fetchmany(2)  #in this line of code it will print in single line format
row=cursor.fetchone()  #in this line of code it will print only the first row
print(row)
print(row[0],row[1],row[2],row[3])  #in this line of code it will print in single line format


#for i in row: #for normally print without nested loop
    #print(i)  #in this line of code it will print in nested loop format
    #print(i[0],i[1],i[2],i[3])  #in this line of code it will print in single line format

conn.commit()  #commit is used to save the changes in the database
conn.close()    