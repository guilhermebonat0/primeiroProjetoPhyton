'''
Dados de entrada: n = numero a ser fatorado;
multiplicar o numero atual pelo seu anterior (5! = 5.4.3.2.1 = 120)
Só podem numeros inteiros positivos como valor de entrada
resultado esperado é o valor total do numero fatorado
'''
numero = int(input("Digite um numero a ser fatorado: \n"))
fatorial = 1;
if numero > 0:
  for item in range(1, numero + 1):
    fatorial = fatorial * item
    print(item, fatorial)
print(fatorial)