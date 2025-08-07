
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista[1:] if x > pivote]
        return quick_sort(menores) + iguales + quick_sort(mayores)

repartidor = {}
cantidad = int(input("¿Cuántos repartidores desea ingresar? "))

for i in range(cantidad):
    print(f"\n Repartidor #{i + 1}")
    empleado = input("Ingrese el número de empleado: ")
    nombre = input("Ingrese el nombre completo: ")
    zona = int(input("Ingrese zona: "))
    paquetes= int(input("Ingrese paquetes entregados: "))

    repartidor[empleado] = {
        "nombre": nombre,
        "zona": zona,
        "paquetes": paquetes,


    }

print("ordenar empleado por paquetes entregados")
paq_ordenado=quick_sort(list(repartidor.items()))
for empleado in paq_ordenado:
    datos = empleado[empleado]
    print(f"\nempleado: {empleado}")
    print(f"Nombre: {datos['nombre']}")
    print(f"zona: {datos['zona']}")
    print(f"paquete: {datos['paquete']}")


print("\nBúsqueda de empleado")
buscado = input("Ingrese codigo de empleado: ")

if buscado in repartidor:
    emp = repartidor[buscado]
    print("\nrepartidor:")
    print(f"Nombre: {emp['nombre']}")
    print(f"zona: {emp['zona']}")
    print(f"paquete: {emp['paquete']}")

else:
    print("repartidor no encontrado.")