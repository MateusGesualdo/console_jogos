# Usando o Github, crie um protótipo de um console de jogos. Ele deve exibir um menu com os jogos disponíveis e perguntar ao usuário qual deles deseja jogar. Se a resposta for válida, o jogo correspondente deve ser executado

from adivinhacao_numeros import advinhacao
from jokenpo import jogo_jokenpo
from quiz import quiz 

print("Bem vindo ao console de jogos em Python!")

menu = '''
Escolha o número referente ao jogo que deseja jogar:

1 - Adivinhação de números
2 - Jokenpo (Pedra, Papel ou Tesoura)
3 - Perguntas e respostas
'''

entrada_usuario = input(menu)

if entrada_usuario == "1":
  advinhacao()
elif entrada_usuario == "2":
  jogo_jokenpo()
elif entrada_usuario == "3":
  quiz()