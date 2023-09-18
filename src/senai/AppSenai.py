import jvdeamo.Calc as Calc
import random
import os
'''
Autor: João Victor Martins Deamo
Date: 16/09/2023
Time: 00:00
IDE: Visual Studio Code
Session Duration: 00:00 - 
Subject: Python
Version: 1.4
Senai - Desenvolvimento de Sistemas

'''
def clear_screen():
    os.system('cls')
def welcome_message():
    print("Seja bem-vindo(a) ao App Senai!")
def iniciar():
    clear_screen()
    welcome_message()
    try:
        while True:
            entrar = int(input("Pressione 1 para ou 0 para sair... "))
            clear_screen()
            if entrar == 1:
                menu()
            elif entrar == 0:
                print("Software encerrado!")
                
                break
            else:
                print("Opção inválida!")
    except ValueError:
        print("Entrada inválida.")        
def menu():
    clear_screen()
    welcome_message()
    try:
        while True:
            print("Menu principal: ")
            print("1 - Calculadora")
            print("2 - Jogos")
            print("3 - Sair")
            opcao = int(input("Digite a opção: "))
            clear_screen()
            if opcao == 1:
                calculadora_menu()
            elif opcao == 2:
                jogos_menu()
            elif opcao == 3:
                print("Software encerrado!")
                
                break   
            else:
                print("Opção inválida!")
    except ValueError:
            print("Entrada inválida.")   
def calculadora_menu():
    while True:
        try:
            print("Calculadora:")
            print("1 - Calculadora de matriz")
            print("2 - Calculadora geométrica")
            print("3 - Calculadora de palíndromo")
            print("4 - Calculadora de fatorial")
            print("5 - Calculadora de vogais")
            print("6 - Conversor de temperatura")
            print("7 - Verificar se o número é primo")
            print("8 - Voltar ao menu principal")

            opcao = int(input("Digite a opção: "))
            clear_screen()
            
            if opcao == 1:
                calculadoraMatriz_menu()
            elif opcao == 2:
                calculadoraGeometrica_menu()
            elif opcao == 3:
                calculadoraPalavras_menu()
            elif opcao == 4:
                calculadoraFatorial_menu()
            elif opcao == 5:
                calculadoraVogais_menu()
            elif opcao == 6:
                calculadoraTemperatura_menu()
            elif opcao == 7:
                calculadoraPrimos_menu()
            elif opcao == 8:
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Entrada inválida.")
def calculadoraMatriz_menu():
    Calc.CalculadoraMatriz()
    while True:
        try:
            print("Que operação deseja fazer?")
            print("1 - Soma")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("5 - Sair")
            opcao = int(input("Digite a opção: "))
            clear_screen()
            if opcao == 1:
                operacao = Calc.SomaMatriz
                descricao = "Soma"
            elif opcao == 2:
                operacao = Calc.SubMatriz
                descricao = "Subtração"
            elif opcao == 3:
                operacao = Calc.MultMatriz
                descricao = "Multiplicação"
            elif opcao == 4:
                operacao = Calc.DivMatriz
                descricao = "Divisão"
            elif opcao == 5:
                break
            if opcao in [1, 2, 3, 4]:
                resultado = operacao(Calc.matriz1, Calc.matriz2)
                print(f"Resultado da {descricao}:")
                for row in resultado:
                    print(row)
            else:
                print("Opção inválida!")     
        except ValueError:
            print("Entrada inválida.")    
def calculadoraGeometrica_menu():
    while True:
        try:
            print("Que forma geométrica deseja calcular a área?")
            print("1 - Círculo")
            print("2 - Triângulo")
            print("3 - Retângulo")
            print("4 - Sair")
            opcao = int(input("Digite a opção: "))
            clear_screen()
            if opcao == 1:
                Calc.CirculoGeometria()
            elif opcao == 2:
                Calc.TrianguloGeometria()
            elif opcao == 3:
                Calc.RetanguloGeometria()
            elif opcao == 4:
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Entrada inválida.")
def calculadoraPalavras_menu():
    while True:
        try:
            print("Que operação deseja fazer?")
            print("1 - Verificar se é palíndromo")
            print("2 - Sair")
            opcao = int(input("Digite a opção: "))
            clear_screen()

            if opcao == 1:
                Calc.Palindromo()
            elif opcao == 2:
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Entrada inválida.")  
def calculadoraFatorial_menu():
    while True:
        try:
            print("Que operação deseja fazer?")
            print("1 - Fatorial")
            print("2 - Sair")
            opcao = int(input("Digite a opção: "))
            clear_screen()

            if opcao == 1:
                Calc.Fatorial()
            elif opcao == 2:
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Entrada inválida.")
def calculadoraVogais_menu():
    while True:
        try:
            print("Que operação deseja fazer?")
            print("1 - Contar vogais")
            print("2 - Sair")
            opcao = int(input("Digite a opção: "))
            clear_screen()

            if opcao == 1:
                Calc.Vogais()
            elif opcao == 2:
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Entrada inválida.")
def calculadoraPrimos_menu():
    while True:
        try:
            print("Que operação deseja fazer?")
            print("1 - Verificar se o número é primo")
            print("2 - Sair")
            opcao = int(input("Digite a opção: "))
            clear_screen()

            if opcao == 1:
                Calc.Numeroprimo()
            elif opcao == 2:
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Entrada inválida.")
def calculadoraTemperatura_menu():
    while True:
        try:
            print("Que conversão deseja fazer?")
            print("1 - Conversor de temperatura")
            print("2 - Sair")
            opcao = int(input("Digite a opção: "))
            clear_screen()

            if opcao == 1:
                Calc.ConversorTemperatura()
            elif opcao == 2:
                break
            else:
                print("Opção inválida!")
        except ValueError:
            print("Entrada inválida.")
def jogos_menu():
    while True:
        try:
            print("Jogos:")
            print("1 - Jogo de adivinhação")
            print("2 - Jogo de dados")
            print("3 - Jogo da velha")
            print("4 - Voltar ao menu principal")

            opcao = int(input("Digite a opção: "))
            clear_screen()
            
            if opcao == 1:
                JogoAdivinhar()
            elif opcao == 2:
                JogoDados()
            elif opcao == 3:
                JogoVelha()
            elif opcao == 4:
                
                menu()
            else:
                print("Opção inválida!")
        except ValueError:
            print("Entrada inválida.")
def JogoAdivinhar():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    try:
        print("Jogo de adivinhação")
        print("Acerte o número secreto entre 1 e 100")
        
        while True:
            numero = int(input("Digite um número: "))
            while numero < 1 or numero > 100:
                print("Número inválido!")
                numero = int(input("Digite o número: "))
            
            if numero == numero_secreto:
                print(f"Você acertou! O número secreto era: {numero_secreto}")
                break
            else:
                print("Você errou!")
                tentativas += 1
                
                if numero > numero_secreto:
                    print("O número secreto é menor!")
                else:
                    print("O número secreto é maior!")
                
                if tentativas == 5:
                    print("Você perdeu!")
                    print(f"O número secreto era: {numero_secreto}")
                    break
    except ValueError:
        print("Entrada inválida.")
def JogoDados():
    print("Jogo de dados")
    print("Em desenvolvimento")
def JogoVelha():
    print("Jogo da velha")
    print("Em desenvolvimento")
def main():
    iniciar()
if __name__ == "__main__":
    main()
