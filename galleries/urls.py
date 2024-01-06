from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path("", login_required(views.GalleryListView.as_view()), name="list"),
    path("new/", login_required(views.GalleryCreateView.as_view()), name="create"),
    path("<pk>/", login_required(views.GalleryView.as_view()), name="detail"),
    path("<pk>/delete", login_required(views.delete_gallery), name="delete"),
    path("<pk>/refresh/", login_required(views.refresh_gallery), name="refresh"),
    path("<pk>/json/", views.gallery_api, name="gallery_api"),
    path("folders", views.get_drive_folders, name="drive_folders"),
]
