from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth.models import User


# Create your views here.
def mainpage(request):
    return render_to_response("principal.html",{ # Millor forma de fer-ho
        'appname': "electrosobres",
        'titlepage': "sobres",
        'author': "Luis Barcenas"
    })



def dashboard(request, usuari): # Per executar: http://127.0.0.1:8000/profile/admin/
    try:
        user = User.objects.get(username=usuari)
    except:
        raise Http404("L'usuari no hi es, c*ll*ns")

    sobres = user.sobre_set.all()
    template = get_template("second.html") # Una altra forma de fer-ho, en lloc de utilitzar el render_to_response
    variables = Context({
        'username': usuari,
        'author': "Luis Barcenas",
        'sobres': sobres
    })
    page = template.render(variables)
    return HttpResponse(page)
