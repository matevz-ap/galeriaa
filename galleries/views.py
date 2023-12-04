from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView

from . import models
from . import services


class GalleryCreateView(CreateView):
    model = models.Gallery
    fields = ["user", "folder"]

    def get_initial(self):
        return {"user": self.request.user}

    def get_success_url(self) -> str:
        return reverse_lazy("gallery", kwargs={"pk": self.object.pk})


class GalleryView(DetailView):
    model = models.Gallery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["files"] = self.object.data
        return context


def gallery_api(request, pk):
    gallery = models.Gallery.objects.get(pk=pk)
    return JsonResponse(gallery.data)


def refresh_gallery(request, pk):
    gallery = models.Gallery.objects.get(pk=pk)
    services.update_gallery_data(gallery)
    return HttpResponse("OK")
