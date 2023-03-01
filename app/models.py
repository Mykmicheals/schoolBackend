from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

# Create your models here.

User = get_user_model()

class StudentClass(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Student Class"

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    date_of_birth =models.DateTimeField(auto_now=False, auto_now_add=False, blank=True,null=True)
   # date_of_birth = models.DateField()
    nationality = models.CharField( max_length=50)
    state_of_origin = models.CharField( max_length=50)
    student_class = models.ForeignKey("app.StudentClass", on_delete=models.PROTECT)
    gender   = models.CharField(max_length=50)
    address = models.CharField( max_length=50)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural = "Student Details"


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
        
class Subjects(models.Model):
    name = models.CharField(max_length=256)
    class_offered = models.ForeignKey(StudentClass,on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher,on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:     
        verbose_name_plural = "Subjects"

class StudentSubject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    score = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} {self.subject}"