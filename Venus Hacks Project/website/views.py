from flask import Blueprint, render_template, request, redirect, url_for
from .installingyoutubeapi import findlinks
from .concertessentials import genre_artist
from .googleImagesInstall import findimages

views = Blueprint('views', __name__)

@views.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "POST":
        data = request.form.get('artistsearch')
        links = findlinks(data)
        items, genre, artist = genre_artist(data)
        
        images = findimages(data)
        return render_template('infopage.html', links = links, artistname = artist.upper(), items = items, genre = genre, images = images, switch = 0)
    else:
        return render_template("index.html")
    
