from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_invoice(order, items):
    doc = SimpleDocTemplate(f"invoice_{order.order_id}.pdf", pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    elements.append(Paragraph(f"Factura #{order.order_id}", styles['Title']))
    elements.append(Paragraph(f"Fecha: {order.creation_date}", styles['Normal']))
    elements.append(Paragraph(f"Método de pago: {order.payment_method}", styles['Normal']))

    data = [['Producto', 'Cantidad', 'Precio Unitario', 'Subtotal']]
    for product, quantity in items.items():
        data.append([product.name, quantity, f"${product.price:.2f}", f"${product.price * quantity:.2f}"])

    data.append(['', '', 'Total', f"${order.total:.2f}"])

    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, -1), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('TOPPADDING', (0, -1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(table)
    doc.build(elements)
    print(f"Factura generada: invoice_{order.order_id}.pdf")