import serial
comunicacaoSerial = serial.Serial('/dev/ttyACM0', 9600)
	
while 1:
	print("corrente: ",comunicacaoSerial.readline()," A")