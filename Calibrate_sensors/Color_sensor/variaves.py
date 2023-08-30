#!/usr/bin/env python3

# ---------- Importa as bibliotecas necessarias
import time # importando o tempo para a logica de programacao
import math # importando a matematica para a logica de programaaao
from ev3dev2.motor import * # importando tudo da biblioteca ev3dev2.motor
from ev3dev2.sound import Sound # importando o som da biblioteca ev3dev2.sound
from ev3dev2.button import Button # importando os botoes da biblioteca ev3dev2.button
from ev3dev2.sensor import * # importando tudo da biblioteca ev3dev2.sensor
from ev3dev2.sensor.lego import * # importando tudo da biblioteca ev3dev2.sensor.lego
import colorsys
#from ev3dev2.sensor.virtual import * # importando tudo da biblioteca ev3dev2.sensor.virtual

CS1 = ColorSensor(INPUT_1)  # setando sensor de cor na entrada 
CS2 = ColorSensor(INPUT_2) # setando sensor de cor na entrada 

CS1.mode = 'RGB-RAW'
CS2.mode = 'RGB-RAW'



# ---------- Aqui é onde seus codigos começam

# ---------- Funções

brancoMin1 = 0, 0, 0
brancoMax1 = 0, 0, 0
azulMin1 = 0, 0, 0
azulMax1 = 0, 0, 0
vermelhoMin1 = 0, 0, 0
vermelhoMax1 = 0, 0, 0
verdeMin1 = 0, 0, 0
verdeMax1 = 0, 0, 0
pretoMin1 = 0, 0, 0
pretoMax1 = 0, 0, 0
amareloMin1 = 0, 0, 0
amareloMax1 = 0, 0, 0
marromMin1 = 0, 0, 0
marromMax1 = 0, 0, 0
(r1, g1, b1) = 0, 0, 0

brancoMin2 = 0, 0, 0
brancoMax2 = 0, 0, 0
azulMin2 = 0, 0, 0
azulMax2 = 0, 0, 0
verdeMin2 = 0, 0, 0
verdeMax2 = 0, 0, 0 
verdeMin2 = 0, 0, 0
verdeMax2 = 0, 0, 0
pretoMin2 = 0, 0, 0
pretoMax2 = 0, 0, 0
amareloMin2  = 0, 0, 0
amareloMax2  = 0, 0, 0
marromMin2 = 0, 0, 0
marromMax2 = 0, 0, 0
(r2, g2, b2) = 0, 0, 0