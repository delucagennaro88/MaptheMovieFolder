import json
import os, datetime, shutil

json_directory = "C:\\Users\\Utente\\Dropbox\\Map the Movie"
json_data = "data.json"
json_data_dir = os.path.join(json_directory, json_data)
json_views = "views.json"
json_views_dir = os.path.join(json_directory, json_views)
cinema_json_file = "cinema.json"
json_file = "attori_amati.json"
json_actor_dir = os.path.join(json_directory, json_file)
json_dir = os.path.join(json_directory, cinema_json_file)
destination_directory = "C:\\Users\\Utente\\Desktop\\Foto Cinema"

movie_class = {}
movie_dic = {}
filmography_dic = {}
film = {}
views_collection = {}
json_views_dic = {}

def search_director(movie_list):
    directors = movie_list
    movie_dic['Director'] = []
    for dir in directors:
        director_name = dir['Name']
        director_id = dir['Id']
        director_presence = dir['Present']
        movie_dic['Director'].append({'Name': director_name, 'Id': director_id, 'Present': director_presence})
    return movie_dic['Director']


def search_cast(movie_list):
    actors = movie_list
    movie_dic['Actor'] = []
    for dir in actors:
        actor_name = dir['Name']
        actor_id = dir['Id']
        actor_presence = dir['Present']
        movie_dic['Actor'].append({'Name': actor_name, 'Id': actor_id, 'Present': actor_presence})
    return movie_dic['Actor']

def search_writer(movie_list):
    writers = movie_list
    movie_dic['Writer'] = []
    for dir in writers:
        writer_name = dir['Name']
        writer_id = dir['Id']
        writer_presence = dir['Present']
        movie_dic['Writer'].append({'Name': writer_name, 'Id': writer_id, 'Present': writer_presence})
    return movie_dic['Writer']


def open_json(json_dir):
    with open(json_dir, encoding='cp1252') as data_file:
        movie_json = json.load(data_file)
        xx = 0
        for i in movie_json.values():
            for x in i:
                home_path = x['Home path']
                file_name = x['File Name']
                id = x['Id']  # nome del File senza Directory
                ext = x['Extension']
                atime = x['Atime']
                ctime = x['Ctime']
                size = x['Size']
                movie_id = x['Movie Id']
                movie_title = x['Movie Title']
                movie_url = x['Movie Url']
                movie_year = x['Movie Year']
                movie_seasons = x['Seasons']
                movie_plot = x['Movie plot']
                movie_banner = x['Banner Pic']
                movie_poster = x['Movie Poster']

                movie_directors = x['Director List']
                movie_dir_list = search_director(movie_directors)

                movie_actors = x['Actor List']
                movie_act_list = search_cast(movie_actors)

                movie_writers = x['Writer List']
                movie_writ_list = search_writer(movie_writers)

                movie_class[movie_title] = []
                movie_class[movie_title].append(
                    {'Home path': home_path, 'File Name': file_name, 'Id': id, 'Atime': atime, 'Ctime': ctime,
                     'Size': size, 'Extension': ext, 'Banner Pic': movie_banner, 'Movie Poster': movie_poster, 'Movie Id': movie_id, 'Movie Url': movie_url,
                     'Movie Title': movie_title, 'Movie Year': movie_year, 'Seasons': movie_seasons,
                     'Movie plot': movie_plot, 'Director List': movie_dir_list, 'Actor List': movie_act_list, 'Writer List': movie_writ_list})

                xx += 1

        return movie_class


# create Json File for NR. of saved files
def createJsonFile(data_saved):
    json_dic = {'Directory': json_data_dir, 'Saved Files': data_saved}
    with open(json_data_dir, 'a') as outfile:
        json.dump(json_dic, outfile, sort_keys=True, indent=4, ensure_ascii=False)

    print('Creato il file')


# read Json File with NR. of saved files
def read_saved_files():
    jsonFile = open(json_data_dir, "r")  # Open the JSON file for reading
    data = json.load(jsonFile)  # Read the JSON into the buffer
    jsonFile.close()  # Close the JSON file

    tmp = data["Saved Files"]
    print('Letto il file')

    return tmp


# update Json File with NR. of saved files
def updateJsonFile(num):
    jsonFile = open(json_data_dir, "r")  # Open the JSON file for reading
    data = json.load(jsonFile)  # Read the JSON into the buffer
    jsonFile.close()  # Close the JSON file

    ## Working with buffered content
    tmp = data["Saved Files"]
    data["Saved Files"] = num

    ## Save our changes to JSON file
    jsonFile = open(json_data_dir, "w+")
    jsonFile.write(json.dumps(data))
    jsonFile.close()

    print("Aggiornato il file")

