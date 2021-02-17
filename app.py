from boggle import Boggle
from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route('/')
def index():
    board = boggle_game.make_board()
    session['board'] = board
    return render_template('index.html', board = board)

@app.route('/guess')
def submit_guess():
    board = session['board']
    # board = [['J', 'D', 'T', 'B', 'O'],['M', 'S', 'L', 'E', 'Q'],['J', 'M', 'V', 'C', 'E'],['V', 'G', 'V', 'N', 'F'],['N', 'C', 'Y', 'S', 'P']]
    guess = request.args.get('guess')
    result = boggle_game.check_valid_word(board, guess)
    return jsonify(result)