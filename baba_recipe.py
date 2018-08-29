import logging

from flask import Flask, render_template

from flask_ask import Ask, statement, question, convert_errors

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
    to an integer (convert={'stepNumber':int).
    then num2words is used to convert the integer 1 to 
    "one"
    '''

    if type(stepNumber) != int:
        unknown = render_template('unknown')
        return question(unknown)

    if stepNumber == 64:
        secret_message = "The master sees beyond what is obvious. He sees the unseen, feels the unfelt, and hears the unheard. He looks below the surface for what is hidden and so finds the great heartbeat of the Universe. He smiles, knowing it is his heartbeat. Your heartbeat. Our heartbeat. Kilo. Yankee. Bravo. Alpha. Lima. India. Oscar. November. End transmission."
        return statement(secret_message)
    
    if stepNumber > 12 or stepNumber < 0:
        unknown = render_template('unknown')
        return question(unknown)

    stepNumber = num2words(stepNumber)
    msg = render_template(stepNumber)
    return question(msg)
    
    
    '''
    


    
    '''
    

@ask.intent('AMAZON.HelpIntent')
def help():
    help_text = 'You can ask me for a recipe step. Step zero is for activation instructions. Steps one through twelve are for recipe instructions. Which step would you like?'
    return question(help_text)

@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye")

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")



if __name__ == '__main__':

    app.run(debug=True)