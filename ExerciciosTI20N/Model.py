class Model:
    def __init__(self): #construtor
        self.num1 = 0
        self.num2 = 0

    def trocar(self, valorA, valorB):
        valorC = valorA
        valorA = valorB
        valorB = valorC
        return f'Valor A: {valorA} \nValor B: {valorB}'

    def tabuada(self, num):
        resultado = "" #Variavel String
        for i in range(0, 11, 1):
            resultado += f'{num} * {i} = {num * i}\n'
        return resultado

    def mediaTres(self, nota1, nota2, nota3):
        return(nota1 + nota2 + nota3)/3

    def exercicioUm(self):
        resultado = ""
        for i in range(1,11,1):
            resultado += f'{i}\n'
        return resultado

    def exercicioDois(self):
        resultado = ""
        for i in range(0,21,2):
            resultado += f'{i}\n'
        return resultado

    def exercicioTres(self):
        resultado = 0
        for i in range(0,101,1):
            resultado += i
        return resultado

    def exercicioQuatro(self):
        resultado = ""
        for i in range(0,51,5):
            resultado += f'{i}\n'
        return resultado

    def exercicioCinco(self, num):
        if num % 2 == 0:
            return f'O número {num} é par'
        else:
            return f'O número {num} é impar'

    def exercicioSeis(self, num):
        if num < 0:
            return f'O número {num} é negativo'
        elif num > 0:
            return f'O número {num} é positivo'
        else:
            return f'O número é 0'

    def exercicioSete(self, num):
        resultado = "" #Variavel String
        for i in range(0, 11, 1):
            resultado += f'{num} * {i} = {num * i}\n'
        return resultado

    def exercicioOito(self,num):
        resultado = ""
        for i in range(1,(num + 1),1):
            resultado += f'{i}\n'
        return resultado

    def exercicioNove(self, num):
        resultado = 0
        for i in range(1, (num + 1), 1):
            resultado += i
        return resultado

    def exercicioDez(self):
        resultado = "2\n 3\n 5\n"
        for i in range(5, 21, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                resultado += f'{i}\n'
        return resultado

    def exercicioOnze(self, num):
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            return f'O número é primo'
        elif num == 2 or num == 3 or num == 0:
            return f'O número é primo'
        else:
            return f'não é primo'

    def exercicioDoze(self, num):
        fatorial = 1
        while num > 1:
            fatorial *= num
            num -= 1
        return fatorial

    def exercicioTreze(self):
        resultado = "0\n1\n"
        fib1 = 0
        fib2 = 1
        fib3 = 0
        for i in range(1, 9, 1):
            fib3 = fib1 + fib2
            resultado += f'{fib3}\n'
            fib1 = fib2
            fib2 = fib3
        return resultado

    def exercicioQuatorze(self, num):
        resultado = "0\n1\n"
        fib1 = 0
        fib2 = 1
        resultado = f'{fib1}\n{fib2}\n'
        for i in range(1, num, 1):
            fib3 = fib1 + fib2
            resultado += f'{fib3}\n'
            fib1 = fib2
            fib2 = fib3
        return resultado

    def exercicioQuinze(self, num):
        resto = 0
        while num / 10 != 0:
            resto += num % 10
            num = int(num / 10)
        return f'A soma dos numeros é {resto}'
    def exercicioDezesseis(self, num):
        par = ""
        impar = ""
        for i in range(1, num, 1):
            if i % 2 == 0:
                par += f'{i}\n'
            else:
                impar += f'{i}\n'
        return f'Pares: {par} \nÍmpares: {impar}'

    def exercicioDezessete(self,num):
        resultado = " "
        for i in range(1, num, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                resultado += f'{i}\n'
            elif i == 2 or i == 3 or i == 0:
                resultado += f'{i}\n'
        return resultado

    def exercicioDezoito(self,num):
        collatz = []
        while num > 1:
            if num % 2 == 0:
                num = num / 2
            else:
                num = 3 * num+1
            collatz.append(num)
        return collatz

    def exercicioDezenove(self, num):
        par = 0
        impar = 0
        for i in range(1, num, 1):
            if i % 2 == 0:
                par += i
            else:
                impar += i
        return f'Pares: {par} \nÍmpares: {impar}'

    def exercicioVinte(self,num):
        aux = 0
        for i in range(1, num, 1):
            if num % i == 0:
                aux += i

        if aux == num:
            return f'O número {num} é um número perfeito'
        else:
            return f'O número {num} não é um número perfeito'

    def exercicioVinteUm(self, valorA, valorB):
        valorC = valorA
        valorA = valorB
        valorB = valorC
        return f'Valor A: {valorA} \nValor B: {valorB}'

    def exercicioVinteDois(self, num):
        return f'O antecessor do numero digitado é {num - 1}'