from flask import Flask, flash, url_for, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from json_manager import search_director, search_cast, open_json, open_json_data
import sys, imdb, os, json, time


directory = "C:\\Users\\Utente\\Desktop\\FILM"
json_directory = "C:\\Users\\Utente\\Dropbox\\Map the Movie"

cinema_json_file = "cinema.json"
json_file = "attori_amati.json"
json_actor_dir = os.path.join(json_directory, json_file)
cinema_json = os.path.join(json_directory, cinema_json_file)
actor_dictionary = {}
actor_collection = {}

ia = imdb.IMDb()

class ActorForm(FlaskForm):
    actor_name = StringField('Personaggio', validators=[DataRequired()])
    submit = SubmitField('Cerca')

def search_filmography(filmography):
    for a in filmography:
        for key, value in a.items():
            key_index = str(key) #qui va salvato l'indice della categoria
            actor_dictionary[key_index] = []
            time.sleep(5)
            for b in value:
                movie_film = ia.search_movie(str(b))
                movie = movie_film[0]
                movie_id = movie.movieID
                title = movie.get('title')
                movie_year = movie['year']
                actor_dictionary[key_index].append({'Title': title, 'Year': movie_year, 'Id': movie_id, 'Present': False})
                time.sleep(5)
    return actor_dictionary


def check_presence():
    change = False
    cinema_file = open_json(cinema_json)
    attori_file = open_json_data(json_actor_dir)#Occorre creare una funzione apposita per aprire il File. OPEN_JSOn non va bene!

    cinema_data = cinema_file.values()

    for z in attori_file.values():
        for w in z:
            #print(w['Name'])
            for y, (key, value) in enumerate(w['Filmography'].items()):
                for x in value:
                    for a in cinema_data:
                        for b in a:
                            if x['Id'] == b['Movie Id'] and x['Present'] == False:
                                print(x['Title'])
                                x['Present'] = True
                                change = True

    if change == True:
        print('Updated')
        with open(json_actor_dir, 'w') as outfile:
            json.dump(attori_file, outfile, indent=4, ensure_ascii=False)
    else:
        print("Non ci sono cambiamenti")
        return

def attori_amati(actor_name):
#1. Dato il nome di un attore, restituisce l'elenco di tutti i suoi film (solo titoli e date)
#2. L'elenco viene salvato in JSON
#3. Scorre l'elenco e verifica quali sono i film già posseduti e quali no.
    try:
        actors = ia.search_person(actor_name)
        actor = actors[0]
        actor_id = actor.personID
        actor_identifier = ia.get_person(actor_id)


        for key, value in actor_identifier.items():
            if key == "birth date":
                birth = actor_identifier['birth date'][:4]
                if key == "death date":
                    death = actor_identifier['death date'][:4]
                    dates = '(' + str(birth) + '-' + str(death) + ')'
                else:
                    dates = '(' + str(birth) + '-' + ')'
            else:
                dates = '(-)'

        filmography = actor_identifier['filmography']
        filmography_box = search_filmography(filmography)

        actor_name_str = str(actor)
        actor_collection[actor_name_str] = []
        actor_collection[actor_name_str].append({'Name': actor_name_str, 'Date': dates, 'Filmography': filmography_box})

        #qui si verifica se il JSON esiste
        #se non esiste si crea e si scrive con W
        #se esiste si aggiorna col metodo inventato
        if not os.path.exists(json_actor_dir):
            with open(json_actor_dir, 'w') as outfile:
                json.dump(actor_collection, outfile, sort_keys=True, indent=4, ensure_ascii=False)
            print("Creato!")

            check_presence()

            print("Aggiornato con le presenze")

            return

        else:
            with open(json_actor_dir, 'r') as outfile:
                data = json.load(outfile)

            data_str = str(data)
            no_brackets = data_str[data_str.find("{") + 1:data_str.rfind("}")]  # ora non è un dizionario, ma una stringa

            # facciamo lo stesso con collection
            collection_str = str(actor_collection)
            no_brackets_coll = collection_str[collection_str.find("{") + 1:collection_str.rfind("}")]

            # ora concateniamo le due stringhe
            new_str = '{' + no_brackets + ', ' + no_brackets_coll + '}'

            # qui ritorna dictionary
            dict1 = eval(new_str)

            with open(json_actor_dir, 'w') as outfile:
                json.dump(dict1, outfile, indent=4, ensure_ascii=False)

            print("Modificato!")

            check_presence()

            print("Aggiornato con le presenze")

    except imdb.IMDbError as e:
        print("Probably you're not connected to Internet.  Complete error report:")
        print(e)
        sys.exit(3)

    if not actor:
        print('It seems that there\'s no actor with "%s"' % actor)
        sys.exit(4)


#attori_amati('Totò')

#check_presence()



app = Flask(__name__)
app.config['SECRET_KEY'] = 'XMLZODSHE8N6NFOZDPZA2HULWSIYJU45K6N4ZO9M'

if os.path.exists(json_actor_dir):
    check_presence()
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
        attori_amati(form.actor_name.data)

        if os.path.exists(json_actor_dir):
            check_presence()
            data_collection = open_json_data(json_actor_dir)
            data = data_collection.values()

        else:
            data = {}

    return render_template('attori_amati.html', title='Cerca', form=form, data=data)


if __name__ == '__main__':
    app.run(debug=True)
