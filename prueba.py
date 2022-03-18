from logging import exception
import mysql.connector as sql

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

print(get_hit_count())

