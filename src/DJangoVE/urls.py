"""DJangoVE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from myFirstApp.views import ProductsView, productsView_URL,ProductsDetails,productsView_URL

from django.contrib import admin
from django.urls import include,path
from .views import index_page, sample_get_request
from rest_framework import routers
from adminpanel import views

router = routers.DefaultRouter()                      # add this
router.register(r'adminapi', views.rest_api, 'adminpanel')     # add this



urlpatterns = [
    path('', index_page),
    path('admin-panel/',include('adminpanel.urls')),
    path('admin/', admin.site.urls),
    path('firstApp/',ProductsView.as_view()),
    path('firstApp-url/',productsView_URL),
    path('firstApp/<int:pk>/',ProductsDetails.as_view()),
    path('firstApp-url/<int:pk>/',productsView_URL),
    path('getRequest/',sample_get_request),
    path('api/',include(router.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
