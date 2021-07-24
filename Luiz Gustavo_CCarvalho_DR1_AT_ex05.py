import sys
import matplotlib.pyplot as plt

def extrair_dados(caminho_arquivo):
    with open(caminho_arquivo, encoding="utf8") as arquivo:
        conteudo = arquivo.read()
        
    conteudo = conteudo.splitlines() # conteúdo é uma lista onde cada linha é um elemento
    rotulos = conteudo[0] # separando a primeira linha (cabeçalho) da var conteúdo
    rotulos = rotulos.split(',') # separando os itens da lista rotulos, onde o separador é a vírgula
    conteudo = conteudo[1:] # conteudo agora é da linha 1 (segunda linha) em diante
    dados = [] # var para transformar cada linha em uma lista diferente
    for elemento in conteudo:
        elemento = elemento.split(',')
        dados.append(elemento)
        
    return rotulos, dados

# A)
def pais_ano_pib(pais, ano): 
    rotulos, dados = extrair_dados('assessment_pib.csv') # Extraindo dados da tabela através da função anterior
    
    lista_paises = [] # Transformando os países em uma lista para verificação do input País
    for elemento in dados:
        paises = elemento[0]
        lista_paises.append(paises)
    if pais in lista_paises: # Verificação do input País
        indice_pais = rotulos.index('País') # Captando índice do país digitado (0) para posterior utilização
    else:
        print("País não disponível.")
        sys.exit()
    if ano in rotulos: # Verificação do input Ano
        indice_ano = rotulos.index(ano) # Captando índice do ano digitado, ou seja, a coluna do PIB desejado
    else:
        print("Ano não disponível.")
        sys.exit()
    
    for elemento in dados:
        if elemento[indice_pais] == pais: # Se índice 0 de alguma lista dentro de dados for = país digitado:
            pib = elemento[indice_ano] # PIB será igual a string localizada no índice do ano digitado (coluna)
            return pib
      

pais = input("Informe um País: ")
ano = input("Informe um ano entre 2013 e 2020: ")
print(f"PIB {pais} em {ano}: US${pais_ano_pib(pais, ano)} trilhões.")
print("--------------------------------------------")

# B)
def var_pib():
    rotulos, dados = extrair_dados('assessment_pib.csv')
    
    dados_2013 = [] # Transformando coluna 2013 em lista de number
    for elemento in dados:
        pib_2013 = float(elemento[1])
        dados_2013.append(pib_2013)
    
    dados_2020 = [] # Transformando coluna 2020 em lista de number
    for elemento in dados:
        pib_2020 = float(elemento[8])
        dados_2020.append(pib_2020)
        
    lista_paises = [] # Transformando os países em uma lista
    for elemento in dados:
        paises = elemento[0]
        lista_paises.append(paises)
        
    # Fazendo operações com os índices de cada lista: ((2020 - 2013) / 2013) * 100
    var_pib = [(((b - a) / a) * 100) for a, b in zip(dados_2013, dados_2020)]
    for impressao in range(len(var_pib)):
        print(f"{lista_paises[impressao]}: Variação de {var_pib[impressao]:.2f}% entre 2013 e 2020.")

var_pib()

# C)
def imprimir_grafico(anos, pib):
    plt.plot(anos, pib)
    plt.show() 

def dados_grafico(pais):
    rotulos, dados = extrair_dados('assessment_pib.csv')
    lista_anos = rotulos
    lista_anos.pop(0) # Transformando os anos em lista sem o índice 0 ('País') --> Eixo X --> ainda é str
    lista_anos_number = []
    for contador in range(len(lista_anos)): # Transformando lista com os anos em números para geração do gráfico
        number = float(lista_anos[contador])
        lista_anos_number.append(number)
    
    for elemento in dados:
        if elemento[0] == pais: # Se índice 0 de alguma lista dentro de dados for = país digitado:
            lista_pibs = elemento # Lista dos PIBs é a lista do pais digitado
    lista_pibs.pop(0) # Retirando o índice 0 (nome do país) da lista de PIBs --> ainda é str
    lista_pibs_number = []
    for contador in range(len(lista_pibs)): # Transformando lista com os PIBs em números para geração do gráfico
        number = float(lista_pibs[contador])
        lista_pibs_number.append(number)
    
    eixo_x = lista_anos_number
    eixo_y = lista_pibs_number
    
    imprimir_grafico(eixo_x, eixo_y)


dados_grafico(pais)
