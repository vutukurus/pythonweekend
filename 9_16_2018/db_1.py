#Database..
#oracle, sql,sqlite3
import sqlite3
import time

con = sqlite3.connect('test.db')

#Create tables in python..
cur = con.cursor()
#create table test (id int,name text)
#cur.execute('''create table test (id int,name text)''')

#insert the datat in to table.
#insert into test values(1, 'python')
#insert into test values(2, 'perl')
#uncomment if neded..
#command = "insert into test values(5, 'python', '%s')" %(time.ctime())
#print command
cur.execute('''insert into test values(5, '%s')''' %(time.ctime()))
#cur.execute('''insert into test values(2, 'perl')''')
con.commit()

#update test set name = "java" where name = "python"
#read the data..
#cursor.fetchone, cursor.fetchall()
#select * from test
cur.execute('''select * from test''')
#print cur.fetchone()
#print cur.fetchone()

print cur.fetchall()

con.close()



