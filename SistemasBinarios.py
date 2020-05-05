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
    num = int(num)
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
    num = int(num)          
    numeroAux = binario_a_decimal(num)
    return decimal_a_base(numeroAux, base) 

def octal_a_base(num, base):
    num = int(num) 
    numeroAux = octal_a_decimal(num)
    return decimal_a_base(numeroAux, base)

def hexa_a_base(num, base):
    numeroAux = hexa_a_decimal(num)
    return decimal_a_base(numeroAux, base)

if __name__ == '__main__':
    bases = {'decimal' : 10, 'hexadecimal': 16, 'Octal' : 8, 'binario' : 2}
    opciones = ['1','2','3','4','5']
    msg = list('Sistemas binarios')
    while(True):
        print(' '.join(msg).upper())
        opcion = input('''Seleccione una opcion:
            [1] Octal a base n
            [2] Decimal a base n
            [3] Hexadecimal a base n
            [4] Binario a base n
            [5] Salir
            
        ''')
        if opcion in opciones:
            if opcion == '5':
                break
                
            base = 0
            while(base not in bases.values()):
                base = int(input('Base a convertir (2, 8, 10, 16): '))
                
            for key, value in bases.items():
                if value == base:
                    print('Conversion a ' + key)
                    break;
            
            n = input('Escriba el numero: ').upper()

            if opcion == '1':
                print(f'{n} en base 8 = {octal_a_base(n, base)} en base {base}')
            elif opcion == '2':
                print(f'{n} en base 10 = {decimal_a_base(n, base)} en base {base}')
            elif opcion == '3':
                print(f'{n} en base 16 = {hexa_a_base(n, base)} en base {base}')
            elif opcion == '4':
                print(f'{n} en base 2 = {binario_a_base(n, base)} en base {base}')
        else:
            print('Seleccione una opcion valida')     
             
        input('Presione una tecla para continuar...')           

