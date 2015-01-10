from socket import *
import time
import sys
from PIL import Image
from ast import literal_eval

if len(sys.argv) != 3:
    print "\nUsage: python client.py <Server_IP_Address> <Server_Port_Number> "
    sys.exit(0)

PORT = int(sys.argv[2])
HOST = sys.argv[1]
ADDR = (HOST, PORT)
BUF_SIZE_IMG = 6400000
BUF_SIZE = 2048


client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(ADDR)

print "Successfully Connected To The Server.\n"

while True:

    stream = client_socket.recv(BUF_SIZE_IMG)

    if not stream:
        break

    time.sleep(0.5)
    size = client_socket.recv(BUF_SIZE)

    l = literal_eval(size)

    image = Image.frombytes("RGB", (int(l[0]), int(l[1])), stream)

    date_string = time.strftime("%m-%d-%H-%M-%S")

    image.save('' + date_string + '.png', 'PNG')
