def change():
    expense = 23.75
    money = 100
    vuelto = str(money - expense)
    position = vuelto.find('.')
    pesos =  vuelto[:position]
    centavos = vuelto[position + 1: ]
    print('Ingresar gasto:')
    print(expense)
    print('Dinero recibido')
    print(money)
    print()
    print('Vuelto')
    print()
    print('Pesos:')
    print(pesos)
    print('Centavos:')
    print(centavos)
