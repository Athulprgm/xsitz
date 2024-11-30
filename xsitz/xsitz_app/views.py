from django.shortcuts import render
from django.views import View

# Create your views here.
class registerpage(View):
    def get(self,request):
        return render(request,'register.html')
class loginpage(View):
    def get(self,request):
        return render(request,'login.html')
class forgotpassword(View):
    def get(self,request):
        return render(request,'forgotpassword.html')

# //////////////////////////////////////////////// ADMIN ///////////////////////////////
class addexam(View):
    def get(self,request):
        return render(request,'ADMIN/addexam.html')
class addclass(View):
    def get(self,request):
        return render(request,'ADMIN/addclass.html')
class addclass2(View):
    def get(self,request):
        return render(request,'ADMIN/addclass2.html')
class addstaff(View):
    def get(self,request):
        return render(request,'ADMIN/addstaff.html')
class addsubject(View):
    def get(self,request):
        return render(request,'ADMIN/addsubject.html')
class allocatestaff(View):
    def get(self,request):
        return render(request,'ADMIN/allocatestaff.html')
class allocateviewstaff(View):
    def get(self,request):
        return render(request,'ADMIN/allocateviewstaff.html')
class viewclass(View):
    def get(self,request):
        return render(request,'ADMIN/viewclass.html')
class editsub(View):
    def get(self,request):
        return render(request,'ADMIN/editsub.html')
class navbar(View):
    def get(self,request):
        return render(request,'ADMIN/navbar.html')
class newallocation(View):
    def get(self,request):
        return render(request,'ADMIN/newallocation.html')
class sem(View):
    def get(self,request):
        return render(request,'ADMIN/sem.html')
class staff(View):
    def get(self,request):
        return render(request,'ADMIN/staff.html')
class table(View):
    def get(self,request):
        return render(request,'ADMIN/table.html')
class base(View):
    def get(self,request):
        return render(request,'TEACHER/base.html')
class addclasstable(View):
    def get(self,request):
        return render(request,'ADMIN/addclasstable.html')
#/////////////////////// TEACHER//////////////////////////
class REPORT(View):
    def get(self,request):
        return render(request,'TEACHER/REPORT.html')
class exam(View):
    def get(self,request):
        return render(request,'TEACHER/exam.html')
class table3(View):
    def get(self,request):
        return render(request,'TEACHER/table3.html')




