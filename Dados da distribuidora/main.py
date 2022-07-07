import json

with open('dados.json', 'r') as faturamentoMensal:
    dados = json.load(faturamentoMensal)
    print(dados)