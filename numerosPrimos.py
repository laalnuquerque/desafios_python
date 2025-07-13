
def range_primos():

    a = input("Digite um número inteiro: ")
    inicio = valida_num(a)

    b = input("Digite outro número inteiro: ")
    fim =valida_num(b)

    primos = primos_no_intervalo_verificacao(inicio, fim)

    print(primos)

def valida_num(num):
    try:
        int(num)
        return int(num)
    except ValueError:
        num3 = input("Por favor, insira um número inteiro válido: ")
        while not num3.isnumeric() :
           num3 =  input("Por favor, insira um número inteiro válido: ")
        return int(num3)



def eh_primo(numero):
    """
    Verifica se um número é primo.
    """
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True

def primos_no_intervalo_verificacao(inicio, fim):
    """
    Encontra números primos em um intervalo usando a verificação individual.
    """
    primos = []
    print(f"Números primos entre {inicio} e {fim}:")
    for numero in range(inicio, fim + 1):
        if eh_primo(numero):
            primos.append(numero)
    return primos




if __name__ == '__main__':
    range_primos()


# Nível: Intermediário
# Descrição:
# Crie uma função que receba dois números inteiros a e b, e retorne todos os números primos nesse intervalo.
#
# Exemplo de entrada: a = 10, b = 30
# Saída esperada: [11, 13, 17, 19, 23, 29]