"""
El objetivo de este trabajo es trabajar con un archivo “sucio” (es decir, desordenado y con filas repetidas), teniendo que procesar y guardar los datos para responder
diversas consultas.

1. Cargar los datos. Lo primero que debe hacer su código es cargar los datos del archivo .csv entregado a diversas estructuras. Deben estar las siguientes
estructuras mínimas, pero pueden crear más si lo consideran necesario.

1.1. tipos_de_pokemon:
Esta estructura debe almacenar todos los tipos de pokemon que
aparecen en el archivo. No se hace diferenciación entre tipos primarios y
secundarios, simplemente se debe guardar una vez cada tipo.

1.2. pokemon_por_tipo:
Esta estructura debe asociar los ids de pokemon a sus tipos. Es decir,
para cada tipo de pokemon, deben guardarse los ids de los pokemon que lo
tienen como tipo primario y los que lo tienen como tipo secundario.

1.3. info_pokemon:
Esta estructura debe asociar toda la información del pokemon menos
el tipo (es decir, nombre, HP, Ataque, defensa, generación.) al id de este.
2. Completar las funciones de consultas. En el código principal entregado
notarás que hay varias definiciones de funciones que no están completas.
Estas son las consultas que se le harán a los datos que obtuviste en el punto
anterior. Las funciones son las siguientes:

2.1 filtrar_y_ordenar_por(tipo_pokemon, criterio)
Esta función recibe un string que representa un tipo de pokemon. Debe
filtrar los pokemon que tengan ese tipo (ya sea primario o secundario) y
entregar los nombres de estos en una lista. Esa lista debe venir ordenada de
mayor a menor según el criterio recibido por la función (que puede ser HP,
Ataque o Defensa).

2.2 estadísticas(tipo_pokemon, criterio)
Esta función recibe un string que representa un tipo de pokemon. Debe
analizar los pokemon que tengan ese tipo (ya sea primario o secundario) y
obtener los estadísticos Máximo, Mínimo y Promedio del valor dado por
criterio (que puede ser HP, Ataque o Defensa). Esto debe ser entregado en
formato de diccionario, donde las llaves son el nombre del estadístico (“max”,
“min”, “prom”) y los valores deben ser justamente, los valores obtenidos.

2.3 tipos(nombre_pokemon)
Esta función recibe el nombre de un pokemon y debe retornar una
tupla, donde el primer elemento es el tipo primario del pokemon y el segundo
elemento es su tipo secundario. En caso de tener únicamente tipo primario, el
segundo elemento debe ser un string vacío.

"""


from collections import defaultdict

tipos_de_pokemon = []
pokemon_por_tipo = {} 
info_pokemon = {}

def def_value():
    file = open("pokemon.csv", "r")
    lineas = file.readlines()
    PÓKEDEX = {}
    for linea in lineas:

        lista = linea.split(",")
        lista[2] = lista[2].split(";")
        lista[6] = lista[6].split("\n")
        lista[6] = lista[6][0]

    
        id = lista[0]
        Nombre = lista[1]
        Tipo = lista[2]
        HP = lista[3]
        Attack = lista[4]
        Defense = lista[5]
        Generation = lista[6]

        if id.isnumeric():
            PÓKEDEX[int(id)] = {
                'Nombre': Nombre,
                'Tipo': Tipo,
                'Hp': int(HP),
                'Attack': int(Attack),
                'Defense': int(Defense),
                'Generation': int(Generation)
            }

            info_pokemon[id] = [Nombre,Tipo]

          

            if(lista[2][0] not in pokemon_por_tipo):
                pokemon_por_tipo[lista[2][0]] = [[id],[]]
            else:
                if(str(pokemon_por_tipo[lista[2][0]][0]) not in str(id)):
                    pokemon_por_tipo[lista[2][0]][0].append(id)               
                       

            if(lista[2][1] != ''):
                if(lista[2][1] not in pokemon_por_tipo):
                    pokemon_por_tipo[lista[2][1]] = [[],[id]]
                else:
                    if(str(pokemon_por_tipo[lista[2][1]][1]) not in str(id)):
                        pokemon_por_tipo[lista[2][1]][1].append(id)

                            

            if(lista[2][0] not in tipos_de_pokemon):
                tipos_de_pokemon.append(lista[2][0])


            if(lista[2][1] != ''):
                if(lista[2][1] not in tipos_de_pokemon):
                    tipos_de_pokemon.append(lista[2][1])


    return PÓKEDEX

def orden_segun(tipo, criterio):
    lista = []
    ordenados = []
    for id in PÓKEDEX:
        for tipe in PÓKEDEX.get(id)["Tipo"]:
            if(tipo == tipe):
                if( criterio == 'Ataque'):
                    lista.append({'Nombre':PÓKEDEX.get(id)["Nombre"],'Criterio':PÓKEDEX.get(id)["Attack"]})
                elif( criterio == 'Defensa'):
                    lista.append({'Nombre':PÓKEDEX.get(id)["Nombre"],'Criterio':PÓKEDEX.get(id)["Defense"]})
                elif( criterio == 'Hp'):
                    lista.append({'Nombre':PÓKEDEX.get(id)["Nombre"],'Criterio':PÓKEDEX.get(id)["Hp"]})
                elif( criterio == 'Generacion'):
                    lista.append({'Nombre':PÓKEDEX.get(id)["Nombre"],'Criterio':PÓKEDEX.get(id)["Generation"]})
                else:
                    return 'Criterio no Existente !'
                
    lista.sort(reverse=True, key=new_order)

    for order in lista:
        ordenados.append(order['Nombre'])

    return ordenados
