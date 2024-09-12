"""
URL configuration for Blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from Api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create', views.create_blog.as_view(), name='create'),
    path('update/<int:id>', views.update_blog.as_view(), name='update'),
    path('delete/<int:id>', views.delete_blog.as_view(), name='delete'),
    path('get/<int:id>', views.get_blog.as_view(), name='get'),
    path('get_all', views.get_all_blog.as_view(), name='get_all')
]
