import sqlite3
class Database:
    def __init__(self,db):
         self.con = sqlite3.connect(db)
         self.cur = self.con.cursor()
         self.cur.execute(''' create table if not exists products
                         (id integer primary key,
                         name text,
                         psell integer,
                         pbuy integer,
                         number integer
                         )''')
         self.con.commit()

    def add (self,name,psell,pbuy,number):
         self.cur.execute("insert into products values(null,?,?,?,?)",(name,psell,pbuy,number))
         self.con.commit()

    def search(self,name):
         self.cur.execute('select * from products where name = ?',(name,))
         record = self.cur.fetchall()
         return record
    
    def delete(self,id):
         self.cur.execute("delete from products where id = ?",(id,))
         self.con.commit()

    def edit(self,id,name,psell,pbuy,number):
         self.cur.execute('''update products set name = ?,
                          psell = ?
                          ,pbuy = ?
                          ,number = ?
                          where id =?
                          '''
                          ,(name,psell,pbuy,number,id))
         self.con.commit()

    def show(self):
         self.cur.execute('select * from products')
         rec = self.cur.fetchall()
         return rec
    