#!/usr/bin/env python3

# Importa as bibliotecas necessárias
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *

CS1 = ColorSensor(INPUT_1)
CS2 = ColorSensor(INPUT_2)

CS1.mode = 'RGB-RAW'
CS2.mode = 'RGB-RAW'

# Classe para representar uma cor em RGB
class Cor:
    def __init__(self, r, g, b, nome):
        self.r = r
        self.g = g
        self.b = b
        self.nome = nome

    def distancia(self, r, g, b):
        return math.sqrt((self.r - r) ** 2 + (self.g - g) ** 2 + (self.b - b) ** 2)

# Definindo algumas cores
vermelho = Cor(200, 27, 37, "vermelho")
vermelho2 = Cor(230, 93, 46, "vermelho 2")
verde = Cor(36, 70, 50, "verde")
verde2 = Cor(45, 141, 41, "verde 2")
azul = Cor(36, 49, 95, "azul")
azul2 = Cor(28, 77, 71, "azul 2")
preto = Cor(30, 30, 37, "preto")
preto2 = Cor(30, 60, 20, "preto 2")
branco = Cor(255, 255, 255, "branco")
branco2 = Cor(170, 255, 204, "branco 2")
amarelo = Cor(220, 190, 70, "amarelo")
amarelo2 = Cor(180, 255, 40, "amarelo 2")
marrom = Cor(61, 35, 43, "marrom")
marrom2 = Cor(62, 77, 43, "marrom 2")

# Lista de cores para o sensor 1
cores1 = [vermelho, verde, azul, marrom, amarelo, preto, branco]

# Lista de cores para o sensor 2
cores2 = [vermelho2, verde2, azul2, marrom2, amarelo2, preto2, branco2]

def encontrar_cor_mais_proxima(r, g, b, cores):
    cor_mais_proxima = None
    menor_distancia = float('inf')

    for cor in cores:
        distancia = cor.distancia(r, g, b)
        if distancia < menor_distancia:
            menor_distancia = distancia
            cor_mais_proxima = cor

    return cor_mais_proxima.nome

leitura = 0
while True:
    leitura += 1
    print('')
    print("leitura numero: {}".format(leitura))
    print('')
    r1,g1,b1 = CS1.rgb
    cor_mais_proxima1 = encontrar_cor_mais_proxima(r1,g1,b1, cores1)
    print("A cor mais proxima lida pelo sensor CS1 e: {}".format(cor_mais_proxima1))

    r2,g2,b2 = CS2.rgb
    cor_mais_proxima2 = encontrar_cor_mais_proxima(r2,g2,b2, cores2)
    print("A cor mais proxima lida pelo sensor CS2 e: {}".format(cor_mais_proxima2))
    print('')
    print('')
    print(CS1.rgb)
    print(CS2.rgb)
    print('---------------------------------')
    time.sleep(2)
