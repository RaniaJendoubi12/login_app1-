from flask import Flask, render_template, request
from data1 import freshservice

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == "POST":
        email = request.form.get('Email')
        Password = request.form.get('Password')
        Ticket_ID = request.form.get('Ticket_ID')


        etat = freshservice(email, Password, Ticket_ID)

        if etat == 'done':
            print('s')
            return render_template('done.html')
        else:
            print('in filed')
            return render_template('error.html')

    return render_template('index.html')
if __name__ == '__main__':
    app.run()