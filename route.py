#!/usr/bin/python
##coding: utf-8

import os
from PyPDF2 import PdfFileWriter, PdfFileReader

#esta função itera sobre o objeto, extrai os textos das paginas para uma string
#e retorna uma lista com o nome dos pagadores
def extraindoPdf(ep):
    list = []
    for i in range(ep.numPages):
        spg = ep.getPage(i).extractText()
        spg[:1000]
        pg = spg.split('\n')
        nome = pg[2]
        numero = pg [10]
        concat = numero + ' - ' + nome
        print(concat)
        list.append(concat)       
    return list

# esta função itera pelas páginas, instancia o objeto de escrita,
# copia uma pagina e escreve no objeto de saida, colocar o nome do pagador no objeto de saida
# e escreve o arquivo
def escrevendoPdf(nb ,lnomes): 

    for i in range(nb.numPages):
        output = PdfFileWriter()
        output.addPage(nb.getPage(i))
        with open(lnomes[i] + '.pdf', "wb") as outputStream:
            output.write(outputStream)
    print('Concluido')

#def listArquivos():
#    print(os.listdir())

#def caminhoNovo():
    

#
def caminho():
    path = 'C:\\Users\\cliente\\Desktop\\BOLETOS\\Boletos 2019'
    print('Diretorio Atual: {}'.format(path))
    dir_nv = str(input('Digite o caminho: '))
    os.chdir(os.path.join(path, dir_nv))
    print(os.listdir())

    #abre o arquivo pdf
    arq = str(input('selecionar Arquivo: '))
    pdfFileObj = open(arq + '.pdf','rb')
    pdf = PdfFileReader(pdfFileObj)
    print('Carregando Arquivo...')
    op = int(input('''1 - extrair no diretorio corrente
2 - Extrair em outro diretorio'''))
    if op == 1:
        lns = extraindoPdf(pdf)
        escrevendoPdf(pdf, lns)
    elif op ==2:
        diretorio = input('Digite o caminho para o diretorio de extração: ')
        if os.path.isdir(diretorio):
            print('já existe uma pasta com esse nome!')
            print(os.chdir(diretorio))
        else:
            os.mkdir(diretorio)
            print(os.chdir(diretorio))
            print('criado com sucessso!')
        lns = extraindoPdf(pdf)
        escrevendoPdf(pdf, lns) 
    else:
        print('Opção invalida, até mais.')
    #chama funções
    #lns = extraindoPdf(pdf)
    #escrevendoPdf(pdf, lns)
    pdfFileObj.close()
