import re

def customer_service(client_input, hour):  # A função primeiro verifica se client_input é uma string não vazia
    if isinstance(client_input, str) and client_input.strip() != "": # Remove quaisquer espaços em branco no início ou no final de client_input.

        client_input = client_input.strip()
        if client_input.isdigit() or re.match(r'^[\W_]+$', client_input): # Verifica se a string contém apenas dígitos ou símbolos não alfanuméricos.
            return "ERRO"
        
        # Verifica hora para retorno da saudação apropriada
        if 5 <= hour <= 11:
            greeting = "Bom dia"
        elif 12 <= hour <= 18:
            greeting = "Boa tarde"
        else:
            greeting = "Boa noite"
        
        return f"{greeting}, em que posso ajudar?"
      
    return "ERRO" # Se a validação inicial da entrada falhar, a função retorna "ERRO"

try:
    client_input = input().strip() # Lê a entrada do usuário e remove espaços em branco no início e no final.
    hour = int(input().strip())
    print(customer_service(client_input, hour))
except ValueError: # Se a entrada para hour não for um inteiro válido, captura o ValueError e imprime "ERRO".
    print("ERRO")