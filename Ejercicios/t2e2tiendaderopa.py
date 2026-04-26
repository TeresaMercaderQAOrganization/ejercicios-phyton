#Definir precios de ropa
#Convertimos a numero. int (sin decimales), float(puede tener decimales)
camiseta = 10
sudadera = 20.5
gorra = 5.5 

print ("camiseta: 10 euros")
print ("sudadera : 20.50 euros")
print ("gorra : 5.5 euros")

#Pedir cantidades
numero_camisetas = int (input("¿cuantas camisetas quieres?"))
numero_sudadera = int (input ("¿cuantas sudaderas quieres?" ))
numero_gorra = int (input("¿cuantas gorras quieres?"))

total_camistas = numero_camisetas * camiseta
total_sudadera = numero_sudadera * sudadera
total_gorra = numero_gorra * gorra

#Total de la compra
Total_compra = (total_camistas + total_sudadera + total_gorra)

print ("Total compra", Total_compra)

iva =(Total_compra * 0.21)

print ("IVA", iva)

total_compra_iva = Total_compra + iva
print ("total_compra_iva", total_compra_iva)






                      
                      
