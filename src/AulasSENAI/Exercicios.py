import os
'''
Autor: João Victor Martins Deamo
Date: 18/09/2023
Time: 08:20
IDE: Visual Studio Code
Session Duration: 08:20 - 08:52
Subject: Python
Version: 1.2
Senai - Desenvolvimento de Sistemas

Observação: O código não ficou tão organizado quanto eu gostaria, mas acredito que está legível e funcional.

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

Exercício 6:
6. Escreva um código em que declara uma variável nome e atribui a ela o seu próprio nome.

Exercício 7:
7. Escreva um código em que solicita ao usuário a sua idade e atribui o valor digitado à variável idade.

Exercício 8:
8. Escreva um código em que converte o valor digitado pelo usuário em um número inteiro.

Exercício 9:
9. Escreva um código em que imprime a sequência de números de 1 a 10.

Exercício 10:
10. Escreva um código em que imprime a sequência de números pares de 1 a 10.

Exercício 11:
11. Escreva um código em que imprime a sequência de números ímpares de 1 a 10.

Exercício 12:
12. Escreva um código em que imprime a sequência de números de 1 a 10, mas pulando os números pares.

Exercício 13:
13. Escreva um código em que imprime a sequência de números de 1 a 10, mas pulando os números ímpares.

Exercício 14:
14. Escreva um código em que verifica se um número é par.

Exercício 15:
15. Escreva um código em que verifica se um número é ímpar.
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
        exercicios2()
    except Exception as e:
        print("Erro: ", e)
# Função exercicios
def exercicios():
    # Função nome
    def exercicio1():
        try:
            nome = input("Digite seu nome: ")
            print(f"Olá, {nome}!")
        except Exception as e:
            print("Erro: ", e)
    exercicio1()
    # Função boas vindas
    def exercicio2():
        try:
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))
            if idade == 1:
                print(f"Olá, {nome}! Você tem {idade} ano.")
            else:
                print(f"Olá, {nome}! Você tem {idade} anos.")
        except Exception as e:
            print("Erro: ", e)
    exercicio2()
    # Função soma
    def exercicio3(num1, num2):
        try:
            return (float(num1) + float(num2))
        except Exception as e:
            print("Erro: ", e)

    # Função fatorial
    def exercicio4(num):
        try:
            fatorial = 1
            for i in range(1, num + 1):
                fatorial = fatorial * i
            return fatorial
        except Exception as e:
            print("Erro: ", e)

    # Função classes
    def exercicio5():
        try:
            class Calculadora:
                def soma(self, num1, num2):
                    return float(float(num1) + float(num2))
                def multiplicacao(self, num1, num2):
                    return float(float(num1) * float(num2))
            return Calculadora()
        except Exception as e:
            print("Erro: ", e)
    # Função atributos
    def atributos():
        try:
            calc = exercicio5()
            somaEx3 = exercicio3(8, 7)
            fatorialEx4 = exercicio4(5)
            somaEx5 = calc.soma(10, 20)
            multEx5 = calc.multiplicacao(5, 10)
            return somaEx3, fatorialEx4, somaEx5, multEx5
        except Exception as e:
            print("Erro: ", e)
    def atributos2():
        resultado_soma, fatorialEx4, resultado_soma1, resultado_multiplicacao = atributos()
        print(f"Soma de 8 + 7: {resultado_soma}.")
        print(f"Fatorial de 5: {fatorialEx4}.")
        print(f"Soma de 10 + 20: {resultado_soma1}.")
        print(f"Multiplicação de 5 * 10: {resultado_multiplicacao}.") 
    # Função poo
    def main():
        try:
            atributos2()
        except Exception as e:
            print("Erro: ", e)
    main()
# Função exercicios2
def exercicios2():
    # Função exercicio 6
    def exercicio6():
        try:
            nome = "João Victor"
            print(f"Meu nome é {nome}.")
        except Exception as e:
            print("Erro: ", e)

    # Função exercício 7
    def exercicio7():
        try:
            idade = int(input("Digite sua idade: "))
            print(f"Você tem {idade} anos.")
        except Exception as e:
            print("Erro: ", e)
    
    # Função exercício 8
    def exercicio8():
        try:
            entrada = input("Digite um número: ")
            numero = int(entrada)
            print(f"O número digitado foi {numero}.")

        except Exception as e:
            print("Erro: ", e)
    
    # Função exercício 9
    def exercicio9():
        try:
            valorMinimo = 1
            valorMaximo = 11
            for i in range(valorMinimo, valorMaximo):
                print(f"O valor atual é {i}.")
        except Exception as e:
            print("Erro: ", e)
    # Função exercício 10
    def exercicio10():
        try:
            valorMinimo = 1
            valorMaximo = 11
            for i in range(valorMinimo, valorMaximo):
                if i % 2 == 0:
                    print(f"O número {i} é par.")
        except Exception as e:
            print("Erro: ", e)
    
    # Função exercício 11
    def exercicio11():
        try:
            valorMinimo = 1
            valorMaximo = 11
            for i in range(valorMinimo, valorMaximo):
                if i % 2 != 0:
                    print(f"O número {i} é ímpar.")
                
        except Exception as e:
            print("Erro: ", e)
            
    # Função exercício 12
    def exercicio12():
        try:
            valorMinimo = 1
            valorMaximo = 11
            for i in range(valorMinimo, valorMaximo):
                if i % 2 == 0:
                    continue
                else:
                    print(f"{i}")
        except Exception as e:
            print("Erro: ", e)
        
    # Função exercício 13
    def exercicio13():
        try:
            valorMinimo = 1
            valorMaximo = 11
            for i in range(valorMinimo, valorMaximo):
                if i % 2 != 0:
                    continue
                else:
                    print(f"{i}")
        except Exception as e:
            print("Erro: ", e)
            
    # Função exercício 14
    def exercicio14():
        try:
            numero = int(input("Digite um número: "))
            if numero % 2 == 0:
                print(f"O número {numero} é par.")
            else:
                print(f"O número {numero} não é par.")
        except Exception as e:
            print("Erro: ", e)
            
    # Função exercício 15
    def exercicio15():
        try:
            numero = int(input("Digite um número: "))
            if numero % 2 != 0:
                print(f"O número {numero} é ímpar.")
            else:
                print(f"O número {numero} não é ímpar.")
        except Exception as e:
            print("Erro: ", e)
    def main():
        try:
            exercicio6()
            exercicio7()
            exercicio8()
            exercicio9()
            exercicio10()
            exercicio11()
            exercicio12()
            exercicio13()
            exercicio14()
            exercicio15()
        except Exception as e:
            print("Erro: ", e)
    main()
# Função atributos
def main():
    try:
        iniciar()
    except Exception as e:
        print("Erro: ", e)
    
if __name__ == "__main__":
    main()
