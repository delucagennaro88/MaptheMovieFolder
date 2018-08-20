import json

movie_class = {}
movie_dic = {}

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

                movie_class[xx] = []
                movie_class[xx].append({'Home path': home_path, 'File Name': file_name, 'Id': id, 'Atime': atime, 'Ctime': ctime, 'Size': size, 'Extension': ext, 'Movie Id': movie_id, 'Movie Url': movie_url, 'Movie Title': movie_title, 'Movie Year': movie_year,
                                                  'Movie Plot': movie_plot, 'Director List': movie_dir_list, 'Actor List': movie_act_list})

                xx+=1

        return movie_class
