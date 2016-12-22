from django.shortcuts import render
from django.http import HttpResponse
from models import Zapisek

# Create your views here.
def ustvariZapisek(request):
    if request.method == 'POST':
        txt_naslov = request.POST.get('naslov')
        txt_besedilo = request.POST.get('besedilo')

        zapisek = Zapisek(naslov=txt_naslov, besedilo=txt_besedilo)
        zapisek.save()
    return HttpResponse('jaka')

def vsiZapiski(request):

    zapiski = Zapisek.objects.all()

    context={'zapiski':zapiski}

    return render(request,'search/index.html',context=context)