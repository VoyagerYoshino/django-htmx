from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView,ListView
from django.views.decorators.http import require_http_methods
from films.forms import RegisterForm
from .models import Film
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

class FilmListView(LoginRequiredMixin,ListView):
    models = Film
    context_object_name = "films"
    template_name = "myfilms.html"

    def get_queryset(self):
        return Film.objects.filter(users=self.request.user)

@login_required
def add_film(request):
    if request.method == "POST":
        name = request.POST.get("filmname")
        film = Film.objects.get_or_create(name=name)[0]
        request.user.films.add(film)
        
        films = request.user.films.all()
        return render(request, "partials/films_list.html", {"films":films})

def search_film(request):
    if request.method == "GET":
        name = request.GET.get("filmname","")
        if name:
            films = Film.objects.filter(name__icontains=name)[0:10]
            print(list(films))
        else:
            films = []
        return render(request,"partials/search_results.html", {"films":films})


@login_required
@require_http_methods(["DELETE"])
def delete_film(request, pk):
    request.user.films.remove(pk)
    films = request.user.films.all()
    return render(request, "partials/films_list.html", {"films":films})

    