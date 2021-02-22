from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle

app.config['TESTING'] = True
app.config['DEBUT_TB_HOSTS'] = ['dont-show-debug-toolbar']

class FlaskTests(TestCase):
    def test_homepage(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>BOGGLE!</h1>', html)

    def test_generate_board(self):
        with app.test_client() as client:
            res = client.get('/generate-board')

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, 'http://localhost/play-boggle')
    
    def test_redirect_generate_board(self):
        with app.test_client() as client:
            res = client.get('generate-board', follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<button>New Game</button>', html)
            self.assertIn('board', session)