import random
#using youtube api
from googleapiclient.discovery import build
youtube = build('youtube','v3',developerKey = 'AIzaSyBxbWm5M8ZJEniTv6oiamRwPbO6_ngUA1A')
api_key = 'AIzaSyBxbWm5M8ZJEniTv6oiamRwPbO6_ngUA1A'


#user inputs artist they are seeing here
artist = input("Enter artist you are seeing:")
print("You are seeing: " + artist.title()) 

#artist name is changed to youtube inquiry 
searchme = artist.title() + ' concert blog'
print ('Words in Youtube Search: ' + searchme)

#using api to search for videos
def search_videos(query):
    # part ='snippet' is required
    # type ='video' only returns videos
    # q = query is what is put into the youtube search bar
    # maxResults = 20 returns FIRST 20 results
    request = youtube.search().list(part='snippet', type='video', q=query, maxResults=20)
    response = request.execute()
    return response

query = searchme
results = search_videos(query)

#create a random list of 3 numbers between 0 and 20
randomlist = []
for i in range(0,3):
    n = random.randint(0,19)
    randomlist.append(n)
print(randomlist)

#for each number, pull the video that is in that number of the results dictionary, then print it's url 
for number in randomlist:
    item = results['items'][number]
    link = 'https://www.youtube.com/watch?v=' + item['id']['videoId']
    print (link)
