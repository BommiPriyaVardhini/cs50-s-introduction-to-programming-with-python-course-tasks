from fpdf import FPDF

class Shirtificate(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "CS50 Shirtificate", align="C", ln=True)
        self.ln(20)

    def add_shirt(self, name):
        self.image("shirtificate.png", x=35, y=60, w=140)
        self.set_xy(35, 140)
        self.set_font("Arial", "B", 24)
        self.set_text_color(255, 255, 255)
        self.cell(140, 10, f"{name}", align="C")

def main():
    name = input("Name: ")
    pdf = Shirtificate(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.add_shirt(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
