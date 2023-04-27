from time import sleep
import os

notas = {}


def adicionar_aluno(nome):
    if nome in notas:
        print(
            f'{nome} já está cadastrado na lista de alunos.\nTente Novamente!')
    else:
        notas[nome] = []
        print(f'{nome} foi adicionado com sucesso a lista de alunos!')


def adicionar_nota(nome):
    if nome in notas:
        nota = int(input('Qual a nota que será adicionada? '))
        if len(notas[nome]) < 3:
            notas[nome].append(nota)
            print('Nota adicionada com sucesso')
        else:
            print(
                f'{nome} já possui 3 notas cadastradas!\nA nota não foi adicionada!'
            )
    else:
        print(
            f'{nome} não está casatrado na lista de alunos.\nTente Novamente!')


def remover_aluno(nome):
    if nome in notas:
        del notas[nome]
        print(f'{nome} foi removido da lista de alunos!')
    else:
        print(
            f'{nome} não está cadastrado na lista de alunos.\nTente Novamente!'
        )


def remover_nota(nome):
    if nome in notas:
        nota = int(input('Qual a nota será deletada? (1ª, 2ª ou 3ª) '))
        if nota == 1:
            notas[nome].pop(0)
            print(f'A 1ª nota de {nome} foi excluída!')
        elif nota == 2:
            notas[nome].pop(1)
            print(f'A 2ª nota de {nome} foi excluída!')
        elif nota == 3:
            notas[nome].pop(2)
            print(f'A 3ª nota de {nome} foi excluída!')
        else:
            print('Opção de nota Inválida!\nTente Novamente!')
    else:
        print(
            f'{nome} não está cadastrado na lista de alunos!\nTente Novamente')


def editar_nome_aluno(nome):
    if nome in notas:
        novo_nome = input(f'O nome {nome} será alterado para qual nome? ')
        notas[novo_nome] = notas[nome].copy()
        print(f'O nome de {nome} foi alterado para {novo_nome}')
        del notas[nome]
    else:
        print(f'{nome} não está cadstrado na lista de alunos')


def editar_nota_aluno(nome, nota):
    if nome in notas:
        nova_nota = int(input('Qual a nova nota?'))
        if nota == 1:
            notas[nome][0] = nova_nota
            print(f'A {int(nota)}ª nota foi substuida pela nota {nova_nota}')
        elif nota == 2:
            notas[nome][1] = nova_nota
            print(f'A {int(nota)}ª nota foi substuida pela nota {nova_nota}')
        elif nota == 3:
            notas[nome][2] = nova_nota
            print(f'A {int(nota)}ª nota foi substuida pela nota {nova_nota}')
        else:
            print(f'Não existe a {nota}ª nota!\nTente Novamente')
    else:
        print(
            f'{nome} não está cadastrado na lista de alunos!\nTente Novamente!'
        )


def buscar_aluno(nome):
    nomes = 0
    for aluno in notas:
        if nome in aluno:
            nota1 = notas[aluno][0]
            nota2 = notas[aluno][1]
            nota3 = notas[aluno][2]
            print(
                f'{aluno}:\n\n  1ª Nota: {nota1:.1f} |  2ª Nota: {nota2:.1f} | 3ª Nota: {nota3:.1f} | Média: {(nota1+nota2+nota3)/3:.1f}\n'
            )
            sleep(0.5)
            nomes += 1
    if nomes == 0:
        print(
            f'{nome} não está cadastrado na lista de alunos!\nTente Novamente!'
        )


def calcular_media_turma():
    soma_total = 0
    for aluno in notas:
        nota1 = notas[aluno][0]
        nota2 = notas[aluno][1]
        nota3 = notas[aluno][2]
        media = (nota1 + nota2 + nota3) / 3
        soma_total += media
    media_total = soma_total / len(notas)
    print(f'A média da turma é de {media_total:.1f}')


def exibir_melhor_aluno():
    maior = 0
    melhor_aluno = ' '
    for aluno in notas:
        nota1 = notas[aluno][0]
        nota2 = notas[aluno][1]
        nota3 = notas[aluno][2]
        media = (nota1 + nota2 + nota3) / 3
        if media > maior:
            maior = media
            melhor_aluno = aluno
    print(f'O melhor aluno foi {melhor_aluno} com média {maior}')


def exibir_alunos_ordem_alfabetica():
    alunos = list(notas.keys())
    alunos.sort()
    c = 1
    for aluno in alunos:
        print(f'{c}. {aluno}:')
        nota1 = notas[aluno][0]
        nota2 = notas[aluno][1]
        nota3 = notas[aluno][2]
        print(
            f'\n      1ª Nota: {nota1:.1f} |  2ª Nota: {nota2:.1f} | 3ª Nota: {nota3:.1f} | Média: {(nota1+nota2+nota3)/3:.1f}\n'
        )
        sleep(0.5)
        c += 1


