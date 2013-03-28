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

Dependency
----
RethinkDB

Install
----
git clone git@github.com:neumino/rethinkdb-driver-development

Run
----
python test.py

Example
----
----------------------------------------
Enter your query (without using .run()):
r.expr(1)
Query:
type: START
query {
    type: DATUM
    datum {
        type: R_NUM
        r_num: 1
    }
}
token: 1
global_optargs {
    key: "db"
    val {
        type: DB
        args {
            type: DATUM
            datum {
                type: R_STR
                r_str: "test"
            }
        }
    }
}

Protobuf sent to the server:
45 0 0 0 8 1 18 15 8 1 18 11 8 3 25 0 0 0 0 0 0 240 63 24 1 50 22 10 2 100 98 18 16 8 14 26 12 8 1 18 8 8 4 34 4 116 101 115 116

Protobuf received from the server:
17 0 0 0 8 1 16 1 26 11 8 3 25 0 0 0 0 0 0 240 63

Parsed Response from the server
type: SUCCESS_ATOM
token: 1
response {
    type: R_NUM
    r_num: 1.0
}

