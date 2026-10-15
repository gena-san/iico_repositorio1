import streamlit as st
from calculos import *
from operaciones import *
from pdf_presupuesto import *
def total(cantidad,precio):
        subtotal=cantidad * precio
        return subtotal
productos = ["alfajor","gaseosa","chicle","agua"]
precios = [1500, 2800, 500, 1800]
st.title("Kiosco IICO")
cliente = st.text_input("Ingrese su nombre")
producto = st.selectbox("Seleccione el producto", productos)
cant = st.number_input(f"ingrese la cantidad de {producto}: ",min_value=0, step=1)
pago = st.radio("Seleccione el metodo de pago", ["efectivo","transferencia"])
fecha = st.date_input("fecha")
i = buscar_posicion(productos,producto)
subtotal = total(cant,precios[i])
if producto == "alfajor":
    subtotal = subtotal - (cant//3)*precios[0]
    st.write(f"el subtotal es: {subtotal}")
    if pago == "efectivo":
        desc = round(calcular_descuento(subtotal,10),2)
        iva = calcular_iva(desc)
        final = round(subtotal + desc + iva,2)
        st.write(f"el descuento por efectivo es: {subtotal-(calcular_descuento(subtotal,10))}")
        st.write(f"el iva es de: {iva}")
        st.write(f"el precio final de {cliente} es de: {final}")
    else:
        desc = 0
        iva = calcular_iva(desc)
        final = round(subtotal + calcular_iva(subtotal),2)
        st.write(f"el iva es de: {calcular_iva(subtotal)}")
        st.write(f"el precio final de {cliente} es de: {final}")
else:
    st.write(f"el subtotal es: {subtotal}")
    desc = 0
    iva = calcular_iva(desc)
    if pago == "efectivo":
        desc = round(calcular_descuento(subtotal,10),2)
        final = round(subtotal + desc + calcular_iva(desc),2)
        st.write(f"el descuento por efectivo es: {subtotal-(calcular_descuento(subtotal,10))}")
        st.write(f"el iva es de: {calcular_iva(desc)}")
        st.write(f"el precio final de {cliente} es de: {final}")
    else:
        final = round(subtotal + calcular_iva(subtotal),2)
        st.write(f"el iva es de: {calcular_iva(subtotal)}")
        st.write(f"el precio final de {cliente} es de: {final}")
archivo = armar_pdf(1,fecha,cliente,producto,cant,precios[i],subtotal,desc,iva,final)
st.download_button(
     label="Descargar presupuesto",
     data=archivo,
     file_name=f"presupuesto_{cliente}.pdf",
     mime="application/pdf"
)
