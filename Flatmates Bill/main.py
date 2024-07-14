from flat import Bill, Flatmate
from pdf_report import PdfReport

import os
amount = int(input("Hey user, enter the bill amount: "))
period = input("What month is it? E.g. July 2024: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"How many days did you stay in the house during the bill period? "))

name2 = input("What is the name of other flatmate? ")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during the bill period? "))


bill = Bill(amount = amount, period = period)
flatmate1 = Flatmate(name = name1, days_in_house = days_in_house1)
flatmate2 = Flatmate(name = name2, days_in_house = days_in_house2)

print(f"{name1} pays: {round(flatmate1.pays(bill = bill, flatmate = flatmate2),2)}")
print(f"{name2} pays: {round(flatmate2.pays(bill = bill, flatmate = flatmate1),2)}")

pdf_report = PdfReport(filename = f"{bill.period}.pdf")
pdf_report.generate(flatmate1 = flatmate1, flatmate2 = flatmate2, bill = bill)

# file_sharer = FileSharer(filepath = pdf_report.filename)
# print(file_sharer.share())
