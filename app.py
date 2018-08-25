from flask import Flask, flash, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from json_manager import open_json_data
import os
from person_manager import check_presence, attori_amati

directory = "C:\\Users\\Utente\\Desktop\\FILM"
json_directory = "C:\\Users\\Utente\\Dropbox\\Map the Movie"

cinema_json_file = "cinema.json"
json_file = "attori_amati.json"
json_actor_dir = os.path.join(json_directory, json_file)
cinema_json = os.path.join(json_directory, cinema_json_file)

class ActorForm(FlaskForm):
    actor_name = StringField('Personaggio', validators=[DataRequired()])
    submit = SubmitField('Cerca')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'XMLZODSHE8N6NFOZDPZA2HULWSIYJU45K6N4ZO9M'

if os.path.exists(json_actor_dir):
    check_presence(cinema_json, json_actor_dir)
    data_collection = open_json_data(json_actor_dir)
    data = data_collection.values()

else:
    data = {}

@app.route('/')
def show_all():
    form = ActorForm()
    return render_template('attori_amati.html', data=data, form=form)

@app.route('/new', methods=['GET', 'POST'])
def new():
    form = ActorForm()

    if form.validate_on_submit():
        flash('Ricerca per {} effettuata'.format(form.actor_name.data))
        attori_amati(cinema_json, json_actor_dir, form.actor_name.data)

        if os.path.exists(json_actor_dir):
            check_presence(cinema_json, json_actor_dir)
            data_collection = open_json_data(json_actor_dir)
            data = data_collection.values()

        else:
            data = {}

    return render_template('attori_amati.html', title='Cerca', form=form, data=data)

if __name__ == '__main__':
    app.run(debug=True)
