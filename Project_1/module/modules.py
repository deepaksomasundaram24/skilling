import json
from os import path

#Defining the classes
class Movie:
    def __init__(self,movie_id: int,title: str, genre: str, rating: int, release_year: int, cast: list):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.rating = rating
        self.release_year = release_year
        self.cast = cast

        self.movie_store = {f"{self.movie_id}":{"title":self.title,"genre":self.genre,
                                           "rating":self.rating,"release_year":self.release_year,
                                           "cast":self.cast}}
        
        #Adding file to the movie database
        file_name = "/Users/user/Projects/Learning/Project_1/database/movie_database.json"

        if path.isfile(file_name) ==  False:
            raise Exception ("File not found.")

        with open(file_name) as file:
            try:
                json_dict = json.load(file)
                json_dict.update(self.movie_store)
            except json.decoder.JSONDecodeError:
                json_dict = {}

        with open(file_name,'w') as json_file:
            json.dump(json_dict,json_file,indent = 4)

    def get_movie_info(self):
        print({"movie_id": self.movie_id,"title" : self.title,"genre" : self.genre,"rating":self.rating
                    ,"release_year":self.release_year,"cast":self.cast})
        
    def update_rating(self,new_rating):
        file_name = "/Users/user/Projects/Learning/Project_1/database/movie_database.json"

        if path.isfile(file_name) ==  False:
            raise Exception ("File not found.")

        with open(file_name) as file:
            try:
                json_dict = json.load(file)
                json_dict[f"{self.movie_id}"]["rating"] = new_rating 
            except json.decoder.JSONDecodeError:
                print("The movie list is empty.")
                return
        
            with open(file_name,'w') as json_file:
                json.dump(json_dict,json_file,indent = 4)

class User:
    def __init__(self,user_id: int,username: str, watched_movies: list, preferred_genres: str):
        self.user_id = user_id
        self.username = username 
        self.watched_movies = watched_movies
        self.preferred_genres = preferred_genres
        self.user_store = {f"{self.user_id}":{"username": self.username,"watched_movies":self.watched_movies,
                                    "preferred_genres":self.preferred_genres}}

        #Adding file to the users database
        file_name = "/Users/user/Projects/Learning/Project_1/database/user_database.json"

        if path.isfile(file_name) ==  False:
            raise Exception ("File not found.")

        with open(file_name) as file:
            try:
                json_dict = json.load(file)
                json_dict.update(self.user_store)
            except json.decoder.JSONDecodeError:
                json_dict = {}

        with open(file_name,'w') as json_file:
            json.dump(json_dict,json_file,indent = 4)

    def watch_movie(self,movie:Movie):
        file_name = "/Users/user/Projects/Learning/Project_1/database/user_database.json"

        if path.isfile(file_name) ==  False:
            raise Exception ("File not found.")

        with open(file_name) as file:
            json_dict = json.load(file)
            movie_list = json_dict[f"{self.user_id}"]["watched_movies"]
            #Checking if the movie has already been watched
            if movie.movie_id not in movie_list:   
                movie_list = json_dict[f"{self.user_id}"]["watched_movies"].append(movie.movie_id)

                with open(file_name,'w') as json_file:
                    json.dump(json_dict,json_file,indent = 4)

            else:
                print("The movie has already been watched")
                return

    def get_recommendations(self):        
        file_name = "/Users/user/Projects/Learning/Project_1/database/movie_database.json"
        if path.isfile(file_name) ==  False:
            raise Exception ("File not found.")

        with open(file_name) as file:
            json_dict = json.load(file)
            movie_list = list(json_dict.values())
            sorted_movie_list = sorted(movie_list,key = lambda x : x['genre'])
            sorted_genre_list = []
            for i in range(len(sorted_movie_list)):
                if sorted_movie_list[i]['genre'] == self.preferred_genres:
                    sorted_genre_list.append(sorted_movie_list[i])
            sorted_genre_list = sorted(sorted_movie_list,key = lambda x : x['rating'])
            print(sorted_genre_list)
            N = 5 
            n = 1
            while True:
                if len(sorted_genre_list) < N:
                    if len(sorted_genre_list) == 1:
                        print(sorted_genre_list[0]["title"],sorted_genre_list[0]["rating"])
                        return
                    N = len(sorted_genre_list)
                    print(N)
                print(sorted_genre_list[-n]["title"],sorted_genre_list[-n]["rating"])
                if n > N:
                    return 
                n += 1

        return

class MovieManager:
    def __init__(self,movies:list): #Manually passing a list of all movies
        self.movies = movies

    def add_movie(self,movie:Movie):
        file_name = "/Users/user/Projects/Learning/Project_1/database/movie_database.json"

        if path.isfile(file_name) ==  False:
            raise Exception ("File not found.")

        with open(file_name) as file:
            try:
                json_dict = json.load(file)
                json_dict.update(self.movie_store)
            except json.decoder.JSONDecodeError:
                json_dict = {}

        with open(file_name,'w') as json_file:
            json.dump(json_dict,json_file,indent = 4)

    def search_movie(self,title: str):
        file_name = "/Users/user/Projects/Learning/Project_1/database/movie_database.json"

        if path.isfile(file_name) ==  False:
            raise Exception ("File not found.")

        with open(file_name) as file:
            json_dict = json.load(file)
            for key,value in json_dict.items():
                if value["title"] == title:
                    print(f"{key},{value}")
                    return
            print("Movie not found")

    def get_top_rated_movies(self,n:int):
        file_name = "/Users/user/Projects/Learning/Project_1/database/movie_database.json"

        if path.isfile(file_name) ==  False:
            raise Exception ("File not found.")

        with open(file_name) as file:
            json_dict = json.load(file)
        
        rating_dict_list = list(json_dict.values())
        sorted_dict_list = sorted(rating_dict_list,key = lambda x : x['rating'])
        print(sorted_dict_list)
        iter = 1
        while True:
            if len(sorted_dict_list) < n:
                n = len(sorted_dict_list)
            print(sorted_dict_list[-iter]["title"],sorted_dict_list[-iter]["rating"])
            if iter > n:
                return
            n += 1
        return

        # movie_id_list = []
        # rating_list = []
        # while(n > 0):
        #     temp_key_update = min(list(json_dict.keys())) # str class
        #     temp_value_update = json_dict[temp_key_update]["rating"] #int class
        #     if len(json_dict) < n:
        #         n = len(json_dict)
        #     for key,value in json_dict.items():
        #         if key in movie_id_list:
        #             continue
        #         temp_rating = value["rating"]
        #        # print("temp_rating",temp_rating,"temp_value_update",temp_value_update)
        #         if (temp_rating > temp_value_update) and (key not in movie_id_list):
        #             temp_key_update = key
        #             temp_value_update = value["rating"]
        #     movie_id_list.append(temp_key_update)
        #     print(movie_id_list)
        #     rating_list.append(temp_value_update) 
        #     print(rating_list)
        #     n -= 1 
        # print(movie_id_list,rating_list)