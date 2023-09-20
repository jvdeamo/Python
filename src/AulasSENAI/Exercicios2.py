import os
import time

'''
Autor: João Victor Martins Deamo
Date: 18/09/2023
Time: 08:52
IDE: Visual Studio Code
Session Duration: 08:52 - 
Subject: Python
Version: 1.0
Senai - Desenvolvimento de Sistemas

Exercício 1: Calculadora Avançada

Crie uma função chamada calculadora_avancada que permita ao usuário escolher entre várias operações matemáticas, como adição, subtração, multiplicação e divisão. A função deve receber dois números e a operação desejada como entrada e retornar o resultado da operação.

Exercício 2: Média de Notas

Escreva um programa que solicite ao usuário que digite várias notas e, em seguida, calcule a média dessas notas. O programa deve continuar pedindo notas até que o usuário decida parar. Implemente isso usando uma função chamada calcular_media_notas.

Exercício 3: Números Primos

Crie uma função chamada verificar_numero_primo que recebe um número inteiro como entrada e verifica se ele é um número primo ou não. A função deve retornar True se o número for primo e False caso contrário.

Exercício 4: Gerador de Sequência de Fibonacci

Implemente uma função chamada gerar_fibonacci que recebe um número inteiro n como entrada e gera os primeiros n termos da sequência de Fibonacci. A sequência de Fibonacci começa com 0 e 1, e cada termo subsequente é a soma dos dois termos anteriores.

Exercício 5: Contagem de Palavras

Crie uma função chamada contar_palavras que recebe uma string como entrada e conta quantas palavras existem na string. Considere que as palavras são separadas por espaços em branco.
'''

def clear_screen():
    os.system('cls')
def welcome_message():
    print("Seja bem-vindo(a) ao App Senai!")
# Função iniciar
def iniciar():
    try:
        clear_screen()
        welcome_message()
        print("Iniciando...")
        exercicios()
    except Exception as e:
        print("Erro: ", e)

def exercicios():
    def calculadoraAvancada():
        class Calculadora:
            def calculadoraAdicao(self, num1, num2):
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = num1 + num2
                print(f"Resultado: {resultado}")
                return resultado
            def calculadoraSubtracao(self, num1, num2):
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = num1 - num2
                print(f"Resultado: {resultado}")
                return resultado
            def calculadoraMultiplicacao(self, num1, num2):
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = float(num1 * num2)
                print(f"Resultado: {resultado}")
                return resultado
            def calculadoraDivisao(self, num1, num2):
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                resultado = float(num1 / num2)
                print(f"Resultado: {resultado}")
                return resultado
        calculadora = Calculadora() 
        print("Calculadora Avançada")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
            calculadora.calculadoraAdicao(5, 2)
        elif opcao == 2:
            calculadora.calculadoraSubtracao(5, 2)
        elif opcao == 3:
            calculadora.calculadoraMultiplicacao(5, 2)
        elif opcao == 4:
            calculadora.calculadoraDivisao(5, 2)
        elif opcao == 5:
            print("Saindo...")
            time.sleep(1)
            clear_screen()
            exercicios()
        else:
            print("Opção inválida!")
            time.sleep(1)
            clear_screen()
            calculadoraAvancada()
        return Calculadora()
    def calculadoraLemon():
        class Calculadora:
            def calculadoraAdicao(self, num1, num2):
                resultado = float(num1 + num2)
                print(f"Resultado: {resultado}")
                return resultado
            def calculadoraSubtracao(self, num1, num2):
                resultado = float(num1 - num2)
                print(f"Resultado: {resultado}")
                return resultado
            def calculadoraMultiplicacao(self, num1, num2):
                resultado = float(num1 * num2)
                print(f"Resultado: {resultado}")
                return resultado
            def calculadoraDivisao(self, num1, num2):
                resultado = float(num1 / num2)
                print(f"Resultado: {resultado}")
                return resultado
        calculadora = Calculadora()
        print("Calculadora Lemon")
        # loop while
        while True:        
            num1 = float(input("Digite o primeiro número: "))
            operacao = input("Digite a operação desejada: ")
            num2 = float(input("Digite o segundo número: "))
            
            if operacao == "+":
                calculadora.calculadoraAdicao(num1, num2)
            elif operacao == "-":
                calculadora.calculadoraSubtracao(num1, num2)
            elif operacao == "*":
                calculadora.calculadoraMultiplicacao(num1, num2)
            elif operacao == "/":
                calculadora.calculadoraDivisao(num1, num2)
            else:
                print("Operação inválida!")
                time.sleep(1)
                clear_screen()
                calculadoraLemon()
                return Calculadora()
            sair = input("Deseja sair? (s/n): ")
            if sair == "s":
                print("Saindo...")
                time.sleep(1)
                clear_screen()
                break
            elif sair == "n":
                print("Continuando...")
                time.sleep(1)
                clear_screen()
                calculadoraLemon()
                break
            else:
                print("Opção inválida!")
                time.sleep(1)
                clear_screen()
                calculadoraLemon()    
    calculadoraLemon()
            

# Função main
def main():
    try:
        iniciar()
    except Exception as e:
        print("Erro: ", e)

# Inicialização do programa
if __name__ == "__main__":
    main()
