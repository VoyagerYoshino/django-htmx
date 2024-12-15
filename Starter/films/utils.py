from .models import UserFilm
from django.db.models import Max
def get_max_order(user):
    max_order = UserFilm.objects.filter(user=user).aggregate(Max('order',default=0))['order__max']
    if max_order:
        return max_order
    else:
        return 0

def reorder(user):
    userfilm = UserFilm.objects.filter(user=user)
    if userfilm.exists():
        new_order = range(1,userfilm.count()+1)
        for film,order in zip(userfilm,new_order):
            film.order = order
            film.save()
    else:
        return
    