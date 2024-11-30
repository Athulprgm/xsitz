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

from django.contrib import admin
from django.urls import include, path

from .views import*

urlpatterns = [
    # ///////////////////////////////////////// ADMIN ////////////////////////////
   path('Add_register',registerpage.as_view(), name="add_register"),
   path('Add_forgotpassword',forgotpassword.as_view(), name="add_forgotpassword"),
   path('Add_login',loginpage.as_view(),name="add_login"),
   path('Add_exam',exam.as_view(),name="exam"),
   path('Add_addclass',addclass.as_view(),name="add_class"),
   path('Add_addclass2',addclass2.as_view(),name="add_class2"),
   path('Add_classtable',addclasstable.as_view(),name="add_classtable"),
   path('Add_staff',addstaff.as_view(),name="add_staff"),
   path('Add_subject',addsubject.as_view(),name="add_subject"),
   path('Add_allocatestaff',allocatestaff.as_view(),name="add_allocatestaff"),
   path('Add_allocateviewstaff',allocateviewstaff.as_view(),name="add_allocateviewstaff"),
   path('Add_base',base.as_view(),name="add_base"),
   path('Add_editsub',editsub.as_view(),name="add_editsub"),
   path('Add_navbar',navbar.as_view(),name="add_navbar"),
   path('Add_newallocation',newallocation.as_view(),name="add_newallocation"),
   path('Add_sem',sem.as_view(),name="add_sem"),
   path('Add_staff',staff.as_view(),name="add_staff"),
   path('Add_table',table.as_view(),name="add_table"),
   path('Add_viewclass',viewclass.as_view(),name="add_viewclass"),





   #////////////////////////////////////// TEACHER ////////////////////////////
   path('Add_REPORT',REPORT.as_view(),name="REPORT"),
   path('Add_exam',exam.as_view(),name="exam"),
   path('Add_table3',table3.as_view(),name="table3"),

]
