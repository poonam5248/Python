#Ques 2. Insert values in the tables.
import pymysql as py

db=py.connect("localhost","root","","library")
cursor=db.cursor()
cursor.execute("insert into book values(001,'Computer','India','Fiction')")
cursor.execute("insert into titles values(001,'FOCP','1101',110,2010)")
cursor.execute("insert into publisher values(001,'ABC','England',10102,11101)")
cursor.execute("insert into zip_code values(001,'Ambala','Haryana',134003)")
cursor.execute("insert into auth_title values(001,11010,1010012)")
cursor.execute("insert into author values(001,'john','null','Black')")
cursor.execute("select * from book")
result=cursor.fetchall()
print(result)
db.commit()
db.close()