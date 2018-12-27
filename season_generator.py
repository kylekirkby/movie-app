# Import
import random
import requests
import json

api_url = "https://api.themoviedb.org/3"
search_show_endpoint = "/search/tv"
search_movie_endpoint = "/search/movie"

def searchMovies(search_query):
    """Search the themoviedb.org based on a search query"""
    payload = {
            "api_key": api_key,
            "query": search_query
        }
    response = requests.request("GET", api_url + search_movie_endpoint , data=payload)
    # print(response.text)
    json_data = json.loads(response.text)
    results = json_data["results"]
    return results

def searchShows(search_query):
    """Search the themoviedb.org based on a search query"""
    payload = {
            "api_key": api_key,
            "query": search_query
        }
    response = requests.request("GET", api_url + search_show_endpoint , data=payload)
    # print(response.text)
    json_data = json.loads(response.text)
    results = json_data["results"]
    return results

def shows():
    query_string = input("Enter TV Show: ")
    results = searchShows(query_string)
    list_num = 1
    for show in results:
        print("{0}. {1}".format(list_num, show["title"]))
        list_num += 1
    choose_show = int(input("Selection: "))
    chosen_show = results[choose_show - 1]
    print(chosen_show)
    chosen_show_id = chosen_show["id"]

def getMovieDetails(movie_id):
    """Get's the movies details based on an ID"""


def movies():
    query_string = input("Enter Movie: ")
    results = searchMovies(query_string)
    list_num = 1
    for show in results:
        print("{0}. {1}".format(list_num, show["title"]))
        list_num += 1
    choose_movie = int(input("Selection: "))
    chosen_movie = results[choose_movie - 1]
    print(chosen_movie)
    chosen_movie_id = chose_movie["id"]

def getShowDetails(id):
    """
        Get the details of a show based on an ID#
    """

def main():
    """Main Application function"""
    end = False
    while not end:
        print("MotionMatch - A TV Series/Movie App")
        print("1. Shows")
        print("2. Movies")
        print("3. Exit")
        try:
            main_option = int(input("Select: "))
            if main_option == 1:       
                shows()
            elif main_option == 2:
                movies()
            elif main_option == 3:
                exit()
        except Exception as e:
            print(e)
            print("Please choose an option listed above!")


# Get a random episode of the specified season
# random_episode = random.randint(0,len(results))

if __name__ == "__main__":
    main()