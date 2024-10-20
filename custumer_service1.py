import re

def custumer_service(client_input):
    # Verifica se a entrada é uma string válida (não vazia, não só números, não só símbolos)
    if isinstance(client_input, str) and client_input.strip() != "":
        # Remove espaços em branco no início e no final
        client_input = client_input.strip()
        
        # Verifica se a entrada é uma sequência de números ou símbolos sem sentido
        if client_input.isdigit() or re.match(r'^[\W_]+$', client_input):
            return "ERRO"
        return "Ola, em que posso ajudar?"
    
    return "ERRO"

# Leitura da entrada
client_input = input().strip()

# Chamada da função e impressão da resposta
print(custumer_service(client_input))