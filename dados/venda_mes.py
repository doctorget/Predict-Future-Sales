import pandas as pd
dados = pd.read_csv('sales_train.csv')

dados['venda_mes'] = 0
lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
for i in range(34):
    print('interação',i)
    selecao = dados['mes_consecutivo'] == i
    dados[selecao]['venda_mes'] = dados['mes_consecutivo'].apply(lambda x:dados[selecao]['venda_item_dia'].sum() if x in lista else 22)

dados.to_csv('sales_mes.csv')
