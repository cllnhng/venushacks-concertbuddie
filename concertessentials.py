import json
import base64
from requests import post,get

client_id = '9c1ef07187ad4ab3a8833b872dba11c9'
client_secret = 'e4fd90f428724b87bee3add4a5360110'

#user inputs artist they are seeing here
artist = input("Enter artist you are seeing:")


#all spotify api stuff :(
def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes),"utf-8")

    url = 'https://accounts.spotify.com/api/token'

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url,headers=headers,data=data)

    json_result = json.loads(result.content)

    token = json_result["access_token"]
    return token
    
def get_auth_header(token):
        return{ "Authorization": "Bearer " + token}



#search for the spotify artist, returns most popular artist with that name on spotify
def search_for_artist(token,artist):
      url = "https://api.spotify.com/v1/search"
      headers = get_auth_header(token)
      query = f"?q={artist}&type=artist&limit=1"

      query_url = url + query
      result = get(query_url,headers=headers)
      json_result = json.loads(result.content)["artists"]["items"]
      return (json_result[0])

#get the genre of the artist
def get_genre_of_artist(artist):
      return artist['genres']

#get the name of the artist
def get_name_of_artist(artist):
      return artist['name']

token = get_token()
spotifyartist = search_for_artist(token,artist)
genre_of_artist = get_genre_of_artist(spotifyartist)
name_of_artist = get_name_of_artist(spotifyartist)
print(name_of_artist)

list_of_spotify_genres = ['pop','edm','k-pop','classical','rock','hip hop','country']

list_of_things_to_bring = {
     'general': ['tickets','wallet','photo id','cash','phone & charger','sweater','water bottle'],

     'pop': ['tickets','wallet','cash','phone & charger','sweater','water bottle','ear plugs'],
     'edm': ['tickets','wallet','photo id','fan','phone & charger','water bottle','ear plugs', 'sunglasses', 'small bag' ],
     'k-pop': ['tickets','wallet','cash','phone & charger','sweater','water bottle', 'light stick', 'clear bag','merch','photocards'],
     'classical': ['tickets','wallet','photo id','cash','nice jacket'],
     'rock': ['tickets','wallet','photo id','phone & charger','sneakers','water bottle'],
     'hip hop': ['tickets','wallet','photo id','cash','phone & charger','sweater','water bottle'],
     'country': ['tickets','wallet','photo id','cash','phone & charger','sweater','water bottle','hat','boots'],
}


def is_genre_in_list():
    genre_is_popular = False
    popular_genre = ""
    for genre in genre_of_artist:
            if genre in list_of_spotify_genres:
                genre_is_popular = True
                popular_genre = genre
                break
            else: 
                genre_is_popular = False
                popular_genre = 'general'
        
    if genre_is_popular == False:
        list = list_of_things_to_bring['general']
        print (list)
        return list

    if genre_is_popular == True:
         list = list_of_things_to_bring[popular_genre]
         print (list)
         return list
   

is_genre_in_list()