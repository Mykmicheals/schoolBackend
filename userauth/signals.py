from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from app.models import Teacher,Student

@receiver(post_save, sender=CustomUser)
def create_teacher_or_student(sender, instance, created, **kwargs):
    if created:
        if instance.is_teacher:
            Teacher.objects.create(user=instance)
        elif instance.is_student:
            Student.objects.create(user=instance)
