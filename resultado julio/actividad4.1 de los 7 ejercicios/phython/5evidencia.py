def calcular_jornal(turno, horas_trabajadas):
    tarifa_diurna = 10
    tarifa_nocturna = 15

    if turno == "diurno":
        valor_a_pagar = tarifa_diurna * horas_trabajadas
    elif turno == "nocturno":
        valor_a_pagar = tarifa_nocturna * horas_trabajadas
    else:
        valor_a_pagar = 0

    return valor_a_pagar

turno_trabajo = input("Ingrese el turno de trabajo (diurno/nocturno): ")
horas_trabajadas = int(input("Ingrese el número de horas trabajadas: "))

jornal = calcular_jornal(turno_trabajo, horas_trabajadas)
print("El valor a pagar es de $" , str(jornal))



ciudad=input("Ingrese su ciudad: ")
Fecha=input("Ingrese la fecha: ")
nombreCliente=input("Ingrese Nombre del cliente: ")
nombreProduct=input("Ingrese nombre del producto: ")
valorProduct=float(input ("Ingrese el valor del producto: "))
cantidadProduct=str(input ("Ingrese la cantidad del producto: "))
valorTotal= str(input(valorProduct*cantidadProduct))
totalConDescu= valorTotal-valorDelDescuento
valorDelDescuento= valorTotal*0.17,5

print ("ciudad: ", ciudad)
print ("fecha: ", Fecha)
print ("Cliente: ", nombreCliente)
print ("producto: ", nombreProduct)
print ("valor producto: ", valorProduct)
print ("cantidad producto: ", cantidadProduct)
print ("valor total ", valorTotal)
print ("valor del descuento ", valorDelDescuento)
print ("total: ", totalConDescu)