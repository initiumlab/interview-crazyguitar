# interview-crazyguitar

How to run all tests

```bash
# check python version
$ python3 --version
Python 3.7.3

# run question 1 & 2
$ python3 q1/q1.py
$ python3 q2/q2.py

# run question 3
$ python3 manage.py runserver
$ curl http://localhost:8000/serverinfo/
"Tue May 21 00:46:49 2019 UTC"

# run question 4
$ docker-compose up
$ curl http://localhost:8080
["2019-05-21T00:48:13"]

# press Ctrl+C
$ docker-compose down
```
