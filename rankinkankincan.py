def ejericio1():
    import random
    intentos=7
    list1 = ["electroencefalografista", "anticonstitucionalidad", "esternocleidomastoideo", "otorrinolaringologico",
             "desoxirribonucleotido", "paralelepipedo"]
    guiones = []
    aleatorio = random.randint(0, 5)
    palabra = list1[aleatorio]
    largo = len(palabra)
    for x in range(0, largo):#aca se utilizo un bucle for para hacer que el largo de la palabra a descubrir sea todo guiones#
        guiones.append("_")

       #--------------------------------------------------#

    while intentos!=0:#en esta parte se utilizo un while para que mientras los intentos no sea 0 se siga corriendo y a su vez sacando intentos de a uno#
        print(f"intentos:{intentos}")
        print(guiones)
        variable=input("pon una letra:")
        intentos-=1

        #-------------------------------------------------#

        for y in range(0,largo):#para este bucle for se hizo que cada vez que pongas una letra que este en la palabra se quite un guion y agrege la letra adivinada en ese indice#
            if variable == palabra[y]:
                guiones[y] = variable

        #-------------------------------------------------#

        #en esta seccion se utilizaron los if para que en los casos que se adivine la palabra, no se adivine o la letra ingresada no este en la palabra, aparezca un mensaje#
        if variable not in palabra:
            print(f"intentos:{intentos}")
            print("la letra no esta en la palabra")
        if "_" not in guiones or variable==palabra:
            print("ganaste")
            break
        if "_" in guiones and intentos==0:
            print("perdiste")
    #aca llore de felicidad por terminar el codigo#

    with open ('labubusificar_el_labubusificador', 'w', encoding='utf-8') as pene:
       pene.write(palabra)
def ejercicio2():
    # en estas listas se van agregar los nombres y numeros de telefono que ingrese el usuario
    contactos_nombre = []
    contactos_numero = []
    # ------------------#
    # en esta variable llamada "ola" se va a permanecer en True hasta que se elija la opcion 4 (Salir)
    ola = True
    # ------------------#
    # este while se va a ejecutar hasta que se seleccione la opcion 4
    while ola:
        print("""
           Wasap

        1)Agregar contacto
        2)Mostrar un contacto
        3)Mostrar todos los contactos
        4)Salir

        """)
        # aca se selecciona la opcion del menu
        op = int(input("ingrese una opcion:"))
        # en este if se van a ingresar contactos pidiendole que ingrese el nombre y el numero de su contacto a agregar, estos se van a guardar en las listas dichas anteriormente
        # -------------------------------#
        if op == 1:
            agregar_contacto_nombre = input("Ingrese el nombre de su contacto:")
            agregar_contacto_telefono = int(input("Ingrese el numero de su contacto:"))
            contactos_nombre.append(agregar_contacto_nombre)
            contactos_numero.append(agregar_contacto_telefono)
            print(f"¡Contactos añadidos con exito!")
        # ---------------------------------#
        # para este elif se va a buscar un contacto, para esto se va a pedir el nombre del contacto al usuario y con otro if se va a buscar el nombre dentro de la lista de contactos_nombre
        elif op == 2:
            buscar_contacto = str(input("Ingrese el nombre del contacto a buscar:"))
            if buscar_contacto in contactos_nombre:
                # aqui se va a usar un index para que se muestre al usuario uel nombre del contacto que se busco
                indice = contactos_nombre.index(buscar_contacto)
                print(f"""
                su contacto es:
                {contactos_nombre[indice], contactos_numero[indice]}
                """)
        # ----------------------------------#
        # para este elif se va a mostrar todos los contactos debido a que el usuario ingreso la opcion 3 previamente
        elif op == 3:
            print(f"""Aqui estan todos sus contactos con sus respectivos numeros:
                Nombre:{contactos_nombre}
                telefono:{contactos_numero}
            """)
            for x in range(0, len(contactos_nombre)):
                with open('balatreros', 'w', encoding='utf-8') as ola:
                    ola.write(contactos_nombre[x])
                    for z in range(0, len(contactos_numero)):
                        z=str(contactos_numero[z])
                        ola.write(z)
        # ---------------------------------#
        # y para finalizar en este else si el usuario ingresa la opcion 4 en adelante la variable "ola" se va a convertir en false haciendo que se rompa el codigo
        else:
            pepe= False
ejercicio2()