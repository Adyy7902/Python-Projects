import webbrowser

# from filestack import Client
from fpdf import FPDF
import os


class PdfReport:

     """
     Creates a Pdf files that contains data about
     the flatmates such as their names, their
     due amount and the period of the bill.
     """

     def __init__(self, filename):
          self.filename = filename

     def generate(self, flatmate1, flatmate2, bill):
          flatmate1_pay = str(round(flatmate1.pays(bill = bill, flatmate = flatmate2), 2))
          flatmate2_pay = str(round(flatmate2.pays(bill = bill, flatmate = flatmate1), 2))

          pdf = FPDF(orientation = 'P', unit = 'pt', format = 'A4')
          pdf.add_page()

          # Add image
          pdf.image("files/house.png", w=30, h=30)
          # Insert Title
          pdf.set_font(family = 'Times', size = 24, style = 'B')
          pdf.cell(w = 0, h = 80, txt = 'Flatmates Bill', border = 0, align = 'C', ln = 1)

          # Insert Period label and value
          pdf.set_font(family = 'Times', size = 14, style = 'B')
          pdf.cell(w = 100, h = 40, txt = 'Period:', border = 0)
          pdf.cell(w = 150, h = 40, txt = bill.period, border = 0, ln = 1)

          # Insert Name and due amount of first flatmate
          pdf.set_font(family = 'Times', size = 12)
          pdf.cell(w = 100, h = 25, txt = flatmate1.name, border = 0)
          pdf.cell(w = 150, h = 25, txt = flatmate1_pay, border = 0, ln = 1)

          # Insert Name and due amount of second flatmate
          pdf.cell(w = 100, h = 25, txt = flatmate2.name, border = 0)
          pdf.cell(w = 150, h = 25, txt = flatmate2_pay, border = 0, ln = 1)
          os.chdir("files")
          # Save the pdf
          pdf.output(self.filename)

          webbrowser.open('file://'+os.path.realpath(self.filename))

# class FileSharer:
#
#      """
#      Takes input the File Path and API Key and outputs
#      the url for the file uploaded online
#      """
#
#      def __init__(self, filepath, api_key):
#           self.api_key = api_key
#           self.filepath = filepath
#
#      def share(self):
#           client = Client(self.api_key)
#
#           new_file_link = client.upload(filepath = self.filepath)
#           return new_file_link.url
