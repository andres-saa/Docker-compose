from logging import exception
import time
import mysql.connector as sql
from flask import Flask

app = Flask(__name__)

db=sql.connect(port=3306, user='andres',password='123456789',db='numeros')
cursor=db.cursor()

def get_hit_count():
    retries = 5
    while True:
        try:
            cursor.execute("update numeros set numeros.id=numeros.id+1;")
            db.commit()
            cursor.execute("select id from numeros")
            return cursor.fetchall()[0][0]

        except exception as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)
       

@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

