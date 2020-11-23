import pyautogui as pg
import webbrowser as wb
import time

wb.open("web.whatsapp.com")
time.sleep(30)

quem=pg.prompt(text='Nome do contato para enviar a mensagem?', title='Quem')
quant=pg.prompt(text='Quantas vezes enviar a mensagem?', title='Quantas Vezes')
mensagem=pg.prompt(text='Qual mensagem enviar?', title='Mensagem')
pg.alert("Clique OK após o site carregar")

#Definindo variáveis
quant=int(quant)
i=0
time.sleep(2)
#Selecionando destino
pg.click(180, 250)
time.sleep(2)
pg.write(quem)
time.sleep(2)
pg.click(200, 380)

#Esperando processar
time.sleep(4)

#Digitar Mensagem
while (i < quant):
    pg.write(mensagem)
    pg.press("enter")
    i=i+1

print("Processo Concluído")
