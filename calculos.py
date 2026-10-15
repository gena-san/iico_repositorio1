"""
calculos.py - Logica de calculo del presupuesto.

>>> REGLA DE ORO DE ESTE ARCHIVO <<<
Aca NO puede haber ni un print() ni un input(). Ni uno.
Cada funcion recibe datos, calcula y DEVUELVE el resultado con return.
El programa que corrige revisa esto automaticamente.

EL PRESUPUESTO SON TRES LISTAS PARALELAS
----------------------------------------
    nombres    = ["teclado", "mouse", "monitor"]
    cantidades = [2,          3,       1]
    precios    = [15000.0,    8000.0,  210000.0]

La POSICION es el hilo que las une: nombres[1], cantidades[1] y precios[1]
son el nombre, la cantidad y el precio DEL MISMO articulo.

Ojo: las funciones de este archivo casi nunca necesitan la lista de nombres.
Para calcular alcanza con cantidades y precios. Fijate en la firma de cada una.

Para recorrer dos listas paralelas se recorre la POSICION, no la lista:

    for i in range(len(cantidades)):
        ... cantidades[i] ... precios[i] ...

ORDEN DE LAS CUENTAS, SIEMPRE ESTE
----------------------------------
    subtotal -> descuento sobre el subtotal -> IVA 21% sobre el monto YA DESCONTADO
    -> total = monto descontado + IVA
Todos los montos se devuelven redondeados a 2 decimales con round(valor, 2).

PRESUPUESTO DE EJEMPLO QUE SE USA EN LOS DOCSTRINGS
---------------------------------------------------
    cantidades = [2, 3, 1]   y   precios = [15000.0, 8000.0, 210000.0]
    con 10 de descuento:
    subtotal 264000.0 | descuento 26400.0 | descontado 237600.0
    iva 49896.0 | total 287496.0
"""

IVA = 0.21


# ---------------------------------------------------------------- 1 de 9
def subtotal_renglon(cantidad, precio):
    """Devuelve cantidad * precio, redondeado a 2 decimales.

    Esta funcion no recibe listas: recibe los dos numeros de UN renglon.
    subtotal_renglon(3, 8000.0) -> 24000.0
    """
    return round(cantidad * precio, 2)
    # TU CODIGO ACA
    pass


# ---------------------------------------------------------------- 2 de 9
def calcular_subtotal(cantidades, precios):
    """Devuelve la suma de todos los renglones, con 2 decimales.

    calcular_subtotal([2, 3, 1], [15000.0, 8000.0, 210000.0]) -> 264000.0
    Con las listas vacias -> 0.0
    (Podes apoyarte en subtotal_renglon en vez de repetir la multiplicacion.)
    """
    total = 0
    for i in range(len(cantidades)):
        total += subtotal_renglon(cantidades[i], precios[i])
    return round(total, 2)


# ---------------------------------------------------------------- 3 de 9
def calcular_descuento(subtotal, porcentaje):
    """Devuelve CUANTA PLATA se descuenta (no el monto ya descontado).

    calcular_descuento(264000.0, 10) -> 26400.0
    Si el porcentaje no esta entre 0 y 100, el descuento no vale: devuelve 0.0
    calcular_descuento(264000.0, 150) -> 0.0
    """
    if porcentaje < 0 or porcentaje > 100:
        return 0.0
    else:
        return round((subtotal * porcentaje)/100, 2)
    # TU CODIGO ACA
    pass


# ---------------------------------------------------------------- 4 de 9
def aplicar_descuento(subtotal, porcentaje):
    """Devuelve el subtotal YA DESCONTADO, con 2 decimales.

    aplicar_descuento(264000.0, 10) -> 237600.0
    Si el porcentaje no esta entre 0 y 100 se rechaza y devuelve el monto sin tocar:
    aplicar_descuento(264000.0, -5) -> 264000.0
    (Ojo: esta funcion puede apoyarse en la anterior en vez de repetir la cuenta.)
    """
    return round((subtotal - calcular_descuento(subtotal, porcentaje)), 2)
    # TU CODIGO ACA
    pass


