import random


aleatorias = ["Sintaxe", "Sequência", "Estritamente", "concatenação", "unária", "Inteligência", "Respeito",
              "Teclado", "Software", "Aprendizado", "Identação", "Algoritmo", "Programação", "Autoconhecimento",
              "Condicional", "Webnar", "Hardware", "Desenvolvimento", "Atribuição", "Escopo", "marisa"]

fim_do_jogo = False

lista_jogadores = []


def pegar_quantidade_de_jogadores():
    while True:
        quantidade_jogadores = int(input('quantas pessoas vão jogar? (de 2 a 5 jogadores)'))
        if 2 <= quantidade_jogadores <= 5:
            return quantidade_jogadores
        print('digite uma opção válida.')

def pegar_nome_dos_jogadores(quantidade_jogadores):
    for i in range(quantidade_jogadores):
        nome_do_jogador = input('Digite o nome do jogador:')
        lista_jogadores.append({'jogador':nome_do_jogador, 'erro': 0})
    return lista_jogadores


def escolher_palavra_aleatoria():   #Função que escolhe uma palavra aleatória (random.choice) no banco de palavras
    palavra1 = random.choice(aleatorias)
    return palavra1

def atribuir_palavra_jogador():
    for i in range(len(lista_jogadores)):
        lista_jogadores[i].update(palavra_secreta=escolher_palavra_aleatoria())


def pegar_opcao_jogador():
    while True:
        opcao = int(input("Selecione uma opção\n 1 - ler a historia do jogo \n 2 - "
                        "escolher quantidade de jogadores \nDigite 1 ou 2 :"))
        if 1 <= opcao <= 2:
            return opcao
        print('digite uma opção válida')

def selecao_jogo(opcao):
    if opcao == 1:
        print(historia_do_jogo())

    elif opcao == 2:
        quantidades_de_jogadores = pegar_quantidade_de_jogadores()
        nome_jogadores = pegar_nome_dos_jogadores(quantidades_de_jogadores)
        atribuir_palavra_jogador()



def historia_do_jogo():
    print(" _    _   _   _   _     _____   _   _____   ______   _____   ____   _____")
    print("| \  / | | | | | | |   |_   _| | | | ___ | |  __  | |  ___| |  __| |     |")
    print("| _\/_ | | |_| | | |__   | |   | | | ___|  | |__| | |   \_  | |__  |  _  |")
    print("|_|  |_| |_____| |____|  |_|   |_| |_|     |______| |_|\__| |____| |_| |_|")
    print('=' * 150)
    print('SEJAM BEM VINDOS AO JOGO DA FORCA:')
    print('=' * 150)
    print('As origens do JOGO DA FORCA são obscuras, significando não descoberto, mas parece ter surgido na época vitoriana ”, ')
    print('diz Tony Augarde, autor de The Oxford Guide to Word Games.')
    print('O jogo é mencionado em “Jogos tradicionais” de Alice Bertha Gomme em 1894 sob o nome de “Pássaros,')
    print('feras e peixes”. As regras são simples; um jogador escreve a primeira e a')
    print('última letras de uma palavra e outro jogador adivinha as letras intermediárias. Em outras fontes,')
    print('O jogo é chamado de “Gallows”, “The Game of Hangin” ou “Hanger”.')
    print('=' * 150)
    print('Implementação:')
    print('=' * 150)
    print('Este é um jogo Hangman simples usando a linguagem de programação Python. ')
    print('Iniciantes podem usar isso como um pequeno projeto para aumentar suas habilidades de programação e compreensão da lógica.')
    print('=' * 150)
    opcao_jogador = pegar_opcao_jogador()
    selecao_jogo(opcao_jogador)


def pegarletra():
    chute = input("Escolha uma letra?").upper().strip()
    return chute

def letrasacertadas():
    for i in range(len(lista_jogadores)):
        palavradavez = lista_jogadores[i]['palavra_secreta']
        letras_acertadas = ["_"]* (len(palavradavez))
        lista_jogadores[i].update(letras_acertadas = letras_acertadas)

def perdeu():
    global fim_do_jogo
    print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
    print(' ░░░░░░░░░░ \033[7;30mVOCÊ PERDEU\033[m ░░░░░░░░░░░')
    print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
    print()
    fim_do_jogo = True


def ganhou():
    global fim_do_jogo
    global vez
    print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
    print(' ░░░░░░░░░░ \033[7;30mVOCÊ GANHOU!\033[m ░░░░░░░░░░░')
    print('●▬▬▬▬▬▬▬▬▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬▬▬▬▬▬▬▬▬●')
    print()
    fim_do_jogo = True




def rodarforca():
    global fim_do_jogo
    vez = 0


    while fim_do_jogo == False:
        print(lista_jogadores[vez]['letras_acertadas'])
        chute = pegarletra()
        palavradavez = lista_jogadores[vez]['palavra_secreta']
        if chute in palavradavez.upper():
            index = 0
            for letra in palavradavez:

                if chute == letra.upper():
                    lista_jogadores[vez]['letras_acertadas'][index] = letra

                index += 1

            if '_' not in lista_jogadores[vez]['letras_acertadas']:
                print(lista_jogadores[vez]['letras_acertadas'])
                print('você ganhou!')
                ganhou()

        else:
            print(f'você errou, vez do próximo jogador:')
            lista_jogadores[vez]['erro'] += 1
            if lista_jogadores[vez]['erro'] == 6:
                print('você perdeu playboy')
                print(f' A Palavra era : {lista_jogadores[vez]["palavra_secreta"]}')

                perdeu()
            else:
                vez += 1
                if vez >= len(lista_jogadores):
                    vez = 0



def jogar():
    opcao_jogador = pegar_opcao_jogador()
    selecao_jogo(opcao_jogador)
    letrasacertadas()
    rodarforca()
jogar()



'''def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()'''

