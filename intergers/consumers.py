import json
from random import randint
from time import sleep
import serial
from .models import Serial_data
from channels.generic.websocket import WebsocketConsumer

port = 'COM3'
baudRate = 115200 #baudrate 수정
serialPort= serial.Serial(port,baudRate)


def Decode(serialLine): 
    serialLineDe = serialLine.decode() 
    serialLineStr = str(serialLineDe)

    if serialLineStr[0] =='B': #첫문자 검사 B
        data = str(serialLineStr[1:-2])
        part1, part2, part3 = data.split(",")
        return int(part1), int(part2), int(part3)
    else : 
        print ("Error_Wrong Signal") 
        return False

class WSConsumer(WebsocketConsumer) :
    def connect(self):
        self.accept()
        while True:
            if serialPort.readable(): 
                readLine = serialPort.readline() 
                code=str(Decode(readLine))
                self.send(json.dumps({'message': code}))         

#MSG = serial.Serial("COM3",9600)
'''
def Decode(A):
    A = A.decode()
    A = str(A)

    if A[0]=='S':
        MSG_dec=int(A[1:9])


        return MSG_dec

    else:
        return False

class WSConsumer(WebsocketConsumer) :
    def connect(self):
        self.accept()
        data = Serial_data()
        while True:
            if MSG.readable():
                LINE = MSG.readline()
                code = Decode(LINE)
                data.data = code
                data.save()
                self.send(json.dumps({'message': code}))
'''
        # for i in range(50):
        #     self.send(json.dumps({'message': i}))
        #     sleep(0.5)

