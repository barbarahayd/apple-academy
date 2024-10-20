import re

accent_map = str.maketrans(    
    'éèêë',
    'eeee'
) #Bárbara

book_stock = ["Jogador Numero 1", "A Divina Comédia", "Dom Casmurro"]

def calc_sum(N):
  birth_year = 1997
  return (N*2) + (birth_year % 100)

def remove_accents(text):
    return text.translate(accent_map)

def customer_service(client_input):  
    client_input = remove_accents(client_input.strip().lower())
    
    if not client_input or client_input.isdigit() or re.match(r'^[\W_]+$', client_input):
        return "ERRO"
    
    normalized_books = [remove_accents(book.lower()) for book in book_stock]
    
    if client_input in normalized_books:
        return "Sim, tenho esse livro!"
    
    return "Infelizmente não tenho esse livro"

client_input = input().strip()
print(customer_service(client_input))