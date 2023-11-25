from django.urls import path

from . import views

urlpatterns = [
    path('new/', views.GalleryCreateView.as_view(), name="create_gallery"),
    path('<pk>/', views.GalleryView.as_view(), name='gallery'),
    path('<pk>/json', views.gallery_api, name='gallery_api'),
]