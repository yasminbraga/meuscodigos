# -*- coding: iso-8859-1 -*-
import RPi.GPIO as GPIO
import time
import sqlite3
import socket
import paho.mqtt.client as mqtt
import sys
import os
#função de checar conexão
confiaveis = ['www.google.com', 'www.yahoo.com', 'www.bb.com.br']
def check_host():
  global confiaveis
  for host in confiaveis:
    a=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a.settimeout(.5)
    try:
      b=a.connect_ex((host, 80))
      if b==0: #ok, conectado
         return True
    except:
          pass
    a.close()
  return False
def bin2dec(string_num):
    return str(int(string_num, 2))

#variavel global que recebe os dados do sensor
data = []
#Alias dos pinos GPIO BCM
GPIO.setmode(GPIO.BCM)

#loop infinito
while(True):
    #definindo variavel para conectar os dados
    conn = sqlite3.connect('DHT11.db')
    #definindo um cursor
    cursor = conn.cursor()
    #para desconectar conn.close()
    #criando tabela
    cursor.execute(
    """CREATE TABLE if not exists DHT11(
            tempo TEXT,
            hum  TEXT,
            temp TEXT);
    """)
    if(len(data)>0):
        #remove os itens do array que recupera os dados  
        del data[0: len(data)]
        
    #seta o pino 4 como saida  
    GPIO.setup(4,GPIO.OUT)

    #execura a leitura do sensor com 20ms para garantir a leitura
    #(Esse sensor leva em torno de 18 ms para ler os dados)
    GPIO.output(4,GPIO.HIGH)
    time.sleep(0.025)
    GPIO.output(4,GPIO.LOW)
    time.sleep(0.02)    
    GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    #armazena os dados lidos do pino 4 na variavel global data
    for i in range(0,500):
        data.append(GPIO.input(4))

    #declara as variaveis que irao receber os bits lidos
    bit_count = 0
    tmp = 0
    count = 0
    HumidityBit = ""
    TemperatureBit = ""
    crc = ""

    #inicia a tentativa de recuperar os bits 
    try:
            while data[count] == 1:
                    tmp = 1
                    count = count + 1

            for i in range(0, 32):
                    bit_count = 0

                    while data[count] == 0:
                            tmp = 1
                            count = count + 1

                    while data[count] == 1:
                            bit_count = bit_count + 1
                            count = count + 1

                    if bit_count > 3:
                            if i>=0 and i<8:
                                    HumidityBit = HumidityBit + "1"
                            if i>=16 and i<24:
                                    TemperatureBit = TemperatureBit + "1"
                    else:
                            if i>=0 and i<8:
                                    HumidityBit = HumidityBit + "0"
                            if i>=16 and i<24:
                                    TemperatureBit = TemperatureBit + "0"

    except:
            #caso ocorrra algum erro entra em excecao
            #print "ERR_RANGE"
            print ("ERRO NA RECUPERACAO DE BITS")
            #exit(0)


   #tenta fazer verificacao se os bits forao recebidos corretamente (total sao 8)
    try:
            for i in range(0, 8):
                    bit_count = 0

                    while data[count] == 0:
                            tmp = 1
                            count = count + 1

                    while data[count] == 1:
                            bit_count = bit_count + 1
                            count = count + 1

                    if bit_count > 3:
                            crc = crc + "1"
                    else:
                            crc = crc + "0"
                    
    except:
            #print "ERR_RANGE"
            print ("ERRO NA VERIFICACAO DE BITS")
            #exit(0)


#E por fim Tenta fazer a conversao de binario para inteiro
# chamando o metodo bin2dec e armazena nas variaveis
# HUmidity e  Temperature
    try:
        Humidity = bin2dec(HumidityBit)
        Temperature = bin2dec(TemperatureBit)
        Tempo_1 = time.asctime(time.localtime(time.time()))

        if int(Humidity) + int(Temperature) - int(bin2dec(crc)) == 0:
            cursor.execute("""INSERT INTO DHT11 (tempo, hum, temp) VALUES (?,?,?)""",(Tempo_1, Humidity, Temperature))
            conn.commit()
            print ("Umidade:"+ Humidity +"%")
            print ("Temperatura:"+ Temperature +" C")
            if (check_host() == True):
                print ("Conexao Ativa")
                cursor.execute("""
                SELECT * FROM DHT11;
                """)
                for linha in cursor.fetchall():
                  print(linha)
                  dado1, dado2, dado3 = linha
                  client = mqtt.Client()
                  client.connect("10.1.19.139",1883,60)
                  MQTT_MSG='{"Horario": "%s","Humidade": "%s","Temperatura": "%s"}'%(str(dado1), str(dado2), str(dado3))
                  client.publish("Tapajos-IoT/", MQTT_MSG)
                conn.close()
                os.remove(r'/home/pi/Tapajos-Iot/DHT11.db')
            else:
                print ("Conexao Inativa")
        #else:
                #print "ERR_CRC"
    except:
        print ("ERRO DE CONVERSAO DE BINARIO PARA INTEIRO")
        #exit(0)

    time.sleep(10)
conn.close()