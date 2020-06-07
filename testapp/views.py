from django.shortcuts import render
from testapp.models import Movie
from testapp.forms import MovieForm
# Create your views here.
def indexview(request):
    return render(request,'testapp/index.html')
def addmovieview(request):
    form=MovieForm()
    if request.method=="POST":
        form=MovieForm(request.POST)
        if form.is_valid():
            form.save()
            print("data inserted successfully")
        return indexview(request)
    return render(request,'testapp/addmovie.html',{'form':form})
def listmovieview(request):
    movie_list=Movie.objects.all()
    return render(request,'testapp/listmovie.html',{'movie_list':movie_list})
