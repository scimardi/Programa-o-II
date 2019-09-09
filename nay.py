def calcular_area_retangulo (b,h):
    area = b * h
    return str (area)

def calcular_perimetro_triangulo (lado1,lado2,lado3):
    perimetro = lado1 + lado2 + lado3
    return str (perimetro)

def calcular_acrescimo (prato, suco, sobremesa):
    conta = prato + suco + sobremesa
    acrescimo = conta * 0,10
    resultado = conta + acrescimo
    return resultado

def calcular_combustivel (distancia):
    combustivel_gasto = distancia / 12
    return str (combustivel_gasto)

def contar_letras (nome):
    contar_letras = (len(str(nome)))
    return str (contar_letras)

def calcular_salario (salariofixo, numcarros, valorpcarro, comissao):
    salario_total = salariofixo + ((numcarros * valorpcarro * 105) / 100) + comissao
    return salario_total

def trocar_valores (a,b):
    c = a
    a = b
    b = c
    return a,b

def realizar_funcao(a,b,c,x):
    funcao = a*x**2 + b *x + c
    return str (funcao)

def calcular_temperatura(celsius):
    fahrenheit = ((celsius * 9) / 5) + 32
    return str (fahrenheit)

def calcular_media (nota1, nota2, nota3):
    media = (nota1*2 + nota2*3 + nota3*5)/10
    return str (media)

if __name__ == "__main__":
    
    programa = True

    while programa:

        print (" ------ Bem-vindo(a)! Digite a opção desejada: ------ ")
        print(""" 1 - Para calcular a área de um retângulo 
                    2 - Para calcular o perímetro de um triângulo
                    3 - Para  calcular o valor da refeição completa em um restaurante
                    4 - Para calcular a quantidade de combústivel gasta em uma viagem
                    5 - Para contar as letras de um nome
                    6 - Para calcular o salário final de um vendedor
                    7 - Para trocar o valor de duas variáveis
                    8 - Para resolver uma equação de segundo grau
                    9 - Para transformar uma temperatura em graus Celsius para graus Fahrenheit
                    10 - Para calcular a média ponderada de um aluno
                    11 - Para parar o programa """)
                    
        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            b = float(input("Digite o valor da base do retângulo: "))
            h = float(input("Digite o valor da altura do retângulo: "))
            print((calcular_area_retangulo(b,h)))

        elif opcao == 2:
            lado1 = float(input("Digite o valor do lado 1 do triângulo: "))
            lado2 = float(input("Digite o valor do lado 2 do triângulo: "))
            lado3 = float(input("Digite o valor do lado 3 do triângulo: "))
            print((calcular_perimetro_triangulo(lado1,lado2,lado3)))

        elif opcao == 3:
            prato = float(input("Digite o valor do prato da refeição: "))
            suco = float(input("Digite o valor do suco da refeição: "))
            sobremesa = float(input("Digite o valor da sobremesa da refeição: "))
            print((calcular_acrescimo(prato, suco, sobremesa)))
        
        elif opcao == 4:
            distancia = float(input("Digite a distância da viagem: "))
            print((calcular_combustivel(distancia)))
        
        elif opcao == 5:
            nome = input("Digite um nome: ")
            print(nome)
            print((contar_letras(nome)))

        elif opcao == 6:
            salariofixo = float(input("Digite o salário fixo do vendedor: "))
            numcarros = float(input("Digite o número de carros vendidos: "))
            valorpcarro = float(input("Digite o valor por carro vendido: "))
            comissao = float(input("Digite o valor da comissão: "))
            print(calcular_salario(salariofixo, numcarros, valorpcarro, comissao))
        
        elif opcao == 7:
            a = float(input("Digite o valor de A: "))
            b = float(input("Digite o valor de B: "))
            print(trocar_valores(a,b))
        
        elif opcao == 8:
            a = float(input("Digite o valor de A: "))
            b = float(input("Digite o valor de B: "))
            c = float(input("Digite o valor de C: "))
            x = float(input("Digite o valor de x: "))
            print((realizar_funcao(a,b,c,x)))

        elif opcao == 9:
            celsius = float(input("Digite uma temperatura em graus Celsius: "))
            print((calcular_temperatura(celsius)))
        
        elif opcao == 10:
            nota1 = float(input("Digite a primeira nota: "))
            nota2 = float(input("Digite a segunda nota: "))
            nota3 = float(input("Digite a terceira nota: "))
            print((calcular_media (nota1, nota2, nota3)))

        elif opcao == 11:
            print("Encerrado! Programa feito por Naielly Röper Cardoso")
            programa = False

        else:
            print("Meu caro, essa opção não existe!")

