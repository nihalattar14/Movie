from django.shortcuts import render
from .forms import MovieForm
from .models import Movie

# Create your views here.
def index(request):
    return render(request,'MovieApp/index.html')

def listMovies(request):
    moviesList=Movie.objects.all()
    return render(request,'MovieApp/listMovies.html',{'movies':moviesList})

def addMovie(request):
    form = MovieForm()
    if request.method == 'POST':
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'MovieApp/addMovie.html',{'form':form})
