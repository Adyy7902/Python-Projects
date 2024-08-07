from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from flatmates_bill.flat import Bill, Flatmate

app = Flask(__name__)

class HomePage(MethodView):

     def get(self):
          return render_template('index.html')

class BillFormPage(MethodView):

     def get(self):
          bill_form = BillForm()
          return  render_template('bill_form_page.html',
                                  billform = bill_form)
     def post(self):
          billform = BillForm(request.form)

          bill = Bill(float(billform.amount.data), billform.period.data)
          flatmate1 = Flatmate(billform.name1.data, float(billform.days_in_house1.data))
          flatmate2 = Flatmate(billform.name2.data, float(billform.days_in_house2.data))

          return render_template('bill_form_page.html',
                                 result=True,
                                 billform = billform,
                                 name1 = flatmate1.name,
                                 amount1 = round(flatmate1.pays(bill, flatmate2), 2),
                                 name2 = flatmate2.name,
                                 amount2 = round(flatmate2.pays(bill, flatmate1), 2))


class ResultsPage(MethodView):
      def post(self):
          billform = BillForm(request.form)

          bill = Bill(float(billform.amount.data), billform.period.data)
          flatmate1 = Flatmate(billform.name1.data, float(billform.days_in_house1.data))
          flatmate2 = Flatmate(billform.name2.data, float(billform.days_in_house2.data))

          return render_template('results_page.html',
                                 name1 =flatmate1.name,
                                 amount1 = round(flatmate1.pays(bill,flatmate2),2),
                                 name2 = flatmate2.name,
                                 amount2 = round(flatmate2.pays(bill,flatmate1),2))

class BillForm(Form):
     amount = StringField("Bill Amount:")
     period = StringField("Bill Period:")

     name1 = StringField("Name: ")
     days_in_house1 = StringField("Days in the house: ")

     name2 = StringField("Name: ")
     days_in_house2 = StringField("Days in the house: ")

     button = SubmitField("Calculate")

app.add_url_rule('/',
                 view_func = HomePage.as_view('home_page'))
app.add_url_rule('/bill',
                 view_func = BillFormPage.as_view('bill_form_page'))
# app.add_url_rule('/results',
#                  view_func = ResultsPage.as_view('results_page'))

app.run(debug = True)