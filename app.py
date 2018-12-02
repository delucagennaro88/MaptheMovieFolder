import datetime
import json
import os

from flask import Flask, flash, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from json_manager import open_json

json_directory = "C:\\Users\\Utente\\Dropbox\\Map the Movie"
json_views = "views.json"
json_views_dir = os.path.join(json_directory, json_views)

current_dic = {}

def current_movie():
    with open(json_views_dir, 'r') as outfile:
        data = json.load(outfile)

    a_year_ago = datetime.datetime.now() - datetime.timedelta(days=365)

    for view, (key, value) in enumerate(data.items()):
        for alfa in value:
            if int(alfa['Views']) == 0 or datetime.datetime.strptime(alfa['Data Views'], "%Y-%m-%d %H:%M:%S.%f") <= a_year_ago:
                current_dic[key] = []
                current_dic[key].append({'Title': alfa['Title'], 'Data Views': alfa['Data Views'], 'Views': alfa['Views']})

    return current_dic

app = Flask(__name__)
app.config['SECRET_KEY'] = 'XMLZODSHE8N6NFOZDPZA2HULWSIYJU45K6N4ZO9M'

@app.route('/')
def home():
    data_collection = current_movie()
    data = data_collection.values()

    return render_template('home.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

