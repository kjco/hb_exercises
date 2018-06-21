"""A madlib game that compliments its users."""

from random import sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)

@app.route('/game')
def show_madlib_form():
    response = request.args.get("yesno")
    if response == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")

@app.route('/madlib', methods=["POST"])
def show_madlib():
    color = request.form.get("color")
    person = request.form.get("person")
    noun = request.form.get("noun")
    adj = request.form.get("adj")
    place = request.form.get("place")
    food = request.form.get("food")
    body = request.form.getlist("body")
    madlib_lst = ["madlib.html", "madlib2.html"]
    madlib_to_run = sample(madlib_lst, 1)

    return render_template(madlib_to_run, color=color, person=person, noun=noun, 
        adj=adj, place=place, food=food, body=body)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
