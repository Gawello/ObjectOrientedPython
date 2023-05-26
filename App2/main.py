from App2.flat import Bill, Flatmate
from App2.report import PdfReport

amount = input("Hey user, enter the bill amount: ")
period = input("Enter period for your bill (E.g. \"March 2023\"): ")
the_bill = Bill(float(amount), period)

name1 = input("Enter first flatmate name: ")
days1 = input(f"How many days {name1} was in house: ")

name2 = input("Enter second flatmate name: ")
days2 = input(f"How many days {name2} was in house: ")

# the_bill = Bill(amount=120, period="March 2023")
mate1 = Flatmate(name1, float(days1))
mate2 = Flatmate(name2, float(days2))

print(f"{name1} pays: ", mate1.pays(the_bill, mate2))
print(f"{name2} pays: ", mate2.pays(the_bill, mate1))

pdf_report = PdfReport(file_name=f"Bill_{the_bill.period}.pdf")
pdf_report.generate(flatmate1=mate1, flatmate2=mate2, bill=the_bill)
