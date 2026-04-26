def datos_compra():
    nombre_producto = input ("nombre_producto: ")
    precio_unidad = float (input ("precio_unidad: "))
    cantidad = float (input ("cantidad: "))
    descuento = float (input ( "descuento (%): "))
    iva = float (input ("iva (%): "))
    return nombre_producto, precio_unidad, cantidad, descuento, iva

#obtener datos
def total_compra (precio_unidad, cantidad, descuento,iva):


#calculos
    total = (precio_unidad* cantidad)
    total_descuento = (total - (total * descuento /100))
    precio_final = (total_descuento + (total_descuento * iva /100))
    return precio_final

print ("introduce los datos de la compra: ")
nombre_producto, precio_unidad,cantidad, descuento, iva = datos_compra()

print ("total: ", total_compra (precio_unidad, cantidad, descuento, iva))













