import mercadopago

# Adicione suas credenciais
sdk = mercadopago.SDK("APP_USR-2950190329009440-120114-f383923769d583cd9c714c610a3c40f0-1181482628")

# Configuração dos dados do item
preference_data = {
    "items": [
        {
            "title": "Pão Pizza",
            "quantity": 1,
            "unit_price": 1
        }
    ]
}

# Criação da preferência
try:
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]

    # Exibir o link de pagamento
    print("Link de pagamento:", preference["init_point"])
except Exception as e:
    print("Erro ao criar a preferência:", e)
