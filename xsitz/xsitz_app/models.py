from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username = models.CharField(max_length=30, null=True, blank=True)
    password = models.CharField(max_length=30, null=True, blank=True)
    Type = models.CharField(max_length=30, null=True, blank=True)

class StudentTable(models.Model):
    LOGIN=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.BigIntegerField( null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)


class TeacherTable(models.Model):
    LOGIN=models.ForeignKey(LoginTable, on_delete=models.CASCADE)
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





