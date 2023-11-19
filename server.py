from flask import Flask, request, render_template
import user_handler
import datetime
import re
import lxml.html
import validators


app = Flask(__name__)


@app.route('/')
def launch():
    return render_template('index.html')


@app.route('/submitForm', methods=['POST', 'GET'])
def form_handler():
    errors = validateData(request.form)
    if errors:
        genErrorPage(errors)
        return render_template('errpg.html')
    form_data = tuple(dict(request.form).values())
    user_handler.add_entry(form_data)
    return "Wait till your bot gets to you :)"

def genBackgroundProcess():
    pass

def validateData(form):
    errors = ['', '', '', '', '', '']
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    flag = 0

    if not form['uname'].isalnum():
        errors[0] = "Username should only be alphanumeric a-z/A-Z/0-9"
        flag = 1

    elif user_handler.isDuplicate(form['uname']):
        errors[0] = "User already exists"
        flag = 1

    if not form['mname'].isalnum():
        errors[1] = "Movie name should only be alphanumeric a-z/A-Z/0-9"
        flag = 1

    try:
        d = list(map(int,form['date'].split('-')))
        dateobj = datetime.date(d[0], d[1], d[2])
        if dateobj < datetime.date.today():
            raise ValueError
    except ValueError:
        errors[2] = "Incorrect date format"
        flag = 1

    if not form['freq'].isnumeric() or int(form['freq']) < 10:
        errors[4] = "Frequency should be a number greater than 10"
        flag = 1

    if not re.fullmatch(regex, form['email']):
        errors[3] = "Invalid mail format"
        flag = 1

    if not validators.url(form['link']):
        errors[5] = "Invalid Link"
        flag = 1

    if flag:
        return errors
    else:
        return 0

def genErrorPage(errors):
    html_str = f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <title>Bookings Bot</title>
        </head>
        <body>
        <h1>Ticket Availability Bot</h1><br>
        <h2>Fill in the following details</h2>
        <form action="/submitForm" id="userInput" method="post">
            Username:<br>
            <input type="text" name="uname"><span style="color:red"> {errors[0]}</span><br>
            Movie Name [Exactly as in website]:<br>
            <input type="text" name="mname"><span style="color:red"> {errors[1]}</span><br>
            Date [yyyy-mm-dd]:<br>
            <input type="text" name="date"><span style="color:red"> {errors[2]}</span><br>
            Theater link [copy url from TicketNew]:<br>
            <input type="text" name="link"><span style="color:red"> {errors[5]}</span><br>
            Email [To get notifications]:<br>
            <input type="text" name="email"><span style="color:red"> {errors[3]}</span><br>
            Frequency [in minutes minimum 10]:<br>
            <input type="text" name="freq"><span style="color:red"> {errors[4]}</span><br><br>
            <input type="submit" id="pass">
        </form>
        </body>
        </html>
    '''
    with open('templates/errpg.html', 'wb') as f:
        content = lxml.html.fromstring(html_str)
        f.write(lxml.html.tostring(content))


if __name__ == '__main__':
    app.run(debug=True)
