import rethinkdb as r
import sys

print "Host (default value is 'localhost'):"
host = raw_input()
if host == '':
    host = 'localhost'

print "Driver port (default value is 28015):"
port_raw = raw_input()
if port_raw is '':
    port = 28015
else:
    port = int(port_raw)

print "Auth key (default value is ''):"
auth_key = raw_input()

print "Connecting to the server..."
c = r.connect(host=host, port=port, auth_key=auth_key)
print "Connected."

while True:
    try:
        print "----------------------------------------"
        print "Enter your query (without using .run()):"
        query_raw = raw_input()
        if query_raw == 'exit':
            sys.exit(0)

        query = eval(query_raw)
        query.run(c)
    except (KeyboardInterrupt, SystemExit):
        print
        print "Bye bye"
        sys.exit(0)
    except:
        e = sys.exc_info()
        for line in e:
            print str(line)
    print
