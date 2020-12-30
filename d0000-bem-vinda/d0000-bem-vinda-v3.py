#!/usr/bin/env python3

#sobre a shebang:
#   deve ser posicionada sempre no início do arquivo;
#   o interpretador é acionado ao chamar o arquivo;
#   #! é a shebang propriamente dita;
#   /usr/bin é o diretório onde ficam os arquivos binários do usuário do SO.
#   env modifica o ambiente do shell temporariamente. É ele quem vai encontrar o interpretador sem que seja necessário definir seu caminho exato.

########
# autora: danielle8farias@gmail.com 
# repositório: https://github.com/danielle8farias
########

#criando uma função
#função recebe como argumento uma string
def cabecalho(msg):
    #repete o caractere por 42 vezes
    print('-'*42)
    #upper() torna a string maiúscula
    #:^42 centralizada, ocupando 42 caracteres no mínimo
    print(f'{msg.upper():^42}')
    print('-'*42)


#função sem argumento
def criar_rodape():
    '''
    sem parâmetro
    retorna a string FIM com espaçamento de 50 caracteres, incluindo a string.
    linha pontilhada em baixo e em cima.
    '''
    print('-'*50)
    print(f'{str.upper("fim"):^50}')
    print('-'*50)


#definindo a função
def ler_nome(msg):
    '''
    Função que faz a validação do dado de entrada.
    Aceita apenas caracteres formados por letras.
    '''
    #tentativa de recebimento do dado
    try:
        nome = input(msg).strip()
        #separando a string onde houver espaços e armazenando cada em uma lista
        lista_nome = nome.split()
        #''. separador da nova string; no caso não haverá um caractere separador
        #join() junta uma lista de string em uma única string; unida pelo separador acima
        nome = ''.join(lista_nome)
        #condicional:
        #   se nome não for apenas formado por letras
        if not nome.isalpha():
            #criando a exceção
            raise Exception('Digite apenas letras.')
    except Exception as erro:
        print(f'Valor inválido: {erro}')
        #retorna o zero
        return 0
    #se o 'try' for válido
    else:
        #retorna o valor da variável nome
        return nome.upper()


#main
cabecalho('programa de boas-vindas')
while True:
    #chamada da função
    nome = ler_nome('Digite seu nome: ')
    print(f'Bem-vinda, {nome}!')
    #variável recebe espaço
    resposta = ' '
    #laço while:
    #   enquando o valor de resposta for diferente de S ou N
    while resposta not in 'SN':
        #\n quebra de linha
        #upper() torna as letras maiúsculas
        #[0] captura apenas o primeiro caractere da string
        resposta = input('\nDeseja rodar o programa de novo? [S/N] ').upper().strip()[0]
    #condicional:
    #   se a resposta for igual a N
    if resposta == 'N':
        #quebra do laço while True
        break
criar_rodape()
