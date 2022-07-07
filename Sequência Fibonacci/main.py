print('Seja bem vindo ao verificador de fibonacci!')
verificado = int(input('Digite o número que você pretende verificar: '))

def fibonacci(num):
    arr = [0,1]

    while(len(arr)<num):
        arr.append(0)
    if(num==0 or num==1):
        return 1
    else:
        arr[0]=0
        arr[1]=1
        for i in range(2,num):
            arr[i]=arr[i-1]+arr[i-2]
        return arr
fibonacci(10)

if verificado in fibonacci(31):
    print(f'o número {verificado} faz parte da sequência de Fibonacci!')
else:
    print(f'o número {verificado} não faz parte da sequência de Fibonacci!')



