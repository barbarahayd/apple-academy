def main():
    try:
        input_line = input().strip()

        quantity = int(input_line)
        
        if quantity <= 0:
            print("ERRO")
            return

        num_C = quantity // 24
        remainder = quantity % 24

        num_B = remainder // 12
        remainder = remainder % 12

        num_A = remainder // 4
        remainder = remainder % 4

        # Se houver resto, significa que a quantidade não pode ser atendida
        if remainder != 0:
            print("ERRO")
            return

        # Formata e imprime a saída com espaços entre as embalagens
        print(f"A({num_A}) B({num_B}) C({num_C})")

    except ValueError:
        # Se ocorrer erro ao converter a entrada para inteiro, imprime ERRO
        print("ERRO")

if __name__ == "__main__":
    main()