import logging

from flask import Flask, render_template

from flask_ask import Ask, statement, question

from num2words import num2words




app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch

def new_recipe():

    welcome_msg = render_template('welcome')

    return question(welcome_msg)




@ask.intent("AnswerIntent", convert={'stepNumber': int})

def answer(stepNumber):
    '''
    stepNumber comes in as "1" so it needs to be converted
    to an integer, then num2words is used to convert 1 to 
    "one"
    '''
    stepNumber = num2words(stepNumber) 
    msg = render_template(stepNumber)
    return question(msg)



@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye")


@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")



if __name__ == '__main__':

    app.run(debug=True)