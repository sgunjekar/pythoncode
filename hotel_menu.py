from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os

def generate_menu_card(input_file, output_pdf="SkyiCounty_Menu.pdf"):
    if not os.path.exists(input_file):
        print(f"File {input_file} not found!")
        return

    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4
    y = height - 50

    # Title
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(colors.darkgreen)
    c.drawCentredString(width / 2, y, "Skyi County Dapoli")
    y -= 30
    c.setFont("Helvetica", 14)
    c.setFillColor(colors.black)
    c.drawCentredString(width / 2, y, "Where the Forest Meets the Sky")
    y -= 40

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    c.setFont("Helvetica", 12)
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Section Header
        if line.isupper() and len(line) < 30:
            y -= 20
            c.setFont("Helvetica-Bold", 14)
            c.setFillColor(colors.darkblue)
            c.drawString(40, y, line)
            y -= 10
            c.setLineWidth(0.3)
            c.line(40, y, width - 40, y)
            y -= 15
            c.setFont("Helvetica", 12)
            c.setFillColor(colors.black)
            continue

        # Dish line
        if "₹" in line:
            try:
                name, price = line.rsplit("₹", 1)
                name = name.strip(". ").strip()
                price = price.strip()
                c.drawString(50, y, name)
                c.drawRightString(width - 50, y, f"₹{price}")
                y -= 18
            except:
                c.drawString(50, y, line)
                y -= 18
        else:
            c.drawString(50, y, line)
            y -= 18

        if y < 60:
            c.showPage()
            y = height - 50
            c.setFont("Helvetica", 12)

    c.save()
    print(f"Menu card generated: {output_pdf}")

# Usage
generate_menu_card("hotel_menu.txt")
