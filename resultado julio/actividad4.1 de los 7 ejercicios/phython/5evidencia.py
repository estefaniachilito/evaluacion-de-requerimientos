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
