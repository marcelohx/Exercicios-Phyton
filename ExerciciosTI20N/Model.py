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

    def exercicioVinteTres(self, base, altura):
        area = 0
        area = base * altura
        return f'De acordo com a base: {base} e a altura: {altura} a área do retângulo é de {area} Metros'

    def exercicioVinteQuatro(self, dia, mes, ano):
        idade = 0
        idade = (ano * 365) + (mes * 30) + dia
        return idade

    def exercicioVinteCinco(self, totalEleitores, votosBrancos, votosNulos, votosValidos):
        return f'O total de eleitores é de: {totalEleitores} \nA porcentagem de votos branco é de: {(votosBrancos / totalEleitores) * 100}% \nA porcentagem de votos nulos é de: {(votosNulos / totalEleitores) * 100}% \nA porcentagem de votos validos é de: {(votosValidos / totalEleitores) * 100}%'

    def exercicioVinteSeis(self, salario, perReajuste):
        salarioFinal = (salario * (perReajuste/100)) + salario
        return f'O salario é de R${salario} \nO percentual do reajuste é de {perReajuste}% \nO valor do novo salario é R${salarioFinal}'

    def exercicioVinteSete(self, custoFabrica):
        valorDistribuidor = custoFabrica * 0.28
        valorImposto = custoFabrica * 0.45
        valorFinal = custoFabrica + valorDistribuidor
        return f'O valor final para o consumidor é R$ {valorFinal}'

    def exercicioVinteOito(self, notaUm, notaDois, notaTres):
        media = (notaUm + notaDois + notaTres) / 3
        return f'A média do aluno de acordo com as notas fornecidas é de {media}'

    def exercicioVinteNove(self, qtdeMaca):
        if qtdeMaca < 6:
            valorMaca = 1.30
            valorTotal = qtdeMaca * valorMaca
            return f'O valor total da compra foi de R$ {valorTotal}, cada maçã saiu por {valorMaca}'
        elif qtdeMaca >= 12:
            valorMaca = 1.00
            valorTotal = qtdeMaca * valorMaca
            return f'O valor total da compra foi de R$ {valorTotal}, cada maçã saiu por {valorMaca}'

    def exercicioTrintaUm(self, salarioFixo, vendas):
        vendasComissao = 0
        if vendas <= 1500:
            vendasComissao = (vendas * 0.03) + salarioFixo
        elif vendas > 1500:
            vendasComissao = (1500 * 0.03) + ((vendas - 1500) * 0.05) + salarioFixo
            return vendasComissao

    def exercicioTrintaDois(self, saldo, debito, credito):
        saldoAtual = saldo - debito + credito
        if saldoAtual <= 0:
            return f'Saldo Negativo'
        else:
            return f'Saldo positivo'

    def exercicioTrintaTres(self, num):
        resultado = ""
        for i in range(1, num + 1, 1):
            resultado += f'{i}\n'
        return resultado

    def exercicioTrintaQuatro(self):
        cont = 0
        for i in range(1, 10, 1):
            num = int(input('Informe um número: '))
            if num < 0:
                cont += 1
        return f'A quantidade de numeros negativos de acordo com os numeros passado foi de {cont}'

    def exercicioTrintaCinco(self):
        cont = 0
        for i in range(1, 10, 1):
            num = int(input('Informe um número: '))
            if num < 40:
                cont += num
        return f'O valor da soma dos valores menores que 40 foi de {cont}'

    def exercicioTrintaSeis(self):
        resultado = 0
        for i in range(15, 101, 1):
            resultado += i
        resultado / 85
        return f'O resultado da media aritimetica de 15 a 100 é de {resultado}'

    def exercicioTrintaSete(self, qtde):
        aux = 0
        maior = ""
        soma = 0
        for i in range(1, qtde + 1, 1):
            num = int(input('Informe um número: '))
            aux = num
            if num > aux:
                maior = num
            elif num == aux:
                maior = num
            else:
                maior = aux
            soma += num
        return f'O maior numero é {maior} e a media aritimética da soma dos numeros foi de {soma / qtde}'

    def exercicioTrintaOito(self):
        soma = 0
        notas = []
        media = 0
        contar = 0
        for i in range(0, 10, 1):
            nota = int(input('Informe a nota: '))
            soma += nota
            notas.append(nota)
        media = soma / 10

        for i in range(0,10,1):
            if(notas[i] > media):
                contar += 1

        return f'A media da sala foi de {media} e a quantidade de alunos com nota acima da media foi de {contar}'

    def exercicioTrintaNove(self, habitantes):
        somaS = 0
        mediaS = 0
        salarios = []
        somaF = 0
        mediaF = 0
        aux = 0
        contar = 0
        porcentagem = 0
        for i in range(0, habitantes, 1):
            salario = int(input('Informe o salario: '))
            qtdeFilho = int(input('Informe a numero de filhos: '))
            salarios.append(salario)
            aux = salario
            somaS += salario
            somaF += qtdeFilho
            if salario > aux:
                maior = salario
            elif salario == aux:
                maior = salario
            else:
                maior = aux
        mediaS = somaS / habitantes
        mediaF = somaF / habitantes

        for i in range(0, habitantes, 1):
            if(salarios[i] < 150):
                contar += 1
        porcentagem = (contar / habitantes) * 100

        return f'A) A media de salario da população é de: {mediaS}\nB) A Media do numero de filhos é de: {mediaF}\nC)O maior salario entre os habitantes é: {maior}\nD)O percentual de pessoas com salario abaixo de R$150.0 é de {porcentagem}%'



