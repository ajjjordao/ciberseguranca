#!/usr/bin/python3
#coding=utf-8
import sys
import os
#definição de funções
def printError(e):
    "Imprime erro ocorrido"
    print(e)

def listar():
    "Lista diretório"
    lista = os.listdir
    print(lista)

def criar():
    "Cria diretório"
    nomeDir = input("\nInsira nome do diretório a criar: ")
    try:
        os.mkdir(nomeDir)
        print("\nDiretório criado com sucesso!\n")
    except:
        printError()

def editar():
    "Edita nome diretório"
    nomeDir = input("\nInsira nome do diretório a renomear: ")
    renDir = input ("\nInsira novo nome: ")
    try:
        os.rename(str(nomeDir),str(renDir))
        print("\nNome do diretório alterado")
    except:
        printError()
        
def  remover():
    "Apaga diretório"
    nomeDir = input("\nInsira nome do diretório a remover: ")
    try:
        os.rmdir(nomeDir)
        print("\nDiretório removido com sucesso!\n")
    except:
        printError()       

def main():
        print("\nIntroduza uma das seguintes opções:\n")
        print("1 - listar diretório\n")
        print("2 - criar diretório\n")
        print("3 - editar diretório\n")
        print("4 - remover diretório\n")
        print("0 - sair\n")

        try:
            while True:
                valor = input("\nIntroduza valor: ")
                try:
                    valor = int(valor)
                except:
                    printError()
                    continue
                if valor == 1:
                    listar()
                elif valor == 2:
                    criar()
                elif valor == 3:
                    editar()
                elif valor == 4:
                    remover()
                else:
                    valor == 0
                    break

if __name__ == "__main__":
    main()
                    