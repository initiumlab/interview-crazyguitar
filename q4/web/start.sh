#!/bin/sh

python -c "
import time
import MySQLdb

kwargs = {
    'host': 'mysql',
    'user':'crazyguitar',
    'passwd': 'password',
    'db': 'interview'
}

for _ in range(60):
    try:
        db = MySQLdb.connect(**kwargs)
        if not db: continue
        db.close()
    except Exception as e:
        time.sleep(5)
        continue
    else:
        print('MySQL is ready')
        break
else:
    exit(1)
"

python manage.py runserver 0.0.0.0:8000
