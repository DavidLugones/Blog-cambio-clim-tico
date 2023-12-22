"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name ='home'),

    #APP INFORMATE
    path('informate/', include('apps.informate.urls')),

    #APP NOTICIAS
    path('noticias/', include('apps.noticias.urls')),

    #APP USUARIOS
    path('Usuarios/', include('apps.usuarios.urls')),

    #APP COMENTARIOS
    path('Comentarios/', include('apps.comentarios.urls')),

    #LOGIN Y LOGOUT
    path('login/',auth.LoginView.as_view(template_name='usuarios/login.html'),name='login'),
    path('logout/',auth.LogoutView.as_view(),name="logout"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

