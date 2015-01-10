from PIL import ImageGrab
from socket import *
import time
import sys
from threading import Thread

if len(sys.argv) != 3:
    print "\nUsage: python server.py <IP_Address> <Port_Number> "
    sys.exit(0)

PORT = int(sys.argv[2])
HOST = sys.argv[1]
ADDR = (HOST, PORT)


def client_handler(cl_sock):
    while True:
        time.sleep(10)
        screen_shot = ImageGrab.grab()
        size = screen_shot.size
        stream = screen_shot.tostring()

        cl_sock.sendall(stream)
        time.sleep(0.2)
        cl_sock.send(str(size))


serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(ADDR)
serverSock.listen(50)

while True:

    print "Waiting For Client ..."
    client_sock, client_addr = serverSock.accept()
    print "Connected from ...", client_addr

    my_thread = Thread(target=client_handler, args={client_sock, })
    # my_thread.daemon = True
    my_thread.start()
