rethinkdb-driver-development
============================

Tool to help users create a new driver for RethinkDB.
A quick and dirty fork of RethinkDB's python driver.

Run `pyhon test.py`
Specify the host and driver port of your RethinkDB instance
Write a query and get back
- The message
- The serialized message
- The serialized response from the server
- The response from the server


Current driver used: 1.11


Dependency
----
- [RethinkDB](https://github.com/rethinkdb/rethinkdb)
- Python 2
- Python protobuf

Install
----
```
git clone git@github.com:neumino/rethinkdb-driver-development
sudo pip install protobuf
```

Run
----
```
python test.py
```

Example
----
```
michel@xone:~/projects/driver_dvpt$ python2 test.py 
Host (default value is 'localhost'):

Driver port (default value is 28015):

Auth key (default value is ''):

Connecting to the server...
Connected.
----------------------------------------
Enter your query (without using .run()):
r.expr(10).add(20)
Query:
[1, [24, [10, 20]], {}]


Response:
{"t":1,"r":[30]}

```
