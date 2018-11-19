def primo(num):
    esPrimo = True
    if num == 1:
        esPrimo = False
    else:
        for i in range(2, num):
            if (num % i) == 0:
                esPrimo = False
    return esPrimo

def fac_primos(num):
    div = []
    a = 2
    while a * a <= num:
        if num % a == 0 and primo(a):
            div.append(a)
            num = int(num / a)
        else:
            a += 1
    if num > 1:
        div.append(num)
    return div

print(max(fac_primos(600851475143)))