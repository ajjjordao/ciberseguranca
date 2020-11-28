#!/usr/bin/python3
#coding=utf-8
#inicializar 2 listas vazias
listaIp = []
listaInt = []
#string gama IP
ip = "192.168.1."
#1 ciclo - endereços IP possiveis
file = open("ipList.txt", "w")
listaIp = [(ip + str(x) + "\n") for x in range(256)]
print(listaIp)
file.writelines(listaIp)
file.close()
#2 ciclo - lista com inteiros de 1 a 1024
file = open("portList.txt","w")
listaInt = [(str(z)+ "\n") for z in range(1, 1024+1)]
print(listaInt)
file.writelines(listaInt)
file.close()
