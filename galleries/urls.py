from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.GalleryListView.as_view()), name="list"),
    path('new/', login_required(views.GalleryCreateView.as_view()), name="create"),
    path('<pk>/', login_required(views.GalleryView.as_view()), name='detail'),
    path('<pk>/refresh/', login_required(views.refresh_gallery), name='gallery_refresh'),
    path('<pk>/json/', views.gallery_api, name='gallery_api'),
]
