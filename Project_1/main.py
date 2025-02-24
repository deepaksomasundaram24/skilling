from module import modules

movie = modules.Movie(1001,"Dhamaka Mama","Action",9,2020,["Yami Gautam","Gregory Gorgeous","Apple Pit"])
movie_2 = modules.Movie(1002,"Dhamaka Mami","Romance",7,2025,["Atulya Ravi","Gregory Amalgamation","Brian Pit"])
movie_3 = modules.Movie(1003,"Maragada Raja","Thriller",7,2024,["Pooja Hegde","Aaravi Julan","Vegita Bostnalina"])
movie_2.update_rating(10)

user = modules.User(52,"Aaron Luke",[1001,1002],"Action")
user.watch_movie(movie_3)
user.get_recommendations()

movie_manager = modules.MovieManager([1001,1002,1003])
movie_manager.search_movie("Don 2")
movie_manager.get_top_rated_movies(5)
