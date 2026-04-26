#solicita cantidad en euros
def cantidad_en_euros():
    
    cantidad_euros = float (input ( "cantidad euros: "))
    return cantidad_en_euros

def convertir_a_dolares():
    cambio = 1.1
    cantidad_dolares = cantidad_en_euros * cambio
    return cantidad_dolares

def convertir_a_libras():
    cambio = 0.87
    cantidad_libras = cantidad_en_euros * cambio
    return cantidad_libras

def conversor():
    print ("introduce cantidad en euros")
    cantidad_en_euros = ("cantidad euros")
    print ("dolares: ", convertir_a_dolares (cantidad_en_euros))
    print ("libras: ", convertir_a_libras (cantidad_en_euros))

    
conversor()




