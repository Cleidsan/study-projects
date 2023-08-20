from tkinter import *
import requests
def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotacoes["text"] = texto


janela = Tk()
janela.title('Cotação Atual Das Moedas')
janela.geometry("350x200")

texto_orient = Label(janela, text="Clique no botão para exibir a cotação atual das moedas.")
texto_orient.grid(column=0, row=0, padx=30, pady=20)

botao = Button(janela, text="Exibir Cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=0, pady=10)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2)

janela.mainloop()