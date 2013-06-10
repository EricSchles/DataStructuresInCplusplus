#!/usr/bin/python    #This is client.py file

from socket import *  #Import socket module

s = socket()          #Create a socket object
host = gethostname()  #Get local machine name
port = 8080           #Reserve a port for your service

s.connect((host,port))
print s.recv(1024)
s.close()             #Close the socket when done

