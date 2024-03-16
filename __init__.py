def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print(f'\033[0;31mERRO! Digite um número inteiro válido:  \033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[0;31mUsuário prefiriu não digitar esse número.\033[m')
            return 0
        else:
            return n


def título(msg):
    tamnh = len(msg) + 4
    print('-'*tamnh)
    print(f'  {msg}')
    print('-'*tamnh)


def Menu(*txt):
    for c,v in enumerate(txt):
        print(f'\033[33m{c+1}\033[m - \033[34m{v}\033[m')