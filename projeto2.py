import random;

numRandom = random.randrange(1,10)
acertou = False;

while acertou == False :
  numero = int(input("Digite um numero:\n\n"));
  if numero < numRandom:
    print("O valor digitado é inferior ao numero random, tente novamente! =)")  
  
  elif numero > numRandom:
    print("O valor digitado é superior ao numero random, tente novamente! =)")
  elif numero == numRandom:
    acertou = True;
    print("Você acertou! O numero sorteado foi:", numRandom)

