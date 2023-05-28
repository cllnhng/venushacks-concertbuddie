import random
#using youtube api
from googleapiclient.discovery import build

def findlinks(artist):

    youtube = build('youtube','v3',developerKey = 'AIzaSyDmaEwNAEPskkxTCDjTb1tOwDyzDfEyiWg')
    api_key = 'AIzaSyBxbWm5M8ZJEniTv6oiamRwPbO6_ngUA1A'


    #artist from from
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
        request = youtube.search().list(part='snippet', type='video', q=query, maxResults=5)
        response = request.execute()
        return response

    query = searchme
    results = search_videos(query)

    #create a random list of 3 numbers between 0 and 20
    randomlist = []
    while len(randomlist) != 3:
        n = random.randint(0,4)
        if n not in randomlist:
            randomlist.append(n)
    print(randomlist)

    #for each number, pull the video that is in that number of the results dictionary, then print it's url
    linklist = []
    for number in randomlist:
        item = results['items'][number]
        linklist.append('https://www.youtube.com/embed/' + item['id']['videoId'])

    return linklist