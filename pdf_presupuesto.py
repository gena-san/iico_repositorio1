from fpdf import FPDF

NOMBRE_KIOSCO = "Kiosco IICO"
LOGO = "IICO.png"

def renglon(pdf, texto, valor):
    pdf.cell(120, 9, texto)
    pdf.cell(0, 9, valor, align="R", new_x="LMARGIN", new_y="NEXT")

def armar_pdf(numero, fecha, cliente, lista_items, subtotal, descuento, iva, total):
    pdf = FPDF()
    pdf.add_page()

    pdf.image(LOGO, x=10, y=10, w=70)
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, NOMBRE_KIOSCO, align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 7, f"Presupuesto N° {numero}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 7, f"Fecha: {fecha}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(15)

    pdf.set_font("Helvetica", "", 12)
    renglon(pdf, "Cliente", cliente)
    pdf.ln(2)
    
    pdf.set_font("Helvetica", "B", 11)
    renglon(pdf, "Producto / Cantidad", "Subtotal")
    pdf.set_font("Helvetica", "", 11)
    
    for producto, cantidad, precio_unitario in lista_items:
        sub_prod = cantidad * precio_unitario
        renglon(pdf, f"- {cantidad} x {producto}", f"${sub_prod:.2f}")
    
    pdf.ln(4)

    renglon(pdf, "Subtotal", f"${subtotal:.2f}")
    renglon(pdf, "Descuento", f"-${descuento:.2f}")
    renglon(pdf, "IVA 21%", f"${iva:.2f}")
    pdf.set_font("Helvetica", "B", 14)
    renglon(pdf, "TOTAL", f"${total:.2f}")

    pdf.ln(10)
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 6, "Presupuesto válido por 7 días.", new_x="LMARGIN", new_y="NEXT")

    return bytes(pdf.output())
