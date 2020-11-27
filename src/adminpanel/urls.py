from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index,add_product,update_quantity,rest_api
from rest_framework import routers

urlpatterns = [
    path('', index),
    path('add-product/', add_product),
    path('update-product/',update_quantity)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
