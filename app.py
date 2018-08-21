from flask import Flask, flash, url_for, redirect, render_template
from json_manager import search_director, search_cast, open_json
import sys, imdb, os, json

directory = "C:\\Users\\Utente\\Desktop\\FILM"
json_directory = "C:\\Users\\Utente\\Dropbox\\Map the Movie"

json_file = "attori_amati.json"
json_actor_dir = os.path.join(json_directory, json_file)
actor_dictionary = {}
movie_dictionary = {}
actor_collection = {}

ia = imdb.IMDb()

def search_filmography(filmography):
    for a in filmography:
        for key, value in a.items():
            key_index = str(key) #qui va salvato l'indice della categoria
            actor_dictionary[key_index] = []
            for b in value:
                movie_film = ia.search_movie(str(b))
                movie = movie_film[0]
                title = movie.get('title')
                movie_year = movie['year']
                actor_dictionary[key_index].append({'Title': title, 'Year': movie_year, 'Present': False})
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

        actor_name = str(actor)
        actor_collection[actor_name] = []
        actor_collection[actor_name].append({ 'Date': dates, 'Filmography': filmography_box})

        #qui si verifica se il JSON esiste
        #se non esiste si crea e si scrive con W
        #se esiste si aggiorna col metodo inventato
        if not os.path.exists(json_actor_dir):
            with open(json_actor_dir, 'w') as outfile:
                json.dump(actor_collection, outfile, sort_keys=True, indent=4, ensure_ascii=False)
            print("Creato!")
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

    except imdb.IMDbError as e:
        print("Probably you're not connected to Internet.  Complete error report:")
        print(e)
        sys.exit(3)

    if not actor:
        print('It seems that there\'s no actor with "%s"' % actor)
        sys.exit(4)

    #print(type(filmography))

attori_amati('Titina De Filippo')




'''

app = Flask(__name__)

data_collection = open_json(json_dir)

data = data_collection.values()

@app.route('/')
def show_all():
    return render_template('show_all.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
'''