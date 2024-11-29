from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(LoginTable)
admin.site.register(StudentTable)
admin.site.register(TeacherTable)
admin.site.register(ClassTable)
admin.site.register(SeatTable)
