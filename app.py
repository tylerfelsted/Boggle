from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# debug = DebugToolbarExtension(app)

boggle_game = Boggle()


@app.route('/')
def index():
    """Displays the homepage. Prompts the user to start a game"""
    return render_template('index.html')

@app.route('/generate-board')
def generate_board():
    """Calls the make_board function and then redirects to the /play-boggle route"""
    board = boggle_game.make_board()
    session['board'] = board
    return redirect('/play-boggle')

@app.route('/play-boggle')
def play_boggle():
    """Displays the board and the form for submitting guesses. Also displays a timer the score."""
    board = session['board']
    return render_template('play_boggle.html', board = board)

@app.route('/guess')
def submit_guess():
    """Recieves a word and checks to see if it is a valid guess."""
    board = session['board']
    guess = request.args.get('guess')
    result = boggle_game.check_valid_word(board, guess)
    return jsonify(result)

@app.route('/game-over', methods=['POST'])
def game_over():
    """Updates the session with number of plays and the current high score"""
    score = request.json['score']

    if not session.get('high_score') or score > session['high_score']:
        session['high_score'] = score

    if session.get('total_plays'):
        session['total_plays'] += 1
    else:
        session['total_plays'] = 1

    statistics = {'high_score': session['high_score'], 'total_plays': session['total_plays']}
    return statistics