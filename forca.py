import random

def jogar():
  imprime_mensagem_abertura()
  palavra_secreta = carrega_palavra_secreta()

  letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
  print(letras_acertadas)

  enforcou = False
  acertou = False
  erros = 0

  while(not enforcou and not acertou):

    chute = pede_chute()

    if (chute in palavra_secreta):
      marca_chute_correto(chute, letras_acertadas, palavra_secreta)
    else:
      erros =+ 1

    enforcou = erros == 7
    acertou = "_" not in letras_acertadas
    print(letras_acertadas)

  if(acertou):
    imprime_mensagem_vencedor()
  else:
    imprime_mensagem_perdedor(palavra_secreta)

def imprime_mensagem_vencedor():
  print("Você Ganhou!")

def imprime_mensagem_perdedor():
  print("Você perdeu!")

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
          letras_acertadas[index] = letra
        index += 1

def pede_chute():
  chute = input("Qual letra? ")
  chute = chute.strip().upper()
  return chute

def inicializa_letras_acertadas(palavra):
  return ["_" for letra in palavra]

def imprime_mensagem_abertura():
  print("********************************")
  print("***Bem Vindo ao Jogo da Forca***")
  print("********************************")

def carrega_palavra_secreta():
    arquivo = open("palavra.txt", "r")
    palavra = []
    for linha in arquivo:
        linha = linha.strip()
        palavra.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavra))
    palavra_secreta = palavra[numero].upper()
    return palavra_secreta

if(__name__=="__main__"):
    jogar()