import os
import socket

def Scan(path_, port_start, port_end, host, window):

    window.destroy()
    port = []

    #port_start
    if os.path.exists(path_) == False:
        open_ports = open(path_, 'w+')
    else:
        open_ports = open(path_, 'w')
    for i in range(port_start, port_end + 1):
        port.append(i)
    for i in port:
        try:
            scan = socket.socket()
            scan.settimeout(0.1)
            scan.connect((host, i))
            open_ports.write(('Port -- ' + str(i) + ' -- [OPEN]\n'))
        except socket.error:
            continue
    print('end')
    open_ports.close()
