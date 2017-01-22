#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      12SigmaTech
#
# Created:     18/01/2017
# Copyright:   (c) 12SigmaTech 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import MySQLdb
conn=MySQLdb.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='',
        db='mysql',
      )

cur=conn.cursor()
##cur.execute('create table student(id int,name varchar(20),class varchar(20),age varchar(20))')
##cur.execute("insert into student values('2','Tom','3 year 2 class','9'),('3','Jack','3 year 3 class','10')")
a= cur.execute("select * from student ")
print a
info=cur.fetchmany(a)
for i in info:
    print i
cur.close()
conn.commit()
conn.close()

