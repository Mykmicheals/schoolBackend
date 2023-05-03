from django.db import models
from userauth.models import CustomUser


class ClassRoom(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Classes"
        
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}" 
    
        
class Subjects(models.Model):
    name = models.CharField(max_length=256)
    class_offered = models.ForeignKey(ClassRoom,on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher,on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:     
        verbose_name_plural = "Subjects"

