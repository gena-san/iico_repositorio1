import streamlit as st
from calculos import *
from operaciones import *
from pdf_presupuesto import *

def total(cantidad, precio):
    subtotal = cantidad * precio
    return subtotal

productos = ["alfajor", "gaseosa", "chicle", "agua", "galletas"]
precios = [1500, 2800, 500, 1800, 2000]

st.title("Kiosco IICO")
cliente = st.text_input("Ingrese su nombre")
cliente = limpiar(cliente)
fecha = st.date_input("fecha")

st.markdown("### Producto 1")
producto_1 = st.selectbox("Seleccione el producto 1", productos, key="p1")
cant_1 = st.number_input(f"ingrese la cantidad de {producto_1}: ", min_value=0, step=1, key="c1")
pago_1 = st.radio("Seleccione el metodo de pago", ["efectivo", "transferencia"], key="pay1")

i_p1 = buscar_posicion(productos, producto_1)
sub1 = total(cant_1, precios[i_p1])

if producto_1 == "alfajor":
    sub1 = sub1 - (cant_1 // 3) * precios[0]
    st.write(f"(3x2 en alfajores) el subtotal es: {sub1}")
    if pago_1 == "efectivo":
        desc1 = round(calcular_descuento(sub1, 10), 2)
        iva1 = calcular_iva(desc1)
        final1 = round(sub1 - desc1 + iva1, 2)
        st.write(f"el descuento por efectivo es: {sub1-(calcular_descuento(sub1,10))}")
        st.write(f"el iva es de: {iva1}")
        st.write(f"el precio final de {cliente} es de: {final1}")
    else:
        desc1 = 0
        iva1 = calcular_iva(sub1)
        final1 = round(sub1 + iva1, 2)
        st.write(f"el iva es de: {iva1}")
        st.write(f"el precio final de {cliente} es de: {final1}")
else:
    st.write(f"el subtotal es: {sub1}")
    desc1 = 0
    if pago_1 == "efectivo":
        desc1 = round(calcular_descuento(sub1, 10), 2)
        iva1 = calcular_iva(desc1)
        final1 = round(sub1 - desc1 + iva1, 2)
        st.write(f"el descuento por efectivo es: {sub1-(calcular_descuento(sub1,10))}")
        st.write(f"el iva es de: {iva1}")
        st.write(f"el precio final de {cliente} es de: {final1}")
    else:
        iva1 = calcular_iva(sub1)
        final1 = round(sub1 + iva1, 2)
        st.write(f"el iva es de: {iva1}")
        st.write(f"el precio final de {cliente} es de: {final1}")

quiere_otro = st.radio("desea elegir otro producto?: ", ["no", "si"], key="otro")

sub2 = 0
desc2 = 0
iva2 = 0
final2 = 0

if quiere_otro == "si":
    producto_2 = st.selectbox("Seleccione el producto 2", productos, key="p2")
    cant_2 = st.number_input(f"ingrese la cantidad de {producto_2}: ", min_value=0, step=1, key="c2")
    pago_2 = st.radio("Seleccione el metodo de pago", ["efectivo", "transferencia"], key="pay2")

    i_p2 = buscar_posicion(productos, producto_2)
    sub2 = total(cant_2, precios[i_p2])

    if producto_2 == "alfajor":
        sub2 = sub2 - (cant_2 // 3) * precios[0]
        st.write(f"(3x2 en alfajores) el subtotal es: {sub2}")
        if pago_2 == "efectivo":
            desc2 = round(calcular_descuento(sub2, 10), 2)
            iva2 = calcular_iva(desc2)
            final2 = round(sub2 - desc2 + iva2, 2)
            st.write(f"el descuento por efectivo es: {sub2-(calcular_descuento(sub2,10))}")
            st.write(f"el iva es de: {iva2}")
            st.write(f"el precio final de {cliente} es de: {final2}")
        else:
            desc2 = 0
            iva2 = calcular_iva(sub2)
            final2 = round(sub2 + iva2, 2)
            st.write(f"el iva es de: {iva2}")
            st.write(f"el precio final de {cliente} es de: {final2}")
    else:
        st.write(f"el subtotal es: {sub2}")
        desc2 = 0
        if pago_2 == "efectivo":
            desc2 = round(calcular_descuento(sub2, 10), 2)
            iva2 = calcular_iva(desc2)
            final2 = round(sub2 - desc2 + iva2, 2)
            st.write(f"el descuento por efectivo es: {sub2-(calcular_descuento(sub2,10))}")
            st.write(f"el iva es de: {iva2}")
            st.write(f"el precio final de {cliente} es de: {final2}")
        else:
            iva2 = calcular_iva(sub2)
            final2 = round(sub2 + iva2, 2)
            st.write(f"el iva es de: {iva2}")
            st.write(f"el precio final de {cliente} es de: {final2}")

items_comprados = []
items_comprados.append((producto_1, cant_1, precios[i_p1]))

if quiere_otro == "si":
    items_comprados.append((producto_2, cant_2, precios[i_p2]))
    subtotal_final = sub1 + sub2
    desc_final = desc1 + desc2
    iva_final = iva1 + iva2
    total_final = final1 + final2
else:
    subtotal_final = sub1
    desc_final = desc1
    iva_final = iva1
    total_final = final1

archivo = armar_pdf(1, fecha, cliente, items_comprados, subtotal_final, desc_final, iva_final, total_final)

if cliente:
    st.download_button(
        label="Descargar presupuesto",
        data=archivo,
        file_name=f"presupuesto_{cliente}.pdf",
        mime="application/pdf"
    )
