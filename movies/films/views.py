from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Test
from django.db.models import F, Sum, Min, Max, Avg, Count, Value
# Create your views here.

def list_films(request):
    # films = Test.objects.all()
    # films = Test.objects.order_by('-raiting')
    # films = Test.objects.order_by(F('name').asc())
    films = Test.objects.annotate(procents=F('budjet')+100).annotate(isbool=Value(False))
    agg = films.aggregate(Max('budjet'), Avg('raiting'), Count('id'))
    for film in films:
        film.save_slug()
    return render(request, 'films/list_films.html', {'title':'Список фильмов', 'films':films, 'agg':agg})

def movie(request, slug_movie):
    # movie = Test.objects.get(id=id_movie)
    movies = get_object_or_404(Test, slug=slug_movie)
    return render(request, 'films/movie.html', {'title':'Информация о фильме', 'movie':movies})
