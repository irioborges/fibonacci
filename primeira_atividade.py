#!/usr/bin/python

import time
import timeit

def fib_i(posicao):
    if posicao == 1:
        return 0
    else:
        if posicao == 2:
            return 1
        else:
            first = 0
            second = 1
            for x in range(3, posicao + 1):
                value = first + second 
                first = second
                second = value
            return value

def fib_r(posicao):
    if posicao == 1:
        return 0
    else:
        if posicao == 2:
            return 1
        else:
            return fib_r(posicao - 1) + fib_r(posicao - 2)

opcao = 0


if __name__ == "__main__":

    opcao = 0
    while opcao != "3":
        print("Escolha uma das opções: ")
        print("1. Fibonacci iterativo")
        print("2. Fibonacci recursivo")
        print("3. Sair")

        opcao = input()

        if opcao == "1":
            resultado_iterativo = open("resultado-iterativo.csv", "w")
            for i in range(1, 101):
                ini = time.time()
                ini2 = timeit.default_timer()
                valor = fib_i(int(i))
                fim = time.time()
                fim2 = timeit.default_timer()
                resultado_iterativo.writelines(str(i)  + "," + str(valor) + "," + str("%f" % (fim - ini)) + "\n")
                print("Posição ", i, "  ", valor, ' %f' % (fim - ini))
        elif opcao == "2":
            resultado_recursivo = open("resultado-recursivo.csv", "w")
            for i in range(1, 101):
                ini2 = timeit.default_timer()
                valor = fib_r(int(i))
                print("Posição ", i, "  ", valor)
                fim2 = timeit.default_timer()
                resultado_recursivo.writelines(str(i)  + "," + str(valor) + "," + str("%f" % (fim2 - ini2)) + "\n")
        