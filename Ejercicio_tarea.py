from datetime import date

fecha_orden = date(2024,2,5)
hoy = date.today()
diferencia_dias = (fecha_orden - hoy).days

ordenes = []

def agregar_orden():
    print("\n-------- AGREGANDO ORDEN --------")
    orden = {}
    orden['fecha'] = fecha_orden
    orden['cliente'] = input("Ingrese nombre del cliente: ")
    orden['fechainicioreparacion'] = fecha_orden(2024,2,12)
    orden['fechaordenlista'] = hoy
    orden['fechaclienteretiro'] = input("Ingrese la fecha cliente retiro: ")
    
    print("1. Orden normal\n2. Orden Garantía")
    tipo_orden = int(input("Seleccione tipo de orden: "))
    
    if tipo_orden == 1:
        orden['precio'] = input("Ingrese el precio de reparación: ")
        print("Orden normal agregada correctamente.")
    elif tipo_orden == 2:
        orden['referencia'] = input("Ingrese referencia: ")
        print("Orden garantía agregada correctamente.")
    else:
        print("Tipo no valido.")
        
    if 'detalles' not in ordenes:
        orden['detalles'] = []
    orden['descripcion'] = input("Ingrese descripcion de reparacion: ")
    orden['falla'] = input("Ingrese tipo de falla: ")
    orden['reparado'] = input("Ingrese si esta reparado: ")
    orden['noreparado'] = input("Ingrese informacion de porque no se reparo: ")
    
    if 'tecnicos' not in ordenes:
        orden['tecnicos'] = []
    orden['tecnico'] = input("Ingrese nombre del tecnico que atendio la orden: ")
    ordenes.append(orden)
        
def mostrar_orden():
    for i, orden in enumerate(ordenes):
        print(f"N. {i} Fecha Orden: {orden['fecha']} Nombre Cliente: {orden['cliente']}")
        
    

seguir = True
while(seguir):
    try:
        print("------ Menu Ordenes ------")
        print("1. Agregar orden")
        print("2. Mostrar ordenes")
        opcion = int(input("Seleccione una opcion: "))
    except:
        print("Opcion no valida.")
    else:
        match opcion:
            case 1:
                agregar_orden()
            case 2:
                mostrar_orden()
            case default:
                print("Opcion no valida.")