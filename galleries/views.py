from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from . import forms
from . import models
from . import services
from . import utils


class GalleryCreateView(CreateView):
    model = models.Gallery
    form_class = forms.GalleryForm

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["user_id"] = self.request.user.id
        return kwargs

    def form_valid(self, form):
        services.update_gallery_data(form.instance)
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("galleries:detail", kwargs={"pk": self.object.pk})


class GalleryChangeView(DetailView):
    model = models.Gallery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["absolute_url"] = self.request.build_absolute_uri(
            reverse_lazy("galleries:detail", args=(self.object.pk,))
        )
        return context


class GalleryListView(ListView):
    model = models.Gallery

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(user=self.request.user)


class GalleryDetailView(DetailView):
    model = models.Gallery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


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


@require_http_methods(["GET"])
def get_drive_folders(request):
    folders = services.get_drive_folders(request.user.id)
    return HttpResponse(utils.folders_to_choices(folders))
