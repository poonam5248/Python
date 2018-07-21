'''Ques 1. Create a database. Create the following tables:
1. Book
2. Titles
3. Publishers
4. Zipcodes
5. AuthorsTitles
6. Authors'''


import pymysql as py
db=py.connect("localhost",'root',"","library")
book="create table book(book_id int,title char(20),loc char(20), gener char(20))"
titles="create table titles(title_id int ,title char(20),ISBN char(20),publisher_id int,publication_year int)"
publisher="create table publisher(publisher_id int ,name char(20), street_add  varchar(20),street_no int,zip_code_id int)"
zip_code="create table zip_code(zip_code_id int, city char(20),state char(20),zip_code int)"
author_title="create table author_title(auth_id int , auther_id int , title_id int) "
author ="create table author (author_id int ,First_name char(20), middle_name char(20),last_name char(20))"
cursor=db.cursor()
cursor.execute(book)
cursor.execute(titles)
cursor.execute(publisher)
cursor.execute(zip_code)
cursor.execute(author_title)
cursor.execute(author)
print(cursor.execute("show tables"))
print(cursor.fetchall())
db.close()






