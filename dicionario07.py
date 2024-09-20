#meu_dic = {'Chave':'valor'}
alunos = {'Maria':888,'João':777,'Ana':222}
alunos['Maria'] = 234 # atualizar o valor 
print(alunos)
alunos['Lucas'] = 123 # adicionar valor
print(alunos)
alunos.pop('joão') # remover chave e valor 
for Nome, matricula in alunos. items():
    print(f'matricula:{matricula}') Nome {nome}
alunoscopia = alunos.copy()
alunoscopia['Ana'] = 678
print('Dicinário alunos',alunos)
print('Dicionários alunosCopia',alunosCopia)