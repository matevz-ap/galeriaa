from django.urls import path

from . import views

urlpatterns = [
    path('', views.GalleryListView.as_view(), name="list"),
    path('new/', views.GalleryCreateView.as_view(), name="create"),
    path('<pk>/', views.GalleryView.as_view(), name='detail'),
    path('<pk>/refresh/', views.refresh_gallery, name='gallery_refresh'),
    path('<pk>/json/', views.gallery_api, name='gallery_api'),
]
