#!/usr/bin/env python3

#Importa as bibliotecas necessarias
import time # importando o tempo para a logica de programacao
import math # importando a matematica para a logica de programaaao
from ev3dev2.motor import * # importando tudo da biblioteca ev3dev2.motor
from ev3dev2.sound import Sound # importando o som da biblioteca ev3dev2.sound
from ev3dev2.button import Button # importando os botoes da biblioteca ev3dev2.button
from ev3dev2.sensor import * # importando tudo da biblioteca ev3dev2.sensor
from ev3dev2.sensor.lego import * # importando tudo da biblioteca ev3dev2.sensor.lego
from variaves import *
#from ev3dev2.sensor.virtual import * # importando tudo da biblioteca ev3dev2.sensor.virtual

CS1 = ColorSensor(INPUT_1)  # setando sensor de cor na entrada 
CS2 = ColorSensor(INPUT_2) # setando sensor de cor na entrada 

CS1.mode = 'RGB-RAW'
CS2.mode = 'RGB-RAW'




#Aqui é onde seus codigos começam

#Funções
corCS1 = 0
corCS2 = 0

def ajustes():
    global brancoMin1, brancoMin2
    global brancoMax1, brancoMax2
    global azulMin1, azulMin2
    global azulMax1, azulMax2
    global vermelhoMin1, vermelhoMin2
    global vermelhoMax1, vermelhoMax2
    global verdeMin1, verdeMin2
    global verdeMax1, verdeMax2
    global pretoMin1, pretoMin2
    global pretoMax1, pretoMax2
    global amareloMin1, amareloMin2
    global amareloMax1, amareloMax2
    global marromMin1, marromMin2
    global marromMax1, marromMax2
    global r1, g1, b1, r2, g2, b2

    print("Coloque no branco")
    time.sleep(5)
    CS1.calibrate_white()
    CS2.calibrate_white()
    print("Parametros iniciais concluidos")
    time.sleep(5)
    print(CS1.rgb, CS2.rgb)
    time.sleep(5)
    (r1, g1, b1) = CS1.rgb
    (r2, g2, b2) = CS2.rgb
    brancoMin1 = (r1-1, g1-1, b1-1)
    brancoMax1 = (r1+1, g1+1, b1+1)
    brancoMin2 = (r2-1, g2-1, b2-1)
    brancoMax2 = (r2+1, g2+1, b2+1)
    print(brancoMin1, brancoMax1)
    print(brancoMin2, brancoMax2)
    time.sleep(5)

    print("Coloque no azul")
    time.sleep(5)
    print(CS1.rgb, CS2.rgb)
    time.sleep(5)
    (r1, g1, b1) = CS1.rgb
    (r2, g2, b2) = CS2.rgb
    azulMin1 = (r1-1, g1-1, b1-1)
    azulMax1 = (r1+1, g1+1, b1+1)
    azulMin2 = (r2-1, g2-1, b2-1)
    azulMax2 = (r2+1, g2+1, b2+1)
    print(azulMin1, azulMax1)
    print(azulMin2, azulMax2)
    time.sleep(5)
    
    print("Coloque no vermelho")
    time.sleep(5)
    print(CS1.rgb, CS2.rgb)
    time.sleep(5)
    (r1, g1, b1) = CS1.rgb
    (r2, g2, b2) = CS2.rgb
    vermelhoMin1 = (r1-1, g1-1, b1-1)
    vermelhoMax1 = (r1+1, g1+1, b1+1)
    vermelhoMin2 = (r2-1, g2-1, b2-1)
    vermelhoMax2 = (r2+1, g2+1, b2+1)
    print(vermelhoMin1, vermelhoMax1)
    print(vermelhoMin2, vermelhoMax2)
    time.sleep(5)

    print("Coloque no verde")
    time.sleep(5)
    print(CS1.rgb, CS2.rgb)
    time.sleep(5)
    (r1, g1, b1) = CS1.rgb
    (r2, g2, b2) = CS2.rgb
    verdeMin1 = (r1-1, g1-1, b1-1)
    verdeMax1 = (r1+1, g1+1, b1+1)
    verdeMin2 = (r2-1, g2-1, b2-1)
    verdeMax2 = (r2+1, g2+1, b2+1)
    print(verdeMin1, verdeMax1)
    print(verdeMin2, verdeMax2)
    time.sleep(5)

    print("Coloque no preto")
    time.sleep(5)
    print(CS1.rgb, CS2.rgb)
    time.sleep(5)
    (r1, g1, b1) = CS1.rgb
    (r2, g2, b2) = CS2.rgb
    pretoMin1 = (r1-1, g1-1, b1-1)
    pretoMax1 = (r1+1, g1+1, b1+1)
    pretoMin2 = (r2-1, g2-1, b2-1)
    pretoMax2 = (r2+1, g2+1, b2+1)
    print(pretoMin1, pretoMax1)
    print(pretoMin2, pretoMax2)
    time.sleep(5)

    print("Coloque no amarelo")
    time.sleep(5)
    print(CS1.rgb, CS2.rgb)
    time.sleep(5)
    (r1, g1, b1) = CS1.rgb
    (r2, g2, b2) = CS2.rgb
    amareloMin1 = (r1-1, g1-1, b1-1)
    amareloMax1 = (r1+1, g1+1, b1+1)
    amareloMin2 = (r2-1, g2-1, b2-1)
    amareloMax2 = (r2+1, g2+1, b2+1)
    print(amareloMin1, amareloMax1)
    print(amareloMin2, amareloMax2)
    time.sleep(5)

    print("Coloque no marrom")
    time.sleep(5)
    print(CS1.rgb, CS2.rgb)
    time.sleep(5)
    (r1, g1, b1) = CS1.rgb
    (r2, g2, b2) = CS2.rgb
    marromMin1 = (r1-1, g1-1, b1-1)
    marromMax1 = (r1+1, g1+1, b1+1)
    marromMin2 = (r2-1, g2-1, b2-1)
    marromMax2 = (r2+1, g2+1, b2+1)
    print(marromMin1, marromMax1)
    print(marromMin2, marromMax2)
    time.sleep(5)
    print("Parametros finais concluidos")
    
