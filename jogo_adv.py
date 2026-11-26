import random

print("=== ESCOLHA A DIFICULDADE ===")
print("  Fácil   (1 a 10)")
print("  Médio   (1 a 100)")
print("  Difícil (1 a 1000)")
print("=============================")

while True:
  opcao = input("Sua escolha: ").strip()

  if opcao == "1":
    limite = 10
    break
  elif opcao == "2":
    limite = 100
    break
  elif opcao == "3":
    limite = 1000
    break
  else:
    print("Digite 1, 2 ou 3")

numero = random.randint(1, limite)

while True:
  palpite = int(input("Digite seu palpite: "))
  if palpite > numero:
    print("O número é menor")
  elif palpite < numero:
    print("O número é maior")
  else:
    print(f"Parabéns você acertou!, {numero} era o número")
    break
