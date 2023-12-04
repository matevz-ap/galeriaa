from typing import Any
from django.db.models.query import QuerySet
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView
from django.views.decorators.http import require_http_methods

from . import models
from . import services
from . import forms


class GalleryCreateView(CreateView):
    model = models.Gallery
    form_class = forms.GalleryForm

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["user_id"] = self.request.user.id
        return kwargs

    def get_success_url(self) -> str:
        return reverse_lazy("galleries:detail", kwargs={"pk": self.object.pk})


class GalleryView(DetailView):
    model = models.Gallery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GalleryListView(ListView):
    model = models.Gallery

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(user=self.request.user)


def gallery_api(request, pk):
    gallery = models.Gallery.objects.get(pk=pk)
    return JsonResponse(gallery.data)


def refresh_gallery(request, pk):
    gallery = models.Gallery.objects.get(pk=pk)
    services.update_gallery_data(gallery)
    return HttpResponse("OK")


@require_http_methods(["DELETE"])
def delete_gallery(request, pk):
    gallery = models.Gallery.objects.get(pk=pk)
    gallery.delete()
    return HttpResponse("OK", headers={"HX-Redirect": reverse_lazy("galleries:list")})
