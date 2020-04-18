def growth_rate():
    population_A = 90000000
    population_B = 200000000
    anos = 0
    cresA = 0.03  #Crescimentos 1,5% ao ano
    cresB = 0.015 #Crescimentos 1,5% ao ano

    while (population_A < population_B): #Comparando as variáveis
        anos += 1 #Inicia em 0 e anos + 1 (contagem)
        population_A = population_A + (population_A * cresA) #Calculo percentual de crescimento continuo
        population_B = population_B + (population_B * cresB)
    print("Após %i anos o país A ultrapassou o país B em número de habitantes." % anos) #Exibir resultado

def verifica():  # Testar se é inteiro
    population_A = 90000000
    population_B = 200000000
    if type(population_A and population_B) == int:  # Built-in type compara se a variável é inteira
        return ("As populações {} e {} são inteiros e maior que zero".format(population_A, population_B))
    else:
        return ("Invalid Argument")

print(growth_rate())
print(verifica())