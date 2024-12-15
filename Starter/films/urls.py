from django.urls import path, reverse_lazy
from films import views
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView

urlpatterns = [
    path('',RedirectView.as_view(url = reverse_lazy('index'))),
    path('index/', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path('films/',views.FilmListView.as_view(),name='filmList'),
]

htmx_urlpatterns = [
    path('username-check/',views.username_check,name="username-check"),
    path('add_film/',views.add_film,name="add-film"),
    path('delete_film/<int:pk>/',views.delete_film,name="delete-film"),
    path('sort/',views.sort,name="sort"),
]

urlpatterns += htmx_urlpatterns