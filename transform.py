def gerar_mensagem(usuario):

    nome = usuario["Nome"]
    conta = usuario["Conta"]
    cartao = usuario["Cartao"][-4:]

    mensagem = (
        f"Olá {nome}, sua conta {conta} foi processada com sucesso. "
        f"Cartão final {cartao}."
    )

    return {
        "Nome": nome,
        "Conta": conta,
        "Mensagem": mensagem
    }
