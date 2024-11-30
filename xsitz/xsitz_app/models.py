import random
import string

from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    Type = models.CharField(max_length=30, null=True, blank=True)

class Branch(models.Model):
    branchname=models.CharField(max_length=100,null=True,blank=True)
    is_active = models.BooleanField(max_length=20, null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    # def _str_(self):
    #     return self.branchname


class Semester(models.Model):
    # user = models.ForeignKey(Userprofile,on_delete=models.CASCADE,null=True,blank=True)
    semestername = models.CharField(max_length=100,null=True,blank=True)
    is_active = models.BooleanField(max_length=20, null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)

class StudentTable(models.Model):
    LOGIN=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.BigIntegerField( null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    registerno = models.CharField(max_length=30, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, null=True, blank=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True, blank=True)
    auto_generate_registerno = models.IntegerField( null=True, blank=True)
    is_active = models.BooleanField(max_length=20, null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Check if it's a new instance
        if not self.id:
            # Find the maximum registration number for the corresponding branchandsemester
            max_registerno = StudentTable.objects.filter(branch=self.branch,semester=self.semester).aggregate(models.Max('auto_generate_registerno'))['auto_generate_registerno__max']
            # If no registration numbers exist for this branchandsemester, start with 1
            if max_registerno is None:
                max_registerno = 0
            # Increment the maximum registration number
            self.auto_generate_registerno = max_registerno + 1
        super().save(*args, **kwargs)


class Subject(models.Model):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,null=True, blank=True)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE,null=True,blank=True)
    subjectname = models.CharField(max_length=100, null=True, blank=True)
    subjectcode = models.CharField(max_length=100, null=True, blank=True, unique=True)
    autogeneratesubjectcode = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(max_length=20, null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    @staticmethod
    def generate_auto_code():
        # Generate a unique random code
        unique_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        # Check if the generated code already exists in the database
        while Subject.objects.filter(autogeneratesubjectcode=unique_code).exists():
            unique_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return unique_code

    def save(self, *args, **kwargs):
        if not self.autogeneratesubjectcode:
            self.autogeneratesubjectcode = self.generate_auto_code()
        super().save(*args, **kwargs)


class TeacherTable(models.Model):
    LOGIN=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,null=True,blank=True,on_delete=models.CASCADE,related_name='staffsubject')

    name = models.CharField(max_length=30, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.BigIntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)



class ClassTable(models.Model):
    room_no = models.IntegerField( null=True, blank=True)
    total_bench = models.IntegerField( null=True, blank=True)
    capacity = models.IntegerField( null=True, blank=True)

class SeatTable(models.Model):
    seat_no = models.IntegerField( null=True, blank=True)
    CLASS=models.ForeignKey(ClassTable,on_delete=models.CASCADE)

class ExamDetails(models.Model):
    exam_name = models.CharField(max_length=100, null=True, blank=True)
    exam_subject=models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True)
    exam_date = models.DateField(null=True, blank=True)
    exam_time = models.TimeField(null=True, blank=True)
    no_of_students = models.CharField(max_length=100,null=True,blank=True)
    duration_hours = models.PositiveSmallIntegerField(default=1)  # Duration of the exam in hours
    # Add any other fields related to the exam details
    is_active = models.BooleanField(max_length=20, null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def _str_(self):
        return self.exam_name
    def save(self, *args, **kwargs):
        # Calculate the number of students for this exam based on the semesterno in the subject
        if self.exam_subject:
            # Count the number of students with the same semester number as the subject
            student_count = StudentTable.objects.filter(branch=self.exam_subject.branch,semester=self.exam_subject.semester).count()
            self.no_of_students = student_count
        super().save(*args, **kwargs)

class Classroom(models.Model):
    hallno=models.CharField(max_length=20,null=True,blank=True)
    capacity=models.IntegerField(null=True,blank=True)
    columns=models.IntegerField(null=True,blank=True)
    is_active = models.BooleanField(max_length=20, null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_active = models.BooleanField(max_length=20, null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

class Seatingarrangement(models.Model):
    classroom_number=models.ForeignKey(Classroom,on_delete=models.CASCADE,null=True,blank=True)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True)
    exam_date=models.CharField(max_length=100,null=True,blank=True)
    exam_name=models.CharField(max_length=100,null=True,blank=True)
    seat_number=models.CharField(max_length=100,null=True,blank=True)
    exam_time=models.CharField(max_length=100,null=True,blank=True)
    register_no=models.CharField(max_length=100,null=True,blank=True)
class Teacherseatingarrangement(models.Model):
    exam = models.ForeignKey(ExamDetails,on_delete=models.CASCADE, null=True, blank=True)
    exam_hall = models.ForeignKey(Classroom,on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey(TeacherTable,on_delete=models.CASCADE,null=True, blank=True)
    








