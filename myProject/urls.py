"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from project import views as pages
from django.contrib import admin
from django.urls import path, include
from project import views as pages
from django.conf.urls.static import static
from django.conf import settings
from order import views as orderview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pages.home, name='home'),
    path('aboutus/', pages.aboutus, name='aboutus'),
    path('menu', pages.menu, name='menu'),
    path('chef/', pages.chef, name='chef'),
    path('klassyweek/', pages.klassyweek, name='klassyweek'),
    path('contactus/', pages.contactus, name='contactus'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('basket/', pages.basket, name='basket'),
    path('order/', include('order.urls')),
    


]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