def open_json_data(json_dir):
    with open(json_dir, encoding='cp1252') as data_file:
        movie_json = json.load(data_file)

        for i, (key, value) in enumerate(movie_json.items()):
            for a in value:
                film[a['Name']] = []
                film[a['Name']].append({'Name': a['Name'], 'Id': a['Id'], 'Date': a['Date'], 'Gif': a['Gif'], 'Poster': a['Poster'], 'Filmography': a['Filmography'], 'Url':a['Url']})
        return film


def query_actor(actor_name, json_dir):
    query_dic = {}
    movie_file = open_json(json_dir)
    cinema_data = movie_file.values()

    for a in cinema_data:
        for b in a:

            for c in b['Actor List']:
                if c['Name'].lower() == actor_name.lower() or actor_name.lower() in c['Name'].lower():
                    query_dic[b['Movie Id']] = []
                    query_dic[b['Movie Id']].append(
                        {'Home path': b['Home path'], 'File Name': b['File Name'], 'Id': b['Id'], 'Atime': b['Atime'],
                         'Ctime': b['Ctime'],
                         'Size': b['Size'], 'Extension': b['Extension'], 'Banner Pic': b['Banner Pic'], 'Movie Poster': b['Movie Poster'], 'Movie Id': b['Movie Id'],
                         'Movie Url': b['Movie Url'],
                         'Movie Title': b['Movie Title'], 'Movie Year': b['Movie Year'], 'Seasons': b['Seasons'],
                         'Movie plot': b['Movie plot'], 'Director List': b['Director List'],
                         'Actor List': b['Actor List']})

            for d in b['Director List']:
                if d['Name'].lower() == actor_name.lower() or actor_name.lower() in d['Name'].lower():
                    query_dic[b['Movie Id']] = []
                    query_dic[b['Movie Id']].append(
                        {'Home path': b['Home path'], 'File Name': b['File Name'], 'Id': b['Id'], 'Atime': b['Atime'],
                         'Ctime': b['Ctime'],
                         'Size': b['Size'], 'Extension': b['Extension'], 'Banner Pic': b['Banner Pic'], 'Movie Poster': b['Movie Poster'], 'Movie Id': b['Movie Id'],
                         'Movie Url': b['Movie Url'],
                         'Movie Title': b['Movie Title'], 'Movie Year': b['Movie Year'], 'Seasons': b['Seasons'],
                         'Movie plot': b['Movie plot'], 'Director List': b['Director List'],
                         'Actor List': b['Actor List']})

            for e in b['Writer List']:
                if e['Name'].lower() == actor_name.lower() or actor_name.lower() in e['Name'].lower():
                    query_dic[b['Movie Id']] = []
                    query_dic[b['Movie Id']].append(
                        {'Home path': b['Home path'], 'File Name': b['File Name'], 'Id': b['Id'], 'Atime': b['Atime'],
                         'Ctime': b['Ctime'],
                         'Size': b['Size'], 'Extension': b['Extension'], 'Banner Pic': b['Banner Pic'], 'Movie Poster': b['Movie Poster'], 'Movie Id': b['Movie Id'],
                         'Movie Url': b['Movie Url'],
                         'Movie Title': b['Movie Title'], 'Movie Year': b['Movie Year'], 'Seasons': b['Seasons'],
                         'Movie plot': b['Movie plot'], 'Director List': b['Director List'],
                         'Actor List': b['Actor List']})

    query_raw = query_dic.values()
    return query_raw

def check_attori_amati(id):
    if not os.path.exists(json_actor_dir):
        return
    else:
        with open(json_actor_dir, encoding='cp1252') as data_file:
            movie_json = json.load(data_file)

        for i, (key, value) in enumerate(movie_json.items()):
            for a in value:
                if a['Id'] == id:
                    return True
                else:
                    pass

def check_filmographies(actor_id):
    change = False
    cinema_file = open_json(json_dir)
    cinema_data = cinema_file.values()

    for a in cinema_data:
        for b in a:

            for c in b['Actor List']:
                if c['Id'] == actor_id and c['Present'] == False:
                    print(c['Name'])
                    c['Present'] = True
                    change = True


    if change == True:
        print('Updated')
        with open(json_dir, 'w') as outfile:
            json.dump(cinema_file, outfile, indent=4, ensure_ascii=False)
    else:
        print("Non ci sono cambiamenti")
        return


