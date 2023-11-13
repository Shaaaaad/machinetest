from django.shortcuts import render,redirect
from.models import Movie

# Create your views here.
def view(request):
    data = Movie.objects.all()
    return render(request,'home.html',{'data': data})


def moviestore(request):


    data = Movie.objects.all()
    # data1 = Book.objects.get()
    return render(request, 'home.html', {'data': data})


def addmovie(request):
    if request.method == 'POST':
        moviename = request.POST['moviename']
        director = request.POST['director']
        year = request.POST['year']
        data = Movie.objects.create(moviename=moviename, director=director, year=year)
        data.save()
        return redirect(moviestore)
    else:
        return render(request,'home.html')


def deletemovie(request):
  data = Movie.objects.all()
  data.delete()
  return redirect(moviestore)
