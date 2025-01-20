def converter_medida(unidade_destino, unidade_origem, valor):
    escala_medidas = {
        "km": 1,
        "hm": 2,
        "dam": 3,
        "m": 4, 
        "dm": 5,
        "cm": 6,
        "mm": 7
    }

    diferenca_escala = escala_medidas[unidade_destino] - escala_medidas[unidade_origem]

    for _ in range(abs(diferenca_escala)):
        if diferenca_escala > 0:  # Se positivo, aumenta a escala
            valor *= 10
        else:  # Se negativo, diminui a escala
            valor /= 10

    return valor

def main():
    origem = input("Informe a UNIDADE DE MEDIDA que está sendo passada: ")
    destino = input("Informe a UNIDADE DE MEDIDA que você quer receber: ")
    valor = float(input("Informe o valor de medida: "))
    calcular_conversao = converter_medida(destino, origem, valor)

    print("Iniciando conversão...")
    print(f"{valor} {origem}")
    print("Está sendo convertido...")
    print(f'{calcular_conversao:,.2f} {destino}')

    return calcular_conversao

if __name__ == "__main__":
    main()
