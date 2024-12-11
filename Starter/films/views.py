from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView,ListView
from django.contrib.auth import get_user_model
from .models import User,Film

from films.forms import RegisterForm

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'
    
class Login(LoginView):
    template_name = 'registration/login.html'

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)

class FilmListView(ListView):
    model = Film
    template_name = "films.html"
    context_object_name = "films"
    
    
def username_check(request):
    if User.objects.filter(username=request.POST.get('username')).exists():
        return HttpResponse("<div class='check-error' id='username-error'>This username already exists.</div>")
    else:
        return HttpResponse("<div class='check-success' id='username-error'>This username is valid.</div>")
    
def add_film(request):
    new = request.POST.get('filmname')
    if not Film.objects.filter(name=new).exists():
        newFilm = Film.objects.create(name=new)
        request.user.films.add(newFilm)
        films = request.user.films.all()
        return render(request,'add_film.html',context={'films':films})
    else:
        films = request.user.films.all()
        return render(request,'add_film.html',context={'films':films})

def delete_film(request,pk):
    film = Film.objects.get(pk=pk)
    request.user.films.remove(film)
    if not film.users.exists():
        film.delete()
    return HttpResponse("")