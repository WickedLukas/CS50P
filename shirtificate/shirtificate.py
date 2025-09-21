from fpdf import FPDF, Align


description_text = "CS50 Shirtificate"

# Ask user for the name which shall be printed on the shirt.
name = input("Name: ")
shirt_text = f"{name} took CS50"

pdf = FPDF(orientation="portrait", format="A4")
pdf.add_page()

# Add description text.
pdf.set_font("helvetica", style="B", size=40)
pdf.cell(text=description_text, h=pdf.eph/6, align=Align.C, center=True)

# Insert image.
pdf.image("shirtificate.png", x=Align.C, y=pdf.eph/5, w=pdf.epw, keep_aspect_ratio=True)

# Add shirt text withe the given name.
pdf.set_font(size=25)
pdf.set_text_color(255, 255, 255)
pdf.cell(text=shirt_text, h=pdf.eph*8/10, align=Align.C, center=True)

# Output pdf.
pdf.output("shirtificate.pdf")
