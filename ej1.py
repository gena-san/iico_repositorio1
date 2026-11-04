import streamlit as st
from calculos import *
from operaciones import *
from pdf_presupuesto import *
def total(cantidad, precio):
    return cantidad * precio
def procesar_y_mostrar(cliente, producto, cant, pago, precios, productos):
    i = buscar_posicion(productos, producto)
    subtotal = total(cant, precios[i])
    if producto == "alfajor":
        subtotal = subtotal - (cant // 3) * precios[0]
        st.write(f"(3x2 en alfajores) el subtotal es: {subtotal}")
    else:
        st.write(f"el subtotal es: {subtotal}")
    desc = 0
    if pago == "efectivo":
        desc = round(calcular_descuento(subtotal, 10), 2)
        iva = calcular_iva(subtotal - desc)
        final = round(subtotal - desc + iva, 2)
        st.write(f"el descuento por efectivo es: {desc}")
        st.write(f"el iva es de: {iva}")
        st.write(f"el precio final de {cliente} es de: {final}")
    else:
        iva = calcular_iva(subtotal)
        final = round(subtotal + iva, 2)
        st.write(f"el iva es de: {iva}")
        st.write(f"el precio final de {cliente} es de: {final}")
    return subtotal, desc, iva, final
productos = ["alfajor", "gaseosa", "chicle", "agua", "galletas"]
precios = [1500, 2800, 500, 1800, 2000]
st.title("Kiosco IICO")
cliente = st.text_input("Ingrese su nombre")
fecha = st.date_input("fecha")
st.write("Producto 1")
producto_1 = st.selectbox("Seleccione el producto 1", productos, key="p1")
cant_1 = st.number_input(f"Ingrese la cantidad de {producto_1}:", min_value=0, step=1, key="c1")
pago_1 = st.radio("Método de pago (Producto 1)", ["efectivo", "transferencia"], key="pay1")
sub1, desc1, iva1, final1 = procesar_y_mostrar(cliente, producto_1, cant_1, pago_1, precios, productos)
st.write("Producto 2 (Opcional)")
quiere_otro = st.radio("¿Desea elegir otro producto?", ["no", "si"], key="otro")

if quiere_otro == "si":
    producto_2 = st.selectbox("Seleccione el producto 2", productos, key="p2")
    cant_2 = st.number_input(f"Ingrese la cantidad de {producto_2}:", min_value=0, step=1, key="c2")
    pago_2 = st.radio("Método de pago (Producto 2)", ["efectivo", "transferencia"], key="pay2")
    sub2, desc2, iva2, final2 = procesar_y_mostrar(cliente, producto_2, cant_2, pago_2, precios, productos)
    subtotal_total = sub1 + sub2
    desc_total = desc1 + desc2
    iva_total = iva1 + iva2
    final_total = final1 + final2
    st.write(f"Total general a pagar por {cliente}: ${final_total}")
    i_p1 = buscar_posicion(productos, producto_1)
    archivo = armar_pdf(1, fecha, cliente, f"{producto_1} y {producto_2}", cant_1, precios[i_p1], subtotal_total, desc_total, iva_total, final_total)
else:
    i_p1 = buscar_posicion(productos, producto_1)
    archivo = armar_pdf(1, fecha, cliente, producto_1, cant_1, precios[i_p1], sub1, desc1, iva1, final1)

if cliente:
    st.download_button(
         label="Descargar presupuesto",
         data=archivo,
         file_name=f"presupuesto_{cliente}.pdf",
         mime="application/pdf"
    )