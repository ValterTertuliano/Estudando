# link do desafio -> https://www.youtube.com/watch?v=IGl-axkYCr8&list=PLLgKYjEKBqxcIeoikzTNZJtmxjW8eYLM2&index=4

# faça uma função que recebe um numero de 1 a 26
# e retorne um array com as letras do alfabeto

# a biblioteca string já tem todas as letras
import string

def funcao_do_cria(n: int) -> list:
    if n <= 26 and n > 0:
        lista_de_letras = []
        for x in range(n):
            lista_de_letras.append(string.ascii_lowercase[x])

        return lista_de_letras
    print("Informe numeros correspondentes a letras do alfabeto !!!")

if __name__=="__main__":
    
    for n in range(26):
        print(funcao_do_cria(n+1))

    del funcao_do_cria
    del n
    