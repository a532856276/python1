#！/usr/bin/env python
# -*-- coding:  utf-8 -*-
# author: albert  time:$(DATA)

import socket
import threading
import  time
serviceIp = "127.0.1.1"
servierPort = 1000
g_ulDataLen = 1024
def threadTask(soc, addr):
    print ("cliet(%s) is coming" % addr)

    soc.send("Welcome")
    while True:
        data = soc.recv(g_ulDataLen)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        soc.send("%s Hello!!"% data)

    soc.close()
    print("cliet(%s) is close" % addr)

def main():
    print ("main is GO!!")
    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    mysocket.bind(serviceIp)
    # 监听的是客户端的数量，并非端口号
    mysocket.listen(servierPort)

    while True:
        soc, addr = mysocket.accept()

        mythread = threading.Thread(target= threadTask, args=(soc, addr))
        mythread.start()

        print("%d is start" % mythread.ident)
    print(data)



if __name__ == 'main':
    print ("before main")
    main()
    print ("after main")
