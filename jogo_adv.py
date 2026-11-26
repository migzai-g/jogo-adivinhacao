import random

DIFICULDADES = {"1": 10, "2": 100, "3": 1000}


def escolher_limite():
    print("=== ESCOLHA A DIFICULDADE ===")
    print("  1 - Fácil   (1 a 10)")
    print("  2 - Médio   (1 a 100)")
    print("  3 - Difícil (1 a 1000)")
    print("=============================")
    while True:
        opcao = input("Sua escolha: ").strip()
        if opcao in DIFICULDADES:
            return DIFICULDADES[opcao]
        print("Digite 1, 2 ou 3.")


def ler_palpite(limite):
    while True:
        texto = input("Digite seu palpite: ").strip()
        if not texto.isdecimal():
            print("Digite só números inteiros.")
            continue
        palpite = int(texto)
        if not 1 <= palpite <= limite:
            print(f"O número está entre 1 e {limite}.")
            continue
        return palpite


def jogar():
    limite = escolher_limite()
    numero = random.randint(1, limite)
    tentativas = 0

    while True:
        palpite = ler_palpite(limite)
        tentativas += 1
        if palpite > numero:
            print("O número é menor.")
        elif palpite < numero:
            print("O número é maior.")
        else:
            print(f"Parabéns, você acertou! Era o {numero}, em {tentativas} tentativa(s).")
            return


jogar()