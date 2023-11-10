from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", size= 45)
        self.cell(0, 57, "CS50 Shirtificate", align= "C")
        self.ln(20)


def create_shirt(s):
    pdf = PDF()
    pdf.add_page(orientation= "P")
    pdf.set_font("helvetica", size= 24)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 215, f"{s} took CS50", align= "C")
    pdf.output("shirtificate.pdf")


def main():
    create_shirt(input("Name: "))

if __name__ == "__main__":
    main()