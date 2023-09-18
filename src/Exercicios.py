import os
'''
Autor: João Victor Martins Deamo
Date: 18/09/2023
Time: 11:10
IDE: Visual Studio Code
Session Duration: 11:10 - 
Subject: Python
Version: 1.0
Senai - Desenvolvimento de Sistemas

Exercícios de Python

Exercício 1:
Escreva um programa que solicite ao usuário que digite seu nome e exiba uma mensagem de boas-vindas.

Exercício 2:
Modifique o programa anterior para solicitar ao usuário que digite sua idade e, em seguida, exiba uma mensagem personalizada com o nome e a idade.

Exercício 3:
Crie uma função chamada `soma` que receba dois números como parâmetros e retorne a soma desses números.

Exercício 4:
Implemente uma função chamada `fatorial` que receba um número inteiro como parâmetro e retorne o fatorial desse número.

Exercício 5:
Crie uma classe chamada `Calculadora` que tenha dois métodos: `soma` e `multiplicacao`. O método `soma` deve receber dois números como parâmetros e retornar a soma, enquanto o método `multiplicacao` deve receber dois números como parâmetros e retornar o resultado da multiplicação.
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
        print("Erro: ", e)# Função exercício 1
def exercicios():
    # Função exercício 1
    def exercicio1():
        try:
            nome = input("Digite seu nome: ")
            print(f"Olá, {nome}!")
        except Exception as e:
            print("Erro: ", e)
        
    # Função exercício 2
    def exercicio2():
        try:
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))
            print(f"Olá, {nome}! Você tem {idade} anos.")
        except Exception as e:
            print("Erro: ", e)
        
    # Função exercício 3
    def soma(num1, num2):
        try:
            return num1 + num2
        except Exception as e:
            print("Erro: ", e)
        
    # Função exercício 4
    def fatorial(num):
        try:
            fatorial = 1
            for i in range(1, num + 1):
                fatorial = fatorial * i
            return fatorial
        except Exception as e:
            print("Erro: ", e)

    # Função exercício 5
    def classes():
        try:
            class Calculadora:
                def soma(self, num1, num2):
                    return float(float(num1) + float(num2))
                def multiplicacao(self, num1, num2):
                    return float(float(num1 * float(num2)))
            return Calculadora()
        except Exception as e:
            print("Erro: ", e)

    def objetos(calc):
        try:
            calc = classes()
            soma = calc.soma(10, 20)
            multiplicacao = calc.multiplicacao(5, 10)
            return soma, multiplicacao
        except Exception as e:
            print("Erro: ", e)
    # Função principal
    def poo():
        try:
            exercicio1()
            exercicio2()
            resultado_soma, resultado_multiplicacao = objetos(classes())
            resultado_fatorial = fatorial(5)
            print(f"Soma de 10 + 20: {resultado_soma}.")
            print(f"Fatorial de 5: {resultado_fatorial}.")
            print(f"Multiplicação de 5 * 10: {resultado_multiplicacao}.")
        except Exception as e:
            print("Erro: ", e)
    poo()
        
# Função atributos
def main():
    try:
        iniciar()
    except Exception as e:
        print("Erro: ", e)
    
if __name__ == "__main__":
    main()
