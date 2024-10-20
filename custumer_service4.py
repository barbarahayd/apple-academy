def calc_total(purchase_A, purchase_B, purchase_C):
    
    price_A = 70.50
    price_B = 21.30
    price_C = 80.00

    try:
        qty_A = int(purchase_A)
        qty_B = int(purchase_B)
        qty_C = int(purchase_C)
        
        if qty_A < 0 or qty_B < 0 or qty_C < 0:
            return "ERRO"
    except ValueError:
        return "ERRO"

    # Cálculo valor total da compra
    total = (qty_A * price_A) + (qty_B * price_B) + (qty_C * price_C)
    
    # Arredonda para 2 casas decimais
    total = round(total, 2)

    # Formata o valor com vírgula como separador decimal
    total_formatted = f"R$ {total:.2f}".replace('.', ',')

    # Para que não considere espaços extras antes ou depois do valor
    return total_formatted.strip()

purchase_A = input()
purchase_B = input()
purchase_C = input()

print(calc_total(purchase_A, purchase_B, purchase_C))