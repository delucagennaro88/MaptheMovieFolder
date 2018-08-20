import os
from flask import Flask, flash, url_for, redirect, render_template
from json_manager import search_director, search_cast, open_json

json_directory = "C:\\Users\\Utente\\Dropbox\\Map the Movie"
json_file = "cinema.json"
json_dir = os.path.join(json_directory, json_file)

app = Flask(__name__)

data_collection = open_json(json_dir)

data = data_collection.values()

@app.route('/')
def show_all():
    return render_template('show_all.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
