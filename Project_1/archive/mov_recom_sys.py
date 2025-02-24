import pandas as pd
import random

#Creating movies database
#This list will be used for randomly assigining a genre for generated movies 
movie_genres = [ "Action", "Adventure", "Comedy", "Drama", "Horror", "Sci-Fi", "Fantasy",
    "Thriller", "Romance", "Mystery", "Crime", "Animation", "Documentary",
    "Musical", "War", "Western"]

#This list of words are used for generating a title
words = [ "ocean", "python", "galaxy", "whisper", "cascade", "horizon", "ember", "velocity", "serenity",
    "nebula", "echo", "labyrinth", "solstice", "zenith", "mirage" ]

#This variable is used in randomly generating rating
rating_lowest_value = 0
rating_highest_value = 5

#This list is used for randomly generating names
names = [
    "Alice", "Bob", "Charlie", "David", "Emma",
    "Fiona", "George", "Hannah", "Isaac", "Julia",
    "Kevin", "Liam", "Mia", "Nathan", "Olivia",
    "Paul", "Quinn", "Rachel", "Samuel", "Tina",
    "Ursula", "Victor", "Wendy", "Xavier", "Yasmine",
    "Zachary", "Aaron", "Bella", "Caleb", "Diana",
    "Ethan", "Felix", "Grace", "Henry", "Ivy",
    "Jack", "Katherine", "Leo", "Madison", "Noah",
    "Oscar", "Penelope", "Ronald", "Sophia", "Travis",
    "Uma", "Vincent", "Willow", "Xander", "Zoe"
]

#Function for generating movie titles, returns a title using the words list with no. of words ranging from 1 to 5
def random_title(words:list):
    j = random.randrange(1,6)
    title_words = random.choices(words,k = j)
    new_title = " ".join(title_words)
    return new_title 

#Function for randomly selecting a movie genre, this function returns a string from the list of genre
def random_genre(movie_genres):
    return random.choice(movie_genres)

#Function for generating random rating within the entered range
lowest_rating = 0
highest_rating = 10
def random_rating():
    return random.randrange(lowest_rating,highest_rating +1)

#Function for generating a year between the inputed years, this function outputs a year
lowest_release_year = 1950
highest_release_year = 2025
def random_release_year(lowest_release_year,highest_release_year):
    return random.randrange(lowest_release_year,highest_release_year+1)

#Function - Random name generation, name formar - Firstname Lastname
def random_name(names):
    name_list = random.choices(names,k = 2)
    name = " ".join(name_list)
    return name

#This function creates pandas Dataframe and uses all the above functions to create a database
def creating_movies_data(n):
    global df
    df = pd.DataFrame({"movie_id":1,"title":"Indiana Moans","genre":"Action","rating":8,
                       "release_year":1987,"cast":"Laurene John"},index = [0])

    for i in range(1,n+1):
        new_row = pd.DataFrame({"movie_id":i+1,"title":random_title(words)
                ,"genre":random_genre(movie_genres),"rating":random_rating(),
                "release_year": random_release_year(lowest_release_year,highest_release_year),
                "cast":random_name(names)},index = [i+1])
        df = pd.concat([df,new_row],ignore_index=True)
    return df

df = creating_movies_data(50)

#Creaing users database
#This list is used for creating a username
names = ["Raj", "Kumar", "Devandra", "Ramachandran", "Deepak", 
         "Bhuvanesh", "Ahalya", "Preeti", "Kalki", "Rambo", "Elon", "Bezos", "Dilesh","Claire", "Katherina",
         "Vishnu", "Bhisma", "Cindy", "Raul", "Elaine", "Kuthcer", "Alexi", "Murdoch"]


#This function is used for generating a list of watched movies, this fuction used movie_id from the movie
#database to create a list of numbers that refer to movid_ids 
min_movie_id= df["movie_id"].min()
max_movie_id = df["movie_id"].max()
def random_movies(min_movie_id,max_movie_id):
    movie_no = random.randrange(2,6)
    movie_ids = [i for i in range(min_movie_id,max_movie_id + 1,1)]
    watched_movies = random.choices(movie_ids,k = movie_no)
    return watched_movies

