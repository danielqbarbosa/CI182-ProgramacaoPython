# -*- coding: utf-8 -*-

"""
======================
Analisador de Amostras 
======================

Um programa que permite analisar amostras e gerar a tabela de frequências e histograma

"""
# Bibliotecas
import math
import os
import time
import referencias 

# Comandos de documentação do código
__author__ = "Enrico Silva (GRR20142316)\n Ana Paula Santos Rodrigues (GRR20176366) \n Ana Maria Deminciano Lima (GRR20140289)"
__license__ = "GPL"
__version__ = "1.0"
# A pessoa que mantém o código
__maintainer__ = "Daniel de Queiroz Barbosa (danielbarbosa@ufpr.br)"  
__professor__ = "Jackson Antonio do Prado Lima (japlima@inf.ufpr.br)"  
__email__ = "danielbarbosa@ufpr.br"
# Status tipicamentente é: Prototype, Development ou Production
__status__ = "Prototype"
print(__doc__)
print('Professor: \n', __professor__)
print('\nAutores: \n', __author__)
print('\nSuporte técnico (monitor voluntário :) )\n' , __maintainer__)
print()

def insere_amostra(amostras):
    '''
    Função que insere amostras
    '''
    entrada = input('Inserir nova amostra (''x'' para fim): ')
    
    while entrada.lower() != 'x':
        try:
            amostras.append(int(entrada))
        except:
            print('Tipo de dado incorreto. Digitar somente número inteiro')
        entrada = input('Inserir nova amostra (''x'' para fim): ')

def lista_amostra(amostras):
    '''
    Função que lista as amostras
    '''
    #chave vai mostrar o indice da lista e valor mostra o conteudo
    for chave, valor in enumerate(amostras): 
        print('Amostra[%s]: %2d' % (chave, valor))
    #len mostra a quantidade de itens dentro da lista amostras
    print('Total de itens na amostra: %d' % len(amostras))
    print()    

def calcula_tabela_frequencia(amostras):
    '''
    Função que calcula a tabela e o histograma de frequência
    
    Regra de Sturges:  k = 1 + 3.3*log(n)
    onde:
      k: número de classes do histograma;
      n: tamanho da amostra de dados
      '''
    if len(amostras) == 0:
        print('Sem amostras para calcular. Inserir valores na amostra.')
    else:
        #
        # aplica a formula de Sturges, arredonda o valor e converte o resultado para inteiro
        k = int(round(2 + 3.3 * math.log10(len(amostras)), 0))
        print()
        print('Número de classes (k): %d' % k)
        '''
        cálculo do intervalo das classes.
        H = R / k
        onde:
          H: intervalo de classes
          R: amplitude da amostra
          k: número de classes do histograma;
        '''
        R = round(max(amostras) - min(amostras),0)
        print('Amplitude (R): %d' % R)
        H = round(R / k) #Arredonda para cima
        print('Intervalo de classe (H): %d' % H)
        print()        
        #
        # determinar o limite inferior (Li) e o limite superior (Ls) da classe
        # busca o menor número da amostra e converte para inteiro
        Li = int(min(amostras))
        Ls = Li + H
        ##################################
        # Aqui foi feita uma tabela ilustrativa apenas para mostrar
        # outra maneira de se fazer
        print('Distribuição dos números nas classes')
        print('Classe|(Li |- Ls)')
        for c in range(0,k):
            '''
            Método sintetico -> List Comprehensions( modo de filtrar valores de uma lista)
            Filtra todos os numeros da lista 'amostras'
            que estejam na faixa (Li -- Ls)
            '''
            l_classe = [int(num) for num in amostras if num in range(Li,Ls)]
            print('%5d |(%2d |- %2d)' % ((c+1), Li, Ls), l_classe)
            # incremetar o (Li) e o (Ls) da classe com a amplitude (H)
            Li = Ls
            Ls = Li + H
        # Verifica se ainda possui valores na amostra
        l_classe = [int(num) for num in amostras if num >= Li]
        if len(l_classe) > 0:
            print('%5d |(   >= %2d)' % (c+2, Li), l_classe)
        #
        # Aqui termina esta tabela ilustrativa
        ##################################
        #
        # Desenha a tabela de frequencia
        #
        Li = int(min(amostras))
        Ls = Li + H
        f_abs = 0   # inicia a frequencia absoluta
        f_acum = 0  # inicia a fequencia acumulada
        l_rel = []  # inicia a lista da freq relativa
        print()
        print('Tabela de Frequencia')
        print('Classe|(Li |- Ls)|Frequencia|Acumulada|Relativa(%)')
        for c in range(0,k):
            l_classe = [int(num) for num in amostras if num in range(Li,Ls)]
            f_abs = len(l_classe)
            f_acum += len(l_classe)
            f_rel = round(100*f_abs/len(amostras),1)
            l_rel.append(f_rel)
            print('%5d |(%2d |- %2d)| %8d | %7d | %7.1f' % (c+1, Li, Ls, f_abs, f_acum, f_rel))
            # incremeta a frequencia acumulada (fa)
            # incremeta o (Li) e o (Ls) da classe com a amplitude (H)
            Li = Ls
            Ls = Li + H
        # Verifica se ainda possui valores na amostra
        l_classe = [int(num) for num in amostras if num >= Li]
        if len(l_classe) > 0:
            f_abs = len(l_classe)
            f_acum += len(l_classe)
            f_rel = round(100*f_abs/len(amostras),1)
            l_rel.append(f_rel)
            print('%5d |(   >= %2d)| %8d | %7d | %7.1f' % (c+2, Li, f_abs, f_acum, f_rel))
        #
        # desenha o histograma de frequencia relativa
        #
        print()
        print('Histograma de Frequencia Relativa')
        #a segunda variavel q sera criada(valor) vai pegar os valores da lista q vai multiplicar pelo caracter # mostrando o histograma
        for indice, valor in enumerate(l_rel):
            print(indice+1, '#'*int(valor))

    print()

