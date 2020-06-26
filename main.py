#!/usr/bin/python
##coding: utf-8
import route
import sys
'''
Função Menu principal do programa que separa o arquivo dos boletos gerados
em varios PDF(s) e cria uma pasta caso ela não exista.  
'''

#Função de tags
def reshTagMenu():
    print('#'*25)

#Função Menu Principal:
def menu():
    reshTagMenu()
    print(' ' * 9 + 'SISBOLL')
    reshTagMenu()
    
    escolha = int(input('''
    Menu
1 - Dividir Boletos
2 - Dividir I.R.
3 - Sair

Escolha: '''))
    if escolha == 1:
        route.caminho()
    elif escolha == 2:
        print('faz nada')     
    elif escolha == 3:
        sys.exit()
    else:
        print('Escolha invalida, tente novamente')
        menu()
menu()
