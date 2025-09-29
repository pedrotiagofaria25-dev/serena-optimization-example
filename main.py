
"""
Exemplo de código Python não otimizado para análise do Serena.
"""

def process_data(data):
    """
    Processa uma lista de números, realizando cálculos ineficientes.
    """
    total = 0
    for i in range(len(data)):
        total += data[i]
    
    average = total / len(data)
    
    squares = []
    for x in data:
        squares.append(x*x)
    
    return total, average, squares

def main():
    """
    Função principal para executar o processamento de dados.
    """
    sample_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total, average, squares = process_data(sample_data)
    
    print(f"Total: {total}")
    print(f"Média: {average}")
    print(f"Quadrados: {squares}")

if __name__ == "__main__":
    main()

