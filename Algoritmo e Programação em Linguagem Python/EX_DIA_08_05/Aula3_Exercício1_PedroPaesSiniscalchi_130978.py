import csv

def output(arquivo_csv):
    sum_soma = 0
    soma_gols = 0
    soma_publico = 0
    contador = 0
    soma_total = 0
    soma_partidas = 0
    pais_champ = 0
    Brasil_quarto = 0
    Franca_terceiro = []
    dicct = {}

    with open(arquivo_csv) as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)

        for lines in reader:
            if len(lines) > 0:
                Ano = lines[0]
                Pais = lines[1]
                Vencedor = lines[2]
                Segundo = lines[3]
                Terceiro = lines[4]
                Quarto = lines[5]
                Gols = lines[6]
                Times = lines[7]
                Jogos = lines[8]
                Publico = lines[9]

                if Ano[-1] == '0':
                    sum_soma += int(Publico.replace('.', ''))

                if int(Ano) >= 1954 and int(Ano) <= 1990:
                    soma_gols += int(Gols)

                soma_publico += int(Publico.replace('.', ''))
                contador += 1

                soma_total += int(Gols)
                soma_partidas += int(Jogos)

                if Pais == Vencedor:
                    pais_champ += 1

                if 'Brazil' in [Vencedor, Segundo, Terceiro, Quarto]:
                    Brasil_quarto += 1

                if 'France' == Terceiro:
                    Franca_terceiro.append(Ano)

                if Vencedor in dicct:
                    dicct[Vencedor] += 1
                else:
                    dicct[Vencedor] = 1

    victory = sorted(dicct.items(), key=lambda x: x[1])
    media_publico = soma_publico / contador
    media_gols_partida = round(soma_total / soma_partidas, 2)

    with open('Resultados.txt', 'w') as txt_result:
        txt_result.write('Soma de público das copas com final 0: {}\n'.format(sum_soma))
        txt_result.write('Quantidade total de gols entre as copas de 1954 e 1990: {}\n'.format(soma_gols))
        txt_result.write('Média de público: {}\n'.format(media_publico))
        txt_result.write('Média de gols por partida: {}\n'.format(media_gols_partida))
        txt_result.write('Quantidade de vezes em que o país sede foi campeão: {}\n'.format(pais_champ))
        txt_result.write('Quantidade de vezes em que o time do Brasil ficou entre uma das 4 primeiras posições: {}\n'.format(Brasil_quarto))
        txt_result.write('Ano das edições em que o time da França finalizou em terceiro lugar: {}\n'.format(','.join(Franca_terceiro))
        txt_result.write('Quantidade de vitórias por país, classificada em ordem crescente do número de títulos:\n')

        for winners in victory:
            txt_result.write('\t{}:{}\n'.format(winners[0], winners[1]))

        output('WorldCups.csv')




