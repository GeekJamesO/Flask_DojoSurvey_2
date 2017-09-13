from flask import Flask, flash, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key="deadbeef0123456789"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/process", methods=['POST'])
def process():
    requestName = request.form['Name']
    requestLocation = request.form['Dojos']
    requestLanguage = request.form['Language']
    requestComment = request.form['Comment']

    # validate
    validInput = True
    if (len(requestName) < 1):
        validInput = False;
        flash("Name field cannot be blank.")

    if (len(requestLanguage) < 1):
        validInput = False;
        flash("Location field cannot be blank.")

    if (len(requestComment) < 1):
        validInput = False;
        flash("Comment field cannot be blank.")
    if (len(requestComment) > 120):
        validInput = False;
        flash("Comment field cannot be larger than 120 characters.")

    if (validInput):
        session['Name'] = requestName
        session['Location'] = requestLocation
        session['Language'] = requestLanguage
        session['Comment'] = requestComment
        return redirect('/result')
    else:
        session['Name'] = ""
        session['Location'] = ""
        session['Language'] = ""
        session['Comment'] = ""
        return redirect('/')

@app.route('/result')
def result():
    return render_template('result.html')

app.run(debug=True)