def new_order(e):
  return e['Criterio']
def estadisticas(tipo, criterio):

    maximo = 0
    minimo = 100000
    lista_prom = []
    promedio = 0

    for id in PÓKEDEX:
        for tipe in PÓKEDEX.get(id)["Tipo"]:
            if(tipo == tipe):
                if( criterio == 'Ataque'):
                    if (PÓKEDEX.get(id)["Attack"] >= maximo):
                        maximo = PÓKEDEX.get(id)["Attack"]

                    if (PÓKEDEX.get(id)["Attack"] <= minimo):
                        minimo = PÓKEDEX.get(id)["Attack"]

                    lista_prom.append(PÓKEDEX.get(id)["Attack"])

                elif( criterio == 'Defensa'):
                    if (PÓKEDEX.get(id)["Defense"] >= maximo):
                        maximo = PÓKEDEX.get(id)["Defense"]

                    if (PÓKEDEX.get(id)["Defense"] <= minimo):
                        minimo = PÓKEDEX.get(id)["Defense"]

                    lista_prom.append(PÓKEDEX.get(id)["Defense"])

                elif( criterio == 'Hp'):
                    if (PÓKEDEX.get(id)["Hp"] >= maximo):
                        maximo = PÓKEDEX.get(id)["Hp"]

                    if (PÓKEDEX.get(id)["Hp"] <= minimo):
                        minimo = PÓKEDEX.get(id)["Hp"]

                    lista_prom.append(PÓKEDEX.get(id)["Hp"])

                elif( criterio == 'Generacion'):
                    if (PÓKEDEX.get(id)["Generation"] >= maximo):
                        maximo = PÓKEDEX.get(id)["Generation"]

                    if (PÓKEDEX.get(id)["Generation"] <= minimo):
                        minimo = PÓKEDEX.get(id)["Generation"]

                    lista_prom.append(PÓKEDEX.get(id)["Generation"])
                else:
                    return 'Criterio no Existente !'

    lista_prom.sort()
    promedio = sum(lista_prom)/len(lista_prom)

    resultado = {'min':minimo,'max':maximo,'prom':promedio}

    return resultado

def tipo_segun_nombre(nombre):
    lista = []
    for id in PÓKEDEX:
        if( PÓKEDEX.get(id)["Nombre"] == nombre):
            for tipe in PÓKEDEX.get(id)["Tipo"]:
                lista.append(tipe)
    return lista
       
        

## Lectura archivo y definicion estructuras ##


## Menu flujo principal ##

PÓKEDEX = def_value()
acciones = defaultdict(def_value)
acciones["1"] = "orden segun"
acciones["2"] = "estadisticas"
acciones["3"] = "encontrar tipo"
acciones["4"] = "revisar"
acciones["0"] = "salir"

continuar = True
while continuar:
    
    print('''
¿Que desea hacer?

1.- Ordenar segun criterio
2.- Obtener estadísticas
3.- Saber el tipo de un pokemon
4.- Revisar Estructuras
0.- Salir
    ''')

    accion = input()
    accion = acciones[accion]

    if accion == "orden segun":
        tipo = input("Tipo : ")
        criterio = input("Criterio :")

        orden = orden_segun(tipo, criterio)

        print(f"Ordenando pokemon de tipo {tipo} segun {criterio}:")
        for elem in orden:
            print(f"  - {elem}")

    elif accion == "estadisticas":
        tipo = input("Tipo : ")
        criterio = input("Criterio :")

        datos = estadisticas(tipo, criterio)

        print(f"Informacion de {criterio} en pokemon de tipo {tipo}")
        print(f"  - Máximo: {datos['max']}")
        print(f"  - Mínimo: {datos['min']}")
        print(f"  - Promedio: {round(datos['prom'],1)}")

    elif accion == "encontrar tipo":

        nombre = input("Nombre del Pókemon : ")

        tipos = tipo_segun_nombre(nombre)
        print(f"El tipo principal de {nombre} es {tipos[0]}")

        if tipos[1] == "":
            print(f"{nombre} no tiene tipo secundario")
        else:
            print(f"El tipo secundario de {nombre} es {tipos[1]}")

    elif accion == "revisar":

        try:
            print("Tipos Encontrados:")
            for tipo in sorted(list(tipos_de_pokemon)):
                print(f"  - {tipo}")

            print("")

            p = pokemon_por_tipo["Electric"]

            print(f"Revisando Primarios: {'25' in p[0]}")
            print(f"Revisando Secundarios: {'170' in p[1]}")

            print("")


            print("Pokemon Ejemplo:")
            i = info_pokemon["25"]
            esta = "Electric" in i
            print(f"  - ID: 25")
            print(f"  - Nombre: {i[0]}")
            print(f"  - Esta Tipo: {esta}") 
        except NameError:
            print("Esta parte no se puede ejecutar ya que aún no has definido todas las estructuras")
             

    elif accion == "salir":
        continuar = False

    else:
        print(accion)