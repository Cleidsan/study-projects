import pandas as pd
import win32com.client as win32

# importar a base de dados     ### pra ler instalar openpyxl
tabela_vendas = pd.read_excel('Vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

# faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)
# quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)
print('-' * 50)
# ticket medio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
ticket_medio = ticket_medio.rename(columns={0: 'Ticket Médio'})
print(ticket_medio)
# enviar um email com o relatorio
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'wspwagne@gmail.com'
mail.Subject = 'Relatorio de Vendas Por Loja'
mail.HTMLBody = f'''
<h1 style="text-align: center;">Prezado Wagne,</h1>

<h2 style="text-align: center;">Segue o Relatorio de Vendas Por Cada Loja.</h2>

<h3 style="margin-left: 90px;">Faturamento:</h3>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<h3 style="margin-left: 76px;">Quantidade vendida:</h3>
{quantidade.to_html()}

<h3 style="margin-left: 2px;">Ticket Médio dos Produtos em cada Loja:</h3>
{ticket_medio.to_html(formatters={'Ticket Médio': 'R${:,.2f}'.format})}

<h4 style="text-align: center;">Qualquer dúvida estou á disposição.</h4>

<h5 style="text-align: center;">Att...,</h5></br>
<h5 style="text-align: center;">Cleidsan.</h5>
'''

mail.Send()

print('Email Enviado!')
