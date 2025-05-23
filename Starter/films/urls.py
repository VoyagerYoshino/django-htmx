from django.urls import path
from films import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("mylist/", views.FilmListView.as_view(), name="film-list"),
]

htmx_urlpatterns = [
    path('add_film/', views.add_film, name='add-film'),
    path('delete_film/<int:pk>/', views.delete_film, name='delete-film'),
    path('search_film/',views.search_film,name='search-film'),
    path('autocomplete_filmname/<int:film_id>/',views.autocomplete_filmname,name='autocomplete-filmname'),
]

urlpatterns += htmx_urlpatterns