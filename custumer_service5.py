import datetime

def check_releases(query_date):
  books = [
    {'name': 'A', 'release': '08/04/2024'},
    {'name': 'B', 'release': '12/03/2023'},
    {'name': 'C', 'release': '22/09/2025'},
    {'name': 'D', 'release': '18/01/2025'},
    {'name': 'E', 'release': '04/06/2023'},
  ]

  try:
    query_date = datetime.datetime.strptime(query_date, '%d/%m/%Y')
  except ValueError:
    return "ERROR"

  released_books = [book for book in books if datetime.datetime.strptime(book['release'], '%d/%m/%Y') <= query_date]

  # Sort by release date
  released_books.sort(key=lambda book: datetime.datetime.strptime(book['release'], '%d/%m/%Y'))

  return ', '.join(book['name'] for book in released_books) or "NENHUM"

# Entrada da data de consulta
query_date = input("Digite a data da consulta (DD/MM/AAAA): ")

# Chamar a função e imprimir o resultado
result = check_releases(query_date)
print(result)
