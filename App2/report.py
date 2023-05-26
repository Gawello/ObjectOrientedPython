import webbrowser
import os
from fpdf import FPDF


class PdfReport:
    """
    Creates a PDF file that contains data about the flatmates such as their due amount and the period of the bill.
    """

    def __init__(self, file_name):
        self.file_name = file_name

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add icon
        pdf.image(name="files/house.png", w=30, h=30)

        # Insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert Period label and value
        pdf.set_font(family="Times", size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        # Insert name and due amount to pay of second flatmate
        pdf.set_font(family="Times", size=12)
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=f"{flatmate1.pays(bill, flatmate2=flatmate2)} PLN", border=1, ln=1)

        # Insert name and due amount to pay of second flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=f"{flatmate2.pays(bill, flatmate2=flatmate1)} PLN", border=1, ln=1)

        # Change directory to "files", save file and open it
        os.chdir("files")
        pdf.output(f"Bill_{bill.period}.pdf")

        # Open PDF (Linux/Mac version)
        # webbrowser.open('file://' + os.path.realpath(self.filename))

        # Open PDF in Windows
        webbrowser.open(self.file_name)
