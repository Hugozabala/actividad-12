def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x[1]['paquetes'] < pivote[1]['paquetes']]
        iguales = [x for x in lista if x[1]['paquetes'] == pivote[1]['paquetes']]
        mayores = [x for x in lista[1:] if x[1]['paquetes'] > pivote[1]['paquetes']]
        return quick_sort(menores) + iguales + quick_sort(mayores)


repartidor = {}
cantidad = int(input("¿Cuántos repartidores desea ingresar? "))


for i in range(cantidad):
    print(f"\nRepartidor #{i + 1}")
    empleado = input("Ingrese el número de empleado: ")
    nombre = input("Ingrese el nombre completo: ")
    zona = int(input("Ingrese zona: "))
    paquetes = int(input("Ingrese paquetes entregados: "))

    repartidor[empleado] = {
        "nombre": nombre,
        "zona": zona,
        "paquetes": paquetes,
    }


print("\n--- Empleados ordenados por paquetes entregados ---")
paq_ordenado = quick_sort(list(repartidor.items()))
for codigo, datos in paq_ordenado:
    print(f"\nCódigo de empleado: {codigo}")
    print(f"Nombre: {datos['nombre']}")
    print(f"Zona: {datos['zona']}")
    print(f"Paquetes entregados: {datos['paquetes']}")


print("\n--- Búsqueda de empleado ---")
buscado = input("Ingrese código de empleado: ")

if buscado in repartidor:
    emp = repartidor[buscado]
    print(f"\nEmpleado encontrado:")
    print(f"Nombre: {emp['nombre']}")
    print(f"Zona: {emp['zona']}")
    print(f"Paquetes entregados: {emp['paquetes']}")
else:
    print("Repartidor no encontrado.")