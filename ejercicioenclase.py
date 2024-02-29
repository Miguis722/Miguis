print("Bienvenido Usuario")
user = input("Por favor escriba como desea identificarse: ")
print(f"A partir de ahora, será identificado como: {user}")






menu = dict({
    "Pasteleria":{
        "Productos":list([
            {"nombre": "Torta de Cumpleaños", "valor": 25000},
            {"nombre": "Torta de Chocolate", "valor": 42000},
            {"nombre": "Torta de Tres Leches", "valor": 48000},
            {"nombre": "Torta de Maracuyá", "valor": 46000},
            {"nombre": "Torta de Amapola", "valor": 42000},
            {"nombre": "Torta de Arequipe", "valor": 42000},
            {"nombre": "Torta Envinada", "valor": 42000},
            {"nombre": "Torta de Milo", "valor": 48000},
            {"nombre": "Torta de Fresa", "valor": 42000},
            {"nombre": "Torta de Frutos Rojos", "valor": 42000},
]),
    "Promociones":list([
        {"codigo": 4, "nombre": "Compra de 2", "valor": 90000},
        {"codigo": 8, "nombre": "Compra de 3", "valor": 100000}
    ])
    } 
})   
dict({
    "Panaderia":{
        "Productos":list([
            {"nombre": "Pancito", "valor": 25000},
            {"nombre": "Pan", "valor": 42000},
            {"nombre": "Pani", "valor": 48000},
            {"nombre": "Pano", "valor": 46000},
            {"nombre": "Pana", "valor": 42000},
            {"nombre": "Pane", "valor": 42000},
            {"nombre": "Panu", "valor": 42000},
            {"nombre": "PanB", "valor": 48000},
            {"nombre": "PanC", "valor": 42000},
            {"nombre": "PanD", "valor": 42000},
]),
    "Promociones":list([
        {"codigo": 0, "nombre": "Compra de 2", "valor": 90000},
        {"codigo": 5, "nombre": "Compra de 3", "valor": 100000}
    ])
    } 
})   

print("Selereccione la categoria")
listaCategoria = list(menu.keys())

for i, val in enumerate(listaCategoria):
    print(f"{i}. {val}")
    
opcionCategoria = int(input())
datosCategoria = menu.get(listaCategoria[opcionCategoria]) 
productosCategoria = datosCategoria["Productos"]

# "Panes Dulces",
 #"Panes Salados",




#precios = 