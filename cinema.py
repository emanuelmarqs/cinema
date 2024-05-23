nome = input('Nome:')
idade = input('Idade:')

while True:  #equanto for verdadeiro

    print('LISTA DE FILMES \n')
    filme = ('Sala 1 - A volta dos que não foram. (+18)')
    filme1 = ('Sala 2 - A roda quadrada. (+12)')
    filme2 = ('Sala 3 - Poeira em alto mar. (Livre)')
    filme3 = ('Sala 4 - As tranças do rei careca. (+16)')
    filme4 = ('Sala 5 - A vingança do peixe frito\n (Livre)')

    print(filme)
    print(filme1)
    print(filme2)
    print(filme3)
    print(filme4)

    sala = input("Sala:")

    if sala == 1 and idade >= 18:
        print("Filme escolhido {filme}, bom filme {nome}!")
    elif sala == 2 and idade >= 12:
        print("Filme escolhido {filme1}, bom filme {nome}! ")
    elif sala == 3 and idade > 0:
        print("Filme escolhido {filme2}, bom filme {nome}!")
    elif sala == 4 and idade >= 16:
        print("Filme escolhido {filme3}, bom filme {nome}!")
    elif sala == 5 and idade > 0:
        print("Filme escolhido {filme4}, bom filme {nome}!")
    else: 
        print("Você ainda não pode assistir a esse filme!")

    continuar = input('Você deseja assistir a outro filme (s/n)?')

    if continuar == ('s'):
        continue
    elif continuar == ('n'):
        break
    else:
        print('Opção Inválida!')
        continue