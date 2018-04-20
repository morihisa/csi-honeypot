# csi-honeypot
This Python3 script is a tiny honeypot for Cisco Smart Install.

# Install
$ git clone https://github.com/morihisa/csi-honeypot.git  
$ cd csi-honeypot  
$ mkdir log  
$ python3 ./csi-honeypot.py

Don't forget! Open 4786/tcp port on your server.

# Log file
./log/SourceIP.log

# Test
Using [SIET:Smart Install Exploitation Tool](https://github.com/Sab0tag3d/SIET)

$ python ./siet.py -t -i 127.0.0.1  
\[INFO]: Sending TCP packet to 127.0.0.1  
\[INFO]: Smart Install Director feature active on 127.0.0.1  
\[INFO]: 127.0.0.1 is not affected  
