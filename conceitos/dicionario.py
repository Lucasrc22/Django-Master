meu_dic = {'nome':'Lucas', 'idade': '25', 'cidade': 'Recife', 'profissao': 'Desenvolvedor'}

print(meu_dic['profissao'])

meu_dic.pop('idade')

print(meu_dic)

print(meu_dic.keys())
print(meu_dic.values())
print(meu_dic.items())
print(meu_dic.get('cidade'))
print(meu_dic.get('idade', 'Chave não encontrada'))
print(meu_dic.clear())

pessoa = {
    'nome':'Lucas',
    'idade': '25',
    'cidade': 'Recife',
    'profissao': 'Desenvolvedor',
    'interesses': ['Jogos', 'Esportes', 'Música'],
    'pet':{
        'nome':'Maya',
        'idade':'7',
        'peso':'7kg'
    }
}

pessoa['cor_favorita'] = ['Azul', 'Preto','Cinza']

print(pessoa)