#Json file of Views
def create_json_views(movie_id, movie_title):
    # salva le views

    movie_gif = movie_title.lower().replace(" ", "") + ".gif"

    if not os.path.exists(json_views_dir):
        views_collection[movie_id] = []
        views_collection[movie_id].append({"Title": movie_title, "Views": 0, "Data Views": 0, "Gif": movie_gif})
        print(views_collection)
        with open(json_views_dir, 'a') as outfile:
            json.dump(views_collection, outfile, sort_keys=True, indent=4, ensure_ascii=False)

        print('Creato il file VIEWS')

    else:
        views_collection[movie_id] = []
        views_collection[movie_id].append({"Title": movie_title, "Views": 0, "Data Views": 0, "Gif": movie_gif})

        with open(json_views_dir, 'r') as outfile:
            data = json.load(outfile)

        data_str = str(data)
        no_brackets = data_str[data_str.find("{") + 1:data_str.rfind("}")]  # ora non è un dizionario, ma una stringa

        # facciamo lo stesso con collection
        collection_str = str(views_collection)
        no_brackets_coll = collection_str[collection_str.find("{") + 1:collection_str.rfind("}")]

        # ora concateniamo le due stringhe
        new_str = '{' + no_brackets + ', ' + no_brackets_coll + '}'

        # qui ritorna dictionary
        dict1 = eval(new_str)

        with open(json_views_dir, 'w') as outfile:
            json.dump(dict1, outfile, indent=4, ensure_ascii=False)

        print('Creato il file VIEWS')

#Aggiorna il file Views con il nuovo film
def update_json_views(movie_id, movie_title):
    # aggiorna lista con nuovo film

    movie_gif = movie_title.lower().replace(" ", "") + ".gif"

    json_views_dic[movie_id] = []
    json_views_dic[movie_id].append({"Title": movie_title, "Views": 0, "Data Views": 0, "Gif": movie_gif})

    with open(json_views_dir, 'r') as outfile:
        data = json.load(outfile)

    data_str = str(data)

    no_brackets = data_str[data_str.find("{") + 1:data_str.rfind("}")]  # ora non è un dizionario, ma una stringa

    # facciamo lo stesso con collection
    collection_str = str(json_views_dic)
    no_brackets_coll = collection_str[collection_str.find("{") + 1:collection_str.rfind("}")]

    # ora concateniamo le due stringhe
    new_str = '{' + no_brackets + ', ' + no_brackets_coll + '}'

    # qui ritorna dictionary
    dict1 = eval(new_str)

    with open(json_views_dir, 'w') as outfile:
        json.dump(dict1, outfile, indent=4, ensure_ascii=False)

    print('Aggiornato il file VIEWS')

#Aggiorna il nr di Views e la Data di Visione
def update_views(movie_id):
    # aggiornamento delle views.

    # aprire il file Cinema.json e recuperare la directory del film
    with open(json_dir, 'r') as outfile:
        movie_data = json.load(outfile)

    for i in movie_data.values():
        for x in i:
            if x['Movie Id'] == movie_id:
                print(x['File Name'])

                file_dir = x['File Name']

                if os.path.isdir(file_dir):
                    file = os.path.basename(file_dir) #estrapoliamo nome cartella dalla Directory
                    dest_file_dir = os.path.join(destination_directory, file) #creaiamo directory con destinazione e nome vecchia cartella
                    os.mkdir(dest_file_dir) #creiamo effetticamente la cartella

                    for i in os.listdir(file_dir): #per ogni file contenuto, creiamo una copia
                        current_file_dir = os.path.join(file_dir, i)
                        print(current_file_dir)
                        shutil.copy(current_file_dir, dest_file_dir)
                else:
                    shutil.copy(file_dir, destination_directory)

    # questo viene chiamato quando copio il Video nell'altra cartella
    current_movie = {}
    # 1. Aprire il FILE
    with open(json_views_dir, 'r') as outfile:
        data = json.load(outfile)

    # 2. Cercare il titolo giusto e Aggiornare le Views
    for i, (key, value) in enumerate(data.items()):
        if key == movie_id:
            for b in value:
                current_views = b['Views']
                b['Views'] = current_views + 1

                b['Data Views'] = datetime.datetime.now()

                current_movie = {"Title": b['Title'], "Views": b['Views'], "Data Views": b['Data Views'], "Gif": b['Gif']}

    # 3. Salvare
    with open(json_views_dir, 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False, default=str)

    print("Updated Json Views File")

    return current_movie