def exibir_aluno_ordem_nota():
    medias = []
    dados = []
    lista = []
    for aluno in notas:
        nota1 = notas[aluno][0]
        nota2 = notas[aluno][1]
        nota3 = notas[aluno][2]
        media = (nota1 + nota2 + nota3) / 3
        dados.append(aluno)
        dados.append(media)
        medias.append(dados[:])
        del dados[:]
    medias.sort()
    for n in medias:
        lista.append(n[1])
    lista.sort(reverse=True)
    valor = 0
    tentativa = 0
    while True:
        if lista[0] == medias[valor][1]:
            print(f'{tentativa+1}. {medias[valor][0]}:\n')
            sleep(0.1)
            print(
                f'\n      1ª Nota: {notas[medias[valor][0]][0]} |  2ª Nota: {notas[medias[valor][0]][1]} |  2ª Nota: {notas[medias[valor][0]][2]} | Média: {(notas[medias[valor][0]][0]+notas[medias[valor][0]][1]+notas[medias[valor][0]][2])/3:.1f}\n'
            )
            sleep(0.5)
            del lista[0]
            del medias[valor]
            tentativa += 1
        else:
            valor += 1
        if valor >= len(medias):
            valor = 0
        if tentativa == len(notas):
            break


def exibir_alunos_aprovados():
    c = 1
    for aluno in notas:
        nota1 = notas[aluno][0]
        nota2 = notas[aluno][1]
        nota3 = notas[aluno][2]
        media = (nota1 + nota2 + nota3) / 3
        if media >= 7:
            print(f'{c}. {aluno}:')
            print(
                f'\n      1ª Nota: {nota1:.1f} |  2ª Nota: {nota2:.1f} | 3ª Nota: {nota3:.1f} | Média: {media:.1f}\n'
            )
            sleep(0.5)
            c += 1


def exibir_alunos_final():
    c = 1
    for aluno in notas:
        nota1 = notas[aluno][0]
        nota2 = notas[aluno][1]
        nota3 = notas[aluno][2]
        media = (nota1 + nota2 + nota3) / 3
        if 7 > media >= 5:
            print(f'{c}. {aluno}:')
            print(
                f'\n      1ª Nota: {nota1:.1f} |  2ª Nota: {nota2:.1f} | 3ª Nota: {nota3:.1f} | Média: {media:.1f}\n'
            )
            sleep(0.5)
            c += 1


def exibir_alunos_reprovados():
    c = 1
    for aluno in notas:
        nota1 = notas[aluno][0]
        nota2 = notas[aluno][1]
        nota3 = notas[aluno][2]
        media = (nota1 + nota2 + nota3) / 3
        if media < 5:
            print(f'{c}. {aluno}:')
            print(
                f'\n      1ª Nota: {nota1:.1f} |  2ª Nota: {nota2:.1f} | 3ª Nota: {nota3:.1f} | Média: {media:.1f}\n'
            )
            sleep(0.5)
            c += 1


opçoes = [
    '[ 1 ] Adicionar Aluno', '[ 2 ] Adicionar Nota', '[ 3 ] Remover Aluno',
    '[ 4 ] Remover Nota', '[ 5 ] Editar Nome Do Aluno',
    '[ 6 ] Editar Nota Do Aluno', '[ 7 ] Buscar Aluno Por Nome',
    '[ 8 ] Calcular Média da Turma', '[ 9 ] Exibir Melhor Aluno',
    '[ 10 ] Exibir Alunos Em Ordem Alfabética',
    '[ 11 ] Exibir Alunos em Ordenados Por Nota',
    '[ 12 ] Exibir Aluno Aprovados Por Média', '[ 13 ] Exibir Alunos Na Final',
    '[ 14 ] Exibir Alunos Reprovados'
]

while True:

    print('-=-' * 30)
    print()
    sleep(0.05)
    print('{:^92}'.format(
        '\033[4m-  E S C O L I N H A   D O   J E M Ã O  -\033[0m\n'))
    print('-=-' * 30)
    print()

    for opçao in range(len(opçoes)):
        if opçao % 2 == 0:
            sleep(0.05)
            print(f'{opçoes[opçao]:<45}', end='')
        else:
            sleep(0.05)
            print(f'{opçoes[opçao]}\n')

    print(f'\n{"[ 15 ] Encerrar Programa":^75}\n')

    print('-=-' * 30)

    operaçao = int(input('Escolha uma opção: '))

    if operaçao == 1:
        nome = input('Qual nome do novo aluno? ').title()
        adicionar_aluno(nome)
    elif operaçao == 2:
        nome = input('A nota será adicionada para qual aluno? ').title()
        adicionar_nota(nome)
    elif operaçao == 3:
        nome = input('Qual Aluno será Removido? ').title()
        remover_aluno(nome)
    elif operaçao == 4:
        nome = input('Qual aluno terá a nota removida? ').title()
        remover_nota(nome)
    elif operaçao == 5:
        nome = input('Qual aluno terá o nome editado? ').title()
        editar_nome_aluno(nome)
    elif operaçao == 6:
        nome = input('Qual aluno terá a nota editada? ').title()
        nota = float(input('Qual nota será alterada? (1ª, 2ª ou 3ª)'))
        editar_nota_aluno(nome, nota)
    elif operaçao == 7:
        nome = input('Deseja visualizar as notas de qual aluno? ').title()
        buscar_aluno(nome)
    elif operaçao == 8:
        calcular_media_turma()
    elif operaçao == 9:
        exibir_melhor_aluno()
    elif operaçao == 10:
        exibir_alunos_ordem_alfabetica()
    elif operaçao == 11:
        exibir_aluno_ordem_nota()
    elif operaçao == 12:
        exibir_alunos_aprovados()
    elif operaçao == 13:
        exibir_alunos_final()
    elif operaçao == 14:
        exibir_alunos_reprovados()
    elif operaçao == 15:
        print('Programa encerrado!')
        break
    else:
        print('Opção invalida\nTente Novamente')
    limpar = input('Pressione a tecla enter para voltar ao menu!')
    os.system('clear')
