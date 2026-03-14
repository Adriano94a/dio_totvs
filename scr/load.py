import csv
from extract import extrair_dados
from transform import gerar_mensagem


def salvar_resultado(caminho_saida, dados_transformados):

    with open(caminho_saida, mode="w", newline="", encoding="utf-8") as arquivo:
        campos = ["Nome", "Conta", "Mensagem"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(dados_transformados)


def main():

    caminho_entrada = "../data/usuarios.csv"
    caminho_saida = "../data/mensagens_geradas.csv"

    usuarios = extrair_dados(caminho_entrada)

    resultados = [gerar_mensagem(usuario) for usuario in usuarios]

    salvar_resultado(caminho_saida, resultados)

    print("Pipeline ETL executado com sucesso!")


if __name__ == "__main__":
    main()
