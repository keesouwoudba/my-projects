from fpdf import FPDF
from datetime import datetime

class myPdf(FPDF):
    def header(self):
        self.set_font("helvetica", "B", 50)
        self.cell(0, 50, "CS50 Shirtificate", align="C")
        self.ln(20)
        
        
        

def main():
    name = input("what's your name: ")
    pdf = myPdf(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()
    pdf.image("shirtificate.png", x=5, y=70, w=200)
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.set_y(140)
    pdf.cell(0, 10, f"{name} took CS50", align="C")
    now = datetime.now().strftime("%H-%M-%S")
    pdf.output(f"shirtificate{now}.pdf")



if __name__ == "__main__":
    main()
    
    
    
