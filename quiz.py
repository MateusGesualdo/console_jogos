def quiz():
  pergunta = "Qual é a capital do Brasil?"
  resposta_correta = "Brasília"

  print(pergunta)
  resposta = input("Sua resposta: ")

  if resposta.lower() == resposta_correta.lower():
      print("Correto!")
  else:
      print(f"Errado! A resposta correta é {resposta_correta}")  

mensagem = "Oi, turma!"