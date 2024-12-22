from django.shortcuts import render
from .models import Course,Module
# Create your views here.
def indexView(request):
    courses = Course.objects.all()
    context = {"courses":courses}
    context["modules"]=None
    return render(request,"base.html",context)

def changeView(request):
    course = request.GET.get("course-bar")
    print(course)
    if course == "Open this select menu":
        modules = None
    else:
        modules = Module.objects.filter(course=course)
    context = {"modules":modules}
    return render(request,"module-part.html",context)