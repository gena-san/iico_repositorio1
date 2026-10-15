"""
operaciones.py - Operaciones sobre las tres listas del presupuesto.

>>> REGLA DE ORO DE ESTE ARCHIVO <<<
Aca tampoco puede haber ni un print() ni un input().

>>> SEGUNDA REGLA, LA QUE MAS PUNTOS DA Y MAS SE OLVIDA <<<
Ninguna de estas funciones modifica las listas que recibe.
Cada una ARMA TRES LISTAS NUEVAS y las DEVUELVE juntas:

    nuevos_nombres = []
    nuevas_cantidades = []
    nuevos_precios = []
    for i in range(len(nombres)):
        nuevos_nombres.append(nombres[i])
        nuevas_cantidades.append(cantidades[i])
        nuevos_precios.append(precios[i])
    ...
    return nuevos_nombres, nuevas_cantidades, nuevos_precios

Si haces nombres.append(...) o cantidades[i] = ... estas tocando las listas
originales, y eso rompe el programa cuando el Nucleo 4 las muestre en pantalla.

>>> LAS TRES LISTAS SE TOCAN SIEMPRE JUNTAS <<<
Si agregas un nombre tenes que agregar tambien su cantidad y su precio.
Si borras la posicion 2 de una, borras la posicion 2 de las tres. Si se
desalinean, el presupuesto queda mal para siempre.

Comparacion de nombres: siempre SIN distinguir mayusculas y sin espacios de
sobra. "Camara", "camara" y " CAMARA " son el mismo articulo.
Se resuelve con .strip().lower() de los dos lados.
"""


# ---------------------------------------------------------------- 1 de 4
def buscar_posicion(nombres, nombre):
    """Devuelve la POSICION del articulo en la lista, o -1 si no esta.

    No devuelve True/False ni el nombre: devuelve el numero de posicion,
    que despues sirve para las tres listas.
    La comparacion no distingue mayusculas ni espacios de sobra.

    buscar_posicion(["camara", "cubierta", "cadena"], "CUBIERTA") -> 1
    buscar_posicion(["camara", "cubierta", "cadena"], "farol") -> -1
    buscar_posicion([], "camara") -> -1
    """
    for i in range(len(nombres)):
        if nombres[i].strip().lower() == nombre.strip().lower():
            return i
    return -1
    # TU CODIGO ACA
    pass
# ---------------------------------------------------------------- 2 de 4
def agregar_articulo(nombres, cantidades, precios, nombre, cantidad, precio):
    """Devuelve TRES listas NUEVAS con el articulo agregado.

    Si el nombre NO estaba, se agrega un renglon nuevo al final de las tres.
    Si el nombre YA estaba (sin distinguir mayusculas), NO se duplica el
    renglon: se le suma la cantidad al que ya existe y se conserva su precio.

    agregar_articulo([], [], [], "camara", 2, 8500.0)
        -> (["camara"], [2], [8500.0])
    agregar_articulo(["camara"], [2], [8500.0], "CAMARA", 3, 8500.0)
        -> (["camara"], [5], [8500.0])      un solo renglon, cantidad sumada
    """
    nuevos_nombres = []
    nuevas_cantidades = []
    nuevos_precios = []
    for i in range(len(nombres)):
        nuevos_nombres.append(nombres[i])
        nuevas_cantidades.append(cantidades[i])
        nuevos_precios.append(precios[i])
    if buscar_posicion(nombres, nombre) == -1:
        nuevos_nombres.append(nombre)
        nuevas_cantidades.append(cantidad)
        nuevos_precios.append(precio)
    else:
        pos = buscar_posicion(nombres, nombre)
        nuevas_cantidades[pos] += cantidad
    return nuevos_nombres, nuevas_cantidades, nuevos_precios
    # TU CODIGO ACA
    pass


# ---------------------------------------------------------------- 3 de 4
def modificar_cantidad(nombres, cantidades, precios, nombre, nueva_cantidad):
    """Devuelve TRES listas NUEVAS con la cantidad de ese articulo cambiada.

    Si el articulo no esta, devuelve las tres listas igual (copias, sin cambios).
    Si nueva_cantidad es menor a 1, la cantidad no es valida: devuelve las tres
    listas igual, sin tocar nada.

    modificar_cantidad(["camara", "cadena"], [2, 1], [8500.0, 19000.0], "camara", 10)
        -> (["camara", "cadena"], [10, 1], [8500.0, 19000.0])
    Con cantidad 0 -> las listas quedan como estaban.
    """
    nuevos_nombres = []
    nuevas_cantidades = []
    nuevos_precios = []
    for i in range(len(nombres)):
        nuevos_nombres.append(nombres[i])
        nuevos_precios.append(precios[i])
        if nombres[i].strip().lower() == nombre.strip().lower():
            if nueva_cantidad >= 1:
                nuevas_cantidades.append(nueva_cantidad)
            else:
                nuevas_cantidades.append(cantidades[i])
        else:
            nuevas_cantidades.append(cantidades[i])
    return nuevos_nombres, nuevas_cantidades, nuevos_precios
    # TU CODIGO ACA
    pass


# ---------------------------------------------------------------- 4 de 4
def eliminar_articulo(nombres, cantidades, precios, nombre):
    """Devuelve TRES listas NUEVAS sin ese articulo.

    Se saca la misma posicion de las tres listas: si sacas el nombre y te
    olvidas la cantidad, el presupuesto queda desalineado.
    Si el articulo no esta, devuelve las tres listas igual.

    eliminar_articulo(["camara", "cadena"], [2, 1], [8500.0, 19000.0], "CAMARA")
        -> (["cadena"], [1], [19000.0])
    """
    nuevos_nombres = []
    nuevas_cantidades = []
    nuevos_precios = []
    for i in range(len(nombres)):
        if nombres[i].strip().lower() != nombre.strip().lower():
            nuevos_nombres.append(nombres[i])
            nuevas_cantidades.append(cantidades[i])
            nuevos_precios.append(precios[i])
    return nuevos_nombres, nuevas_cantidades, nuevos_precios
    # TU CODIGO ACA
    pass