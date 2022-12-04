"""HelloWorld URL Configuration

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
from .views import Home,aboutUs 
from HelloWorld import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Home,name="index"),
    path("aboutus/",views.aboutUs,name="aboutus"),
    path("register/",views.register,name="register"),
    path("contactus/",views.contactus,name="contactus"),
    path("help/",views.help_page,name="help"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("login",views.login,name="login"),
    path('get_doc/',views.get_doc,name='get_doc'),
    path('get_face/',views.get_face,name='get_face'),
    path("personal_information/",views.personal_information,name='personal_information'),
    path('compare_faces/',views.compare_faces,name='compare_faces'),
    path('logout/', views.logout, name='logout'),
    
    
    path("index", Home, name="index"),
    
]
