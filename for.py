def enviar_email(cliente):
    print(f"Email enviado para {cliente}")

clientes = ["João", "Maria", "Pedro"]

for i,cliente in enumerate(clientes):
    if i == 1:
        break
    enviar_email(cliente)

for x,cliente in enumerate(clientes):
    if x == 2:
        break
    enviar_email(cliente)
