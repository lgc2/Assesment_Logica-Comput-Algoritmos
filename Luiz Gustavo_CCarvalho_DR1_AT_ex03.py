def saude_financeira(renda, gastos_moradia, gastos_educacao, gastos_transporte):
    per_gastos_moradia = round((gastos_moradia / renda) * 100, 2)
    per_gastos_educacao = round((gastos_educacao / renda) * 100, 2)
    per_gastos_transporte = round((gastos_transporte / renda) * 100, 2)
    max_moradia = renda * 0.30
    max_educacao = renda * 0.20
    max_transporte = renda * 0.15
    
    if per_gastos_moradia <= 30:
        print(f"Seus gastos totais com moradia comprometem {per_gastos_moradia}% de sua renda total. O máximo recomendado é 30%. Seus gastos estão dentro da margem recomendada.")
    else:
        print(f"Seus gastos totais com moradia comprometem {per_gastos_moradia}% de sua renda total. O máximo recomendado é 30%. Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {max_moradia}.")
    if per_gastos_educacao <= 20:
        print(f"Seus gastos totais com educação comprometem {per_gastos_educacao}% de sua renda total. O máximo recomendado é 20%. Seus gastos estão dentro da margem recomendada.")
    else:
        print(f"Seus gastos totais com educação comprometem {per_gastos_educacao}% de sua renda total. O máximo recomendado é 20%. Portanto, idealmente, o máximo de sua renda comprometida com educação deveria ser de R$ {max_educacao}.")
    if per_gastos_transporte <= 15:
        print(f"Seus gastos totais com transporte comprometem {per_gastos_transporte}% de sua renda total. O máximo recomendado é 15%. Seus gastos estão dentro da margem recomendada.")
    else:
        print(f"Seus gastos totais com transporte comprometem {per_gastos_transporte}% de sua renda total. O máximo recomendado é 15%. Portanto, idealmente, o máximo de sua renda comprometida com transporte deveria ser de R$ {max_transporte}.")
    
renda = float(input("Renda mensal total: "))
gastos_moradia = float(input("Gastos totais com moradia: "))
gastos_educacao = float(input("Gastos totais com educação: "))
gastos_transporte = float(input("Gastos totais com transporte: "))

print("Diagnóstico:")
saude_financeira(renda, gastos_moradia, gastos_educacao, gastos_transporte)
