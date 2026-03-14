import csv

def extrair_dados(caminho_arquivo):
    usuarios = []

    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            usuarios.append(linha)

    return usuarios
