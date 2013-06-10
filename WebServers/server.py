#!/usr/bin/python #this is server.py file

from socket import * #import socket module

s = socket() #create socket object

host = gethostname() # get local machine name

port = 8080 #reserve a port for your service

s.bind((host,port)) #bind to the port

s.listen(5) #now wait for a client connection

while True:
    c,addr = s.accept() #establish connection with client
    print 'Got connection from', addr
    c.send('Thank you for connecting')
    c.close()