ajustes()
while True:
#def qualCor1():
    #global corCS1
    cor1 = CS1.rgb
    if (cor1 >= azulMin1 and cor1 <= azulMax1):
        corCS1 = 2
    if (cor1 >= brancoMin1 and cor1 <= brancoMax1):
        corCS1 = 6
    if (cor1 >= verdeMin1 and cor1 <= verdeMax1):
        corCS1 = 3
    if (cor1 >= marromMin1 and cor1 <= marromMax1):
        corCS1 = 7
    if (cor1 >= pretoMin1 and cor1 <= pretoMax1):
        corCS1 = 1
    if (cor1 >= vermelhoMin1 and cor1 <= vermelhoMax1):
        corCS1 = 5
    if (cor1 >= amareloMin1 and cor1 <= amareloMax1):
        corCS1 = 4
    
#def qualCor2():
    #global corCS2
    cor2 = CS2.rgb
    if (cor2 >= azulMin2 and cor2 <= azulMax2):
        corCS2 = 2
    if (cor2 >= brancoMin2 and cor2 <= brancoMax2):
        corCS2 = 6
    if (cor2 >= verdeMin2 and cor2 <= verdeMax2):
        corCS2 = 3
    if (cor2 >= marromMin2 and cor2 <= marromMax2):
        corCS2 = 7
    if (cor2 >= pretoMin2 and cor2 <= pretoMax2):
        corCS2 = 1
    if (cor2 >= vermelhoMin2 and cor2 <= vermelhoMax2):
        corCS2 = 5
    if (cor2 >= amareloMin2 and cor2 <= amareloMax2):
        corCS2 = 4

    print(corCS1, corCS2)