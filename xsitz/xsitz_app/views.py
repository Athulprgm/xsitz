from django.shortcuts import render
from django.views import View

# Create your views here.
class registerpage(View):
    def get(self,request):
        return render(request,'register.html')
class indexpage(View):
    def get(self,request):
        return render(request,'index.html')
# //////////////////////////////////////////////// ADMIN ///////////////////////////////
class exam(View):
    def get(self,request):
        return render(request,'ADMIN/exam.html')
class addclass(View):
    def get(self,request):
        return render(request,'ADMIN/addclass.html')
class addclass2(View):
    def get(self,request):
        return render(request,'ADMIN/addclass2.html')
#/////////////////////// TEACHER//////////////////////////
class report(View):
    def get(self,request):
        return render(request,'TEACHER/report.html')

