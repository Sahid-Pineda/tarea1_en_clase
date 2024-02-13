ordenes = []

def agregar_ordenes():
    print("---- AGREGANDO UNA ORDEN ----")
    orden = {}
    orden['fecha'] = input("Ingrese fecha: ")
    orden['cliente'] = input("Ingrese nombre del cliente: ")

agregar_ordenes()