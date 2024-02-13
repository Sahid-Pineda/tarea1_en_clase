from datetime import datetime, timedelta

ordenes_reparacion = []
tecnicos = []

def ingresar_orden():
    orden = {}
    orden['Identificador'] = len(ordenes_reparacion) + 1
    orden['Fecha de Orden'] = input("Ingrese la fecha de la orden (YYYY-MM-DD): ")
    orden['Cliente'] = input("Ingrese el nombre del cliente: ")
    orden['Fecha de Inicio'] = input("Ingrese la fecha de inicio de reparación (YYYY-MM-DD): ")
    orden['Fecha de Presentación'] = input("Ingrese la fecha de presentación para retiro (YYYY-MM-DD): ")
    orden['Fecha de Retiro'] = input("Ingrese la fecha de retiro por el cliente (deje en blanco si aún no se retira): ")

    tipo_orden = input("Ingrese el tipo de orden (Normal/Garantía): ").lower()
    orden['Tipo de Orden'] = tipo_orden

    if tipo_orden == 'normal':
        orden['Precio'] = float(input("Ingrese el precio: "))
    elif tipo_orden == 'garantia':
        orden['Documento de Referencia'] = input("Ingrese el documento de referencia: ")
        orden['Vigencia de Garantía'] = 15  # Días de garantía

    orden['Detalles de Aparatos'] = []

    while True:
        detalle = {}
        detalle['Descripción del Aparato'] = input("Ingrese la descripción del aparato electrónico: ")
        detalle['Falla del Aparato'] = input("Ingrese la falla del aparato: ")
        detalle['Estado de Reparación'] = input("¿Se reparó el aparato? (Sí/No): ").lower()

        orden['Detalles de Aparatos'].append(detalle)

        continuar = input("¿Desea agregar otro aparato? (Sí/No): ").lower()
        if continuar != 'sí':
            break

    ordenes_reparacion.append(orden)

def ingresar_tecnico():
    tecnico = {}
    tecnico['Identificador de Técnico'] = len(tecnicos) + 1
    tecnico['Nombre del Técnico'] = input("Ingrese el nombre del técnico: ")
    tecnicos.append(tecnico)

def en_garantia(orden):
    if 'Vigencia de Garantía' in orden:
        fecha_retiro = datetime.strptime(orden['Fecha de Retiro'], "%Y-%m-%d")
        fecha_limite_garantia = fecha_retiro + timedelta(days=orden['Vigencia de Garantía'])
        hoy = datetime.now()
        return hoy <= fecha_limite_garantia
    else:
        return False

def mostrar_ordenes():
    print("\nLista de ordenes: ")
    for orden in ordenes_reparacion:
        print("\nOrden ID:", orden['Identificador'])
        print("Fecha de Orden:", orden['Fecha de Orden'])
        print("Cliente:", orden['Cliente'])
        print("Fecha de Inicio:", orden['Fecha de Inicio'])
        print("Fecha de Presentación:", orden['Fecha de Presentación'])
        print("Fecha de Retiro:", orden['Fecha de Retiro'])

        if en_garantia(orden):
            print("Estado de Garantía: Dentro del período de garantía")
        else:
            print("Estado de Garantía: Garantía expirada")

        print("Tipo de Orden:", orden['Tipo de Orden'])

        if orden['Tipo de Orden'] == 'normal':
            print("Precio:", orden['Precio'])
        elif orden['Tipo de Orden'] == 'garantía':
            print("Documento de Referencia:", orden['Documento de Referencia'])

        print("Detalles de Aparatos:")
        for detalle in orden['Detalles de Aparatos']:
            print("- Descripción:", detalle['Descripción del Aparato'])
            print("- Falla:", detalle['Falla del Aparato'])
            print("- Estado de Reparación:", detalle['Estado de Reparación'])

seguir = True

while(seguir):
    try:
        print("\nMenú:")
        print("1. Ingresar Orden de Reparación")
        print("2. Ingresar Técnico")
        print("3. Mostrar ordenes")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))
    except:
        print("Opcion no válida.")
    else:
        match opcion:
            case 1:
                ingresar_orden()
            case 2:
                ingresar_tecnico()
            case 3:
                mostrar_ordenes()
            case 4:
                print("Saliendo...")
                seguir = False
            case default:
                print("Opcion no válida. Intente de nuevo")