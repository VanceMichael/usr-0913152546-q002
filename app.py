import sqlite3,os
from flask import Flask,request,jsonify
app=Flask(__name__);DB=os.getenv('DB_PATH','data/app.db');os.makedirs('data',exist_ok=True)
def init(): c=sqlite3.connect(DB);c.execute('create table if not exists lessons(id integer primary key,name text,slot text unique)');c.commit();return c
@app.post('/lessons')
def add():
 v=request.get_json() or {};c=init()
 try: cur=c.execute('insert into lessons(name,slot) values(?,?)',(v.get('name'),v.get('slot')));c.commit();return jsonify(id=cur.lastrowid),201
 except sqlite3.IntegrityError:return jsonify(error='slot occupied'),409
if __name__=='__main__':init();app.run(host='0.0.0.0',port=8080)