# ---------------------------------------------------------------- 5 de 9
def calcular_iva(monto):
    """Devuelve el 21% del monto que recibe, redondeado a 2 decimales.

    calcular_iva(237600.0) -> 49896.0
    Cuidado: el IVA se calcula sobre el monto YA DESCONTADO.
    Si lo calculas sobre el subtotal sin descontar el total te va a dar 293040.0,
    que es el error mas comun de todo el trabajo.
    """
    porcentaje = 21
    return round((monto * porcentaje) / 100, 2)
    # TU CODIGO ACA
    pass


# ---------------------------------------------------------------- 6 de 9
def contar_unidades(cantidades):
    """Devuelve cuantas unidades hay en total sumando la lista de cantidades.

    contar_unidades([2, 3, 1]) -> 6
    Con la lista vacia -> 0
    Ojo: no es len(cantidades). len te da cuantos RENGLONES hay, no cuantas
    unidades. Con [2, 3, 1] len da 3 y la respuesta es 6.
    """
    return sum(cantidades)
    # TU CODIGO ACA
    pass


# ---------------------------------------------------------------- 7 de 9
def posicion_mas_caro(cantidades, precios):
    """Devuelve la POSICION del renglon de mayor subtotal (cantidad x precio).

    No devuelve el nombre ni el monto: devuelve el numero de posicion, para
    que quien llama pueda usarlo en las tres listas.

    posicion_mas_caro([2, 3, 1], [15000.0, 8000.0, 210000.0]) -> 2
    Con las listas vacias -> -1
    Ojo: es por SUBTOTAL, no por precio unitario. 10 lapiceras de $100 (1000)
    pesan mas que 1 pendrive de $500 (500).
    """
    mayor=0
    for i in range(len(cantidades)-1):
        if len(cantidades) == 0:
            return -1
        else:
            if subtotal_renglon(cantidades[i],precios[i]) > subtotal_renglon(cantidades[i+1], precios[i+1]):
                mayor=i
    return mayor
    # TU CODIGO ACA
    pass


# ---------------------------------------------------------------- 8 de 9
def promedio_por_renglon(cantidades, precios):
    """Devuelve el subtotal dividido por la CANTIDAD DE RENGLONES, con 2 decimales.

    promedio_por_renglon([2, 3, 1], [15000.0, 8000.0, 210000.0]) -> 88000.0
    (264000 dividido 3 renglones)
    Con las listas vacias -> 0.0  (no puede romper por division por cero)
    """
    if len(cantidades) == 0:
        return 0.0
    else:
        return round(calcular_subtotal(cantidades,precios) / len(cantidades),2)
    # TU CODIGO ACA
    pass


# ---------------------------------------------------------------- 9 de 9
def resumen_presupuesto(cantidades, precios, porcentaje):
    """Funcion coordinadora: NO hace cuentas nuevas, llama a las anteriores.

    Devuelve CINCO valores de una sola vez, siempre en este orden:

        return subtotal, descuento, descontado, iva, total

    (Eso arma una tupla. Quien la recibe la desarma en una linea:
     subtotal, descuento, descontado, iva, total = resumen_presupuesto(...) )

    Con el ejemplo y 10 de descuento:
        (264000.0, 26400.0, 237600.0, 49896.0, 287496.0)
    Con las listas vacias: (0.0, 0.0, 0.0, 0.0, 0.0)
    """
    return (calcular_subtotal(cantidades,precios), calcular_descuento(calcular_subtotal(cantidades,precios), porcentaje), aplicar_descuento(calcular_subtotal(cantidades,precios), porcentaje), calcular_iva(aplicar_descuento(calcular_subtotal(cantidades,precios), porcentaje)), aplicar_descuento(calcular_subtotal(cantidades,precios), porcentaje)+calcular_iva(aplicar_descuento(calcular_subtotal(cantidades,precios), porcentaje)))
    # TU CODIGO ACA
    pass
