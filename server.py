from flask import Flask
import random

app = Flask(__name__)

def color_black(function):
    def wrapped():
        return '<h1>' + function() + '</h1>'
    return wrapped

def randomize_number():
    number = random.randint(0, 9)
    return number

def color_blue(function):
    def wrapped():
        return '<h1  style="blue">' + function() + '</h1>'

def color_red(function):
    def wrapped():
        return '<h1 style="red">' + function() + '</h1>'
    return wrapped

def color_green(function):
    def wrapped():
        return '<h1 style="green">' + function() + '</h1>'
    return wrapped

randomized_number = randomize_number()


@app.route('/')
@color_black
def guess():
    return 'Guess a number between 0 and 9' \
           '<p><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"></img></p>'



@app.route('/<int:number>')
def guessed_number(number):
    if randomized_number > number:
        return '<h1 style="color:red;">Too low, try again!</h1>' \
               '<p><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"<img></p>'
    elif randomized_number < number:
        return '<h1 style="color:blue;">Too high, try again!</h1>' \
               '<p><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"<img></p>'
    elif randomized_number == number:
        return '<h1 style="color:green;">You found the number!</h1>' \
               '<p><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"<img></p>'
    









if __name__ == '__main__':
    app.run(debug=True)