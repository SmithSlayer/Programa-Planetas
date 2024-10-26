from planetas import planetas

def adicionar_planeta():
  nome = input('Digite o nome do planeta: ')
  tamanho = input('Digite o tamanho do planeta: ')
  distancia = input('Digite o a distância do Sol: ')
  apelido = input('Digite o apelido desse planeta: ')
  planetas[nome] = {'Tamanho': tamanho, 'Distância': distancia, 'Apelido': apelido}
  print(f'O planeta {nome} foi adicionado com sucesso!')
  
def remover_planeta():
  nome = input('Digite o planeta que deseja remover: ')
  if nome in planetas:
    del planetas[nome]
    print(f'O planeta {nome} foi removido com sucesso')
  else:
    print('Planeta nao encontrado no banco de dados')
    
def editar_planeta():
  nome = input('Digite o nome do planeta que deseja editar: ')
  if nome in planetas:
    novo_tamanho = input('Digite o novo tamanho: ')
    nova_distancia = input('Digite a nova distância do Sol: ')
    novo_apelido = input('Digite o novo apelido: ')
    planetas[nome]['Tamanho'] = novo_tamanho
    planetas[nome]['Distância'] = nova_distancia
    planetas[nome]['Apelido'] = novo_apelido
    print(f'O planeta {nome} foi editado com sucesso!')
  else:
    print('Planeta não encontrado.')
    
def listar_planetas():
    if not planetas:
        print('Não há planetas cadastrados.')
    else:
        for planeta, info in planetas.items():
            print(f'Planeta: {planeta}')
            print(f'Tamanho: {info["Tamanho"]}')
            print(f'Distância do Sol: {info["Distância"]}')
            print(f'Apelido: {info["Apelido"]}')
            print('-' * 20)
            
def buscar_planetas():
    nome = input('Digite o nome do planeta que deseja buscar: ')
    if nome in planetas:
        print(f'Planeta: {nome}')
        print(f'Tamanho: {planetas[nome]["Tamanho"]}')
        print(f'Distância do Sol: {planetas[nome]["Distância"]}')
        print(f'Apelido: {planetas[nome]["Apelido"]}')
    else:
        print('Planeta não encontrado.')