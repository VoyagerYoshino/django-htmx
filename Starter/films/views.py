from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView,ListView
from django.contrib.auth import get_user_model
from .models import User,Film,UserFilm
from .utils import get_max_order,reorder
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
    template_name = "films.html"
    context_object_name = "films"
    
    def get_queryset(self):
        return UserFilm.objects.prefetch_related('film').filter(user=self.request.user)
    
    
def username_check(request):
    if User.objects.filter(username=request.POST.get('username')).exists():
        return HttpResponse("<div class='check-error' id='username-error'>This username already exists.</div>")
    else:
        return HttpResponse("<div class='check-success' id='username-error'>This username is valid.</div>")
    
def add_film(request):
    new = request.POST.get('filmname')
    film = Film.objects.get_or_create(name=new)[0]
    if not UserFilm.objects.filter(film=film,user=request.user).exists():
        UserFilm.objects.create(
            user = request.user,
            film = film,
            order = get_max_order(request.user)+1
        )
    films = UserFilm.objects.filter(user=request.user)
    return render(request,'films_ul.html',context={'films':films})

def delete_film(request,pk):
    UserFilm.objects.get(pk=pk).delete()
    reorder(request.user)
    films = UserFilm.objects.filter(user=request.user)
    return render(request,'films_ul.html',context={'films':films})

def search_film(request):
    word = request.POST.get('filmname')
    userfilms = UserFilm.objects.filter(user=request.user)
    if word:
        films = Film.objects.filter(name__contains=word).exclude(name__in=userfilms.values_list('film__name',flat=True))
    else:
        films = Film.objects.none()
    return render(request,'search_ul.html',context={'films':films})

def sort(request):
    order_pk_list = request.POST.getlist("film_order")
    films=[]
    films_dict = {film.pk: film for film in UserFilm.objects.filter(user=request.user)}
    for index, film_pk in enumerate(order_pk_list, start=1):
        film = films_dict.get(int(film_pk))
        if film:
            film.order = index
            films.append(film)
    UserFilm.objects.bulk_update(films, ['order'])
    return render(request,'films_ul.html',context={'films':films})
    
        
    