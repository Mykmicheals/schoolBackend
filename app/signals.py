from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Teacher,Student,StudentSubject,Subjects



@receiver(post_save, sender=get_user_model())
def create_teacher(sender, instance, created, **kwargs):
    if created and instance.is_teacher:
        Teacher.objects.create(user=instance)
        

@receiver(post_save, sender=Subjects)
def link_subject_to_students(sender, instance, created , **kwargs):

    if created:
        students = Student.objects.filter(student_class=instance.class_offered)
           
        for student in students:
            StudentSubject.objects.create(student=student, subject=instance)
      