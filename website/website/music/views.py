# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Album
from django.template import loader

def index(request):
    all_albums =  Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {"all_albums": all_albums}
    return HttpResponse(template.render(context,request))


def detail(request, album_id):
    album = get_object_or_404(Album,pk = album_id)
    context ={'album':album}
    template = loader.get_template('music/details.html')
    return HttpResponse(template.render(context,request))

def favourite(request,album_id):
    album = get_object_or_404(Album,pk = album_id )
    context ={'error_message':"the song is already exists,now u deselected it", 'album':album}

    template = loader.get_template('music/details.html')
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):

        return HttpResponse(template.render(context,request))
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return HttpResponse(template.render(context,request))







