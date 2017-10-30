import sqlite3

con = sqlite3.connect('alunos.db')
cur = con.cursor()

cur.execute('insert into alunos values("matheus", 42)')
cur.execute('insert into alunos values("masanori", 666)')
cur.execute('select * from alunos')

for x in cur.fetchall():
    print(x)

cur.close()
con.commit()
con.close()
