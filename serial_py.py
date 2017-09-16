import serial
comunicacaoSerial = serial.Serial('/dev/ttyACM0', 9600)
value = comunicacaoSerial.readline()
while 1:
	#print("corrente: ",comunicacaoSerial.readline()," A")
	print (type(value))