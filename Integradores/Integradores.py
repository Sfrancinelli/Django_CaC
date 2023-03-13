"""Para calcular los factores primos de un número, se puede seguir los siguientes pasos:

Dividir el número por el número primo más pequeño posible (2). Si el número es divisible por 2, dividirlo hasta que ya no sea divisible por 2.
Si el número no es divisible por 2, pasar al siguiente número primo (3) y dividirlo hasta que ya no sea divisible por 3.
Continuar de esta manera, dividiendo el número por cada número primo sucesivo hasta que el número no sea divisible por ningún número primo más pequeño.
Los factores primos del número son los números primos que se usaron como divisores en este proceso.

Por ejemplo, para calcular los factores primos de 60:

Dividir 60 por 2, obteniendo 30. Como 30 es divisible por 2, dividirlo por 2 de nuevo, obteniendo 15. Como 15 es divisible por 3, dividirlo por 3, obteniendo 5. Como 5 es primo, el proceso termina. Los factores primos de 60 son 2, 2, 3 y 5 (o, de forma más concisa, 2^2 x 3 x 5).
Una vez que se tienen los factores primos de dos números, se puede calcular el MCD (máximo común divisor) multiplicando todos los factores primos comunes elevados a la menor potencia.

Por ejemplo, para calcular el MCD de 60 y 96:

Los factores primos de 60 son 2^2 x 3 x 5.
Los factores primos de 96 son 2^5 x 3.
Los factores primos comunes son 2^2 y 3.
El MCD es el producto de los factores primos comunes elevados a la menor potencia: 2^2 x 3 = 12."""

def mcd(num1, num2):
    fact_prim_num1 = []
    fact_prim_num2 = []
    factores_primos = num1 % 2
    numero1 = num1
    numero2 = num2
    while factores_primos == 0:
        fact_prim_num1.append(2)
        num1 = num1 / 2
        factores_primos = num1 % 2

        if factores_primos != 0:
            factores_primos = num1 % 3
            while factores_primos == 0:
                fact_prim_num1.append(3)
                num1 = num1 / 3
                factores_primos = num1 % 3

        elif factores_primos != 0:
            factores_primos = num1 % 5
            while factores_primos == 0:
                fact_prim_num1.append(5)
                num1 = num1 / 5
                factores_primos = num1 % 5

        elif factores_primos != 0:
            factores_primos = num1 % 7
            while factores_primos == 0:
                fact_prim_num1.append(7)
                num1 = num1 / 7
                factores_primos = num1 % 7

    factores_primos = num2 % 2
    while factores_primos == 0:
        fact_prim_num2.append(2)
        num2 = num2 / 2
        factores_primos = num2 % 2

        if factores_primos != 0:
            factores_primos = num2 % 3
            while factores_primos == 0:
                fact_prim_num2.append(3)
                num2 = num2 / 3
                factores_primos = num2 % 3

        elif factores_primos != 0:
            factores_primos = num2 % 5
            while factores_primos == 0:
                fact_prim_num2.append(5)
                num2 = num2 / 5
                factores_primos = num2 % 5

        elif factores_primos != 0:
            factores_primos = num2 % 7
            while factores_primos == 0:
                fact_prim_num2.append(7)
                num2 = num2 / 7
                factores_primos = num2 % 7

    factor_2_num1 = fact_prim_num1.count(2)
    factor_2_num2 = fact_prim_num2.count(2)

    if factor_2_num1 < factor_2_num2:
        factor_2 = factor_2_num1
    else: 
        factor_2 = factor_2_num2

    print(factor_2)

    factor_3_num1 = fact_prim_num1.count(3)
    factor_3_num2 = fact_prim_num2.count(3)

    if factor_3_num1 < factor_3_num2:
        factor_3 = factor_3_num1
    else: 
        factor_3 = factor_3_num2

    print(factor_3)

    factor_5_num1 = fact_prim_num1.count(5)
    factor_5_num2 = fact_prim_num2.count(5)
    
    if factor_5_num1 < factor_5_num2:
        factor_5 = factor_5_num1
    else: 
        factor_5 = factor_5_num2

    print(factor_5)

    factor_7_num1 = fact_prim_num1.count(7)
    factor_7_num2 = fact_prim_num2.count(7)
    
    if factor_7_num1 < factor_7_num2:
        factor_7 = factor_7_num1
    else: 
        factor_7 = factor_7_num2

    print(factor_7)

    if factor_2 != 0:
        mcd = factor_2 * 2
    elif factor_3 != 0:
        mcd = mcd * (factor_3 * 3)
    elif factor_5 != 0:
        mcd = mcd * (factor_5 * 5)
    elif factor_7 != 0:
        mcd = mcd * (factor_7 * 7) 

    return f"El máximo común divisor entre {numero1} y {numero2} es: {mcd}"

print(mcd(60, 96))


