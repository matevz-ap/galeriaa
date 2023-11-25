from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.http import JsonResponse

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
        print(self.object.user_id, self.object.folder)
        files = services.get_files_from_folder(self.object.user_id, self.object.folder)
        print("files", files)
        context["files"] = files
        return context
    
def gallery_api(request, pk):
    gallery = models.Gallery.objects.get(pk=pk)
    return JsonResponse(gallery.data)