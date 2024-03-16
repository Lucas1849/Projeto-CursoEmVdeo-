
def Abrir(arquivo):
    try:
        a = open(arquivo,'a')
        a.close()
    except:
        print('\033[31mHouve um erro na arbetura do arquivo!\033[m')
    else:
        print(f'\033[32mArquivo {arquivo} aberto com sucesso!\033[m')


def Escrever(arquivo,nome,idade):
    try:
        a = open(arquivo,'at')
    except:
        print('\033[31mHouve um erro ao escrever no arquivo\033[m')
    else:
        a.write(f'{nome};{idade}\n')
        a.close()



def Ler(arquivo):
    try:
        a = open(arquivo,'rt')
    except:
        print('\033[31mHouve um erro ao abrir seu arquivo!\033[m')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<20}{dado[1]:>3} ')