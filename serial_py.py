import serial

def binario_para_decimal(leitura):
    return str(float(leitura))

comunicacaoSerial = serial.Serial('/dev/ttyACM0', 9600)

while 1:
	value_bin = comunicacaoSerial.readline()
	value = binario_para_decimal(value_bin)
	print("corrente: ",value," A")
	#print ("tipo: ",type(value))