def enviar_email(nome,email):
    nome_dest = nome
    email_dest = email
    return f"Email enviado para {nome_dest} no endereço {email_dest}"


pessoas = [
    {
        "nome": "João",
        "email": "joao@gmail.com",

    },
    {
        "nome": "Maria",
        "email": "maria@gmail.com",
    },
    {
        "nome": "Pedro",
        "email": "pedro@gmail.com"
    }
]

for pessoa in pessoas:
    email_enviado = enviar_email(pessoa["nome"], pessoa["email"])
    print(email_enviado)
