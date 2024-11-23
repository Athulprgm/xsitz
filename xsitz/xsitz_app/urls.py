"""
URL configuration for xsitz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from xsitz_app.views import *
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # ///////////////////////////////////////// ADMIN ////////////////////////////
   path('Add_register',registerpage.as_view(), name="add_register"),
   path('Add_index',indexpage.as_view(),name="add_index"),
   path('Add_exam',exam.as_view(),name="exam"),
   path('Add_addclass',addclass.as_view(),name="add_class"),
   path('Add_addclass2',addclass2.as_view(),name="add_class2t"),


   #////////////////////////////////////// TEACHER ////////////////////////////
   path('Add_report',report.as_view(),name="report"),
]