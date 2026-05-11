from django.urls import path
from . import views

# TODO: Asignar el namespace de la app.
# Esto permite usar {% url 'publicaciones:inicio' %} en los templates.
app_name = "publicaciones"

urlpatterns = [
    path("",views.InicioView.as_view(),name = "inicio"),
    path("publicaciones/",views.PublicacionListView.as_view(),name = "lista_publicaciones"),
    path("publicaciones/<int:publicacion_id>/",views.PublicacionDetailView.as_view(), name = "detalle_publicacion"),


    
]