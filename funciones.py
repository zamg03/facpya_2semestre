def no_parametro_no_retorno():
    print('prueba 1 realizada con exito')

no_parametro_no_retorno()

def si_parametros_no_retorno(texto):
    print(texto)

si_parametros_no_retorno('prueba 2 realizada con exito')


num_1 = 10
num_2 = 20

def no_parametro_si_retorno():
    return num_1+num_2

print(no_parametro_si_retorno())

def si_parametros_si_retorno(val1,val2):
    return val1+val2

print(si_parametros_si_retorno(num_1,num_1))

#Elabora una funcion que reciba el diametro de un circulo, y retorne el radio y el area del circulo

def radio_area(d):
    radio = d/2
    area = (3.1416(radio*radio))
    return radio,area

a,b = radio_area(20)
print(a,b)

def velocidad(distancia,tiempo):
    return (distancia/tiempo)

print(velocidad(100,40))

