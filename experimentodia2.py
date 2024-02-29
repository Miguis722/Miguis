# Categorias = ["Pasteleria", "Panaderia", "Bebidas"]
#Se crea el diccionario el cual almacenara 3 categorias (pasteleria, panaderia y bebidas)
menu = dict({
    "Pasteleria":({
        "Productos":list([
            {"nombre": "1 - Torta de Cumpleaños", "valor": 25000},
            {"nombre": "2 - Torta de Chocolate", "valor": 42000},
            {"nombre": "3 - Torta de Tres Leches", "valor": 48000},
            {"nombre": "4 - Torta de Maracuyá", "valor": 46000},
            {"nombre": "5 - Torta de Amapola", "valor": 42000},
            {"nombre": "6 - Torta de Arequipe", "valor": 42000},
            {"nombre": "7 - Torta Envinada", "valor": 42000},
            {"nombre": "8 - Torta de Milo", "valor": 48000},
            {"nombre": "9 - Torta de Fresa", "valor": 42000},
            {"nombre": "10 - Torta de Frutos Rojos", "valor": 42000}
    #Despues de haber creado la lista de 10 productos de pasteleria, procedemos creando una SUBlista en la que se almacenaran los descuentos a aplicar.
]),
    "Promociones":list([
        {"codigo": 4, "nombre": "Compra de 2", "valor": 90000},
        {"codigo": 8, "nombre": "Compra de 3", "valor": 100000}
    ])
    }),
#Despues procedemos cerrando parentesis, corchetes y llaves, continuamos con la siguiente categoria del diccionario
    "Panaderia":{
        "Productos":list([
            {"nombre": "1 - Pan de leche", "valor": 2500},
            {"nombre": "2 - Pan de fruta", "valor": 3000},
            {"nombre": "3 - Pan de bocadillo", "valor": 5000},
            {"nombre": "4 - Pan de chocolate", "valor": 12000},
            {"nombre": "5 - Pan de queso", "valor": 2000},
            {"nombre": "6 - Pan de pescado", "valor": 2500},
            {"nombre": "7 - Pan de tomate", "valor": 2500},
            {"nombre": "8 - Pan de yuca", "valor": 3000},
            {"nombre": "9 - Pan de breva", "valor": 5000},
            {"nombre": "10 - Pan de arequipe", "valor": 3500}
    #Repetimos el mismo proceso las veces que queramos, asi haciendo más larga nuestro diccionario
        ]),
        "Promociones":list([
            {"codigo": 3, "nombre": "Compra de 2", "valor": 20000},
            {"codigo": 9, "nombre": "Compra de 3", "valor": 12000}
        ])},

    "Bebidas":({
        "Productos":list([
            {"nombre": "1 - Gaseosa Coca Cola", "valor": 2000},
            {"nombre": "2 - Gaseosa 7UP", "valor": 2000},
            {"nombre": "3 - Gaseosa Pepsi Cola", "valor": 2000},
            {"nombre": "4 - Gaseosa Canada Dry", "valor": 3000},
            {"nombre": "5 - Gaseosa Quatro", "valor": 2000},
            {"nombre": "6 - Gaseosa Sprite", "valor": 2000},
            {"nombre": "7 - Gaseosa Colombiana", "valor": 2000},
            {"nombre": "8 - Milo", "valor": 8000},
            {"nombre": "9 - Café", "valor": 2000},
            {"nombre": "10 - Soda Gran Bretaña", "valor": 4000}
    ]),
    "Promociones":list([
        {"codigo": 4, "nombre": "Compra de 2", "valor": 5000},
        {"codigo": 8, "nombre": "Compra de 3", "valor": 10000}
    ])
})
})
#Saludo hacia el usuario, pediremos un nombre al usuario para poder llamarlo de esa forma, para no decirle todo el tiempo un nombre muy "Habitual"
#Por lo que colocamos una variable donde guardaremos como desea que se le llame
print("Bienvenido Usuario")
user = input("Por favor escriba como desea identificarse: ")
print(f"A partir de ahora, serás identificado como: {user}")

 
#Seleccion de la Categoria (Se muestra categoria y se pide que se escoja cual desea)
print("Seleccione la categoria:")
listaCategoria = list(menu.keys())

