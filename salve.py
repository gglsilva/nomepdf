#!/usr/bin/python
##coding: utf-8

import os
from PyPDF2 import PdfFileWriter, PdfFileReader

'''
#########
def month(chain):
    list_month = []
    meses = chain
    stri = meses[3] + meses[4]
    dic = {'01': 'Janeiro', '02': 'Fevereiro', '03':'Março','04':'Abril',
'05':'Maio','06':'Junho','07':'Julho','08':'Agosto','09':'Setembro','10':'Outubro',
'11':'Novembro','12':'Dezembro'}
    for item in dic:
        if item == stri:
            list_month.append(dic[item])
    
    #print(stri)
    return list_month


########
def extraindoPdf(ep):
    list = []
    for i in range(ep.numPages):
        spg = ep.getPage(i).extractText()
        spg[:1000]
        pg = spg.split('\n')
        nome = pg[2]
        numero = pg [10]
        data = pg [20]#obs
        month(data)
        concat = numero + ' - ' + nome + ' - ' + data
        print(concat)
        list.append(concat)       
    return list
'''

########
def caminho():
    path = 'C:\\Users\\cliente\\Desktop\\'       
    os.chdir(path)
    print(os.listdir())

    #abre o arquivo pdf
    arq = str(input('selecionar Arquivo: '))
    pdfFileObj = open(arq + '.pdf','rb')
    pdf = PdfFileReader(pdfFileObj)
    print('Carregando Arquivo...')
    #lns = extraindoPdf(pdf)
    escrevendoPdf(pdf)
        
    pdfFileObj.close()


#########
def escrevendoPdf(pdf): 
    
    for i in range(pdf.numPages):
        output = PdfFileWriter()
        output.addPage(pdf.getPage(i))
        output.write(outputStream)
    print('Concluido')
    pdf.close()
caminho()
