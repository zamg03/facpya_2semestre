precios_servicios = ""
total = 0
tematica = ""
nuevo_cliente = "si"
clientes = 0
num_tematicas = 0

def servicios_precios(precios_servicios):
    print("Lista de servicios:")
    print(" (1) Pastel $250 \n (2) Piñata $350 \n (3) Refrescos $650 \n (4) Aguas de sabor $250 \n (5) Botanas $300 \n (6) Gelatinas $100 \n (7) Invitaciones $250 \n (8) Espectaculo $700 \n (9) Música ambiental $200 \n (10) Chilidog $400 \n (11) Hot dog $300 \n (12) Pizza $600 \n (13) Marinitas $450")

while nuevo_cliente == "SI" or nuevo_cliente == "Si" or nuevo_cliente == "si":
    clientes += 1
    carrito = 0
    renta = 0
    articulo = ""
    lista = ""
    precio = 0

    print('Salon de Fiestas Infantiles "DivertiLandia"')

    op = input("La renta del salon tiene un costo de $3,000 para 60 personas \nDesea rentar el salon de fiestas?: ")

    if op == "SI" or op == "Si" or op == "si":
        renta += 3000
        total += renta
        carrito += renta

        tematica = input("¿Quieres que la fiesta sea con tematica? \nLos costos del pastel, piñata, invitaciones, espectáculo y la música ambiental aumentan un 15% \nIngresa tu desición: ")
        if tematica == "SI" or tematica == "Si" or tematica == "si":
            num_tematicas += 1

        extras = input("Desea añadir a personas extras?(si)(no): ")
        if extras == "SI" or extras == "Si" or extras == "si":
            print("Puedes agregar un maximo 140 personas, el salon es de 200 personas maximo")
            cantidad_personas = int(input("¿Cuantas personas desea agregar?: "))
            while cantidad_personas > 140:
                print("Cantidad rebasada")
                cantidad_personas = int(input("Ingresa las personas extras: "))

        print("Los servicios son los siguiente: ")
        servicios_precios(precios_servicios)
        serv = input("Desea agregar algun servicio?: ")
        while op == "SI" or op == "Si" or op == "si":
            if serv == "SI" or serv == "Si" or serv == "si":
                select = int(input("Selecciona un servicio: "))

            if select == 1:
                if tematica == "SI" or tematica == "Si" or tematica == "si":
                    print("Agregaste Pastel con Tematica al carrito")
                    Pastel = 250 * 1.15
                    total += Pastel
                    articulo = "Pastel"
                    costo = Pastel
                    carrito += Pastel
                else:
                    print("Agregaste Pastel al carrito")
                    Pastel = 250
                    total += Pastel
                    articulo = "Pastel"
                    costo = Pastel
                    carrito += Pastel
            
            elif select == 2:
                if tematica == "SI" or tematica == "Si" or tematica == "si":
                    print("Agregaste Piñata con Tematica al carrito")
                    Piñata = 350 * 1.15
                    total += Piñata
                    articulo = "Piñata"
                    costo = Piñata
                    carrito += Piñata
                else:
                    print("Agregaste Piñata al carrito")
                    Piñata = 350
                    total += Piñata
                    articulo = "Piñata"
                    costo = Piñata
                    carrito += Piñata

            elif select == 3:
                print("Agregaste Refrescos al carrito")
                Refrescos = 650
                total += Refrescos
                articulo = "Refrescos"
                costo = Refrescos
                carrito += Refrescos

            elif select == 4:
                print("Agregaste Aguas de Sabores al carrito")
                Agua_sabor = 250
                total += Agua_sabor
                articulo = "Agua de Sabores"
                costo = Agua_sabor
                carrito += Agua_sabor

            elif select == 5:
                print("Agregaste Botanas al carrito")
                Botanas = 350
                total += Botanas
                articulo = "Botanas"
                costo = Botanas
                carrito += Botanas

            elif select == 6:
                print("Agregaste Gelatinas al carrito")
                Gelatinas = 100
                total += Gelatinas
                articulo = "Gelatinas"
                costo = Gelatinas
                carrito += Gelatinas

            elif select == 7:
                if tematica == "SI" or tematica == "Si" or tematica == "si":
                    print("Agregaste Invitaciones con Tematica al carrito")
                    Invitaciones = 250 * 1.15
                    total += Invitaciones
                    articulo = "Invitaciones"
                    costo = Invitaciones
                    carrito += Invitaciones
                else:
                    print("Agregaste Invitaciones al carrito")
                    Invitaciones = 250
                    total += Invitaciones
                    articulo = "Invitaciones"
                    costo = Invitaciones
                    carrito += Invitaciones

            elif select == 8:
                if tematica == "SI" or tematica == "Si" or tematica == "si":
                    print("Agregaste Espectaculo con Tematica al carrito")
                    Espectaculo = 700 * 1.15
                    total += Espectaculo
                    articulo = "Espectaculo"
                    costo = Espectaculo
                    carrito += Espectaculo
                else:
                    print("Agregaste Espectaculo al carrito")
                    Espectaculo = 700
                    total += Espectaculo
                    articulo = "Espectaculo"
                    costo = Espectaculo
                    carrito += Espectaculo

            elif select == 9:
                if tematica == "SI" or tematica == "Si" or tematica == "si":
                    print("Agregaste Musica Ambiental al carrito")
                    Musica_Ambiental = 200 * 1.15
                    total += Musica_Ambiental
                    articulo = "Musica Ambiental"
                    costo = Musica_Ambiental
                    carrito += Musica_Ambiental

                else:
                    print("Agregaste Musica Ambiental al carrito")
                    Musica_Ambiental = 200
                    total += Musica_Ambiental
                    articulo = "Musica Ambiental"
                    costo = Musica_Ambiental
                    carrito += Musica_Ambiental

            elif select == 10:
                if extras == "SI" or extras == "Si" or extras == "si":
                    print("Agregaste a chillidog al carrito")
                    chili_ind = 15 * cantidad_personas
                    chillidog = 400 + chili_ind
                    total += chillidog
                    articulo = "Chilidog"
                    costo = chillidog
                    carrito += chillidog
                else:
                    print("Agregaste a chillidog al carrito")
                    chillidog = 400
                    total += chillidog
                    articulo = "Chilidog"
                    costo = chillidog
                    carrito += chillidog

            elif select == 11:
                if extras == "SI" or extras == "Si" or extras == "si":
                    print("Agregaste hot dog al carrito")
                    hotdog_ind = 10 * cantidad_personas
                    hotdog = 300 + hotdog_ind
                    total += hotdog
                    articulo = "Hotdog"
                    costo = hotdog
                    carrito += hotdog
                else:
                    print("Agregaste hot dog al carrito")
                    hotdog = 300
                    total += hotdog
                    articulo = "Hotdog"
                    costo = hotdog
                    carrito += hotdog

            elif select == 12:
                if extras == "SI" or extras == "Si" or extras == "si":
                    print ("Agregaste Pizza con Espagueti")
                    pizza_ind = 50 * cantidad_personas
                    pizza = 600 + pizza_ind
                    total += pizza
                    articulo = "Pizza con Espagueti"
                    costo = pizza
                    carrito += pizza
                else:
                    print ("Agregaste Pizza con Espagueti")
                    pizza = 600
                    total += pizza
                    articulo = "Pizza con Espagueti"
                    costo = pizza
                    carrito += pizza

            elif select == 13:
                if extras == "SI" or extras == "Si" or extras == "si":
                    print (" Agregaste Marinitas al carrito")
                    Marinitas_ind = 12 * cantidad_personas
                    Marinitas = 450 + Marinitas_ind
                    total += Marinitas
                    articulo = "Marinitas"
                    costo = Marinitas
                    carrito += Marinitas
                else:
                    print (" Agregaste Marinitas al carrito")
                    Marinitas = 450
                    total += Marinitas
                    articulo = "Marinitas"
                    costo = Marinitas
                    carrito += Marinitas

            else:
                print("Articulo no encontrado")

            
            lista += f"{articulo, costo}\n"
            op = input("¿Quisiera agregar otro servicio?: ")

        print("")
        print("Salon de fiestas infantiles\n'Divertilandia'")
        print("")
        print("('Renta de salon de Fiestas',  3000)")
        print(lista)
        print("Valor total del carrito es de: $", carrito)
        print("")
    nuevo_cliente = input("Nuevo cliente?: ")
    
print("Total vendido hoy: $", total)
print("Fiestas tematicas hoy: ", num_tematicas)
print("Clientes atendidos hoy: ", clientes)