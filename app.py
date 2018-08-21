import os
from flask import Flask, flash, url_for, redirect, render_template
from json_manager import search_director, search_cast, open_json
import sys, imdb

actor_dictionary = {}
movie_dictionary = {}
actor_collection = {}

ia = imdb.IMDb()

def search_filmography(filmography):

    for a in filmography:
        for key, value in a.items():
            alfa = 0
            key_index = key #qui va salvato l'indice della categoria
            actor_dictionary[key_index] = []
            for b in value:
                movie_film = ia.search_movie(str(b))
                movie = movie_film[0]
                title = movie.get('title')
                movie_year = movie['year']
                actor_dictionary[key_index].append({'Title': title, 'Year': movie_year})
    return actor_dictionary

def attori_amati(actor_name):
#1. Dato il nome di un attore, restituisce l'elenco di tutti i suoi film (solo titoli e date)
#2. L'elenco viene salvato in JSON
#3. Scorre l'elenco e verifica quali sono i film già posseduti e quali no.
    try:
        actors = ia.search_person(actor_name)
        actor = actors[0]
        actor_id = actor.personID
        actor_identifier = ia.get_person(actor_id)

        birth = actor_identifier['birth date'][:4]
        death = actor_identifier['death date'][:4]
        dates = '(' + str(birth) + '-' + str(death) + ')'

        filmography = actor_identifier['filmography']

        filmography_box = search_filmography(filmography)

        actor_collection[actor] = []
        actor_collection[actor].append({'Nome': actor, 'Date': dates, 'Filmography': filmography_box})

        #qui si verifica se il JSON esiste
        #se non esiste si crea e si scrive con W
        #se esiste si aggiorna col metodo inventato

    except imdb.IMDbError as e:
        print("Probably you're not connected to Internet.  Complete error report:")
        print(e)
        sys.exit(3)

    if not actor:
        print('It seems that there\'s no actor with "%s"' % actor)
        sys.exit(4)

    #print(type(filmography))

attori_amati('Tina Pica')




'''
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
'''