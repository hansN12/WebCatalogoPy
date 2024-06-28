from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.index, name='index'),
    path('albums', views.albums, name='albums'),
    path('artistas', views.artistas, name='artistas'),
    path('artistas/agregar',views.agregar_art, name='agregar_art'),
    path('albums/agregar',views.agregar_alb, name='agregar_alb'),
    path('artistas/editar', views.editar_art, name='editar_art'),
    path('albums/editar', views.editar_alb, name='editar_alb'),
    path('artistas/eliminar/<int:id>', views.eliminar_art, name='eliminar_art'),
    path('albums/eliminar/<int:id>', views.eliminar_alb, name='eliminar_alb'),
    path('artistas/editar/<int:id>', views.editar_art, name='editar_art'),
    path('albums/editar/<int:id>', views.editar_alb, name='editar_alb')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)