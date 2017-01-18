from random import choice, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_medlib_form():
    """ Play the game """

    user_response = request.args.get("game")
    if user_response == "No":

        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """Show game results """

    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    rainbows = request.args.get("rainbows")
    foods = request.args.getlist("food")

    #print foods

    if rainbows == "Yes":
        rainbows = True
    else:
        rainbows = False

    templates = ["madlib.html", "madlib1.html"]
    madlib = choice(templates)

    return render_template(madlib,
                           person=person,
                           color=color,
                           noun=noun,
                           adjective=adjective,
                           rainbows=rainbows,
                           foods=foods)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
