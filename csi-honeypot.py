#!/usr/bin/env python3
# Author: Twitter @morihi_soc
# 20/Apr/2018
#
# Honeypot for Cisco Smart Install
#

import socket
from time import sleep
import datetime
import binascii
import sys
import os.path

VERSION = 1.1
IP = "0.0.0.0"
PORT = 4786

logdir = "log" + os.path.sep
if not os.path.exists(logdir):
    print("[ERROR] Please create log directory first. ex. $ mkdir log")
    sys.exit(1)

print("csi-honeypot ver.{0} start.".format(VERSION))

servsoc = socket.socket()
servsoc.bind((IP, PORT))

response = '0' * 7 + '4' + '0' * 8 + '0' * 7 + '3' + '0' * 7 + '8' + '0' * 7 + '1' + '0' * 8

try:
    while True:
        print("Listening. {0}/tcp".format(PORT))
        servsoc.listen(5)
        client, addr = servsoc.accept()
        print("someone coming! {0}".format(addr))
        while True:
            try:
                data = client.recv(4096)
                if len(data) > 0:
                    with open(logdir+addr[0]+".log", "a") as f:
                        f.write("[{0}] {1}\r\n".format(datetime.datetime.today(), data))
                    print(data)
                    client.send(binascii.a2b_hex(response))
            except:
                break
            sleep(1)
        client.close()

except KeyboardInterrupt:
    print("csi-honeypot quit.")
    servsoc.close()
