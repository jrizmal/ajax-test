from django.shortcuts import render, HttpResponse
from search.models import Zapisek
from serializers import ZapisekSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# Create your views here.
def dobiZapisek(request,indeks):
    try:
        zapisek=Zapisek.objects.get(id=indeks)

        serializer = ZapisekSerializer(zapisek)

        content = JSONRenderer().render(serializer.data)

        return HttpResponse(content)
    except:
        return HttpResponse("ne obstaja")
    

def vsiZapiski(request):
    zapisek = Zapisek.objects.all()

    serializer = ZapisekSerializer(zapisek, many=True)

    content = JSONRenderer().render(serializer.data)

    return HttpResponse(content)

def ustvariZapisek(request):
    if request.method=='POST':
        txt_naslov=request.POST.get('naslov','default')
        txt_besedilo=request.POST.get('besedilo','default')

        Zapisek.objects.create(
            naslov=txt_naslov,
            besedilo=txt_besedilo
        )

        

    return HttpResponse('ustvari')

def vrniZadetke(request):
    query = request.GET.get('query',None)
    if query:
        zadetki=Zapisek.objects.filter(naslov__icontains=query).distinct()
        
        serializer = ZapisekSerializer(zadetki, many=True)

        content = JSONRenderer().render(serializer.data)

        return HttpResponse(content)
    else:
        return HttpResponse("ni zadetkov")
    
def vrniZapisekGet(request):
    indeks=request.GET.get('id',None)
    try:
        zapisek=Zapisek.objects.get(id=indeks)
        serializer = ZapisekSerializer(zapisek)
        content = JSONRenderer().render(serializer.data)
        return HttpResponse(content)
    except:
        return HttpResponse("ni ujemanja")
        
def izbrisiZapisek(request):
    indeks=request.GET.get('id',None)
    try:
        Zapisek.objects.filter(id=indeks).delete()
        return HttpResponse("izbrisano")
    except:
        return HttpResponse("napaka")