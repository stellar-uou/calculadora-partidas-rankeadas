#calculadora de partidas rankeadas#

nome = input("Digite seu nick: ")

print("Seja bem vindo a calculadora de rankeadas", nome, "!")

vitorias = int(input("Quantas partidas você ganhou? "))

derrotas = int(input("Quantas partidas você perdeu? "))

def calcular_saldo():
    saldo = vitorias - derrotas
    return saldo

def nivel():
    saldo = calcular_saldo()
    
    if saldo <= 10:
        return "ferro"
        
    elif 11 >= saldo <= 20:
        return "bronze"
        
    elif 21 >= saldo <= 50:
        return "prata"
        
    elif 51 >= saldo <= 80:
        return "ouro"
        
    elif 81 >= saldo <= 90:
        return "diamante"
        
    elif 91 >= saldo <= 100:
        return "lendário"
        
    else:
        return "imortal"

nivel_heroi = nivel()

print("O herói tem saldo de", calcular_saldo(), "vitórias e está no rank", nivel_heroi,"!")
