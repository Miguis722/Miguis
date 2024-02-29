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
]),
    "Promociones":list([
        {"codigo": 4, "nombre": "Compra de 2", "valor": 90000},
        {"codigo": 8, "nombre": "Compra de 3", "valor": 100000}
    ])
    }),

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

print("Bienvenido Usuario")
user = input("Por favor escriba como desea identificarse: ")
print(f"A partir de ahora, serás identificado como: {user}")
print("Seleccione la categoria:")
listaCategoria = list(menu.keys())

for i, val in enumerate(listaCategoria):
    print(f"{i}. {val}")

opcionCategoria = int(input())   

categoriaSeleccionada = listaCategoria[opcionCategoria]

datosCategoria = menu[categoriaSeleccionada]

productosCategoria = datosCategoria["Productos"]

promocionesCategoria = datosCategoria["Promociones"]

print(f"{user} has seleccionado la categoría: {categoriaSeleccionada}")
print("Lista de productos:" )
for producto in productosCategoria:
    print(f"Nombre: {producto['nombre']}, Precio: ${producto['valor']}")

print("Promociones disponibles")
for promocion in promocionesCategoria:
    print(f"Código: {promocion['codigo']}, Nombre: {promocion['nombre']}, Precio: ${promocion['valor']}")

opcion = int(input("Escriba el número de producto que desea seleccionar: "))

productoSeleccionado = productosCategoria[opcion - 1] #Recordemos que restamos uno porque ponemos la opciones 
#desde el numero 1
nombreProducto = productoSeleccionado["nombre"]
precioProducto = productoSeleccionado["valor"]

print(f"{user} ha seleccionado el producto '{nombreProducto}' con un valor de ${precioProducto}")

dinero = int(input("Ingrese la cantidad de dinero disponible: "))

opcion_promocion = int(input("Elija una promoción (0 para ninguna): "))

if opcion_promocion != 0:
    promocion_elegida = None
    for promocion in promocionesCategoria:
        if promocion['codigo'] == opcion_promocion:
            promocion_elegida = promocion
            break

    if promocion_elegida is not None:
        precio_promocion = promocion_elegida['valor']
        print(f"Ha seleccionado la promoción: {promocion_elegida['nombre']}")

        if dinero >= precio_promocion:
            cambio = dinero - precio_promocion
            print(f"{user}, usted compró el producto '{nombreProducto}' con la promoción '{promocion_elegida['nombre']}' con un valor de ${precio_promocion}, por lo que su cambio es: ${cambio}")
        else:
            falta = precio_promocion - dinero
            print(f"{user}, el producto que desea comprar '{nombreProducto}' con la promoción '{promocion_elegida['nombre']}', con un valor de ${precio_promocion}, le falta un total de ${falta}")
    else:
        print("La promoción seleccionada no es válida.")

if dinero >= precioProducto:
     vueltos = int(dinero) - precioProducto
     print(f"{user}, usted compro el producto {nombreProducto} con un valor de ${precioProducto}, por lo que sus vueltos son: #{vueltos}")
else:
    dinerofaltante = precioProducto - dinero
    print(f"{user}, el producto que desea comprar {nombreProducto}, con un valor de ${precioProducto}, le falta un total de ${dinerofaltante}")
    