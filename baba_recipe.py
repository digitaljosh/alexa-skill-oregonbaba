import logging

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session



app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def new_recipe():

    welcome_msg = render_template('welcome')

    return question(welcome_msg)




@ask.intent("AnswerIntent", convert={'stepNumber': int})

def answer(stepNumber):

    
    if stepNumber == 1:
        msg = render_template('one')

    elif stepNumber == 2:
        msg = render_template('two')

    elif stepNumber == 3:
        msg = render_template('three')
    
    elif stepNumber == 4:
        msg = render_template('four')

    elif stepNumber == 5:
        msg = render_template('five')

    elif stepNumber == 6:
        msg = render_template('six')

    elif stepNumber == 7:
        msg = render_template('seven')

    elif stepNumber == 8:
        msg = render_template('eight')

    elif stepNumber == 9:
        msg = render_template('nine')

    elif stepNumber == 10:
        msg = render_template('ten')

    elif stepNumber == 11:
        msg = render_template('eleven')

    elif stepNumber == 12:
        msg = render_template('twelve')

    else:
        msg = render_template('unknown')

    return question(msg)


@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye")


@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")



if __name__ == '__main__':

    app.run(debug=True)