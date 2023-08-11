# 1. Una empresa de insumos agrícolas esta de promoción por el día de hoy y ofrece un
# descuente del 17.5% por las compras realizadas. Elaborar un script donde muestre la
# factura de venta con el descuento con la siguiente información:
# Ciudad y Fecha:
# Nombre del cliente:
# Nombre del producto:
# Valor del producto:
# Cantidad del producto:
# Valor total:
# Valor del descuento:
# Valor total con descuento:

# nombre=(input("Ingrese su nombre: "))
# ciudad=(input("Ingrese ciudad: "))
# fecha=(input("Ingrese la Fecha: "))
# producto=(input("Ingrese el nombre del producto: "))
# valor=int(input("Ingrese el valor del producto: "))
# cantidad=int(input("Ingrese la cantidad del producto deseado: "))
# valort=str((valor*cantidad))
# descuento=str((valor*cantidad*17.5/100))
# valortcd=str((valor+(-valor*cantidad*17.5/100)))

# if fecha.lower() == "11/08/2023" or "11 de agosto" or "11 de agosto de 2023" :
#     print("FACTURA ","<br>","Informacion del cliente: ",nombre,"<br>",ciudad,"<br>",fecha,"<br>","Producto: ",producto,"<br>","Cantidad: ",cantidad,"<br>",
#           "valor por unidad: ",valor,"<br>","valor de la compra: ",valort,"<br>","valor del descuento: ",descuento,"<br>","valor a pagar: ",valortcd)

# else:
#     print("FACTURA ","<br>","Informacion del cliente: ",nombre,"<br>",ciudad,"<br>",fecha,"<br>","Producto: ",producto,"<br>","Cantidad: ",cantidad,"<br>",
#           "valor por unidad: ",valor,"<br>","valor de la compra: ",valort,"<br>","valor a pagar: ",valortcd)
          

nombre=(input("Ingrese su nombre: "))
ciudad=(input("Ingrese ciudad: "))
fecha=(input("Ingrese la Fecha: "))
producto=(input("Ingrese el nombre del producto: "))
valor=int(input("Ingrese el valor del producto: "))
cantidad=int(input("Ingrese la cantidad del producto deseado: "))
valort=str((valor*cantidad))
descuento=str((valor*cantidad*17.5/100))
valortcd=str((valor+(-valor*cantidad*17.5/100)))

if fecha.lower() == "11/08/2023" or "11 de agosto" or "11 de agosto de 2023" :
    print("FACTURA ","<br>","Informacion del cliente: ",nombre,"<br>",ciudad,"<br>",fecha,"<br>","Producto: ",producto,"<br>","Cantidad: ",cantidad,"<br>",
          "valor por unidad: ",valor,"<br>","valor de la compra: ",valort,"<br>","valor del descuento: ",descuento,"<br>","valor a pagar: ",valortcd)

else:
    print("FACTURA ","<br>","Informacion del cliente: ",nombre,"<br>",ciudad,"<br>",fecha,"<br>","Producto: ",producto,"<br>","Cantidad: ",cantidad,"<br>",
          "valor por unidad: ",valor,"<br>","valor de la compra: ",valort,"<br>","valor a pagar: ",valortcd)