import os, json
from classes import Folder, Movie, Actor, Director
from flask import Flask, flash, url_for, redirect, render_template

json_directory = "C:\\Users\\Utente\\Dropbox\\Map the Movie"
json_file = "cinema.json"
json_dir = os.path.join(json_directory, json_file)
collection = {}
director_list = {}
actor_list = {}
movie_class = {}
movie_dic = {}
app = Flask(__name__)

def search_director(movie_list):
    directors = movie_list
    movie_dic['Director'] = []
    for dir in directors:
        director_name = dir['Name']
        director_id = dir['Id']
        movie_dic['Director'].append({'Name': director_name, 'Id': director_id})
    return movie_dic['Director']

def search_cast(movie_list):
    actors = movie_list
    movie_dic['Actor'] = []
    for dir in actors:
        actor_name = dir['Name']
        actor_id = dir['Id']
        movie_dic['Actor'].append({'Name': actor_name, 'Id': actor_id})
    return movie_dic['Actor']

def open_json(json_dir):

    with open(json_dir, encoding='cp1252') as data_file:
        movie_json = json.load(data_file)
        xx = 0
        for i in movie_json.values():
            for x in i:
                home_path = x['Home Directory']
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
                movie_plot = x['Movie plot']
                movie_directors = x['Movie Director']
                movie_dir_list = search_director(movie_directors)

                movie_actors = x['Movie Actor']
                movie_act_list = search_cast(movie_actors)
                '''
                nn = 0
                for y in x['Movie Director']:
                    director_name = y['Name']
                    director_id = y['Id']
                    director_list[nn] = []
                    director_list[nn].append({'Director Name': director_name, 'Director Id': director_id})
                    nn += 1
                
                '''
                mm = 0
                for z in x['Movie Actor']:
                    actor_name = z['Name']
                    actor_id = z['Id']
                    actor_list[mm] = []
                    actor_list[mm].append({'Actor Name': actor_name, 'Actor Id': actor_id})
                    mm += 1

                movie_class[xx] = []
                movie_class[xx].append({'Home path': home_path, 'File Name': file_name, 'Id': id, 'Atime': atime, 'Ctime': ctime, 'Size': size, 'Extension': ext, 'Movie Id': movie_id, 'Movie Url': movie_url, 'Movie Title': movie_title, 'Movie Year': movie_year,
                                                  'Movie Plot': movie_plot, 'Director List': movie_dir_list, 'Actor List': movie_act_list})

                xx+=1

        return movie_class


data_collection = open_json(json_dir)

data = data_collection.values()
'''
for a in data_collection.values():
    for b in a:
        print(b['File Name'])
        for actor in b['Actor List']:
            print(actor['Name'])



'''

@app.route('/')
def show_all():
    return render_template('show_all.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
