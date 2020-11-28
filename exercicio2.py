#!/usr/bin/python3
#coding=utf-8

#lista
l = ["windows","macos","linux","solaris","android","ios"]
z = len(l)
print('\n')
print('Exercicio 2 - Loops\n')
#Loop for
for x in l:
    if x != 'solaris':
        print(x)
        w = open('exerc2for.txt','a')
        w.write(x +'\n')
        w.close()
print('\n')
#loop while
while z > 0:
    if l[z-1] != 'solaris':
        print(l[z-1])
        w = open('exerc2while.txt','a')
        w.write(l[z-1]+'\n')
        w.close
    z -= 1
print('\n')
