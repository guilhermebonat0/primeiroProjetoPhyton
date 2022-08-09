velocidade = int(input("Qual a sua velocidade?\n"));
velocidadeMaxima = 80;

if (velocidade < velocidadeMaxima):
  print("Você não levou multa, continue dirigindo da maneira correta! =)")
elif(velocidade <= velocidadeMaxima + 10):
  print("Levou multa leve! Tome mais cuidado!");
elif(velocidade >= velocidadeMaxima + 11) and (velocidade <= velocidadeMaxima + 20):
  print("Levou multa grave! Tome mais cuidado!");
elif(velocidade > velocidadeMaxima + 20):
  print("Levou multa gravíssima! Tome mais cuidado!");