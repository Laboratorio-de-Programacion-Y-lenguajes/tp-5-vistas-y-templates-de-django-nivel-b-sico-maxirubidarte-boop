from django.views.generic import TemplateView, ListView, DetailView
from .models import Publicacion


class InicioView(TemplateView):
    template_name = "publicaciones/inicio.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Bienvenidos"
        context ["mensaje"] ="Bienvenido al portal de publicaciones"
        return context
    

class PublicacionListView(ListView):
    model = Publicacion
    template_name = "publicaciones/publicacion_list.html"
    context_object_name = "lista_publicaciones"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["publicacion_list"] = context["lista_publicaciones"]
        return context
    


class PublicacionDetailView(DetailView):
    model = Publicacion
    context_object_name = "publicacion"
    pk_url_kwarg = "publicacion_id"
