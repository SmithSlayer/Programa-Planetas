from crud import *

#Programa Principal
fim = False

while not fim:
    print('\nGereciador de Planeta')
    print('1. Adicionar Planeta')
    print('2. Remover planetas')
    print('3. Listar planetas')
    print('4. Buscar planeta')
    print('5. Editar planeta')
    print('0. Sair')
    
    opcao = input('Digite a opção desejada: ')
    
    if opcao == '1':
      adicionar_planeta()
    elif opcao == '2':
      remover_planeta()
    elif opcao == '3':
      listar_planetas()
    elif opcao == '4':
      buscar_planetas()
    elif opcao == '5':
      editar_planeta()
    elif opcao == '0':
      print('\nObrigado por usar nosso sistema!')  
      fim = True
    else:
      print('Opção inválida.')  
        
    
        