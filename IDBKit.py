import sqlite3
'''
Shu Chang
2017-9-23 PolyU

get a easy connect to sqllit3
'''


class IDBKit:
   path="C:\\work\python\\";#default path
   name="poly.db";#defalut dbname
   conn="";
   cursor="";
   
   def __init__(self,path=path,name=name):
       self.conn=sqlite3.connect(self.path+self.name);
       self.cursor=self.conn.cursor();
   
   def instance():
       return self.cursor;
   
   
   def find(self,sql):
       cur = self.cursor.execute(sql);
       return cur.fetchall();
       
  
   def findone(self,sql):
       cur = self.cursor.execute(sql);
       return cur.fetchone();
       
'''db=IDBKit();
sql="select * from DATAMINING_ASS1_APRIOR";
cur=db.cursor
cur.execute(sql);
list=cur.fetchall();
#list=db.find(sql)

for item in list:
   print(item)
'''