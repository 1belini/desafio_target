def fibonacci(n):
    sequencia = [0, 1]
    while sequencia[-1] < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia

def pertence(number):
    sequence = fibonacci(number)
    if number in sequence:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} não pertence à sequência de Fibonacci."


numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
print(pertence(numero))