import sys, time
from socket import *
import threading


port = 19189
BUFSIZE = 1024000

def server():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', int(port)))
    s.listen(1)
    print ('Server ready...')
    while 1:
        conn, (host, remoteport) = s.accept()
        while 1:
            data = conn.recv(BUFSIZE)
            if not data:
                break
            del data
        #conn.send('OK\n')
        conn.close()
        print ('Done with', host, 'port', remoteport)

def client(ip):
    count = 100
    testdata = 'x' * (BUFSIZE-1) + '\n'
    t1 = time.time()
    s = socket(AF_INET, SOCK_STREAM)
    t2 = time.time()
    s.connect((ip, int(port)))
    t3 = time.time()
    i = 0
    while i < count:
        i = i+1
        s.send(bytearray(testdata,"utf-8"))
    s.shutdown(1)
    t4 = time.time()
    data = s.recv(BUFSIZE)
    t5 = time.time()
    # print (data.decode())
    # print ('ping:', (t3-t2)+(t5-t4)/2)
    # print ('Time:', t4-t3)
    # print ('Bandwidth:', round((BUFSIZE*count*0.001) / (t4-t3), 3),)
    # print ('Kb/sec.')
    # return round((BUFSIZE*count*0.001) / (t4-t3), 3)
    return (t5-t1)
