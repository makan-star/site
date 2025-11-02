from flask import Flask
import random

facts_list = [' hgvhgvh', 'gvhgvhvhgvg']

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f'<p>{random.choice(facts_list)}</p>'

app.run(debug=True)
@app.route("/secret")
def secret():
    return "<h1>Ты нашёл тайную страницу!</h1>"
