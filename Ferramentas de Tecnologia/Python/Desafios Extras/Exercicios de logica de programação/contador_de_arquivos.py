import os

# Caminho raiz das pastas contendo os PDFs a serem vistoriados
CAMINHO = "C:\\Users\\valte\\Desktop"

# Função para contar PDFs dentro de uma pasta raiz
def contar_pdfs(caminho: str) -> int :
    """
    Localiza todos os pdfs encontrados em um caminho especifico
    
    Parametros:
    caminho: Caminho da Pasta onde vai ser a busca

    Retorna:
    contador = Total de Pdfs localizados
    """

    contador = 0 # numerar total de pdfs
    
    for pasta, _, arquivos in os.walk(caminho):
        for arqui in arquivos:

            # obtem o caminho do arquivo atual
            caminho_abs = os.path.join(pasta, arqui)

            # separa a extensão do arquivo para checar se é um PDF
            _, ext = os.path.splitext(caminho_abs)
            if (ext.lower() == '.pdf'):
                contador += 1
    return contador

if __name__ == "__main__":
    total = contar_pdfs(CAMINHO)
    print(f"Existem {total} pdfs na pasta informada")
    del total
    exit()