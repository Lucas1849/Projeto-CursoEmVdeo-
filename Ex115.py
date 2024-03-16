from Menu import *
from time import sleep
from Arquivo import *
NomeArq = 'Dados.txt'
Abrir(NomeArq)
while True:
    título('CADASTRO DE PESSOAS')
    Menu('Ver pessoas cadastradas','Cadastrar pessoas','Finalizar programa')
    print('-'*23)
    escolha = leiaInt('\033[32mSua opção: \033[m')
    if escolha == 1:
        título('PESSOAS CADASTRADAS')
        Ler(NomeArq)
        sleep(1.5) 
    elif escolha == 2:
        título('NOVO CADASTRO')
        nome = str(input('\033[36mNome: \033[m')).title().strip()
        idade = leiaInt('\033[34mIdade: \033[m')
        Escrever(NomeArq,nome,idade)
        sleep(1.5)  
    elif escolha == 3:
        print('\033[33mFinalizando o programa...\033[m')
        sleep(1.5)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
        sleep(2)
