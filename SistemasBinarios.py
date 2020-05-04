def binario_a_decimal(num):
    numero, i = 0, 0
    while(num != 0): 
        aux = num % 10
        numero = numero + aux * pow(2, i) 
        num = num // 10
        i += 1
    return numero

def octal_a_decimal(num):
    numero, i = 0, 0
    while(num != 0): 
        aux = num % 10
        numero = numero + aux * pow(8, i) 
        num = num // 10
        i += 1
    return numero

def hexa_a_decimal(num):
    numero = 0 
    i = 0     
    largo = len(num)  
    exp = largo - 1
    while(i < largo):             
        aux = str(num[i])
        if(aux == 'A'):
            numero =  10 * pow(16, exp) + numero
        elif(aux == 'B'):
            numero =  11 * pow(16, exp) + numero
        elif(aux == 'C'):
            numero =  12 * pow(16, exp) + numero
        elif(aux == 'D'):
            numero =  13 * pow(16, exp) + numero
        elif(aux == 'E' ):
            numero =  14 * pow(16, exp) + numero
        elif(aux == 'F'):
            numero =  15 * pow(16, exp) + numero  
        else:
            numero =  int(aux) * pow(16, exp) + numero 
        i+= 1
        exp -= 1
    return numero


def decimal_a_base(num, base):
    numero = ''
    aux = 0
    while(num != 0):  
        aux = num % base
        if(aux == 10):
            numero =  'A' + numero
        elif(aux == 11):
            numero =  'B' + numero 
        elif(aux == 12):
            numero =  'C' + numero 
        elif(aux == 13):
            numero =  'D' + numero 
        elif(aux == 14):
            numero =  'E' + numero
        elif(aux == 15):
            numero =  'F' + numero   
        else:
            numero =  str(aux) + numero 
        num = num // base
    return numero


def binario_a_base(num, base):           
    numeroAux = binario_a_decimal(num)
    return decimal_a_base(numeroAux, base) 

def octal_a_base(num, base):
    numeroAux = octal_a_decimal(num)
    return decimal_a_base(numeroAux, base)

def hexa_a_base(num, base):
    numeroAux = hexa_a_decimal(num)
    return decimal_a_base(numeroAux, base)

n = input()
print(hexa_a_base(n, 10))
print(hexa_a_base(n, 8))
print(hexa_a_base(n, 16))
print(hexa_a_base(n, 2))



