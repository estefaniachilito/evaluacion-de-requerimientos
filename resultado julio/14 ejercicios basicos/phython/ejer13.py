#  13. Realizar un programa que capture los datos de un empleado: Nombre, Genero (1-masculino, 2-femenino), Salario básico, y tiempo de servicio.
# El sistema debe calcular el valor de la bonificación anual en base a los siguientes
# lineamientos de la empresa:
# Si es mujer y el tiempo de servicio es superior a 5 años, su bonificación será de un 20% del
# Salario básico
# Si es mujer y el tiempo de servicio es inferior o igual a 5 años, su bonificación será de un
# 15% del Salario básico
# Si es hombre y el tiempo de servicio es superior a 6 años, su bonificación será de un 20% del
# Salario Básico.
# Si es hombre y el tiempo de servicio está entre 1 y 6 años su bonificación será de un 15%
# del Salario Básico.

nombre = str(input("Nombre: "))
genero = int(input("Genero (1=Masculino; 2=Femenino): "))
salario_basico = float(input("Salario Basico: $"))
tiempo = int(input("Tiempo de servicio: "))

if genero == 2 and tiempo > 5 :
    bonificacion = 0.20
    print (f"Salario con bonificación: {(salario_basico*bonificacion) + (salario_basico)}")
elif genero == 2 and tiempo <= 5 :
    bonificacion = 0.15
    print (f"Salario con bonificación: {(salario_basico*bonificacion) + (salario_basico)}")
elif genero == 1 and tiempo > 6 :
    bonificacion = 0.20
    print (f"Salario con bonificación: {(salario_basico*bonificacion) + (salario_basico)}")
elif genero == 1 and tiempo >=1 and tiempo <= 6 :
    bonificacion = 0.15
    print (f"Salario con bonificación: {(salario_basico*bonificacion) + (salario_basico)}")

if genero != 1 or genero != 2:
    print(f"genero incorrecto")