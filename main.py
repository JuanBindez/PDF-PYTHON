'''
Author: www.github.com/JuanBindez
Description: generate pdf
Python Version: 3.10
year: 2022
Local: Brazil
'''

import os

try:
    from reportlab.pdfgen import canvas
except ModuleNotFoundError:
    os.system("pip install reportlab")


def gerador_de_pdf(lista):
    nome_pdf = input('informe o nome do pdf: ')
    pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
    x = 720
    for nome,idade in lista.items():
        x -= 20
        pdf.drawString(247,x, '{} : {}'.format(nome,idade))
        
    #configurações do canvas
    pdf.setTitle(nome_pdf)
    pdf.setFont("Helvetica-Oblique", 14)
    pdf.drawString(245,750, 'Lista De Clientes')
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(245,724, 'Nome e Idade')
    pdf.save()
    print('{}.pdf Criado com Sucesso!'.format(nome_pdf))

    

lista = {'Juan': '27', 'Jose': '42', 'Maria': '22', 'Eduardo': '31'}

gerador_de_pdf(lista)
