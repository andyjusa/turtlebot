import socket
import signal
import sys
import threading
import time
import rospy
import test
def signal_handler(signal, frame):
    print('signal_handler called')
    sys.exit(0)
def ClientFunc(conn):
    global a
    global x
    global y
    global z
    while True:
        try:
            data = conn.recv(8192)
            if (len(data) == 0):
                print('client is closed')
                break
            print(data)
            data1=data[:len(data)-2]
            data1=data1.split(" ")
            print data1[0]
            if data1[0] == "cawe":
                x = float(data1[1])
                y = float(data1[2])
                z = float(data1[3])
                a=True
        except:
            pass
def ServerFunc(server):
    global a
    a=False
    while True:
        conn, addr = server.accept()
        print(addr, 'client is connected')
        p = threading.Thread(target=ClientFunc, args=(conn,))
        p.daemon = True
        p.start()
signal.signal(signal.SIGINT, signal_handler)
rospy.init_node('movebase_client_py',anonymous=True)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8000))
server.listen(5)
p = threading.Thread(target=ServerFunc, args=(server,))
p.daemon = True
p.start()
while True:
    time.sleep(0.1)
    if a:
        test.move(x,y,z)
        a=False
        print ("jkkkjkj")

server.close()