#En esta funcion se empieza a enlistar y a enumerar las categorias para el usuario
for i, val in enumerate(listaCategoria):
    print(f"{i}. {val}")
    
#Adquirimos el número de categoria al cual desea dirigirse el usuario
opcionCategoria = int(input())   


categoriaSeleccionada = listaCategoria[opcionCategoria]

datosCategoria = menu[categoriaSeleccionada]

productosCategoria = datosCategoria["Productos"]

promocionesCategoria = datosCategoria["Promociones"]

print(f"{user} has seleccionado la categoría: {categoriaSeleccionada}")

#Una vez ya seleccionada la categoria, procedemos a mostrar los productos especificos de cada categoria
print("Lista de productos:" )
for producto in productosCategoria:
    print(f"Nombre: {producto['nombre']}, Precio: ${producto['valor']}")

#Además, mostramos las prmociones disponibles en la categoria seleccionada
print("Promociones disponibles")
for promocion in promocionesCategoria:
    print(f"Código: {promocion['codigo']}, Nombre: {promocion['nombre']}, Precio: ${promocion['valor']}")

#

opcion = int(input("Escriba el número de producto que desea seleccionar: "))

productoSeleccionado = productosCategoria[opcion - 1] #Recordemos que retiramos uno porque ponemos la opciones 
#desde el numero 1
nombreProducto = productoSeleccionado["nombre"]
precioProducto = productoSeleccionado["valor"]

print(f"{user} ha seleccionado el producto '{nombreProducto}' con un valor de ${precioProducto}")

#Cobro del monto a pagar ("Facturacion")
#Se pide al cliente que digite la cantidad de dinero que tiene en el momento para pagar el o los productos que desea adquirir
dinero = int(input("Ingrese la cantidad de dinero disponible: "))

opcion_promocion = int(input("Elija una promoción que desea aplicar (0 para ninguna): "))

if opcion_promocion != 0:
    promocion_elegida = None
    for promocion in promocionesCategoria:
        if promocion['codigo'] == opcion_promocion:
            promocion_elegida = promocion
            break

#     ↑     Se pide que escoja una promocion de las que estan disponibles en el momento, aunque tambien puede escoger no aplicar ninguna promocion y pasar directamente a pagar.
        # 

    if promocion_elegida is not None:
        precio_promocion = promocion_elegida['valor']
        print(f"Ha seleccionado la promoción: {promocion_elegida['nombre']}")

# Proceso de pago del producto, EN CASO DE HABER ESCOGIDO UNA PROMOCION.
        
        if dinero >= precio_promocion:
            cambio = dinero - precio_promocion
            print(f"{user}, usted compró el producto '{nombreProducto}' con la promoción '{promocion_elegida['nombre']}' con un valor de ${precio_promocion}, por lo que su cambio es: ${cambio}")
        else:
            falta = precio_promocion - dinero
            print(f"{user}, el producto que desea comprar '{nombreProducto}' con la promoción '{promocion_elegida['nombre']}', con un valor de ${precio_promocion}, le falta un total de ${falta}")
    else:
        print("La promoción seleccionada no es válida.")

# Proceso para el pago del producto, EN CASO DE QUE NO HAYA ESCOGIDO UNA PROMOCION, despues de haber pedido el dinero aqui se hace la resta para saber si puede adquirir el producto o no
        #gracias a que el producto tiene un precio pre-establecido.
        
if dinero >= precioProducto:
     vueltos = int(dinero) - precioProducto
     print(f"{user}, usted compro el producto {nombreProducto} con un valor de ${precioProducto}, por lo que sus vueltos son: ${vueltos}, Muchas Gracias por adquirir nuestros productos")
else:
    dinerofaltante = precioProducto - dinero
    print(f"{user}, el producto que desea comprar {nombreProducto}, con un valor de ${precioProducto}, le falta un total de ${dinerofaltante}")
    
