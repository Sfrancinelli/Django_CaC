"""Proyecto1 URL Configuration

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
from django.contrib import admin
from django.urls import path
from Proyecto1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.saludo),
    path('despedida/', views.goodbye),
    path('date/', views.show_date),
    # This is how you add parameters to de url, using <> and a slash(/) to add another one.
    path('age_calculator/<int:year>/<int:age>', views.age_calculator),
    path('children/', views.children_template)
]
