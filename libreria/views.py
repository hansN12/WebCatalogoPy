from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Artists
from .models import Albums
from .forms import ArtistsForm
from .forms import AlbumsForm
# Create your views here.

def index(request):
    return render(request, 'paginas/index.html')

def albums(request):
    albums = Albums.objects.all()
    return render(request, 'catalogo/albums.html', {'albums': albums})

def artistas(request):
    artistas = Artists.objects.all()
    return render(request, 'catalogo/artistas.html', {'artistas': artistas})

def agregar_art(request):
    formulario = ArtistsForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('artistas')
    return render(request, 'catalogo/agregar_art.html', {'formulario': formulario})

def agregar_alb(request):
    impreso = AlbumsForm(request.POST or None, request.FILES or None)
    if impreso.is_valid():
        impreso.save()
        return redirect('albums')
    artistas = Artists.objects.all()
    return render(request, 'catalogo/agregar_alb.html', {'impreso': impreso, 'artistas': artistas})

def editar_art(request,id):
    artistas = Artists.objects.get(id=id)
    formulario = ArtistsForm(request.POST or None, request.FILES or None, instance=artistas)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('artistas')
    return render(request, 'catalogo/editar_art.html', {'formulario': formulario})

def editar_alb(request,id):
    albums = Albums.objects.get(id=id)
    impreso = AlbumsForm(request.POST or None, request.FILES or None, instance=albums)
    if impreso.is_valid() and request.POST:
        impreso.save()
        return redirect('albums')
    artistas = Artists.objects.all()
    return render(request, 'catalogo/editar_alb.html', {'impreso': impreso, 'artistas': artistas})

def eliminar_art(request, id):
    artistas = Artists.objects.get(id=id)
    artistas.delete()
    return redirect('artistas')

def eliminar_alb(request, id):
    albums = Albums.objects.get(id=id)
    albums.delete()
    return redirect('albums')
    