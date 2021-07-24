import matplotlib.pyplot as plt

# Jeito que encontrei de poder tirar a variável montante para fora da função foi usar
# return, inicialmente eu havia utilizado a função print dentro desta função
def valor_futuro(montante_inicial, aliquota_periodo, aporte_periodo, num_periodo):

    for mes in range(num_periodo): # O primeiro mês tem fórmula um pouco diferente por conta do valor de entrada
        if mes == 0: # Se for índice 0, ou seja, 1º mês, utilize esta fórmula
            montante_mes = montante_inicial * (aliquota_periodo / 100 + 1) + aporte_periodo
            y = [montante_mes] # Onde inicio a lista do eixo y do gráfico
        else: # Para todos os outros meses (índice != 0), utilize esta fórmula
            montante_mes = montante_mes * (aliquota_periodo / 100 + 1) + aporte_periodo
            y.append(montante_mes) # Onde vou adicionando montante_mes à lista do eixo y do gráfico
    return y # Esta função retorna uma lista chamada y (eixo do gráfico)    
    

montante_inicial = float(input("Valor inicial: R$ "))
aliquota_periodo = float(input("Rendimento por período (%): "))
aporte_periodo = float(input("Aporte a cada período: R$ "))
num_periodo = int(input("Total de períodos: "))

# Transportando a variável montante_mes para fora da função
y = valor_futuro(montante_inicial, aliquota_periodo, aporte_periodo, num_periodo)

# Fazendo com que seja impresso cada mês do período digitado
for contador in range(len(y)):
    print(f"Após {contador + 1}º período, o montante será de R${y[contador]:.2f}.")


def imprimir_grafico(x, y):
    
    plt.plot(x, y)
    plt.show()
    
x = list(range(num_periodo + 1)) # Transformando o número de períodos em lista
x.pop(0) # Retirando o índice zero, que é igual a zero
eixo_x = x
eixo_y = y

imprimir_grafico(eixo_x, eixo_y)
