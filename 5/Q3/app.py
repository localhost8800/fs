# 3. Design a form that accepts customer details (CustName,email,MobNo,address,pincode),on submit retrieve customer details in template which shows on web
# page in the table format by using flask request object and template.
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

customers = []

@app.route('/', methods=['GET', 'POST'])
def customer():
    if request.method == 'POST':
        data = {
            'name': request.form['CustName'],
            'email': request.form['email'],
            'mob': request.form['MobNo'],
            'address': request.form['address'],
            'pincode': request.form['pincode']
        }

        customers.append(data)
        return redirect('/details')

    return render_template('form.html')

@app.route('/details')
def details():
    return render_template('details.html', customers=customers)

if __name__ == '__main__':
    app.run(debug=True)