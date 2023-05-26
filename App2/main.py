import webbrowser
from fpdf import FPDF


class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return round(to_pay, 2)


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
        pdf.image(name="house.png", w=30, h=30)

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

        pdf.output(f"Bill_{bill.period}.pdf")

        # Open PDF (Linux/Mac version)
        # webbrowser.open('file://' + os.path.realpath(self.filename))

        # Open PDF in Windows
        # webbrowser.open(self.file_name)


# CLI
# User enter amount and period of a bill
amount = input("Hey user, enter the bill amount: ")
period = input("Enter period for your bill (like: \"March 2023\"): ")
the_bill = Bill(float(amount), period)

# Enter first flatmates name and number of days
name1 = input("Enter first flatmate name: ")
days1 = input(f"How many days {name1} was in the house: ")

# Enter second flatmate name and number of days
name2 = input("Enter second flatmate name: ")
days2 = input(f"How many days {name2} was in the house: ")

flatmate1 = Flatmate(name1, float(days1))
flatmate2 = Flatmate(name2, float(days2))

# # the_bill = Bill(amount=120, period="March 2023")
# john = Flatmate(name="John", days_in_house=20)
# marry = Flatmate(name="Marry", days_in_house=25)

print(f"{name1} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{name2} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(file_name="Report1.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)
