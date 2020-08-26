import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.10.10.4", 4444))
complete_info = b''
password = input("Enter the password here: ")
s.send(password.encode('utf-8'))
while True:
    file_data = s.recv(128)
    if len(file_data) <= 0:
        break
    complete_info += file_data
    file = open(os.getcwd() + "/credentials" ,"ab")
    file.write(complete_info)
    file.close()

