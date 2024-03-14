...
"hallar el pago total en una tienda sabiendo que siemprehay descuentros del 20% para todo los clientes, sabiendo queel precio de venta de los televisoress es de 560dolares por cada unidad"
...
#entrada

nombre=input("ingrese su nombre:")
cantidad=int(input("ingresela cantidad de tvcompradas:"))


#processo
montoBruto = cantidad * 560
descuento = (montoBruto * 20) / 100
montoFinal = montoBruto - descuento

#salida
print(nombre, "usted compro ", cantidad, "televisores")
print("montosin descuento: s/ ", montoBruto)
print("descuento: s/", descuento)
print("usted debe pagar: s/", montoFinal)

