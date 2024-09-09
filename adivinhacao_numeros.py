import random

def advinhacao():
  alvo = random.randint(0, 100)
  tentativas = 5
  print("JOGO DE ADVINHÇÃO")
  ganhou = False

  while tentativas > 0:
    tentativas -= 1
    print(f"Tentativas restantes: {tentativas}")##
    try:
      alvo = int(input("Digite um número entre 1 e 100: "))
      if chute == alvo:
          print("Parabéns! Você acertou!")
          ganhou = True
          break
      elif chute < alvo:
            print("Tente um número maior.")
      else:
          print('tente um número menor.')

        tentativas == tentativas - 1
    except ValueError:
      if chute < 0 or chute > 100:
        print("Por favor, digite um número válido.")
      elif alvo == str:
        print ("saindo...")
        break


      if tentativas == 0:
        print('Fim de jogo')
        if ganhou = False:
      print(f"Você perdeu! O número alvo era {alvo}.")
    except vallueError:
        break