def le_nome_arquivo():
    '''
    Função que lê o nome do arquivo informado pelo usuário.
    O nome do arquivo deve obrigatoriamente terminar com .dat
    Essa função é usada tanto na leitura quanto na escrita do arquivo.
    '''
    # Solicita que o usuário digite o nome do arquivo
    arquivo = input('Nome do arquivo (ex: a.dat): ')

    # Apenas arquivos que contenham extensão .dat são permitidos.
    # Ex.: amostras.dat
    while(not arquivo.endswith(".dat")):
        print('Nome de arquivo inválido!')
        arquivo = input('Forneça outro nome de arquivo:')

    # Retorna o nome do arquivo
    return arquivo 

def salva_amostra_arquivo(nome_arquivo, amostras):
    '''
    Função que salva as amostras em um arquivo
    '''
    resposta = input('Deseja salvar as alteracoes feitas? (S)im ')

    # Se o usuário desejar salvar as amostras em um arquivo
    if resposta.upper() == 'S':
        # Se o usuário ainda não informou um nome para o arquivo, solicita um
        if nome_arquivo == '':
            nome_arquivo = le_nome_arquivo()

        # Salva as amostras no arquivo, 'w' sera no modo escrita
        with open(nome_arquivo, 'w') as arquivo:
            for amostra in amostras:
                arquivo.write(str(amostra)+'\n')


def le_amostra_arquivo(amostras):
    '''
    Função que lê as amostras contidas em um arquivo
    '''

    """
    Criamos uma variável com o nome do arquivo, pois retornaremos
    esse nome para ser utilizado no menu principal.
    Assim, salvamos as alterações que realizamos no mesmo arquivo.
    Caso o usuário não desejar abrir um arquivo de dados,
    iremos verificar o nome do arquivo na hora de salvar para saber
    se necessitamos que ele informe o nome do arquivo.
    """
    nome_arquivo = ''

    resposta = input('Deseja abrir um arquivo com os dados? (S)im ')

    # Se o usuário desejar ler amostras salvas em um arquivo
    if resposta.upper() == 'S':
        # Solicita o noem do arquivo ao usuário
        nome_arquivo = le_nome_arquivo() 
        """
        Abre o arquivo pra leitura e salva na variável arquivo.
        Ao abrir um arquivo, o programa 'bloqueia' o arquivo para ser utilizado por ele
        Usando o comando "with open(nome_arquivo, 'r') as arquivo"
        permite que após a leitura o arquivo fique "desbloqueado"
        para ser utilizado novamente.
        """
        with open(nome_arquivo, 'r') as arquivo:
            # Lê as linhas do arquivo
            for linha in arquivo:
                # Como cada amostra está em uma linha, guarda a amostra lida no vetor de amostras
                amostras.append(float(linha.strip('\n')))
    return nome_arquivo

def menu():
    '''
    Função que contém o menu do programa
    '''
    # Mostra as opções pro usuário na tela
    print('Menu:')
    print('\t1 - Insere amostras')
    print('\t2 - Listar amostras')
    print('\t3 - Calcular Tabela de Frequência')
    print('\t4 - Sair')

    # Retorna o que o usuário digitar
    return int(input('Digite a opção desejada: ')) 

def main():
    '''
    Programa principal
    '''

    # guardaremos as amostras em um vetor/array
    amostras = []

    # lê as amostras salvas em um arquivo (se o usuário desejar)
    nome_arquivo = le_amostra_arquivo(amostras)

    # Limpa a tela do terminal para ficar mais "elegante" a apresentação
    os.system('cls' if os.name == 'nt' else 'clear')

    # chama a função menu que mostra o menu e solicita uma opção ao usuário
    opcao = menu()

    # enquanto o usuário não digitar a opção: 4 - Sair
    while opcao != 4:
        # Se for a opção: 1 - Insere amostras
        if opcao == 1:
            # chama a função que insere amostras no vetor de amostras
            insere_amostra(amostras)
        # Se for a opção: 2 - Listar amostras
        elif opcao == 2:
            # chama a função que imprime as amostras na tela
            # passando o vetor que contém as amostras
            lista_amostra(amostras)
            time.sleep(5)
        # Se for a opção: 3 - Calcular Tabela de Frequência
        elif opcao == 3:
            # chama a função que calcula a tabela de frequência
            # e monta o histograma
            calcula_tabela_frequencia(amostras) 
            # time.sleep(2)
            print()
            opcao = input('Pressione <ENTER> para continuar') 			
        # Se digitou uma opção de menu inválida
        else:
            print("\nOpção inválida! Por favor, informe uma opção válida.\n")
            # Faz o programa esperar 1 segundo e depois continua
            time.sleep(2)

        # Limpa a tela do terminal
        os.system('cls' if os.name == 'nt' else 'clear')

        # Mostra ao usuário o menu novamente e aguarda ele escolher uma opção
        opcao = menu()

    # Antes de finalizar o programa, salva as amostras em um arquivo
    salva_amostra_arquivo(nome_arquivo, amostras)

    # Exibe as referências bilbiograficas
    referencias.doc()


if __name__ == "__main__":
    '''
    Quando executar o programa python esse trecho de código será executado e chamará o programa principal.
    Para um melhor entendimento acesse os links abaixo:
    http://www.devfuria.com.br/python/entenda-__name__-__main__/
    https://pythonhelp.wordpress.com/2012/06/15/por-que-__name__-__main__/
    '''

    # Chama a função main
    main()