#This function creates a user database using all the above functions
def creating_users_data(n,min_movie_id,max_movie_id):
    list_1 = []
    list_1.append(random_movies(min_movie_id,max_movie_id))
    df1 = pd.DataFrame({"user_id" : 1, "username": "Prem Krish",
                        "watched_movies": list_1, "preferred_genres": random_genre(movie_genres)},index = [0])
    
    for i in range(n):
        list_1 = []
        list_1.append(random_movies(min_movie_id,max_movie_id))
        new_row = pd.DataFrame({"user_id" : i+2, "username": random_name(names),
                        "watched_movies": list_1, "preferred_genres": random_genre(movie_genres)},index = [i+1])
        df1 = pd.concat([df1,new_row],ignore_index=True)
    return df1

df2 = creating_users_data(200,min_movie_id,max_movie_id)

#Defining the classes
class Movie:
    def __init__(self,movie_id: int,title: str, genre: str, rating: int, release_year: int, cast: str):
        self.movie_id = movie_id
        self.title = title
        self.genre = genre
        self.rating = rating
        self.release_year = release_year
        self.cast = cast
        self.movie_store = {self.movie_id:{"title":self.title,"genre":self.genre,
                                           "rating":self.rating,"release_year":self.release_year,
                                           "cast":self.cast}}

    def get_movie_info(self):
        print({"movie_id": self.movie_id,"title" : self.title,"genre" : self.genre,"rating":self.rating
                    ,"release_year":self.release_year,"cast":self.cast})
        
    def update_rating(self,new_rating):
        self.rating = new_rating
        return self.rating
    
class User:
    def __init__(self,user_id: int,username: str, watched_movies: list, preferred_genres: str):
        self.user_id = user_id
        self.username = username 
        self.watched_movies = watched_movies
        self.preferred_genres = preferred_genres
        self.user_store = {self.user_id:{"username": self.username,"watched_movies":self.watched_movies,
                                    "preferred_genres":self.preferred_genres}}
    
    def watch_movie(self,movie):
        df2.at[self.user_id -1,"watched_movies"].append(movie.movie_id)
        print(df2.at[self.user_id -1,"watched_movies"]) 

    def get_recommendations(self,movie_list: list):
        genre_best_movies = df[df["genre"] == self.preferred_genres].nlargest(10, "rating")
        genre_best_movies_list = genre_best_movies["movie_id"].to_list()
        #print(genre_best_movies_list)
        #print(movie_list)
        movie_ids = [recom_list for recom_list in genre_best_movies_list if recom_list in movie_list]
        for ids in movie_ids:
            print(df.loc[df["movie_id"] == ids])

class MovieManager:
    def __init__(self,movies:list):
        self.movies = movies

    def add_movie(self,movie: object,df):
        index = df.shape[0]
        new_row = pd.DataFrame({"movie_id":movie.movie_id,"title":movie.title
        ,"genre":movie.genre,"rating":movie.rating,
        "release_year": movie.release_year,
        "cast": movie.cast},index = [index]) #Dummy index since ignore index is True
        df = pd.concat([df,new_row],ignore_index=True)
        print(df)

    def search_movie(self,title: str):
        result = df[df["title"].str.match(title, case=False, na=False)].index.to_list()
        if len(result) > 0:
            for i in result:
                print(df.iloc[i])
        else:
            print("The given title does not exist.")

    def get_top_rated_movies(self,n:int):
        top_rating = df["rating"].max()
        sorted = pd.DataFrame(df.groupby("rating")[["rating","title"]].get_group(top_rating).head(10))
        print(sorted["title"].to_list())

clip = Movie(52,"The Movie","Action",9,2011,"Roche Mache")

# clip.get_movie_info()
# print(clip.update_rating(8))
# print(clip.movie_store)

user = User(52,"Aaron Luke",[2,3,5],"Action")
user.watch_movie(clip)
# movies_index = [i for i in range(min_movie_id,max_movie_id+1)]
# user.get_recommendations(movies_index)

# movie_sys = MovieManager(movies_index)
# movie_sys.search_movie("ocean galaxy")
# movie_sys.get_top_rated_movies(10)
# movie_sys.add_movie(clip,df)